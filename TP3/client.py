import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import webbrowser

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        ##################################################

        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your host IP:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)

        ##################################################

        self.label3 = QLabel("Enter your API Key:", self)
        self.label3.move(10, 90)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 120)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 150)

        ##################################################

        self.label5 = QLabel("Enter your IP:", self)
        self.label5.move(10, 180)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 210)

        ##################################################

        self.label6 = QLabel("Answer:", self)
        self.label6.move(10, 240)
        self.button = QPushButton("Send", self)
        self.button.move(10, 300)
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)
        self.show()

        ##################################################

    def on_click(self):
        hostname = self.text1.text()
        api_key = self.text2.text()
        ip = self.text3.text()

        ##############################################

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the ip field")
        if api_key == "":
            QMessageBox.about(self, "Error", "Please fill the api field")
        if ip == "":
            QMessageBox.about(self, "Error", "Please fill the hostname field")
        else:
            res = self.__query(hostname,api_key,ip)
            if res:
                self.label6.setText("Coraganization: %s Pays: %s \n Région: %s Villes: %s" % (res["Organization"],res["Country"],res["Region"],res["City"], ))
                self.label6.adjustSize()    
                url= "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Lat"],res["Long"])
                webbrowser.open(url)          
                self.show()

        ########################################################################################

    def __query(self, hostname,api_key,ip):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip, api_key) #http://127.0.0.1:8000/ip/<ip>?key=<api key>
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found or API key wrong or somethings else")
        if r.status_code == requests.codes.OK:
            return r.json()


    #################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()