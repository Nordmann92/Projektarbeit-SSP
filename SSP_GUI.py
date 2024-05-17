from SSP_Core import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout,
                             QLabel, QLineEdit, QWidget, QFormLayout, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("SSP")
        # self.setFixedSize(400, 400)

        # main_widget
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # mein widget Elemente
        self.label_greetings = QLabel("Willkommen zu unserem Spiel 'Schere, Stein, Papier'")
        self.main_layout.addWidget(self.label_greetings, 0, 0, 1, 2)

        self.show_winner = QLineEdit()
        self.main_layout.addWidget(self.show_winner, 2, 0, 1, 2)

        self.button_exit = QPushButton("Exit")
        self.main_layout.addWidget(self.button_exit, 3, 0)

        self.button_play_again = QPushButton("nochmal?")
        self.main_layout.addWidget(self.button_play_again, 3, 1)

        # p1_widget
        self.p1_widget = QWidget()
        self.p1_layout = QGridLayout()
        self.p1_widget.setLayout(self.p1_layout)

        # p1 widget Elemente
        self.p1_label_name = QLabel("Name:")
        self.p1_layout.addWidget(self.p1_label_name, 0, 0)

        self.p1_enter_name = QLineEdit()
        self.p1_layout.addWidget(self.p1_enter_name, 0, 1)

        self.p1_button_use_name = QPushButton("OK")
        self.p1_layout.addWidget(self.p1_button_use_name, 0, 2)
        self.p1_button_use_name.clicked.connect(self.select_name)

        self.p1_show_stats = QLineEdit("Show stats")
        self.p1_layout.addWidget(self.p1_show_stats, 1, 1)

        self.p1_button_scissor = QPushButton("Schere")
        self.p1_button_scissor.clicked.connect(self.p1_pick_scissor)
        self.p1_layout.addWidget(self.p1_button_scissor, 2, 0)

        self.p1_button_rock = QPushButton("Stein")
        self.p1_button_rock.clicked.connect(self.p1_pick_rock)
        self.p1_layout.addWidget(self.p1_button_rock, 2, 1)

        self.p1_button_paper = QPushButton("Papier")
        self.p1_button_paper.clicked.connect(self.p1_pick_paper)
        self.p1_layout.addWidget(self.p1_button_paper, 2, 2)

        # p2_widget
        self.p2_widget = QWidget()
        self.p2_layout = QGridLayout()
        self.p2_widget.setLayout(self.p2_layout)

        # p2 widget Elemente

        self.p2_label_name = QLabel("NPC")
        self.p2_layout.addWidget(self.p2_label_name, 0, 1)

        self.p2_show_stats = QLineEdit("Show stats")
        self.p2_layout.addWidget(self.p2_show_stats, 1, 1)

        self.p2_scissor = QPushButton("Schere")
        self.p2_layout.addWidget(self.p2_scissor, 2, 0)


        self.p2_rock = QPushButton("Stein")
        self.p2_layout.addWidget(self.p2_rock, 2, 1)

        self.p2_paper = QPushButton("Papier")
        self.p2_layout.addWidget(self.p2_paper, 2, 2)


        self.main_layout.addWidget(self.p1_widget, 1, 0)
        self.main_layout.addWidget(self.p2_widget, 1, 1)
        self.setCentralWidget(self.main_widget)

        self.show()

    def select_name(self):
        p1.name = self.p1_enter_name.text()
        print(p1.__dict__)
    def p1_pick_scissor(self):
        p1.move = "scissor"

    def p1_pick_rock(self):
        p1.move = "rock"

    def p1_pick_paper(self):
        p1.move = "paper"

if __name__ == "__main__":
    p1 = Character("")
    p2 = Character("NPC")

    app = QApplication([])
    window = MainWindow()
    app.exec()

