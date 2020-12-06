from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import pyqtSignal
from TopMenu import TopMenu

class SubMenu(QListWidget):
    subMenuChanged = pyqtSignal(int, int)
    
    def __init__(self, topMenu: TopMenu):
        super().__init__()

        self.__topMenu = topMenu

        self._items = [
            # 학교
            [
                "역사",
                "시설",
                "표창",
                "위치",
                "홍보영상",
                "교복",
                "홈페이지"
            ],

            # 과학중점학교
            [
                "소개",
                "사진"
            ],

            # 동아리
            [
                "정규",
                "자율",
                "홍보영상",
                "사진"
            ],

            # 학생
            [
                "진학",
                "표창",
                "현황"
            ],

            # 교사
            [
                "현황"
            ]
        ]

        self.initUI()

    def initUI(self):
        self.__topMenu.topMenuChanged.connect(self.updateList)
        self.__topMenuIndex = 0

        # initialize SubMenu
        self.updateList(0)

        self.setFixedWidth(200)

        self.itemClicked.connect(self.updateContent)

        with open('SubMenu.qss') as f:
            self.setStyleSheet(f.read())

    def updateList(self, index: int):
        self.__topMenuIndex = index

        self.clear()
        self.addItems(self._items[index])
        self.setCurrentRow(0)

    def updateContent(self):
        self.subMenuChanged.emit(self.__topMenuIndex, self.currentIndex().row())

