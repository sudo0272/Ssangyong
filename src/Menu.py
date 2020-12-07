from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import pyqtSignal

class Menu(QListWidget):
    menuChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self._items = [
            "역사",
            "시설",
            "학교 표창",
            "학생 표창",
            "위치",
            "홈페이지",
            "과학중점학교"
        ]

        self.initUI()

    def initUI(self):
        self.setFixedWidth(200)

        self.addItems(self._items)

        self.itemClicked.connect(self.updateContent)

        with open('Menu.qss') as f:
            self.setStyleSheet(f.read())

    def updateContent(self):
        self.menuChanged.emit(self.currentIndex().row())

