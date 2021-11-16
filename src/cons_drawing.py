#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    print ("Error: This program needs PySide module.", file=sys.stderr)
    sys.exit(1)

from cm_lisp_graphic import *


class MainWidget(QMainWindow):
    """ Create the main widget """

    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        widget = QWidget()
        
        graphicalGroup = GraphicalLispGroupWidget(self)
        screenshotBtn = QPushButton(QIcon("../icons/screenshot"), 'prendre une capture')

        layout.addWidget(graphicalGroup)
        layout.addWidget(screenshotBtn)

        self.setLayout(layout)

        screenshotBtn.clicked.connect(graphicalGroup.glisp_widget.takeScreenshot)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = MainWidget()
    client.show()
    sys.exit(app.exec_())
