# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_console_log.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsoleLog(object):
    def setupUi(self, ConsoleLog):
        ConsoleLog.setObjectName("ConsoleLog")
        ConsoleLog.resize(313, 263)
        self.dockWidget_ConsoleLogContents = QtWidgets.QWidget(ConsoleLog)
        self.dockWidget_ConsoleLogContents.setGeometry(QtCore.QRect(10, 20, 292, 228))
        self.dockWidget_ConsoleLogContents.setObjectName("dockWidget_ConsoleLogContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidget_ConsoleLogContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.dockWidget_ConsoleLogContents)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_console = QtWidgets.QTextEdit(self.widget)
        self.textEdit_console.setObjectName("textEdit_console")
        self.gridLayout.addWidget(self.textEdit_console, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(ConsoleLog)
        QtCore.QMetaObject.connectSlotsByName(ConsoleLog)

    def retranslateUi(self, ConsoleLog):
        _translate = QtCore.QCoreApplication.translate
        ConsoleLog.setWindowTitle(_translate("ConsoleLog", "Console Log"))
        self.textEdit_console.setHtml(_translate("ConsoleLog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsoleLog = QtWidgets.QWidget()
    ui = Ui_ConsoleLog()
    ui.setupUi(ConsoleLog)
    ConsoleLog.show()
    sys.exit(app.exec_())
