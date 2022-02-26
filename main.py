import os
import sys
import time
import threading
import webbrowser
from modules.md5Get import Md5
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, qApp, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QApplication, QStackedWidget, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QColor


class Main(QMainWindow):

        def __init__(self):

                super().__init__()
                loadUi('ui_files/main.ui', self)
                self.etat = 0
                self.exitButton.clicked.connect(qApp.quit)
                self.minimizeButton.clicked.connect(widget.showMinimized)
                self.maximizeButton.clicked.connect(self.maximizeominimize)
                self.fullScanButton.clicked.connect(self.goToFullScanScene)
                self.submitMalwareButton.clicked.connect(self.goToSubmitScene)
                self.choiceFrame.clicked.connect(self.check_malware)

                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(50)
                self.shadow.setColor(QColor("#92FE9D"))
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.choiceFrame.setGraphicsEffect(self.shadow)

        def maximizeominimize(self):

                if self.etat == 0:
                        widget.showMaximized()
                        self.etat = 1
                else:
                        widget.showNormal()
                        self.etat = 0

        def goToFullScanScene(self):

                full_scan = FullScan()
                widget.addWidget(full_scan)
                widget.setCurrentIndex(widget.currentIndex()+1)

        def goToSubmitScene(self):

                submit = Submit("http://aotb.000webhostapp.com/index.php")
                submit.openWeb()

        def check_malware(self):

                home_dir = str(Path.home())
                fname = QFileDialog.getOpenFileName(self, 'Choisir un fichier', home_dir)
                print(fname[0])
                self.inputFile.setText(fname[0])
                md5_getter = Md5(file=fname[0])
                hash = md5_getter.get_hash()
                print(hash)

                with open("hashs.txt", "r") as file:

                        datas = file.readlines()
                        file.close()

                for hashs in datas:
                        #print(hashs)
                        if hash in hashs:
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Warning)
                                msg.setText("Ce fichier est infecté par un malware.")
                                msg.setWindowTitle("Menace détecté.")
                                retval = msg.exec_()
                                break
                        else:
                                pass
                msg = QMessageBox()
                msg.setText("Ce fichier semble sûr.")
                msg.setWindowTitle("Tous semble bon.")
                retval = msg.exec_()


class FullScan(QMainWindow):

        def __init__(self):

                super().__init__()

                loadUi('ui_files/full_scan.ui', self)
                self.etat = 0
                self.exitButton.clicked.connect(qApp.quit)
                self.minimizeButton.clicked.connect(widget.showMinimized)
                self.maximizeButton.clicked.connect(self.maximizeominimize)
                self.scanButton.clicked.connect(self.goToMainScene)
                self.submitFrame.clicked.connect(self.goToSubmitScene)
                self.startButton.clicked.connect(self.scan_all_files)

                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(50)
                self.shadow.setColor(QColor("#92FE9D"))
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.startButton.setGraphicsEffect(self.shadow)

        def maximizeominimize(self):

                if self.etat == 0:
                        widget.showMaximized()
                        self.etat = 1
                else:
                        widget.showNormal()
                        self.etat = 0

        def goToMainScene(self):

                main = Main()
                widget.addWidget(main)
                widget.setCurrentIndex(widget.currentIndex()-1)

        def goToSubmitScene(self):

                submit = Submit("http://aotb.000webhostapp.com/index.php")
                submit.openWeb()

        def scan_all_files(self):

                def scan():
                        for root, directories, files in os.walk("C:\\"):
                                for file in files:
                                        rep = os.path.join(root, file)
                                        print(rep)
                                        self.labelFile.setText(f"Analyse de: {rep}")
                                        try:
                                                hash_file = Md5(file=rep)
                                                h = hash_file.get_hash()
                                                with open("hashs.txt", "r") as file:

                                                        datas = file.readlines()
                                                        file.close()

                                                for hashs in datas:

                                                        if h in hashs:
                                                                with open("infected.txt", "a") as file:
                                                                        file.write(f"{rep} est infecté.")
                                                        else:
                                                                #print(f"Fichier: {rep} semble sûr.\n")
                                                                pass
                                        except:
                                                print("Erreur")

                for i in range(2):

                        t = threading.Thread(target=scan)
                        t.start()



class Submit:

        def __init__(self, url):

                self.url = url

        def openWeb(self):

                webbrowser.open("http://aotb.000webhostapp.com/index.php")

if __name__ == "__main__":

        app = QApplication(sys.argv)
        widget = QStackedWidget()
        main = Main()
        fullscan = FullScan()
        widget.setWindowFlag(Qt.FramelessWindowHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.addWidget(main)
        widget.addWidget(fullscan)
        widget.resize(949, 585)
        widget.show()
        sys.exit(app.exec())
