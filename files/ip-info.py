import sys
import requests
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *


class WorkThread(QThread):
    threadSignal = pyqtSignal(str)

    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def run(self):
        try:
            if self.ip == '':
                self.threadSignal.emit(f'<div style="color: #0FF0F1">[Info] Ваш ip</div>')
                response = requests.get(url=f'http://ip-api.com/json/').json()
                ip = response.get('query')
            else:
                response = requests.get(url=f'http://ip-api.com/json/{self.ip}').json()
        except:
            self.threadSignal.emit('''
                <div style="color: #DD4A48">
                [ERROR] Internet not found [ERROR]
                </div>
            ''')
            self.msleep(0)
        data = {}
        try:
            data = {
                '[⚝ IP]': response.get('query'),
                '∟[Int prov]': response.get('isp'),
                '∟[Org]': response.get('org'),
                '∟[Country]': response.get('country'),
                '∟[Region Name]': response.get('regionName'),
                '∟[City]': response.get('city'),
                '∟[ZIP]': response.get('zip'),
                '∟[Lat]': response.get('lat'),
                '∟[Lon]': response.get('lon')
            }
        except:
            if data:           
                self.threadSignal.emit(
                    '<div style="color: #f00">IP address entered incorrectly</div>')
        
        for k, v in data.items():
            text = f'{k} : {v}'
            if k == '∟[Int prov]' and v is None:
                self.threadSignal.emit(
                    f'<div style="color: #f00">IP address entered incorrectly</div>')
                break
            else:
                self.threadSignal.emit(f'<div style="color: #1100FF">{text}</div>')
                
            self.msleep(10)
            
        self.threadSignal.emit(f'{"ー" * 30} ')  
        

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainwindow")
        
        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setText(' Aerlis IP info ')
        
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("I P : ")
        self.lineEdit.returnPressed.connect(self.requests_get)
        
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.lineEdit)
        self.lineEdit.setFocus() 
        
    def requests_get(self):
        ip = self.lineEdit.text()
        self.thread = WorkThread(ip)
        self.thread.threadSignal.connect(self.on_threadSignal)
        self.thread.start()    
    
    def on_threadSignal(self, data):
        self.textBrowser.append(data)    
    

qss = """
#mainwindow {
    background-color: black;
}

QLineEdit {
    background-color: rgb(227, 229, 235);
    border-radius: 5px;
    border: 2px solid rgb(227, 29, 35);
    padding-left: 10px;
    height: 40px;
    /* color: #f00;  */
}
QLineEdit:hover {
    border: 2px solid rgb(64, 71, 188);
}
QLineEdit:focus {
    border: 2px solid rgb(91, 201, 124);
}

QTextBrowser {
    background-color: #000000; 
    border: 2px solid; 
    color: #0FF0F1;
}
QTextBrowser:hover,
QTextBrowser:!hover,
QTextBrowser::selected,
QTextBrowser::pressed {
    border: 4px solid black;    
    padding: -4px 0px 0px 4px;
}

"""


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Comfortaa", 14))
    app.setStyleSheet(qss)
    w = MainWindow()
    w.resize(560, 400)
    w.show()
    sys.exit(app.exec_())