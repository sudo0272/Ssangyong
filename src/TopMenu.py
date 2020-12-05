from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class TopMenu(QListWidget):
    def __init__(self):
        super().__init__()

        self.__top_menus = [
            '학교',
            '학생',
            '교사'
        ]

        self.addItems(self.__top_menus)

