# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_igus_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IgusManager(object):
    def setupUi(self, IgusManager):
        IgusManager.setObjectName("IgusManager")
        IgusManager.resize(739, 822)
        self.dockWidget_IgusManagerContents = QtWidgets.QWidget(IgusManager)
        self.dockWidget_IgusManagerContents.setGeometry(QtCore.QRect(40, 50, 422, 378))
        self.dockWidget_IgusManagerContents.setObjectName("dockWidget_IgusManagerContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidget_IgusManagerContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidget_IgusManagerContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_linear = QtWidgets.QWidget()
        self.tab_linear.setObjectName("tab_linear")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_linear)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dockWidget_IgusManagerContents_1 = QtWidgets.QWidget(self.tab_linear)
        self.dockWidget_IgusManagerContents_1.setObjectName("dockWidget_IgusManagerContents_1")
        self.dockWidget_CompositeManagerContents = QtWidgets.QVBoxLayout(self.dockWidget_IgusManagerContents_1)
        self.dockWidget_CompositeManagerContents.setObjectName("dockWidget_CompositeManagerContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox_run_linear = QtWidgets.QCheckBox(self.dockWidget_IgusManagerContents_1)
        self.checkBox_run_linear.setText("")
        self.checkBox_run_linear.setObjectName("checkBox_run_linear")
        self.horizontalLayout.addWidget(self.checkBox_run_linear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_reconnect_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_reconnect_linear.setObjectName("pushButton_reconnect_linear")
        self.horizontalLayout.addWidget(self.pushButton_reconnect_linear)
        self.pushButton_debug_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_debug_linear.setObjectName("pushButton_debug_linear")
        self.horizontalLayout.addWidget(self.pushButton_debug_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox_port_linear = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_1)
        self.comboBox_port_linear.setObjectName("comboBox_port_linear")
        self.horizontalLayout_2.addWidget(self.comboBox_port_linear)
        self.pushButton_refresh_device = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_refresh_device.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refresh_device.setIcon(icon)
        self.pushButton_refresh_device.setObjectName("pushButton_refresh_device")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh_device)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.spinBox_velocity_linear = QtWidgets.QSpinBox(self.dockWidget_IgusManagerContents_1)
        self.spinBox_velocity_linear.setMinimum(1)
        self.spinBox_velocity_linear.setMaximum(3000)
        self.spinBox_velocity_linear.setProperty("value", 1000)
        self.spinBox_velocity_linear.setObjectName("spinBox_velocity_linear")
        self.horizontalLayout_3.addWidget(self.spinBox_velocity_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.comboBox_dir_linear = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_1)
        self.comboBox_dir_linear.setObjectName("comboBox_dir_linear")
        self.comboBox_dir_linear.addItem("")
        self.comboBox_dir_linear.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_dir_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.doubleSpinBox_value_linear = QtWidgets.QDoubleSpinBox(self.dockWidget_IgusManagerContents_1)
        self.doubleSpinBox_value_linear.setMinimum(0.0)
        self.doubleSpinBox_value_linear.setMaximum(9999999.99)
        self.doubleSpinBox_value_linear.setObjectName("doubleSpinBox_value_linear")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_value_linear)
        self.comboBox_value_unit_linear = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_1)
        self.comboBox_value_unit_linear.setObjectName("comboBox_value_unit_linear")
        self.comboBox_value_unit_linear.addItem("")
        self.comboBox_value_unit_linear.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_value_unit_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.pushButton_refresh_pos_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_refresh_pos_linear.setText("")
        self.pushButton_refresh_pos_linear.setIcon(icon)
        self.pushButton_refresh_pos_linear.setObjectName("pushButton_refresh_pos_linear")
        self.horizontalLayout_9.addWidget(self.pushButton_refresh_pos_linear)
        self.label_current_pos_linear = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_1)
        self.label_current_pos_linear.setObjectName("label_current_pos_linear")
        self.horizontalLayout_9.addWidget(self.label_current_pos_linear)
        self.comboBox_currentPos_unit_linear = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_1)
        self.comboBox_currentPos_unit_linear.setObjectName("comboBox_currentPos_unit_linear")
        self.comboBox_currentPos_unit_linear.addItem("")
        self.comboBox_currentPos_unit_linear.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_currentPos_unit_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_Home_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_Home_linear.setObjectName("pushButton_Home_linear")
        self.horizontalLayout_8.addWidget(self.pushButton_Home_linear)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.pushButton_zero_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_zero_linear.setObjectName("pushButton_zero_linear")
        self.horizontalLayout_8.addWidget(self.pushButton_zero_linear)
        self.pushButton_Move_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_Move_linear.setObjectName("pushButton_Move_linear")
        self.horizontalLayout_8.addWidget(self.pushButton_Move_linear)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.pushButton_Stop_linear = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_1)
        self.pushButton_Stop_linear.setObjectName("pushButton_Stop_linear")
        self.horizontalLayout_8.addWidget(self.pushButton_Stop_linear)
        self.dockWidget_CompositeManagerContents.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dockWidget_CompositeManagerContents.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.dockWidget_IgusManagerContents_1)
        self.tabWidget.addTab(self.tab_linear, "")
        self.tab_rotate = QtWidgets.QWidget()
        self.tab_rotate.setObjectName("tab_rotate")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_rotate)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.tab_rotate)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dockWidget_IgusManagerContents_2 = QtWidgets.QWidget(self.widget_2)
        self.dockWidget_IgusManagerContents_2.setObjectName("dockWidget_IgusManagerContents_2")
        self.dockWidget_CompositeManagerContents_2 = QtWidgets.QVBoxLayout(self.dockWidget_IgusManagerContents_2)
        self.dockWidget_CompositeManagerContents_2.setObjectName("dockWidget_CompositeManagerContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.checkBox_run_rotate = QtWidgets.QCheckBox(self.dockWidget_IgusManagerContents_2)
        self.checkBox_run_rotate.setText("")
        self.checkBox_run_rotate.setObjectName("checkBox_run_rotate")
        self.horizontalLayout_4.addWidget(self.checkBox_run_rotate)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.pushButton_reconnect_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_reconnect_rotate.setObjectName("pushButton_reconnect_rotate")
        self.horizontalLayout_4.addWidget(self.pushButton_reconnect_rotate)
        self.pushButton_debug_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_debug_rotate.setObjectName("pushButton_debug_rotate")
        self.horizontalLayout_4.addWidget(self.pushButton_debug_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.comboBox_port_rotate = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_2)
        self.comboBox_port_rotate.setObjectName("comboBox_port_rotate")
        self.horizontalLayout_7.addWidget(self.comboBox_port_rotate)
        self.pushButton_refresh_device_2 = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_refresh_device_2.setText("")
        self.pushButton_refresh_device_2.setIcon(icon)
        self.pushButton_refresh_device_2.setObjectName("pushButton_refresh_device_2")
        self.horizontalLayout_7.addWidget(self.pushButton_refresh_device_2)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.spinBox_velocity_rotate = QtWidgets.QSpinBox(self.dockWidget_IgusManagerContents_2)
        self.spinBox_velocity_rotate.setMinimum(1)
        self.spinBox_velocity_rotate.setMaximum(3000)
        self.spinBox_velocity_rotate.setProperty("value", 4)
        self.spinBox_velocity_rotate.setObjectName("spinBox_velocity_rotate")
        self.horizontalLayout_10.addWidget(self.spinBox_velocity_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.comboBox_dir_rotate = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_2)
        self.comboBox_dir_rotate.setObjectName("comboBox_dir_rotate")
        self.comboBox_dir_rotate.addItem("")
        self.comboBox_dir_rotate.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_dir_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.doubleSpinBox_value_rotate = QtWidgets.QDoubleSpinBox(self.dockWidget_IgusManagerContents_2)
        self.doubleSpinBox_value_rotate.setMinimum(0.0)
        self.doubleSpinBox_value_rotate.setMaximum(9999999.99)
        self.doubleSpinBox_value_rotate.setProperty("value", 400.0)
        self.doubleSpinBox_value_rotate.setObjectName("doubleSpinBox_value_rotate")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_value_rotate)
        self.comboBox_value_unit_rotate = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_2)
        self.comboBox_value_unit_rotate.setObjectName("comboBox_value_unit_rotate")
        self.comboBox_value_unit_rotate.addItem("")
        self.comboBox_value_unit_rotate.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_value_unit_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem14)
        self.pushButton_refresh_pos_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_refresh_pos_rotate.setText("")
        self.pushButton_refresh_pos_rotate.setIcon(icon)
        self.pushButton_refresh_pos_rotate.setObjectName("pushButton_refresh_pos_rotate")
        self.horizontalLayout_13.addWidget(self.pushButton_refresh_pos_rotate)
        self.label_current_pos_rotate = QtWidgets.QLabel(self.dockWidget_IgusManagerContents_2)
        self.label_current_pos_rotate.setObjectName("label_current_pos_rotate")
        self.horizontalLayout_13.addWidget(self.label_current_pos_rotate)
        self.comboBox_currentPos_unit_rotate = QtWidgets.QComboBox(self.dockWidget_IgusManagerContents_2)
        self.comboBox_currentPos_unit_rotate.setObjectName("comboBox_currentPos_unit_rotate")
        self.comboBox_currentPos_unit_rotate.addItem("")
        self.comboBox_currentPos_unit_rotate.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_currentPos_unit_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_Home_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_Home_rotate.setObjectName("pushButton_Home_rotate")
        self.horizontalLayout_14.addWidget(self.pushButton_Home_rotate)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem15)
        self.pushButton_zero_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_zero_rotate.setObjectName("pushButton_zero_rotate")
        self.horizontalLayout_14.addWidget(self.pushButton_zero_rotate)
        self.pushButton_Move_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_Move_rotate.setObjectName("pushButton_Move_rotate")
        self.horizontalLayout_14.addWidget(self.pushButton_Move_rotate)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.pushButton_Stop_rotate = QtWidgets.QPushButton(self.dockWidget_IgusManagerContents_2)
        self.pushButton_Stop_rotate.setObjectName("pushButton_Stop_rotate")
        self.horizontalLayout_14.addWidget(self.pushButton_Stop_rotate)
        self.dockWidget_CompositeManagerContents_2.addLayout(self.horizontalLayout_14)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dockWidget_CompositeManagerContents_2.addItem(spacerItem17)
        self.verticalLayout_3.addWidget(self.dockWidget_IgusManagerContents_2)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab_rotate, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(IgusManager)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_refresh_device.clicked.connect(self.pushButton_refresh_device_2.click) # type: ignore
        self.pushButton_refresh_device_2.clicked.connect(self.pushButton_refresh_device.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(IgusManager)

    def retranslateUi(self, IgusManager):
        _translate = QtCore.QCoreApplication.translate
        IgusManager.setWindowTitle(_translate("IgusManager", "Igus Manager"))
        self.label.setText(_translate("IgusManager", "Connect:"))
        self.pushButton_reconnect_linear.setText(_translate("IgusManager", "reconnect"))
        self.pushButton_debug_linear.setText(_translate("IgusManager", "debug"))
        self.label_2.setText(_translate("IgusManager", "Port:"))
        self.label_6.setText(_translate("IgusManager", "Velocity:"))
        self.label_3.setText(_translate("IgusManager", "Direction:"))
        self.comboBox_dir_linear.setItemText(0, _translate("IgusManager", "R"))
        self.comboBox_dir_linear.setItemText(1, _translate("IgusManager", "L"))
        self.label_4.setText(_translate("IgusManager", "Value:"))
        self.comboBox_value_unit_linear.setItemText(0, _translate("IgusManager", "step"))
        self.comboBox_value_unit_linear.setItemText(1, _translate("IgusManager", "mm"))
        self.label_7.setText(_translate("IgusManager", "Current postion:"))
        self.label_current_pos_linear.setText(_translate("IgusManager", "_____"))
        self.comboBox_currentPos_unit_linear.setItemText(0, _translate("IgusManager", "mm"))
        self.comboBox_currentPos_unit_linear.setItemText(1, _translate("IgusManager", "step"))
        self.pushButton_Home_linear.setText(_translate("IgusManager", "Home"))
        self.pushButton_zero_linear.setText(_translate("IgusManager", "Zero"))
        self.pushButton_Move_linear.setText(_translate("IgusManager", "Move"))
        self.pushButton_Stop_linear.setText(_translate("IgusManager", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linear), _translate("IgusManager", "Linear"))
        self.label_5.setText(_translate("IgusManager", "Connect:"))
        self.pushButton_reconnect_rotate.setText(_translate("IgusManager", "reconnect"))
        self.pushButton_debug_rotate.setText(_translate("IgusManager", "debug"))
        self.label_8.setText(_translate("IgusManager", "Port:"))
        self.label_9.setText(_translate("IgusManager", "Velocity:"))
        self.label_10.setText(_translate("IgusManager", "Direction:"))
        self.comboBox_dir_rotate.setItemText(0, _translate("IgusManager", "R"))
        self.comboBox_dir_rotate.setItemText(1, _translate("IgusManager", "L"))
        self.label_11.setText(_translate("IgusManager", "Value:"))
        self.comboBox_value_unit_rotate.setItemText(0, _translate("IgusManager", "step"))
        self.comboBox_value_unit_rotate.setItemText(1, _translate("IgusManager", "mm"))
        self.label_12.setText(_translate("IgusManager", "Current postion:"))
        self.label_current_pos_rotate.setText(_translate("IgusManager", "_____"))
        self.comboBox_currentPos_unit_rotate.setItemText(0, _translate("IgusManager", "mm"))
        self.comboBox_currentPos_unit_rotate.setItemText(1, _translate("IgusManager", "step"))
        self.pushButton_Home_rotate.setText(_translate("IgusManager", "Home"))
        self.pushButton_zero_rotate.setText(_translate("IgusManager", "Zero"))
        self.pushButton_Move_rotate.setText(_translate("IgusManager", "Move"))
        self.pushButton_Stop_rotate.setText(_translate("IgusManager", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rotate), _translate("IgusManager", "Rotate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IgusManager = QtWidgets.QWidget()
    ui = Ui_IgusManager()
    ui.setupUi(IgusManager)
    IgusManager.show()
    sys.exit(app.exec_())
