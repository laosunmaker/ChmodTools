# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tools.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(352, 341)
        icon = QIcon()
        icon.addFile(u"th.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Or = QCheckBox(self.centralwidget)
        self.Or.setObjectName(u"Or")
        font = QFont()
        font.setPointSize(11)
        self.Or.setFont(font)

        self.gridLayout.addWidget(self.Or, 3, 1, 1, 1)

        self.Ux = QCheckBox(self.centralwidget)
        self.Ux.setObjectName(u"Ux")
        self.Ux.setFont(font)

        self.gridLayout.addWidget(self.Ux, 1, 3, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Gr = QCheckBox(self.centralwidget)
        self.Gr.setObjectName(u"Gr")
        self.Gr.setFont(font)

        self.gridLayout.addWidget(self.Gr, 2, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.Ow = QCheckBox(self.centralwidget)
        self.Ow.setObjectName(u"Ow")
        self.Ow.setFont(font)

        self.gridLayout.addWidget(self.Ow, 3, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Ox = QCheckBox(self.centralwidget)
        self.Ox.setObjectName(u"Ox")
        self.Ox.setFont(font)

        self.gridLayout.addWidget(self.Ox, 3, 3, 1, 1)

        self.Sgid = QCheckBox(self.centralwidget)
        self.Sgid.setObjectName(u"Sgid")
        self.Sgid.setFont(font)

        self.gridLayout.addWidget(self.Sgid, 4, 2, 1, 1)

        self.EnableSGT = QCheckBox(self.centralwidget)
        self.EnableSGT.setObjectName(u"EnableSGT")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.EnableSGT.setFont(font1)

        self.gridLayout.addWidget(self.EnableSGT, 5, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1, 1))
        self.label.setMaximumSize(QSize(500, 30))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.ans = QLineEdit(self.centralwidget)
        self.ans.setObjectName(u"ans")
        font3 = QFont()
        font3.setPointSize(18)
        self.ans.setFont(font3)

        self.gridLayout.addWidget(self.ans, 5, 0, 1, 3)

        self.Sticky = QCheckBox(self.centralwidget)
        self.Sticky.setObjectName(u"Sticky")
        self.Sticky.setFont(font)

        self.gridLayout.addWidget(self.Sticky, 4, 3, 1, 1)

        self.Gx = QCheckBox(self.centralwidget)
        self.Gx.setObjectName(u"Gx")
        self.Gx.setFont(font)

        self.gridLayout.addWidget(self.Gx, 2, 3, 1, 1)

        self.Suid = QCheckBox(self.centralwidget)
        self.Suid.setObjectName(u"Suid")
        self.Suid.setFont(font)

        self.gridLayout.addWidget(self.Suid, 4, 1, 1, 1)

        self.Uw = QCheckBox(self.centralwidget)
        self.Uw.setObjectName(u"Uw")
        self.Uw.setFont(font)

        self.gridLayout.addWidget(self.Uw, 1, 2, 1, 1)

        self.Ur = QCheckBox(self.centralwidget)
        self.Ur.setObjectName(u"Ur")
        self.Ur.setFont(font)

        self.gridLayout.addWidget(self.Ur, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.Gw = QCheckBox(self.centralwidget)
        self.Gw.setObjectName(u"Gw")
        self.Gw.setFont(font)

        self.gridLayout.addWidget(self.Gw, 2, 2, 1, 1)

        self.calcbutton = QPushButton(self.centralwidget)
        self.calcbutton.setObjectName(u"calcbutton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calcbutton.sizePolicy().hasHeightForWidth())
        self.calcbutton.setSizePolicy(sizePolicy1)
        self.calcbutton.setFont(font3)

        self.gridLayout.addWidget(self.calcbutton, 6, 0, 1, 4)

        self.calcbackbutton = QPushButton(self.centralwidget)
        self.calcbackbutton.setObjectName(u"calcbackbutton")
        self.calcbackbutton.setFont(font3)

        self.gridLayout.addWidget(self.calcbackbutton, 7, 0, 1, 4)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setRowStretch(2, 5)
        self.gridLayout.setRowStretch(3, 5)
        self.gridLayout.setRowStretch(4, 5)
        self.gridLayout.setRowStretch(5, 5)
        self.gridLayout.setRowStretch(6, 5)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ChmodTools by lsmaker", None))
        self.Or.setText(QCoreApplication.translate("MainWindow", u"\u8bfb(r)", None))
        self.Ux.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c(x)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u62e5\u6709\u8005(User)\uff1a", None))
        self.Gr.setText(QCoreApplication.translate("MainWindow", u"\u8bfb(r)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u4eba(Others):", None))
        self.Ow.setText(QCoreApplication.translate("MainWindow", u"\u5199(w)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7fa4\u7ec4(Group):", None))
        self.Ox.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c(x)", None))
        self.Sgid.setText(QCoreApplication.translate("MainWindow", u"sgid", None))
        self.EnableSGT.setText(QCoreApplication.translate("MainWindow", u"\u9644\u52a0\u6743\u9650", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"chmod\u6743\u9650\u5c0f\u5de5\u5177", None))
        self.Sticky.setText(QCoreApplication.translate("MainWindow", u"sticky", None))
        self.Gx.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c(x)", None))
        self.Suid.setText(QCoreApplication.translate("MainWindow", u"suid", None))
        self.Uw.setText(QCoreApplication.translate("MainWindow", u"\u5199(w)", None))
        self.Ur.setText(QCoreApplication.translate("MainWindow", u"\u8bfb(r)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9644\u52a0\u6743\u9650(SGT):", None))
        self.Gw.setText(QCoreApplication.translate("MainWindow", u"\u5199(w)", None))
        self.calcbutton.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5411\u8ba1\u7b97", None))
        self.calcbackbutton.setText(QCoreApplication.translate("MainWindow", u"\u9006\u5411\u8ba1\u7b97", None))
    # retranslateUi

