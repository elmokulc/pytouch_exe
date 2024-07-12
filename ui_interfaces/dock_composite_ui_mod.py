# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_composite.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Composites(object):
    def setupUi(self, Composites):
        Composites.setObjectName("Composites")
        Composites.resize(508, 324)
        self.dockWidget_compositesContents = QtWidgets.QWidget(Composites)
        self.dockWidget_compositesContents.setGeometry(QtCore.QRect(10, 10, 489, 302))
        self.dockWidget_compositesContents.setObjectName("dockWidget_compositesContents")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.dockWidget_compositesContents)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.spinBox_hSlider_cornerRefinementMaxIteractions = QtWidgets.QSpinBox(self.dockWidget_compositesContents)
        self.spinBox_hSlider_cornerRefinementMaxIteractions.setMinimum(1)
        self.spinBox_hSlider_cornerRefinementMaxIteractions.setMaximum(100)
        self.spinBox_hSlider_cornerRefinementMaxIteractions.setProperty("value", 10)
        self.spinBox_hSlider_cornerRefinementMaxIteractions.setObjectName("spinBox_hSlider_cornerRefinementMaxIteractions")
        self.gridLayout_10.addWidget(self.spinBox_hSlider_cornerRefinementMaxIteractions, 4, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_compositeSourceFileName = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_compositeSourceFileName.setMinimumSize(QtCore.QSize(0, 20))
        self.label_compositeSourceFileName.setMaximumSize(QtCore.QSize(200, 20))
        self.label_compositeSourceFileName.setToolTip("")
        self.label_compositeSourceFileName.setStatusTip("")
        self.label_compositeSourceFileName.setWhatsThis("")
        self.label_compositeSourceFileName.setScaledContents(False)
        self.label_compositeSourceFileName.setOpenExternalLinks(False)
        self.label_compositeSourceFileName.setObjectName("label_compositeSourceFileName")
        self.gridLayout_10.addWidget(self.label_compositeSourceFileName, 7, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 5, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hSlider_cornerRefinementMaxIterations = QtWidgets.QSlider(self.dockWidget_compositesContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hSlider_cornerRefinementMaxIterations.sizePolicy().hasHeightForWidth())
        self.hSlider_cornerRefinementMaxIterations.setSizePolicy(sizePolicy)
        self.hSlider_cornerRefinementMaxIterations.setMinimum(1)
        self.hSlider_cornerRefinementMaxIterations.setMaximum(100)
        self.hSlider_cornerRefinementMaxIterations.setSingleStep(1)
        self.hSlider_cornerRefinementMaxIterations.setPageStep(1)
        self.hSlider_cornerRefinementMaxIterations.setProperty("value", 10)
        self.hSlider_cornerRefinementMaxIterations.setTracking(False)
        self.hSlider_cornerRefinementMaxIterations.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider_cornerRefinementMaxIterations.setObjectName("hSlider_cornerRefinementMaxIterations")
        self.gridLayout_10.addWidget(self.hSlider_cornerRefinementMaxIterations, 4, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 4, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_12.setMinimumSize(QtCore.QSize(0, 20))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 7, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.comboBox_solvePnpMethod = QtWidgets.QComboBox(self.dockWidget_compositesContents)
        self.comboBox_solvePnpMethod.setObjectName("comboBox_solvePnpMethod")
        self.comboBox_solvePnpMethod.addItem("")
        self.comboBox_solvePnpMethod.addItem("")
        self.gridLayout_10.addWidget(self.comboBox_solvePnpMethod, 5, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.checkBox_cornerRefinementMethod = QtWidgets.QCheckBox(self.dockWidget_compositesContents)
        self.checkBox_cornerRefinementMethod.setText("")
        self.checkBox_cornerRefinementMethod.setChecked(True)
        self.checkBox_cornerRefinementMethod.setObjectName("checkBox_cornerRefinementMethod")
        self.gridLayout_10.addWidget(self.checkBox_cornerRefinementMethod, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_compositeSourceFilePath = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_compositeSourceFilePath.setMinimumSize(QtCore.QSize(0, 20))
        self.label_compositeSourceFilePath.setMaximumSize(QtCore.QSize(200, 20))
        self.label_compositeSourceFilePath.setToolTip("")
        self.label_compositeSourceFilePath.setStatusTip("")
        self.label_compositeSourceFilePath.setWhatsThis("")
        self.label_compositeSourceFilePath.setScaledContents(False)
        self.label_compositeSourceFilePath.setOpenExternalLinks(False)
        self.label_compositeSourceFilePath.setObjectName("label_compositeSourceFilePath")
        self.gridLayout_10.addWidget(self.label_compositeSourceFilePath, 6, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.checkBox_displayDetectMarker = QtWidgets.QCheckBox(self.dockWidget_compositesContents)
        self.checkBox_displayDetectMarker.setObjectName("checkBox_displayDetectMarker")
        self.gridLayout_10.addWidget(self.checkBox_displayDetectMarker, 9, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.checkBox_displayComposite = QtWidgets.QCheckBox(self.dockWidget_compositesContents)
        self.checkBox_displayComposite.setObjectName("checkBox_displayComposite")
        self.gridLayout_10.addWidget(self.checkBox_displayComposite, 9, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hSlider_cornerRefinementWinSize = QtWidgets.QSlider(self.dockWidget_compositesContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hSlider_cornerRefinementWinSize.sizePolicy().hasHeightForWidth())
        self.hSlider_cornerRefinementWinSize.setSizePolicy(sizePolicy)
        self.hSlider_cornerRefinementWinSize.setMinimum(1)
        self.hSlider_cornerRefinementWinSize.setMaximum(100)
        self.hSlider_cornerRefinementWinSize.setSingleStep(1)
        self.hSlider_cornerRefinementWinSize.setPageStep(1)
        self.hSlider_cornerRefinementWinSize.setProperty("value", 5)
        self.hSlider_cornerRefinementWinSize.setTracking(False)
        self.hSlider_cornerRefinementWinSize.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider_cornerRefinementWinSize.setObjectName("hSlider_cornerRefinementWinSize")
        self.gridLayout_10.addWidget(self.hSlider_cornerRefinementWinSize, 3, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pushButton_browserCompositeFile = QtWidgets.QPushButton(self.dockWidget_compositesContents)
        self.pushButton_browserCompositeFile.setObjectName("pushButton_browserCompositeFile")
        self.gridLayout_10.addWidget(self.pushButton_browserCompositeFile, 6, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pushButton_applyCompositeParam = QtWidgets.QPushButton(self.dockWidget_compositesContents)
        self.pushButton_applyCompositeParam.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_applyCompositeParam.setObjectName("pushButton_applyCompositeParam")
        self.gridLayout_10.addWidget(self.pushButton_applyCompositeParam, 8, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.spinBox_hSlider_cornerRefinementWinSize = QtWidgets.QSpinBox(self.dockWidget_compositesContents)
        self.spinBox_hSlider_cornerRefinementWinSize.setMinimum(1)
        self.spinBox_hSlider_cornerRefinementWinSize.setMaximum(100)
        self.spinBox_hSlider_cornerRefinementWinSize.setProperty("value", 5)
        self.spinBox_hSlider_cornerRefinementWinSize.setObjectName("spinBox_hSlider_cornerRefinementWinSize")
        self.gridLayout_10.addWidget(self.spinBox_hSlider_cornerRefinementWinSize, 3, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pushButton_addNewComposite = QtWidgets.QPushButton(self.dockWidget_compositesContents)
        self.pushButton_addNewComposite.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_addNewComposite.setObjectName("pushButton_addNewComposite")
        self.gridLayout_10.addWidget(self.pushButton_addNewComposite, 8, 2, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 6, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_9.setMinimumSize(QtCore.QSize(0, 20))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_compositeRuntime = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_compositeRuntime.setMinimumSize(QtCore.QSize(0, 20))
        self.label_compositeRuntime.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_compositeRuntime.setObjectName("label_compositeRuntime")
        self.gridLayout_10.addWidget(self.label_compositeRuntime, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13 = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_13.setMinimumSize(QtCore.QSize(0, 20))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_compositeID = QtWidgets.QLabel(self.dockWidget_compositesContents)
        self.label_compositeID.setMinimumSize(QtCore.QSize(0, 20))
        self.label_compositeID.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_compositeID.setObjectName("label_compositeID")
        self.gridLayout_10.addWidget(self.label_compositeID, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.retranslateUi(Composites)
        QtCore.QMetaObject.connectSlotsByName(Composites)

    def retranslateUi(self, Composites):
        _translate = QtCore.QCoreApplication.translate
        Composites.setWindowTitle(_translate("Composites", "Composites"))
        self.label_compositeSourceFileName.setText(_translate("Composites", "..."))
        self.label_10.setText(_translate("Composites", "SolvePnP method : "))
        self.label_7.setText(_translate("Composites", "CornerRefinementMethod : "))
        self.label_8.setText(_translate("Composites", "CornerRefinementMaxIterations : "))
        self.label_12.setText(_translate("Composites", "Composite source file name : "))
        self.comboBox_solvePnpMethod.setItemText(0, _translate("Composites", "cv2"))
        self.comboBox_solvePnpMethod.setItemText(1, _translate("Composites", "pycopo"))
        self.label_compositeSourceFilePath.setText(_translate("Composites", "..."))
        self.checkBox_displayDetectMarker.setText(_translate("Composites", "Primary detection"))
        self.checkBox_displayComposite.setText(_translate("Composites", "Composite detection"))
        self.pushButton_browserCompositeFile.setText(_translate("Composites", "..."))
        self.label_5.setText(_translate("Composites", "CornerRefinementWinSize : "))
        self.pushButton_applyCompositeParam.setText(_translate("Composites", "Apply now"))
        self.pushButton_addNewComposite.setText(_translate("Composites", "Add new composite"))
        self.label_11.setText(_translate("Composites", "Composite source file :"))
        self.label_9.setText(_translate("Composites", "Frequency"))
        self.label_compositeRuntime.setText(_translate("Composites", "..."))
        self.label_13.setText(_translate("Composites", "Composite ID : "))
        self.label_compositeID.setText(_translate("Composites", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Composites = QtWidgets.QWidget()
    ui = Ui_Composites()
    ui.setupUi(Composites)
    Composites.show()
    sys.exit(app.exec_())
