# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_virtual_visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VirtualVisualizer(object):
    def setupUi(self, VirtualVisualizer):
        VirtualVisualizer.setObjectName("VirtualVisualizer")
        VirtualVisualizer.resize(700, 859)
        self.dockWidget_VirtualVisualizerContents = QtWidgets.QWidget(VirtualVisualizer)
        self.dockWidget_VirtualVisualizerContents.setGeometry(QtCore.QRect(10, 20, 671, 821))
        self.dockWidget_VirtualVisualizerContents.setMinimumSize(QtCore.QSize(400, 400))
        self.dockWidget_VirtualVisualizerContents.setObjectName("dockWidget_VirtualVisualizerContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidget_VirtualVisualizerContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidget_VirtualVisualizerContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_stlObj_name = QtWidgets.QLabel(self.dockWidget_VirtualVisualizerContents)
        self.label_stlObj_name.setObjectName("label_stlObj_name")
        self.horizontalLayout.addWidget(self.label_stlObj_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_loadStlObj = QtWidgets.QPushButton(self.dockWidget_VirtualVisualizerContents)
        self.pushButton_loadStlObj.setObjectName("pushButton_loadStlObj")
        self.horizontalLayout.addWidget(self.pushButton_loadStlObj)
        self.pushButton_razViews = QtWidgets.QPushButton(self.dockWidget_VirtualVisualizerContents)
        self.pushButton_razViews.setObjectName("pushButton_razViews")
        self.horizontalLayout.addWidget(self.pushButton_razViews)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidget_VirtualVisualizerContents)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_VirtualVisualizer_holder = QtWidgets.QFrame(self.tab_3)
        self.frame_VirtualVisualizer_holder.setMinimumSize(QtCore.QSize(400, 600))
        self.frame_VirtualVisualizer_holder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_VirtualVisualizer_holder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_VirtualVisualizer_holder.setObjectName("frame_VirtualVisualizer_holder")
        self.horizontalLayout_7.addWidget(self.frame_VirtualVisualizer_holder)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_current_point = QtWidgets.QLabel(self.tab)
        self.label_current_point.setObjectName("label_current_point")
        self.horizontalLayout_3.addWidget(self.label_current_point)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.comboBox_scale_factor = QtWidgets.QComboBox(self.tab)
        self.comboBox_scale_factor.setObjectName("comboBox_scale_factor")
        self.comboBox_scale_factor.addItem("")
        self.comboBox_scale_factor.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_scale_factor)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_interest_point = QtWidgets.QComboBox(self.tab)
        self.comboBox_interest_point.setObjectName("comboBox_interest_point")
        self.comboBox_interest_point.addItem("")
        self.comboBox_interest_point.addItem("")
        self.comboBox_interest_point.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_interest_point)
        self.pushButton_storeCurrenPoint = QtWidgets.QPushButton(self.tab)
        self.pushButton_storeCurrenPoint.setObjectName("pushButton_storeCurrenPoint")
        self.horizontalLayout_2.addWidget(self.pushButton_storeCurrenPoint)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_point_1 = QtWidgets.QLabel(self.tab)
        self.label_point_1.setObjectName("label_point_1")
        self.gridLayout_3.addWidget(self.label_point_1, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_point_3 = QtWidgets.QLabel(self.tab)
        self.label_point_3.setObjectName("label_point_3")
        self.gridLayout_3.addWidget(self.label_point_3, 3, 1, 1, 1)
        self.label_point_2 = QtWidgets.QLabel(self.tab)
        self.label_point_2.setObjectName("label_point_2")
        self.gridLayout_3.addWidget(self.label_point_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_triPointRef = QtWidgets.QCheckBox(self.tab)
        self.checkBox_triPointRef.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_triPointRef.setChecked(False)
        self.checkBox_triPointRef.setObjectName("checkBox_triPointRef")
        self.horizontalLayout_4.addWidget(self.checkBox_triPointRef)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(self.dockWidget_VirtualVisualizerContents)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.comboBox_customActor = QtWidgets.QComboBox(self.widget)
        self.comboBox_customActor.setObjectName("comboBox_customActor")
        self.comboBox_customActor.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_customActor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_currentActorColor = QtWidgets.QLabel(self.widget)
        self.label_currentActorColor.setObjectName("label_currentActorColor")
        self.horizontalLayout_6.addWidget(self.label_currentActorColor)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.pushButton_color = QtWidgets.QPushButton(self.widget)
        self.pushButton_color.setObjectName("pushButton_color")
        self.horizontalLayout_6.addWidget(self.pushButton_color)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_solType = QtWidgets.QComboBox(self.widget)
        self.comboBox_solType.setObjectName("comboBox_solType")
        self.comboBox_solType.addItem("")
        self.comboBox_solType.addItem("")
        self.gridLayout.addWidget(self.comboBox_solType, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)
        self.doubleSpinBox_rvec_offset_Y = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rvec_offset_Y.setDecimals(5)
        self.doubleSpinBox_rvec_offset_Y.setMinimum(-9999.0)
        self.doubleSpinBox_rvec_offset_Y.setMaximum(9999.0)
        self.doubleSpinBox_rvec_offset_Y.setSingleStep(0.01)
        self.doubleSpinBox_rvec_offset_Y.setObjectName("doubleSpinBox_rvec_offset_Y")
        self.gridLayout.addWidget(self.doubleSpinBox_rvec_offset_Y, 5, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.doubleSpinBox_tvec_offset_X = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tvec_offset_X.setDecimals(5)
        self.doubleSpinBox_tvec_offset_X.setMinimum(-9999.0)
        self.doubleSpinBox_tvec_offset_X.setMaximum(9999.0)
        self.doubleSpinBox_tvec_offset_X.setSingleStep(0.5)
        self.doubleSpinBox_tvec_offset_X.setProperty("value", 34.5)
        self.doubleSpinBox_tvec_offset_X.setObjectName("doubleSpinBox_tvec_offset_X")
        self.gridLayout.addWidget(self.doubleSpinBox_tvec_offset_X, 1, 2, 1, 1)
        self.doubleSpinBox_rvec_offset_Z = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rvec_offset_Z.setDecimals(5)
        self.doubleSpinBox_rvec_offset_Z.setMinimum(-9999.0)
        self.doubleSpinBox_rvec_offset_Z.setMaximum(9999.0)
        self.doubleSpinBox_rvec_offset_Z.setSingleStep(0.01)
        self.doubleSpinBox_rvec_offset_Z.setProperty("value", 0.28)
        self.doubleSpinBox_rvec_offset_Z.setObjectName("doubleSpinBox_rvec_offset_Z")
        self.gridLayout.addWidget(self.doubleSpinBox_rvec_offset_Z, 5, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)
        self.doubleSpinBox_rvec_offset_X = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rvec_offset_X.setDecimals(5)
        self.doubleSpinBox_rvec_offset_X.setMinimum(-9999.0)
        self.doubleSpinBox_rvec_offset_X.setMaximum(9999.0)
        self.doubleSpinBox_rvec_offset_X.setSingleStep(0.01)
        self.doubleSpinBox_rvec_offset_X.setObjectName("doubleSpinBox_rvec_offset_X")
        self.gridLayout.addWidget(self.doubleSpinBox_rvec_offset_X, 5, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.doubleSpinBox_tvec_offset_Y = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tvec_offset_Y.setDecimals(5)
        self.doubleSpinBox_tvec_offset_Y.setMinimum(-9999.0)
        self.doubleSpinBox_tvec_offset_Y.setMaximum(9999.0)
        self.doubleSpinBox_tvec_offset_Y.setSingleStep(0.5)
        self.doubleSpinBox_tvec_offset_Y.setProperty("value", 4.0)
        self.doubleSpinBox_tvec_offset_Y.setObjectName("doubleSpinBox_tvec_offset_Y")
        self.gridLayout.addWidget(self.doubleSpinBox_tvec_offset_Y, 1, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 4, 1, 1)
        self.doubleSpinBox_tvec_offset_Z = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tvec_offset_Z.setDecimals(5)
        self.doubleSpinBox_tvec_offset_Z.setMinimum(-9999.0)
        self.doubleSpinBox_tvec_offset_Z.setMaximum(9999.0)
        self.doubleSpinBox_tvec_offset_Z.setSingleStep(0.5)
        self.doubleSpinBox_tvec_offset_Z.setProperty("value", -1.0)
        self.doubleSpinBox_tvec_offset_Z.setObjectName("doubleSpinBox_tvec_offset_Z")
        self.gridLayout.addWidget(self.doubleSpinBox_tvec_offset_Z, 1, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(VirtualVisualizer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VirtualVisualizer)

    def retranslateUi(self, VirtualVisualizer):
        _translate = QtCore.QCoreApplication.translate
        VirtualVisualizer.setWindowTitle(_translate("VirtualVisualizer", "Virtual visuliazer"))
        self.label.setText(_translate("VirtualVisualizer", "STL object:"))
        self.label_stlObj_name.setText(_translate("VirtualVisualizer", "..."))
        self.pushButton_loadStlObj.setText(_translate("VirtualVisualizer", "Load"))
        self.pushButton_razViews.setText(_translate("VirtualVisualizer", "Reset views"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("VirtualVisualizer", "Virtual Scene"))
        self.label_7.setText(_translate("VirtualVisualizer", "Current point position: "))
        self.label_current_point.setText(_translate("VirtualVisualizer", "..."))
        self.comboBox_scale_factor.setItemText(0, _translate("VirtualVisualizer", "mm"))
        self.comboBox_scale_factor.setItemText(1, _translate("VirtualVisualizer", "m"))
        self.label_3.setText(_translate("VirtualVisualizer", "Define point: "))
        self.comboBox_interest_point.setItemText(0, _translate("VirtualVisualizer", "point_1"))
        self.comboBox_interest_point.setItemText(1, _translate("VirtualVisualizer", "point_2"))
        self.comboBox_interest_point.setItemText(2, _translate("VirtualVisualizer", "point_3"))
        self.pushButton_storeCurrenPoint.setText(_translate("VirtualVisualizer", "Store"))
        self.label_2.setText(_translate("VirtualVisualizer", "Point_1:"))
        self.label_6.setText(_translate("VirtualVisualizer", "X, Y, Z coordinates"))
        self.label_4.setText(_translate("VirtualVisualizer", "Point_2:"))
        self.label_point_1.setText(_translate("VirtualVisualizer", "..."))
        self.label_5.setText(_translate("VirtualVisualizer", "Point_3:"))
        self.label_point_3.setText(_translate("VirtualVisualizer", "..."))
        self.label_point_2.setText(_translate("VirtualVisualizer", "..."))
        self.checkBox_triPointRef.setText(_translate("VirtualVisualizer", "Plots points"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VirtualVisualizer", "Capture points"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("VirtualVisualizer", "Customizing"))
        self.label_9.setText(_translate("VirtualVisualizer", "Actor"))
        self.comboBox_customActor.setItemText(0, _translate("VirtualVisualizer", "None"))
        self.label_10.setText(_translate("VirtualVisualizer", "Define color"))
        self.label_currentActorColor.setText(_translate("VirtualVisualizer", "...."))
        self.pushButton_color.setText(_translate("VirtualVisualizer", "Set Color"))
        self.comboBox_solType.setItemText(0, _translate("VirtualVisualizer", "pre_sol"))
        self.comboBox_solType.setItemText(1, _translate("VirtualVisualizer", "full_sol"))
        self.label_15.setText(_translate("VirtualVisualizer", "Z [rad]"))
        self.label_8.setText(_translate("VirtualVisualizer", "Rvec offset:"))
        self.label_17.setText(_translate("VirtualVisualizer", "X [rad]"))
        self.label_18.setText(_translate("VirtualVisualizer", "Sol type:"))
        self.label_13.setText(_translate("VirtualVisualizer", "Y [mm]"))
        self.label_11.setText(_translate("VirtualVisualizer", "Tvec offset:"))
        self.label_16.setText(_translate("VirtualVisualizer", "Y [rad]"))
        self.label_12.setText(_translate("VirtualVisualizer", "X [mm]"))
        self.label_14.setText(_translate("VirtualVisualizer", "Z [mm]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VirtualVisualizer = QtWidgets.QWidget()
    ui = Ui_VirtualVisualizer()
    ui.setupUi(VirtualVisualizer)
    VirtualVisualizer.show()
    sys.exit(app.exec_())
