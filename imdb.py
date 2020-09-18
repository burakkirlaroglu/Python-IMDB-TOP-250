# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imdb.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1007, 651)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(770, 350, 227, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rate_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.rate_label.setObjectName("rate_label")
        self.horizontalLayout.addWidget(self.rate_label)
        self.rate_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.rate_line_edit.setObjectName("rate_line_edit")
        self.horizontalLayout.addWidget(self.rate_line_edit)
        self.rate_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rate_button.setObjectName("rate_button")
        self.horizontalLayout.addWidget(self.rate_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 260, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 741, 601))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.movielistWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.movielistWidget.setObjectName("movielistWidget")
        self.verticalLayout_2.addWidget(self.movielistWidget)
        self.clearbutton = QtWidgets.QPushButton()
        self.clearbutton.setText("Clear")
        self.verticalLayout_2.addWidget(self.clearbutton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IMDB SEARCH MOVIE TOP 250"))
        self.rate_label.setText(_translate("Form", "Rate:"))
        self.rate_button.setText(_translate("Form", "show"))
        self.label.setText(_translate("Form", "IMDB TOP 250 MOVIES"))
        self.label_2.setText(_translate("Form", "IMDB TOP 250 MOVIES "))

        self.rate_button.clicked.connect(self.calculate_rate)
        self.clearbutton.clicked.connect(self.clear)

    def clear(self):
        self.movielistWidget.clear()

    def calculate_rate(self):
        url = "https://www.imdb.com/chart/top/"
        response = requests.get(url)

        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        soup.prettify()

        td_name = soup.find_all("td", {"class": "titleColumn"})
        td_rate = soup.find_all("td", {"class": "ratingColumn imdbRating"})

        for i, j in zip(td_name, td_rate):
            i = i.text
            j = j.text
            i = i.strip()
            i = i.replace("\n", "")
            j = j.strip()
            j = j.replace("\n", "")
            result = i + " ===> " + j
            sorted(result)

            if float(j) > float(self.rate_line_edit.text()):
                # result = i +" ===> "+ j
                self.movielistWidget.insertItem(len(i), result)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

