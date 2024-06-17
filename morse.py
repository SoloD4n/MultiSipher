from PyQt5 import QtCore, QtGui, QtWidgets

morse_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Morse</class>
 <widget class="QMainWindow" name="Morse">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>370</width>
    <height>200</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="firstText">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>40</y>
      <width>331</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="resultText">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>80</y>
      <width>331</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label1">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Исходный текст</string>
    </property>
   </widget>
   <widget class="QLabel" name="label2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>101</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Результат</string>
    </property>
   </widget>
   <widget class="QPushButton" name="encryptBtn">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>110</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Зашифровать</string>
    </property>
   </widget>
   <widget class="QPushButton" name="hintBtn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>110</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Открыть подсказку</string>
    </property>
   </widget>
   <widget class="QPushButton" name="infoBtn">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>10</y>
      <width>21</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>?</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>370</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Ui_Morse(object):
    def setupUi(self, Morse):
        Morse.setObjectName("Morse")
        Morse.resize(370, 200)
        self.centralwidget = QtWidgets.QWidget(Morse)
        self.centralwidget.setObjectName("centralwidget")
        self.firstText = QtWidgets.QLineEdit(self.centralwidget)
        self.firstText.setGeometry(QtCore.QRect(20, 40, 331, 21))
        self.firstText.setObjectName("firstText")
        self.resultText = QtWidgets.QLineEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(20, 80, 331, 21))
        self.resultText.setObjectName("resultText")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 60, 101, 21))
        self.label2.setObjectName("label2")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(260, 110, 91, 23))
        self.encryptBtn.setObjectName("encryptBtn")
        self.hintBtn = QtWidgets.QPushButton(self.centralwidget)
        self.hintBtn.setGeometry(QtCore.QRect(20, 110, 121, 23))
        self.hintBtn.setObjectName("hintBtn")
        self.infoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.infoBtn.setGeometry(QtCore.QRect(340, 10, 21, 23))
        self.infoBtn.setObjectName("infoBtn")
        Morse.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Morse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        Morse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Morse)
        self.statusbar.setObjectName("statusbar")
        Morse.setStatusBar(self.statusbar)

        self.retranslateUi(Morse)
        QtCore.QMetaObject.connectSlotsByName(Morse)

    def retranslateUi(self, Morse):
        _translate = QtCore.QCoreApplication.translate
        Morse.setWindowTitle(_translate("Morse", "MainWindow"))
        self.label1.setText(_translate("Morse", "Исходный текст"))
        self.label2.setText(_translate("Morse", "Результат"))
        self.encryptBtn.setText(_translate("Morse", "Зашифровать"))
        self.hintBtn.setText(_translate("Morse", "Открыть подсказку"))
        self.infoBtn.setText(_translate("Morse", "?"))
