from PyQt5 import QtCore, QtGui, QtWidgets

main_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>640</width>
    <height>480</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="titleLable">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>90</y>
      <width>271</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Мультишифратор</string>
    </property>
   </widget>
   <widget class="QComboBox" name="instrumentsList">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>190</y>
      <width>221</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Выбрать инструмент</string>
     </property>
    </item>
   </widget>
   <widget class="QPushButton" name="openBtn">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>290</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Открыть</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>640</width>
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLable = QtWidgets.QLabel(self.centralwidget)
        self.titleLable.setGeometry(QtCore.QRect(190, 90, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titleLable.setFont(font)
        self.titleLable.setObjectName("titleLable")
        self.instrumentsList = QtWidgets.QComboBox(self.centralwidget)
        self.instrumentsList.setGeometry(QtCore.QRect(210, 190, 221, 22))
        self.instrumentsList.setObjectName("instrumentsList")
        self.instrumentsList.addItem("")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(250, 290, 131, 41))
        self.openBtn.setObjectName("openBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLable.setText(_translate("MainWindow", "Мультишифратор"))
        self.instrumentsList.setItemText(0, _translate("MainWindow", "Выбрать инструмент"))
        self.openBtn.setText(_translate("MainWindow", "Открыть"))
