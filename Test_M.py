from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout
from tkinter import Frame, Tk, Label, Button

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.my_label = Label(master, text="Wilkommen", borderwidth=1, relief="raised", width=70)
        self.my_button = Button(master, text="Exit", relief="sunken", command=self.change_label)

        self.my_label.grid(row=0, column=0, ipadx=60, ipady=60, padx=30, pady=30)
        self.my_button.grid(row=1, column=0, ipadx=60, ipady=60, padx=30, pady=30)

        self.my_label1 = Label(master, text="Wilkommen", borderwidth=1, relief="raised", width=70)
        self.my_button1 = Button(master, text="Exit", relief="sunken", command=self.change_label)

        self.my_label1.grid(row=0, column=0, ipadx=60, ipady=60, padx=30, pady=30)
        self.my_button1.grid(row=1, column=0, ipadx=60, ipady=60, padx=30, pady=30)

    def change_label(self):
        self.my_label.config(bg="light blue")
        self.my_label1.config(bg="light pink")


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("GUI")
        self.button = QPushButton("Push Button")
        self.setCentralWidget(self.button)

        main_widget = Frame(root, bg="lightgrey", width=200, height=200)
        main_widget.grid(row=0, column=0, rowspan=3, columnspan=3)

        self.setFixedSize(900, 500)
        self.show()


root = Tk()
app = Application(root)
app.mainloop()

app = QApplication([])
window = MainWindow()
app.exec()