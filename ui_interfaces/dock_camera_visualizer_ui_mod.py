# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_camera_visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraVisualizer(object):
    def setupUi(self, CameraVisualizer):
        CameraVisualizer.setObjectName("CameraVisualizer")
        CameraVisualizer.resize(547, 696)
        self.dockWidget_CameraVisualizerContents = QtWidgets.QWidget(CameraVisualizer)
        self.dockWidget_CameraVisualizerContents.setGeometry(QtCore.QRect(20, 10, 512, 686))
        self.dockWidget_CameraVisualizerContents.setMinimumSize(QtCore.QSize(400, 400))
        self.dockWidget_CameraVisualizerContents.setObjectName("dockWidget_CameraVisualizerContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidget_CameraVisualizerContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.frame_CameraVisualizer_holder = QtWidgets.QFrame(self.dockWidget_CameraVisualizerContents)
        self.frame_CameraVisualizer_holder.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_CameraVisualizer_holder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CameraVisualizer_holder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CameraVisualizer_holder.setObjectName("frame_CameraVisualizer_holder")
        self.horizontalLayout_3.addWidget(self.frame_CameraVisualizer_holder)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.groupBox = QtWidgets.QGroupBox(self.dockWidget_CameraVisualizerContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_DisplayFrame = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_DisplayFrame.setObjectName("checkBox_DisplayFrame")
        self.horizontalLayout_2.addWidget(self.checkBox_DisplayFrame)
        self.checkBox_holdFrame = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_holdFrame.setObjectName("checkBox_holdFrame")
        self.horizontalLayout_2.addWidget(self.checkBox_holdFrame)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.comboBox_switchCh = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_switchCh.setAccessibleName("")
        self.comboBox_switchCh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_switchCh.setEditable(False)
        self.comboBox_switchCh.setMinimumContentsLength(2)
        self.comboBox_switchCh.setObjectName("comboBox_switchCh")
        self.comboBox_switchCh.addItem("")
        self.comboBox_switchCh.addItem("")
        self.comboBox_switchCh.addItem("")
        self.comboBox_switchCh.setItemText(2, "")
        self.horizontalLayout_4.addWidget(self.comboBox_switchCh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.horizontalSlider_scaleDisplay = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_scaleDisplay.setMinimum(1)
        self.horizontalSlider_scaleDisplay.setMaximum(100)
        self.horizontalSlider_scaleDisplay.setProperty("value", 100)
        self.horizontalSlider_scaleDisplay.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_scaleDisplay.setInvertedControls(False)
        self.horizontalSlider_scaleDisplay.setObjectName("horizontalSlider_scaleDisplay")
        self.horizontalLayout_5.addWidget(self.horizontalSlider_scaleDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_imageBatchCtrl = QtWidgets.QHBoxLayout()
        self.horizontalLayout_imageBatchCtrl.setObjectName("horizontalLayout_imageBatchCtrl")
        self.label_disp_imgIndex_0 = QtWidgets.QLabel(self.groupBox)
        self.label_disp_imgIndex_0.setObjectName("label_disp_imgIndex_0")
        self.horizontalLayout_imageBatchCtrl.addWidget(self.label_disp_imgIndex_0)
        self.label_disp_imgIndex_1 = QtWidgets.QLabel(self.groupBox)
        self.label_disp_imgIndex_1.setObjectName("label_disp_imgIndex_1")
        self.horizontalLayout_imageBatchCtrl.addWidget(self.label_disp_imgIndex_1)
        self.label_current_img = QtWidgets.QLabel(self.groupBox)
        self.label_current_img.setObjectName("label_current_img")
        self.horizontalLayout_imageBatchCtrl.addWidget(self.label_current_img)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_imageBatchCtrl.addItem(spacerItem7)
        self.spinBox_currentImage = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_currentImage.setMaximum(100000)
        self.spinBox_currentImage.setProperty("value", 0)
        self.spinBox_currentImage.setObjectName("spinBox_currentImage")
        self.horizontalLayout_imageBatchCtrl.addWidget(self.spinBox_currentImage)
        self.horizontalSlider_currentImage = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_currentImage.setMaximum(10000)
        self.horizontalSlider_currentImage.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_currentImage.setObjectName("horizontalSlider_currentImage")
        self.horizontalLayout_imageBatchCtrl.addWidget(self.horizontalSlider_currentImage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_imageBatchCtrl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.pushButton_IOCam = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_IOCam.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_IOCam.setObjectName("pushButton_IOCam")
        self.horizontalLayout.addWidget(self.pushButton_IOCam)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(20, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(47, 198, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 198, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(CameraVisualizer)
        self.horizontalSlider_scaleDisplay.valueChanged['int'].connect(self.label.setNum) # type: ignore
        self.spinBox_currentImage.valueChanged['int'].connect(self.label_current_img.setNum) # type: ignore
        self.horizontalSlider_currentImage.valueChanged['int'].connect(self.spinBox_currentImage.setValue) # type: ignore
        self.spinBox_currentImage.valueChanged['int'].connect(self.horizontalSlider_currentImage.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CameraVisualizer)

    def retranslateUi(self, CameraVisualizer):
        _translate = QtCore.QCoreApplication.translate
        CameraVisualizer.setWindowTitle(_translate("CameraVisualizer", "Camera visualizer"))
        self.groupBox.setTitle(_translate("CameraVisualizer", "Controls"))
        self.checkBox_DisplayFrame.setText(_translate("CameraVisualizer", "Display"))
        self.checkBox_holdFrame.setText(_translate("CameraVisualizer", "Hold Frame"))
        self.label_21.setText(_translate("CameraVisualizer", "Switch channels"))
        self.comboBox_switchCh.setItemText(0, _translate("CameraVisualizer", "RGB"))
        self.comboBox_switchCh.setItemText(1, _translate("CameraVisualizer", "BGR"))
        self.label_9.setText(_translate("CameraVisualizer", "Display slice scale :"))
        self.label.setText(_translate("CameraVisualizer", "100"))
        self.label_2.setText(_translate("CameraVisualizer", "%"))
        self.label_disp_imgIndex_0.setText(_translate("CameraVisualizer", "Selected image:"))
        self.label_disp_imgIndex_1.setText(_translate("CameraVisualizer", "N°"))
        self.label_current_img.setText(_translate("CameraVisualizer", "...."))
        self.pushButton_IOCam.setText(_translate("CameraVisualizer", "I/O Cam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraVisualizer = QtWidgets.QWidget()
    ui = Ui_CameraVisualizer()
    ui.setupUi(CameraVisualizer)
    CameraVisualizer.show()
    sys.exit(app.exec_())
