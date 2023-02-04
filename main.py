import os
import threading
from PySide2.QtWidgets import QApplication
from Functions import Package, UserInterface


class Main:
    def __init__(self):
        super().__init__()

        # Ui Definition
        self.UserInterface = UserInterface()
        self.UserInterface.stackedWidget.setCurrentIndex(0)

        # Button(s) Fun(s)
        self.UserInterface.StartButton.clicked.connect(lambda: [self.UserInterface.stackedWidget.setCurrentIndex(1), self.UserInterface.BackButton.setDisabled(True), self.UserInterface.WorkingLabel.setText("Working ..."), self.startup()])
        self.UserInterface.BackButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(0))
        self.UserInterface.Mp3FolderButton.clicked.connect(lambda: self.UserInterface.Mp3FolderButton.setText(Package.ask_for_directory()))
        self.UserInterface.OutputFolderButton.clicked.connect(lambda: self.UserInterface.OutputFolderButton.setText(Package.ask_for_directory()))
        self.UserInterface.HowDoesItWorkButton.clicked.connect(lambda: Package.help())

        # Program Path
        self.program_address = f'{os.path.expanduser("~")}\AppData\Local\Mp3 Silence Remover'

    def startup(self):
        try:
            # Getting Required Data
            self.required_data()

            # StartUp
            start = threading.Thread(target=self.main)
            start.start()

        except Exception as e:
            print(e)
            self.UserInterface.WorkingLabel.setText("Error Occured, Take a screenshot of the CMD (Black Screen) and Contact : +201150169348")
            self.UserInterface.CurrentFileLabel.setText("")
            self.UserInterface.BackButton.setDisabled(False)

    def main(self):
        # Printing Mp3 Folder and Output Folder (in case there was an error)
        print(f"The mp3 Folder is: {self.mp3_folder_path}, and output folder is: {self.output_folder_path}")
        Failed_Conversions = []
        counter = 0

        for mp3 in Package.extension_finder(self.mp3_folder_path, ".mp3"):
            try:
                # Setting the text of the current file in the UI
                self.UserInterface.CurrentFileLabel.setText(f"Current File : {mp3}")
                print(f"Current mp3 : {mp3}")

                # Mp3 Full Path
                mp3_path = f"{self.mp3_folder_path}/{mp3}"

                # Generating Audio
                Package.remove_silence(mp3, mp3_path, self.output_folder_path)
            except Exception as e:
                print(e)
                Failed_Conversions.append(f"File : {mp3}")

        # Re-Defining UserInterface
        self.UserInterface.WorkingLabel.setText("Program Finished ...")
        self.UserInterface.CurrentFileLabel.setText("")
        self.UserInterface.BackButton.setDisabled(False)

        # Printing Files With errors (if found)
        if len(Failed_Conversions) > 0:
            print("*****************************************************************************")
            print("Check out the Errors with these Files :")
            print(Failed_Conversions)

    def required_data(self):
        self.mp3_folder_path = self.UserInterface.Mp3FolderButton.text()
        self.output_folder_path = self.UserInterface.OutputFolderButton.text()


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
