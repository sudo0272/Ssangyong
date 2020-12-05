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

        # initialize TopMenu
        self.setCurrentRow(0)

        self.setFixedWidth(200)

        self.itemClicked.connect(self.updateSubMenu)

    def updateSubMenu(self):
        self.topMenuChanged.emit(self.currentIndex().row())

