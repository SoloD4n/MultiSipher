from PyQt5 import QtCore, QtGui, QtWidgets

caesar_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>CaesarCipher</class>
 <widget class="QMainWindow" name="CaesarCipher">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>390</width>
    <height>210</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Caesar</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="firstEdit">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>60</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="infoBtn">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>10</y>
      <width>21</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>?</string>
    </property>
   </widget>
   <widget class="QLabel" name="firstText">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>40</y>
      <width>91</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Исходный текст</string>
    </property>
   </widget>
   <widget class="QLabel" name="resultText">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>100</y>
      <width>91</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Результат</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="resultEdit">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>120</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="encryptBtn">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>80</y>
      <width>91</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Зашифровать</string>
    </property>
   </widget>
   <widget class="QSpinBox" name="shiftSpinBox">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>60</y>
      <width>42</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="shiftText">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>40</y>
      <width>47</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Сдвиг</string>
    </property>
   </widget>
   <widget class="QComboBox" name="chosenLanguage">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Русский язык</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Английский язык</string>
     </property>
    </item>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>390</width>
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


class Ui_CaesarCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(390, 210)
        self.centralwidget = QtWidgets.QWidget(CaesarCipher)
        self.centralwidget.setObjectName("centralwidget")
        self.firstEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstEdit.setGeometry(QtCore.QRect(50, 60, 113, 20))
        self.firstEdit.setObjectName("firstEdit")
        self.infoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.infoBtn.setGeometry(QtCore.QRect(360, 10, 21, 21))
        self.infoBtn.setObjectName("infoBtn")
        self.firstText = QtWidgets.QLabel(self.centralwidget)
        self.firstText.setGeometry(QtCore.QRect(60, 40, 91, 20))
        self.firstText.setObjectName("firstText")
        self.resultText = QtWidgets.QLabel(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(60, 100, 91, 20))
        self.resultText.setObjectName("resultText")
        self.resultEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resultEdit.setGeometry(QtCore.QRect(50, 120, 113, 20))
        self.resultEdit.setObjectName("resultEdit")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(240, 80, 91, 31))
        self.encryptBtn.setObjectName("encryptBtn")
        self.shiftSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.shiftSpinBox.setGeometry(QtCore.QRect(170, 60, 42, 22))
        self.shiftSpinBox.setObjectName("shiftSpinBox")
        self.shiftText = QtWidgets.QLabel(self.centralwidget)
        self.shiftText.setGeometry(QtCore.QRect(170, 40, 47, 21))
        self.shiftText.setObjectName("shiftText")
        self.chosenLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.chosenLanguage.setGeometry(QtCore.QRect(10, 10, 121, 22))
        self.chosenLanguage.setObjectName("chosenLanguage")
        self.chosenLanguage.addItem("")
        self.chosenLanguage.addItem("")
        CaesarCipher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaesarCipher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 21))
        self.menubar.setObjectName("menubar")
        CaesarCipher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaesarCipher)
        self.statusbar.setObjectName("statusbar")
        CaesarCipher.setStatusBar(self.statusbar)

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "Caesar"))
        self.infoBtn.setText(_translate("CaesarCipher", "?"))
        self.firstText.setText(_translate("CaesarCipher", "Исходный текст"))
        self.resultText.setText(_translate("CaesarCipher", "Результат"))
        self.encryptBtn.setText(_translate("CaesarCipher", "Зашифровать"))
        self.shiftText.setText(_translate("CaesarCipher", "Сдвиг"))
        self.chosenLanguage.setItemText(0, _translate("CaesarCipher", "Русский язык"))
        self.chosenLanguage.setItemText(1, _translate("CaesarCipher", "Английский язык"))
