from PyQt5.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QApplication
from TopMenu import TopMenu
from SubMenu import SubMenu
from Timeline import Timeline
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        container = QHBoxLayout()

        topMenu = TopMenu()
        subMenu = SubMenu(topMenu)
        content = QStackedWidget()

        timeline = Timeline([('2022', ['hello', 'hi']), ('ho', ['aa', 'bb'])])

        content.addWidget(timeline)

        container.addWidget(topMenu)
        container.addWidget(subMenu)
        container.addWidget(content)

        self.setLayout(container)

        with open('Window.qss') as f:
            self.setStyleSheet(f.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.show()
    app.exec_()

