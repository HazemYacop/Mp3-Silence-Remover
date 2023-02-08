import os
import webbrowser
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from PySide2.QtWidgets import *
from UserInterface import Ui_MainWindow as design
from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint


class Package:
    @staticmethod
    def help():
        print("This will be available in the future")
        # webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')

    @staticmethod
    def ask_for_directory():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        directory = filedialog.askdirectory()
        if directory != "":
            return directory
        else:
            return "..."

    @staticmethod
    def extension_finder(directory, extension):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if os.path.splitext(filename)[1] == extension:
                    yield filename

    @staticmethod
    def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
        '''
        sound is a pydub.AudioSegment
        silence_threshold in dB
        chunk_size in ms

        iterate over chunks until you find the first one with sound.
        '''
        trim_ms = 0  # ms

        assert chunk_size > 0  # to avoid infinite loop
        while sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
            trim_ms += chunk_size

        return trim_ms

    @staticmethod
    def remove_silence(mp3_name, mp3_path, output):
        sound = AudioSegment.from_file(mp3_path, format="mp3")
        start_trim = Package.detect_leading_silence(sound)
        end_trim = Package.detect_leading_silence(sound.reverse())
        duration = len(sound)
        trimmed_sound = sound[start_trim:duration - end_trim]
        trimmed_sound.export(f"{output}/{mp3_name}")


class UserInterface(QMainWindow, design):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Mp3 Silence Remover")
        self.show()

    def transition(self, ui_element):
        self.anim_group = QParallelAnimationGroup()

        for element in ui_element:
            self.element = element
            x = self.element.x()
            y = self.element.y()
            element.move(x - 50, y)

        for element in ui_element:
            effect = QGraphicsOpacityEffect(element)
            self.element = element
            x = self.element.x()
            y = self.element.y()
            self.element.setGraphicsEffect(effect)
            self.anim_1 = QPropertyAnimation(effect, b"opacity")
            self.anim_1.setStartValue(0)
            self.anim_1.setEndValue(1)
            self.anim_1.setDuration(400)
            self.child = element
            self.anim = QPropertyAnimation(self.child, b"pos")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setEndValue(QPoint(x+50, y))
            self.anim.setDuration(300)
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim)

        self.anim_group.start()