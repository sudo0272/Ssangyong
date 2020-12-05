from TopMenu import TopMenu
from SubMenu import SubMenu
from PyQt5 import QtWidgets
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        container = QtWidgets.QHBoxLayout()

        topMenu = TopMenu()
        subMenu = SubMenu(topMenu)

        container.addWidget(topMenu)
        container.addWidget(subMenu)

        self.setLayout(container)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

