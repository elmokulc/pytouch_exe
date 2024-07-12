# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_console.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsoleLog(object):
    def setupUi(self, ConsoleLog):
        ConsoleLog.setObjectName("ConsoleLog")
        ConsoleLog.resize(605, 263)
        self.dockWidget_ConsoleLogContents = QtWidgets.QWidget(ConsoleLog)
        self.dockWidget_ConsoleLogContents.setGeometry(QtCore.QRect(10, 20, 571, 210))
        self.dockWidget_ConsoleLogContents.setObjectName(
            "dockWidget_ConsoleLogContents"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidget_ConsoleLogContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_console = QtWidgets.QTextEdit(self.dockWidget_ConsoleLogContents)
        self.textEdit_console.setObjectName("textEdit_console")
        self.verticalLayout.addWidget(self.textEdit_console)

        self.retranslateUi(ConsoleLog)
        QtCore.QMetaObject.connectSlotsByName(ConsoleLog)

    def retranslateUi(self, ConsoleLog):
        _translate = QtCore.QCoreApplication.translate
        ConsoleLog.setWindowTitle(_translate("ConsoleLog", "Form"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ConsoleLog = QtWidgets.QWidget()
    ui = Ui_ConsoleLog()
    ui.setupUi(ConsoleLog)
    ConsoleLog.show()
    sys.exit(app.exec_())
