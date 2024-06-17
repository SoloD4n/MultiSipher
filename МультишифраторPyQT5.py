import sys
import io
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFormLayout, QDialogButtonBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QPixmap

from main import Ui_MainWindow, main_template
from caesar import Ui_CaesarCipher, caesar_template
from morse import Ui_Morse, morse_template
from binary import Ui_Binary, binary_template


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Мультишифратор")
        self.instrumentsList.addItem("Шифр Цезаря")
        self.instrumentsList.addItem("Шифр Морзе")
        self.instrumentsList.addItem("Бинарный шифр+")
        self.instrumentsList.currentTextChanged.connect(self.open_available)

        self.openBtn.setEnabled(False)
        self.openBtn.clicked.connect(self.open)

    def open_available(self):
        if self.instrumentsList.currentText() == "Выбрать инструмент":
            self.openBtn.setEnabled(False)
        else:
            self.openBtn.setEnabled(True)

    def open(self):
        chosen_instrument = self.instrumentsList.currentText()
        if chosen_instrument == "Шифр Цезаря":
            ex_caesar.show()
        if chosen_instrument == "Шифр Морзе":
            ex_morse.show()
        if chosen_instrument == "Бинарный шифр+":
            ex_binary.show()


class CaesarCipher(QMainWindow, Ui_CaesarCipher):
    def __init__(self):
        super().__init__()
        f = io.StringIO(caesar_template)
        uic.loadUi(f, self)
        self.languages = {"Русский язык": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                          "Английский язык": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Шифр Цезаря")
        self.shiftSpinBox.setMinimum(-999)
        self.shiftSpinBox.setMaximum(999)
        self.resultEdit.setReadOnly(True)
        self.encryptBtn.clicked.connect(self.encrypt)
        self.infoBtn.clicked.connect(self.open_info)

    def encrypt(self):
        self.statusbar.showMessage("")
        first_text = self.firstEdit.text()
        shift = self.shiftSpinBox.text()
        result_text = ""
        lang = self.chosenLanguage.currentText()
        alphabet = self.languages[lang]
        wrong_letter_message = False

        for letter in first_text:
            if letter.isalpha() and letter.upper() not in alphabet:
                wrong_letter_message = True
            if letter.isalnum() and letter.upper() in alphabet:
                new_letter = alphabet[(alphabet.index(letter.upper()) + int(shift)) % len(alphabet)]
                if letter.islower():
                    new_letter = new_letter.lower()
            else:
                new_letter = letter
            result_text += new_letter

        if wrong_letter_message:
            self.statusbar.showMessage("Символы другого алфавита не были заменены")
        self.resultEdit.setText(result_text)

    def open_info(self):
        caesar_info.show()


class MorseCipher(QMainWindow, Ui_Morse):
    def __init__(self):
        super().__init__()
        f = io.StringIO(morse_template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Шифр Морзе")

        self.infoBtn.clicked.connect(self.open_info)
        self.hintBtn.clicked.connect(self.open_hint)
        self.encryptBtn.clicked.connect(self.encrypt)

    def encrypt(self):
        first_text = self.firstText.text()
        result = ""

        con = sqlite3.connect("multisipher.sqlite")
        cur = con.cursor()

        for symb in first_text:
            morse_symb = cur.execute(f"""SELECT morse_symbol FROM morse 
                                        WHERE symbol = '{symb.capitalize()}'""").fetchone()
            result += morse_symb[0] + " "

        con.close()
        self.resultText.setText(result[:-1])

    def open_info(self):
        morse_info.show()

    def open_hint(self):
        morse_hint.show()


class BinaryCipher(QMainWindow, Ui_Binary):
    def __init__(self):
        super().__init__()
        f = io.StringIO(binary_template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Бинарный шифр+")
        self.infoBtn.clicked.connect(self.open_info)
        self.encryptBtn.setEnabled(False)
        self.chooseNS.currentTextChanged.connect(self.check)
        self.mode = "from_int"
        self.ownNS.toggled.connect(self.change_mode)
        self.encryptBtn.clicked.connect(self.encrypt)

    def change_mode(self):
        if self.ownNS.isChecked():
            self.mode = "to_int"
            self.chooseNS.setEnabled(False)
            self.encryptBtn.setEnabled(True)
        else:
            self.chooseNS.setEnabled(True)
            self.mode = "from_int"
            if self.chooseNS.currentText() != "Выберите систему счисления":
                self.encryptBtn.setEnabled(True)
            else:
                self.encryptBtn.setEnabled(False)

    def encrypt(self):
        first_num = self.first_text.text()
        try:
            if self.mode == "from_int":
                if self.chooseNS.currentText() == "2":
                    self.result_text.setText(bin(int(first_num))[2:])
                if self.chooseNS.currentText() == "8":
                    self.result_text.setText(oct(int(first_num))[2:])
                if self.chooseNS.currentText() == "10":
                    self.result_text.setText(str(int(first_num)))
                if self.chooseNS.currentText() == "16":
                    self.result_text.setText(hex(int(first_num))[2:])
            else:
                self.result_text.setText(str(int(first_num, int(self.ownNSEdit.text()))))
        except Exception:
            error = QDialog(self)
            error.resize(100, 50)
            layout = QFormLayout(error)
            ok = QDialogButtonBox()
            ok.setStandardButtons(QDialogButtonBox.Ok)
            layout.addRow("Вы ввели неправильные символы!", QLabel(self))
            layout.addWidget(ok)
            ok.accepted.connect(error.accept)

            error.exec()

    def check(self):
        if self.chooseNS.currentText() == "Выберите систему счисления":
            self.encryptBtn.setEnabled(False)
        else:
            self.encryptBtn.setEnabled(True)

    def open_info(self):
        binary_info.show()


class CaesarInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 660, 440)
        self.setWindowTitle("Шифр Цезаря")

        self.pm = QPixmap("info_caesar.jpg")
        self.info = QLabel(self)
        self.info.resize(660, 440)
        self.info.move(0, 0)
        self.info.setPixmap(self.pm)


class MorseHint(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 434, 600)
        self.setWindowTitle("Алфавит Морзе")

        self.pm = QPixmap("morse_alph.jpg")
        self.info = QLabel(self)
        self.info.resize(434, 600)
        self.info.move(0, 0)
        self.info.setPixmap(self.pm)


class MorseInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 1127, 270)
        self.setWindowTitle("Информация про Азбуку Морзе")

        self.pm = QPixmap("morse_info.png")
        self.info = QLabel(self)
        self.info.resize(1127, 270)
        self.info.move(0, 0)
        self.info.setPixmap(self.pm)


class BinaryInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 661, 174)
        self.setWindowTitle("Системы счисления")

        self.pm = QPixmap("binary_plus.png")
        self.info = QLabel(self)
        self.info.resize(661, 174)
        self.info.move(0, 0)
        self.info.setPixmap(self.pm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex_caesar = CaesarCipher()
    caesar_info = CaesarInfo()
    morse_info = MorseInfo()
    morse_hint = MorseHint()
    binary_info = BinaryInfo()
    ex_morse = MorseCipher()
    ex_binary = BinaryCipher()
    ex.show()
    sys.exit(app.exec())
