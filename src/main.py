import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QSize
from Menu import Menu
from Content import Content

class Window(QWidget):
    def __init__(self):
        super().__init__()
        container = QHBoxLayout()

        menu = Menu()
        content = Content(menu)

        container.addWidget(menu)
        container.addWidget(content)

        self.setLayout(container)

        self.setStyleSheet('''
            Window {
              background-color: #ddeffb;
            }
        ''')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setMinimumSize(QSize(800, 600))
    window.setWindowTitle('쌍용고')
    window.show()
    app.exec_()

