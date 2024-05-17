# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(983, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 936, 590))
        self.mainwidget = QGridLayout(self.gridLayoutWidget)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainwidget.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_p2 = QGridLayout()
        self.gridLayout_p2.setObjectName(u"gridLayout_p2")
        self.pushButton_scissorp2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_scissorp2.setObjectName(u"pushButton_scissorp2")
        self.pushButton_scissorp2.setMinimumSize(QSize(150, 150))
        self.pushButton_scissorp2.setMaximumSize(QSize(150, 150))
        self.pushButton_scissorp2.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_p2.addWidget(self.pushButton_scissorp2, 2, 2, 1, 1)

        self.listView_p2 = QListView(self.gridLayoutWidget)
        self.listView_p2.setObjectName(u"listView_p2")
        self.listView_p2.setMinimumSize(QSize(150, 300))
        self.listView_p2.setMaximumSize(QSize(150, 300))

        self.gridLayout_p2.addWidget(self.listView_p2, 1, 2, 1, 1)

        self.label_name_p2 = QLabel(self.gridLayoutWidget)
        self.label_name_p2.setObjectName(u"label_name_p2")
        self.label_name_p2.setMinimumSize(QSize(150, 50))
        self.label_name_p2.setMaximumSize(QSize(150, 50))
        self.label_name_p2.setAlignment(Qt.AlignCenter)
        self.label_name_p2.setMargin(4)

        self.gridLayout_p2.addWidget(self.label_name_p2, 0, 2, 1, 1)

        self.pushButton_paperp2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_paperp2.setObjectName(u"pushButton_paperp2")
        self.pushButton_paperp2.setMinimumSize(QSize(150, 150))
        self.pushButton_paperp2.setMaximumSize(QSize(150, 150))
        self.pushButton_paperp2.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_p2.addWidget(self.pushButton_paperp2, 2, 3, 1, 1)

        self.pushButton_rockp2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_rockp2.setObjectName(u"pushButton_rockp2")
        self.pushButton_rockp2.setMinimumSize(QSize(150, 150))
        self.pushButton_rockp2.setMaximumSize(QSize(150, 150))
        self.pushButton_rockp2.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_p2.addWidget(self.pushButton_rockp2, 2, 0, 1, 1)


        self.mainwidget.addLayout(self.gridLayout_p2, 1, 1, 1, 1)

        self.gridLayout_p1 = QGridLayout()
        self.gridLayout_p1.setObjectName(u"gridLayout_p1")
        self.label_name = QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(150, 50))
        self.label_name.setMaximumSize(QSize(150, 50))
        self.label_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_p1.addWidget(self.label_name, 0, 1, 1, 1)

        self.pushButton_scissor = QPushButton(self.gridLayoutWidget)
        self.pushButton_scissor.setObjectName(u"pushButton_scissor")
        self.pushButton_scissor.setMinimumSize(QSize(150, 150))
        self.pushButton_scissor.setMaximumSize(QSize(150, 150))
        self.pushButton_scissor.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_p1.addWidget(self.pushButton_scissor, 2, 2, 1, 1)

        self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_name.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_p1.addWidget(self.lineEdit_name, 0, 2, 1, 1)

        self.pushButton_ok = QPushButton(self.gridLayoutWidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setMinimumSize(QSize(50, 0))
        self.pushButton_ok.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_p1.addWidget(self.pushButton_ok, 0, 3, 1, 1)

        self.pushButton_rock = QPushButton(self.gridLayoutWidget)
        self.pushButton_rock.setObjectName(u"pushButton_rock")
        self.pushButton_rock.setMinimumSize(QSize(150, 150))
        self.pushButton_rock.setMaximumSize(QSize(160, 160))
        self.pushButton_rock.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_p1.addWidget(self.pushButton_rock, 2, 1, 1, 1)

        self.pushButton_paper = QPushButton(self.gridLayoutWidget)
        self.pushButton_paper.setObjectName(u"pushButton_paper")
        self.pushButton_paper.setMinimumSize(QSize(150, 150))
        self.pushButton_paper.setMaximumSize(QSize(150, 150))
        self.pushButton_paper.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_p1.addWidget(self.pushButton_paper, 2, 3, 1, 1)

        self.listView_score = QListView(self.gridLayoutWidget)
        self.listView_score.setObjectName(u"listView_score")
        self.listView_score.setMinimumSize(QSize(150, 300))
        self.listView_score.setMaximumSize(QSize(150, 300))

        self.gridLayout_p1.addWidget(self.listView_score, 1, 2, 1, 1)


        self.mainwidget.addLayout(self.gridLayout_p1, 1, 0, 1, 1)

        self.pushButton_exit = QPushButton(self.gridLayoutWidget)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.mainwidget.addWidget(self.pushButton_exit, 3, 0, 1, 2)

        self.label_gewinner = QLabel(self.gridLayoutWidget)
        self.label_gewinner.setObjectName(u"label_gewinner")
        self.label_gewinner.setAlignment(Qt.AlignCenter)

        self.mainwidget.addWidget(self.label_gewinner, 2, 0, 1, 2)

        self.label_willkommen = QLabel(self.gridLayoutWidget)
        self.label_willkommen.setObjectName(u"label_willkommen")

        self.mainwidget.addWidget(self.label_willkommen, 0, 0, 1, 2)
        self.label_willkommen.setAlignment(Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 983, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_rock.clicked.connect(self.pushButton_rock.toggle)

        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_scissorp2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_name_p2.setText(QCoreApplication.translate("MainWindow", u"NPC", None))
        self.pushButton_paperp2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.pushButton_rockp2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.pushButton_scissor.setText(QCoreApplication.translate("MainWindow", u"Schere", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_rock.setText(QCoreApplication.translate("MainWindow", u"Stein", None))
        self.pushButton_paper.setText(QCoreApplication.translate("MainWindow", u"Papier", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"Aufh\u00f6ren", None))
        self.label_gewinner.setText(QCoreApplication.translate("MainWindow", u"Gewinner", None))
        self.label_willkommen.setText(QCoreApplication.translate("MainWindow", u"Willkommen zu Stein, Schere, Papier!", None))
    # retranslateUi

