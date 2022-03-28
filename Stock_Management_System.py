import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import webbrowser
import time
import sys
import os
import datetime
from datetime import datetime
from datetime import date
from numpy import str_
import icons_rc
from PyQt5 import Qt, QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import QPropertyAnimation,QDate,QDateTime,QTime,Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import  QDialog,QDateEdit,QHeaderView,QComboBox,QApplication, QMessageBox, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip,QFileDialog,QLineEdit
from PyQt5.uic import loadUi
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    user='root', 
    password='india123abcd$',
    host='127.0.0.1',
    database='hotel_management')

cursor = conn.cursor()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("main_window.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.windowbtn.clicked.connect(self.gotocreate)

    def gotocreate(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)
        
        '''signup=HotelMenu()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)'''

#############################################################################
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.show()
app.exec_()

###