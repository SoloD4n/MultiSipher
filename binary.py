from PyQt5 import QtCore, QtGui, QtWidgets

binary_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Binary</class>
 <widget class="QMainWindow" name="Binary">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>520</width>
    <height>180</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="encryptBtn">
    <property name="geometry">
     <rect>
      <x>424</x>
      <y>108</y>
      <width>81</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Зашифровать</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="ownNS">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>60</y>
      <width>91</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>В 10 из своей</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="ownNSEdit">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>60</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="result_text">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>78</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="chooseNS">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>30</y>
      <width>181</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Выберите систему счисления</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>2</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>8</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>10</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>16</string>
     </property>
    </item>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>48</y>
      <width>151</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Результат</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="first_text">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>28</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>0</y>
      <width>151</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Исходный текст</string>
    </property>
   </widget>
   <widget class="QPushButton" name="infoBtn">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>0</y>
      <width>21</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>?</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>61</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Из 10</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>520</width>
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


class Ui_Binary(object):
    def setupUi(self, Binary):
        Binary.setObjectName("Binary")
        Binary.resize(520, 180)
        self.centralwidget = QtWidgets.QWidget(Binary)
        self.centralwidget.setObjectName("centralwidget")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(424, 108, 81, 23))
        self.encryptBtn.setObjectName("encryptBtn")
        self.ownNS = QtWidgets.QRadioButton(self.centralwidget)
        self.ownNS.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.ownNS.setObjectName("ownNS")
        self.ownNSEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ownNSEdit.setGeometry(QtCore.QRect(110, 60, 81, 20))
        self.ownNSEdit.setObjectName("ownNSEdit")
        self.result_text = QtWidgets.QLineEdit(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(220, 78, 291, 20))
        self.result_text.setObjectName("result_text")
        self.chooseNS = QtWidgets.QComboBox(self.centralwidget)
        self.chooseNS.setGeometry(QtCore.QRect(10, 30, 181, 22))
        self.chooseNS.setObjectName("chooseNS")
        self.chooseNS.addItem("")
        self.chooseNS.addItem("")
        self.chooseNS.addItem("")
        self.chooseNS.addItem("")
        self.chooseNS.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 48, 151, 31))
        self.label_2.setObjectName("label_2")
        self.first_text = QtWidgets.QLineEdit(self.centralwidget)
        self.first_text.setGeometry(QtCore.QRect(220, 28, 291, 20))
        self.first_text.setObjectName("first_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 151, 31))
        self.label.setObjectName("label")
        self.infoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.infoBtn.setGeometry(QtCore.QRect(490, 0, 21, 23))
        self.infoBtn.setObjectName("infoBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label_3.setObjectName("label_3")
        Binary.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Binary)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        Binary.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Binary)
        self.statusbar.setObjectName("statusbar")
        Binary.setStatusBar(self.statusbar)

        self.retranslateUi(Binary)
        QtCore.QMetaObject.connectSlotsByName(Binary)

    def retranslateUi(self, Binary):
        _translate = QtCore.QCoreApplication.translate
        Binary.setWindowTitle(_translate("Binary", "MainWindow"))
        self.encryptBtn.setText(_translate("Binary", "Зашифровать"))
        self.ownNS.setText(_translate("Binary", "В 10 из своей"))
        self.chooseNS.setItemText(0, _translate("Binary", "Выберите систему счисления"))
        self.chooseNS.setItemText(1, _translate("Binary", "2"))
        self.chooseNS.setItemText(2, _translate("Binary", "8"))
        self.chooseNS.setItemText(3, _translate("Binary", "10"))
        self.chooseNS.setItemText(4, _translate("Binary", "16"))
        self.label_2.setText(_translate("Binary", "Результат"))
        self.label.setText(_translate("Binary", "Исходный текст"))
        self.infoBtn.setText(_translate("Binary", "?"))
        self.label_3.setText(_translate("Binary", "Из 10"))
