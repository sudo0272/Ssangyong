from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class TopMenu(QListWidget):
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

        self.itemClicked.connect(self.openSubmenu)

    def openSubmenu(self):
        #TODO: add codes

        print(self.currentIndex().row())

