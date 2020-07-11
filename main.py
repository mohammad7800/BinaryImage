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
First = True
# end

# res detect
for i in os.listdir('res'):
    if os.path.isdir('res/' + i):
        ress.append(i)
# end

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
        self.setObjectName("self")
        self.setFixedSize(483, 351)
        self.setIconSize(QtCore.QSize(24, 24))
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
        self.actionExit.triggered.connect(exit)
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
                    if img_tm[i][j] < 127:
                        tmp[i].append((1, img_tm[i][j]))
                    else:
                        tmp[i].append((0, img_tm[i][j]))
        else:
            for i in range(img_tm.shape[0]):
                tmp.append([])
                for j in range(img_tm.shape[1]):
                    if img_tm[i][j] < 127:
                        tmp[i].append(1)
                    else:
                        tmp[i].append(0)
        percent_check = 0
        percent = 0
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    sys.exit(app.exec_())
