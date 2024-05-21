# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from SSP_Core import *

from time import sleep

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_ok.clicked.connect(self.select_name)

        self.ui.pushButton_paper.clicked.connect(self.p1_paper)
        self.ui.pushButton_paper.clicked.connect(self.zudecken)
        self.ui.pushButton_paper.clicked.connect(self.play_game)

        self.ui.pushButton_rock.clicked.connect(self.p1_rock)
        self.ui.pushButton_rock.clicked.connect(self.zudecken)
        self.ui.pushButton_rock.clicked.connect(self.play_game)

        self.ui.pushButton_scissor.clicked.connect(self.p1_scissor)
        self.ui.pushButton_scissor.clicked.connect(self.zudecken)
        self.ui.pushButton_scissor.clicked.connect(self.play_game)

        self.ui.pushButton_exit.clicked.connect(app.closeAllWindows)

    def select_name(self):
        p1.name = self.ui.lineEdit_name.text()
        # print(p1.__dict__)

    def p1_paper(self):
        p1.move = "paper"
        # print(p1.__dict__)

    def p1_scissor(self):
        p1.move = "scissor"
        # print(p1.__dict__)

    def p1_rock(self):
        p1.move = "rock"
        # print(p1.__dict__)

    def zudecken(self):
        self.ui.pushButton_paperp2.setText("?")
        self.ui.pushButton_rockp2.setText("?")
        self.ui.pushButton_scissorp2.setText("?")

    def play_game(self):
        p2.choose_random_move()
        a = choose_winner(p1, p2)
        self.ui.label_gewinner.setText(f"Der Gewinner ist: {a}!")
        if p2.move == "rock":
            self.ui.pushButton_rockp2.setText("Stein")
        elif p2.move == "scissor":
            self.ui.pushButton_scissorp2.setText("Schere")
        elif p2.move == "paper":
            self.ui.pushButton_paperp2.setText("Papier")
        else:
            pass


if __name__ == "__main__":
    p1 = Character("")
    p2 = Character("NPC")

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
