from TopMenu import TopMenu
from SubMenu import SubMenu
from PyQt5 import QtWidgets
import sys
import glob

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        for i in glob.glob('./**/*.qss', recursive=True):
            with open(i) as f:
                self.setStyleSheet(f.read())

        container = QtWidgets.QHBoxLayout()

        topMenu = TopMenu()
        subMenu = SubMenu(topMenu)

        container.addWidget(topMenu)
        container.addWidget(subMenu)

        self.setLayout(container)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.show()
    app.exec_()

