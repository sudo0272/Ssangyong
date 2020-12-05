from PyQt5 import QtWidgets, QtCore

class TopMenu(QtWidgets.QListWidget):
    topMenuChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.__items = [
            '학교',
            '과학중점학교',
            '동아리',
            '학생',
            '교사'
        ]

        self.initUI()

    def initUI(self):
        self.addItems(self.__items)

        self.itemClicked.connect(self.openSubMenu)

    def openSubMenu(self):
        self.topMenuChanged.emit(self.currentIndex().row())

