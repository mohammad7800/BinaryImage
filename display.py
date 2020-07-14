from PyQt5 import QtCore, QtGui, QtWidgets
import sys

onScreen = False


class Ui_DisplayWindow(QtWidgets.QMainWindow):

    def setupUi(self, ready, icon):
        global onScreen
        onScreen = True
        self.setObjectName("self")
        self.setFixedSize(755, 504)
        self.move(100, 200)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 755, 504))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        try:
            if not ready:
                self.label.setText("Nothing to display")
                self.label.setStyleSheet('color: #fff;background-color: #000;')
                self.label.setAlignment(QtCore.Qt.AlignCenter)
        except ValueError:
            height, width, channel = ready.shape
            bytesPerLine = 3 * width
            qImg = QtGui.QImage(ready.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.setFixedSize(width, height)
            self.label.setFixedSize(width, height)
            self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Display"))

    def update(self, img):
        height, width, channel = img.shape
        self.setFixedSize(width, height)
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setFixedSize(width, height)
        self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def quitt(self):
        sys.exit(0)

    def closeEvent(self, event):
        global onScreen
        onScreen = False
        event.accept()

