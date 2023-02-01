# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 650)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 		rgba(255, 154, 158, 255), stop:1 rgba(250, 208, 196, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0.545, x2:1, y2:0.534, stop:0 rgba(67, 233, 123, 255), stop:1 rgba(56, 249, 215, 255));\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.gridLayout_2 = QGridLayout(self.MainPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.InputsLayout = QVBoxLayout()
        self.InputsLayout.setSpacing(30)
        self.InputsLayout.setObjectName(u"InputsLayout")
        self.InputsLayout.setContentsMargins(100, -1, 100, 30)
        self.Spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer1)

        self.Mp3FolderLayout = QHBoxLayout()
        self.Mp3FolderLayout.setSpacing(0)
        self.Mp3FolderLayout.setObjectName(u"Mp3FolderLayout")
        self.Mp3FolderText = QLabel(self.MainPage)
        self.Mp3FolderText.setObjectName(u"Mp3FolderText")
        self.Mp3FolderText.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.Mp3FolderLayout.addWidget(self.Mp3FolderText)

        self.Mp3FolderButton = QPushButton(self.MainPage)
        self.Mp3FolderButton.setObjectName(u"Mp3FolderButton")
        self.Mp3FolderButton.setMinimumSize(QSize(300, 35))
        self.Mp3FolderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.Mp3FolderButton.setStyleSheet(u"QPushButton#Mp3FolderButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#Mp3FolderButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.Mp3FolderLayout.addWidget(self.Mp3FolderButton)


        self.InputsLayout.addLayout(self.Mp3FolderLayout)

        self.OutputFolderLayout = QHBoxLayout()
        self.OutputFolderLayout.setSpacing(0)
        self.OutputFolderLayout.setObjectName(u"OutputFolderLayout")
        self.OutputFolderLabel = QLabel(self.MainPage)
        self.OutputFolderLabel.setObjectName(u"OutputFolderLabel")
        self.OutputFolderLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.OutputFolderLayout.addWidget(self.OutputFolderLabel)

        self.OutputFolderButton = QPushButton(self.MainPage)
        self.OutputFolderButton.setObjectName(u"OutputFolderButton")
        self.OutputFolderButton.setMinimumSize(QSize(300, 35))
        self.OutputFolderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.OutputFolderButton.setStyleSheet(u"QPushButton#OutputFolderButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#OutputFolderButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.OutputFolderLayout.addWidget(self.OutputFolderButton)


        self.InputsLayout.addLayout(self.OutputFolderLayout)

        self.Spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer2)


        self.gridLayout_2.addLayout(self.InputsLayout, 0, 0, 1, 1)

        self.StartLayout = QHBoxLayout()
        self.StartLayout.setObjectName(u"StartLayout")
        self.StartLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer3)

        self.StartButtonLayout = QVBoxLayout()
        self.StartButtonLayout.setObjectName(u"StartButtonLayout")
        self.HowDoesItWorkButton = QPushButton(self.MainPage)
        self.HowDoesItWorkButton.setObjectName(u"HowDoesItWorkButton")
        self.HowDoesItWorkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HowDoesItWorkButton.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 9pt \"MS Sans Serif\";\n"
"text-decoration: underline;")

        self.StartButtonLayout.addWidget(self.HowDoesItWorkButton)

        self.StartButton = QPushButton(self.MainPage)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setMinimumSize(QSize(300, 40))
        self.StartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartButton.setStyleSheet(u"QPushButton#StartButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#StartButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartButtonLayout.addWidget(self.StartButton)


        self.StartLayout.addLayout(self.StartButtonLayout)

        self.Spacer4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer4)


        self.gridLayout_2.addLayout(self.StartLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.StatusPage = QWidget()
        self.StatusPage.setObjectName(u"StatusPage")
        self.gridLayout_3 = QGridLayout(self.StatusPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spacer7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.spacer7, 0, 0, 1, 1)

        self.BackButtonLayout = QHBoxLayout()
        self.BackButtonLayout.setObjectName(u"BackButtonLayout")
        self.BackButtonLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer5)

        self.BackButton = QPushButton(self.StatusPage)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setMinimumSize(QSize(300, 40))
        self.BackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackButton.setStyleSheet(u"QPushButton#BackButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.BackButtonLayout.addWidget(self.BackButton)

        self.Spacer6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer6)


        self.gridLayout_3.addLayout(self.BackButtonLayout, 3, 0, 1, 1)

        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setSpacing(50)
        self.StatusLayout.setObjectName(u"StatusLayout")
        self.WorkingLabel = QLabel(self.StatusPage)
        self.WorkingLabel.setObjectName(u"WorkingLabel")
        self.WorkingLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WorkingLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.WorkingLabel)

        self.CurrentFileLabel = QLabel(self.StatusPage)
        self.CurrentFileLabel.setObjectName(u"CurrentFileLabel")
        self.CurrentFileLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.CurrentFileLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.CurrentFileLabel)


        self.gridLayout_3.addLayout(self.StatusLayout, 1, 0, 1, 1)

        self.spacer8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.spacer8, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.StatusPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Mp3FolderText.setText(QCoreApplication.translate("MainWindow", u"Mp3 Folder :", None))
        self.Mp3FolderButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.OutputFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Output Folder :", None))
        self.OutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.HowDoesItWorkButton.setText(QCoreApplication.translate("MainWindow", u"How does it work ?", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.WorkingLabel.setText(QCoreApplication.translate("MainWindow", u"Working ...", None))
        self.CurrentFileLabel.setText(QCoreApplication.translate("MainWindow", u"Current File :", None))
    # retranslateUi

