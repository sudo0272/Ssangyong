from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class TopMenu(QListWidget):
    def __init__(self):
        super().__init__()

        self.__top_menus = [
            '학교',
            '학생',
            '교사'
        ]

        self.initUI()

    def initUI(self):
        self.addItems(self.__top_menus)

        self.itemClicked.connect(self.open_submenu)

    def open_submenu(self):
        #TODO: add codes

        print(self.currentIndex().row())

