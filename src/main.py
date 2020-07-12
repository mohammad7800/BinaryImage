# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import display
import cv2
import numpy as np
import os
import sys
# variables
img = ''
width, height = 0, 0
img_0 = ''
img_1 = ''
final_width, final_height = 0, 0
final_img = ''
main_color = (0, 0, 0)
bg_color = (255, 255, 255)
ress = []
icon = b'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'
# end

def iconFromBase64(base64):
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(base64))
    icon = QtGui.QIcon(pixmap)
    return icon


class Ui_MainWindow(QtWidgets.QMainWindow):
    def display(self):
        global final_img
        if display.onScreen:
            self.ui.close()
        self.ui = display.Ui_DisplayWindow()
        self.ui.setupUi(final_img)
        self.ui.show()

    def closeEvent(self, event):
        if display.onScreen:
            self.ui.quitt()
        event.accept()

    def setupUi(self):
        global icon
        self.setObjectName("self")
        self.setFixedSize(483, 351)
        self.setIconSize(QtCore.QSize(24, 24))
        self.setWindowIcon(iconFromBase64(icon))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setAnimated(True)
        self.mainwindow = self
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.edt_browse = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_browse.setGeometry(QtCore.QRect(20, 30, 321, 20))
        self.edt_browse.setInputMask("")
        self.edt_browse.setObjectName("edt_browse")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(360, 15, 75, 23))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(360, 43, 75, 23))
        self.btn_save.setObjectName("btn_save")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 250, 471, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.btn_display = QtWidgets.QPushButton(self.centralwidget)
        self.btn_display.setGeometry(QtCore.QRect(200, 195, 81, 23))
        self.btn_display.setObjectName("btn_display")
        self.btn_progress = QtWidgets.QPushButton(self.centralwidget)
        self.btn_progress.setGeometry(QtCore.QRect(200, 220, 81, 23))
        self.btn_progress.setObjectName("btn_progress")
        self.lb_Done = QtWidgets.QLabel(self.centralwidget)
        self.lb_Done.setEnabled(True)
        self.lb_Done.setGeometry(QtCore.QRect(210, 280, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lb_Done.setFont(font)
        self.lb_Done.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_Done.setObjectName("lb_Done")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 80, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(8)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(80, 110, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(13)
        self.lb_width = QtWidgets.QLabel(self.centralwidget)
        self.lb_width.setGeometry(QtCore.QRect(20, 80, 47, 16))
        self.lb_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_width.setObjectName("lb_width")
        self.lb_height = QtWidgets.QLabel(self.centralwidget)
        self.lb_height.setGeometry(QtCore.QRect(20, 110, 47, 16))
        self.lb_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_height.setObjectName("lb_height")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 90, 200, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 100, 81, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        for _ in ress:
            self.comboBox.addItem('')
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 160, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.sens = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sens.setGeometry(QtCore.QRect(80, 210, 60, 17))
        self.sens.setMinimum(0)
        self.sens.setMaximum(1)
        self.sens.setValue(0.5)
        self.sens.setSingleStep(0.1)
        self.lb_sens = QtWidgets.QLabel(self.centralwidget)
        self.lb_sens.setGeometry(QtCore.QRect(30, 210, 40, 17))
        self.lb_sens.setText('Sens :')
        self.btn_bgcolor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bgcolor.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.btn_bgcolor.setObjectName("btn_bgcolor")
        self.btn_maincolor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_maincolor.setGeometry(QtCore.QRect(290, 160, 81, 23))
        self.btn_maincolor.setObjectName("btn_maincolor")
        self.clr_bg = QtWidgets.QLabel(self.centralwidget)
        self.clr_bg.setEnabled(True)
        self.clr_bg.setGeometry(QtCore.QRect(127, 163, 16, 16))
        self.clr_bg.setAutoFillBackground(False)
        self.clr_bg.setText("")
        self.clr_bg.setObjectName("clr_bg")
        self.clr_bg.setStyleSheet('background-color: #fff')
        self.clr_main = QtWidgets.QLabel(self.centralwidget)
        self.clr_main.setGeometry(QtCore.QRect(270, 163, 16, 16))
        self.clr_main.setText("")
        self.clr_main.setObjectName("clr_main")
        self.clr_main.setStyleSheet('background-color: #000')
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Binary Image"))
        self.spinBox.valueChanged.connect(self.spinbox_value_changed)
        self.spinBox_2.valueChanged.connect(self.spinbox_value_changed)
        self.edt_browse.setText(_translate("self", "Choose Your Image..."))
        self.btn_browse.setText(_translate("self", "Browse"))
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_save.setText(_translate("self", "Save"))
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_progress.setText(_translate("self", "Progress"))
        self.btn_progress.clicked.connect(self.btn_progress_clicked)
        self.btn_display.setText(_translate("self", "Display"))
        self.btn_display.clicked.connect(self.display)
        self.lb_Done.setText(_translate("self", ""))
        self.lb_width.setText(_translate("self", "Width : "))
        self.lb_height.setText(_translate("self", "Height : "))
        self.label_3.setText(_translate("self", "Final Image size : ? x ?"))
        for l in range(len(ress)):
            self.comboBox.setItemText(l, _translate("self", ress[l]))
        self.checkBox.setText(_translate("self", "Gradient"))
        self.btn_bgcolor.setText(_translate("self", "Pick bg color"))
        self.btn_bgcolor.clicked.connect(self.color_pick_bg)
        self.btn_maincolor.setText(_translate("self", "Pick main color"))
        self.btn_maincolor.clicked.connect(self.color_pick_main)
        self.menuFile.setTitle(_translate("self", "File"))
        self.menuHelp.setTitle(_translate("self", "Help"))
        self.actionOpen.setText(_translate("self", "Browse"))
        self.actionOpen.triggered.connect(self.btn_browse_clicked)
        self.actionSave.setText(_translate("self", "Save"))
        self.actionSave.triggered.connect(self.btn_save_clicked)
        self.actionExit.setText(_translate("self", "Exit"))
        self.actionExit.triggered.connect(sys.exit)
        self.actionAbout.setText(_translate("self", "About"))
        self.actionAbout.triggered.connect(self.show_about)
        self.show()

    def spinbox_value_changed(self):
        global final_width, final_height
        final_width, final_height = self.standard_Image_Size()
        self.display_img_size()

    def color_pick_main(self):
        global main_color
        color = QtWidgets.QColorDialog.getColor()
        main_color = color.getRgb()[:3]
        self.clr_main.setStyleSheet('background-color: {};'.format(color.name()))
        if all([main_color == (0, 0, 0), bg_color == (255, 255, 255)]):
            self.checkBox.setEnabled(True)
        else:
            self.checkBox.setChecked(False)
            self.checkBox.setEnabled(False)

    def color_pick_bg(self):
        global bg_color
        color = QtWidgets.QColorDialog.getColor()
        bg_color = color.getRgb()[:3]
        self.clr_bg.setStyleSheet('background-color: {};'.format(color.name()))
        if all([main_color == (0, 0, 0), bg_color == (255, 255, 255)]):
            self.checkBox.setEnabled(True)
        else:
            self.checkBox.setChecked(False)
            self.checkBox.setEnabled(False)

    def display_img_size(self):
        global final_height, final_width
        self.label_3.setText("Final Image size : {width} x {height}".format(width=final_width, height=final_height))

    def show_about(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle('About')
        dialog.setText('This programm is created by mohammadamin Alidoost\n\nContact me: mohammad_780@yahoo.com')
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dialog.exec()

    def btn_browse_clicked(self):
        global img, width, height, final_height, final_width
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Imgaes (*.png *.jpg *.jpeg)')[0]
        if not filename:
            return
        self.edt_browse.setText(filename)
        img = cv2.imread(filename, 0)
        height, width = img.shape[:2]
        final_width, final_height = self.standard_Image_Size()
        self.display_img_size()

    def btn_save_clicked(self):
        global final_img
        path = QtWidgets.QFileDialog.getSaveFileName(filter='Images(*.Jpg *.Jpeg *.png)')
        cv2.imwrite(path[0], final_img)

    def btn_progress_clicked(self):
        global final_img, final_height, final_width, width, height, img_1, img_0
        self.lb_Done.setText('')
        self.progressBar.setValue(0)
        sens = int(self.sens.value() * 255)
        img_1 = cv2.imread('res/' + self.comboBox.currentText() + '/' + list(filter(lambda x: x.lower().startswith('1'), os.listdir('res/' + self.comboBox.currentText())))[0], 0)
        img_0 = cv2.imread('res/' + self.comboBox.currentText() + '/' + list(filter(lambda x: x.lower().startswith('0'), os.listdir('res/' + self.comboBox.currentText())))[0], 0)
        if self.edt_browse.text() == 'Choose Your Image...':
            return
        final_img = np.zeros((final_height, final_width, 3), np.uint8)
        img_tm = cv2.resize(img, (int(width / self.spinBox.value()), int(height / self.spinBox_2.value())))
        tmp = []
        if self.checkBox.isChecked():
            for i in range(img_tm.shape[0]):
                tmp.append([])
                for j in range(img_tm.shape[1]):
                    if img_tm[i][j] < sens:
                        tmp[i].append((1, img_tm[i][j]))
                    else:
                        tmp[i].append((0, img_tm[i][j]))
        else:
            for i in range(img_tm.shape[0]):
                tmp.append([])
                for j in range(img_tm.shape[1]):
                    if img_tm[i][j] < sens:
                        tmp[i].append(1)
                    else:
                        tmp[i].append(0)
        for i in range(final_height):
            for j in range(final_width):
                tm = tmp[i // 13][j // 8]
                if self.checkBox.isChecked():
                    if tm[0] == 0:
                        val = tm[1]
                        if img_0[i % 13][j % 8] > 127:
                            final_img[i][j][0] = 255
                            final_img[i][j][1] = 255
                            final_img[i][j][2] = 255
                        else:
                            final_img[i][j][0] = val
                            final_img[i][j][1] = val
                            final_img[i][j][2] = val
                    else:
                        if img_1[i % 13][j % 8] > 127:
                            final_img[i][j][0] = 255
                            final_img[i][j][1] = 255
                            final_img[i][j][2] = 255
                        else:
                            final_img[i][j][0] = val
                            final_img[i][j][1] = val
                            final_img[i][j][2] = val
                else:
                    if tm == 0:
                        if img_0[i % 13][j % 8] > 127:
                            final_img[i][j][0] = bg_color[0]
                            final_img[i][j][1] = bg_color[1]
                            final_img[i][j][2] = bg_color[2]
                        else:
                            final_img[i][j][0] = main_color[0]
                            final_img[i][j][1] = main_color[1]
                            final_img[i][j][2] = main_color[2]
                    else:
                        if img_1[i % 13][j % 8] > 127:
                            final_img[i][j][0] = bg_color[0]
                            final_img[i][j][1] = bg_color[1]
                            final_img[i][j][2] = bg_color[2]
                        else:
                            final_img[i][j][0] = main_color[0]
                            final_img[i][j][1] = main_color[1]
                            final_img[i][j][2] = main_color[2]
        self.lb_Done.setText('Done !')
        self.progressBar.setValue(100)
        self.ui.update(final_img)

    def standard_Image_Size(self):
        global width, height
        spin = self.spinBox.value()
        spin2 = self.spinBox_2.value()
        width_res = int(width / spin) * 8
        height_res = int(height / spin2) * 13
        return width_res, height_res


if __name__ == "__main__":
    def btn_clicked(i):
        sys.exit(0)
    app = QtWidgets.QApplication(sys.argv)
    # res detect
    try:
        for i in os.listdir('res'):
            if os.path.isdir('res/' + i):
                ress.append(i)
    except FileNotFoundError:
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Critical)
        dialog.setText('Failed to access /res directory')
        dialog.setWindowTitle('Error')
        dialog.setWindowIcon(iconFromBase64(icon))
        dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        dialog.buttonClicked.connect(btn_clicked)
        dialog.show()
        QtCore.QEventLoop().exec_()
    # end
    ui = Ui_MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())
