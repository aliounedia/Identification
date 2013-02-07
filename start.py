# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysoft/mysoft.ui'
#
# Created: Tue Jan 15 19:35:55 2013
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from Identification import *
import sys
from PyQt4 import QtCore, QtGui
import sqlite
from  manage_window import *
_debug=True

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None , application =None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # The application
        self.application  = application

        # Hide The Title Bar
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # `QTCore` utilise les signaux pour activer , les evenements
        # sur le Widget, I l'image des listeneur sous Java,
        # Add un signal avec ui_object.connect(<ui>,
        #  Signa, whatToDo if signal
        QtCore.QObject.connect(self.ui.pushButton,
                               QtCore.SIGNAL("clicked()"),
                               self.indentify_user)

##        QtCore.QObject.connect(self,
##                            QtCore.SIGNAL('destroyed()'),
##                            self.onQuit)

        # Hide Window Task bar
        hide_Taskmgr()
        # Hide Window Task Manager
        hide_taskbar()
      
    def  indentify_user(self):
        print 'Indentify User'
        sqlite.insert(
             self.ui.lineEdit.text(),
             self.ui.lineEdit_2.text())
        # Hide Window Task bar
        unhide_Taskmgr()
        # Hide Window Task Manager
        unhide_taskbar()
      
        self.application.exit()

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4(application = app)
    myapp.show()
    sys.exit(app.exec_())
