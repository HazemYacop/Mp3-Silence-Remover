import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from PySide2.QtWidgets import *
from PySide2 import QtGui
from UserInterface import Ui_MainWindow as design


class Package:
    @staticmethod
    def mp3_folder_path_finder():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        main_folder_path = filedialog.askdirectory()
        if main_folder_path == "":
            return "..."
        else:
            return main_folder_path

    @staticmethod
    def output_folder_path_finder():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        banner_path = filedialog.askdirectory()
        if banner_path == "":
            return "..."
        else:
            return banner_path

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
        self.setWindowTitle("Silence Remover")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.show()