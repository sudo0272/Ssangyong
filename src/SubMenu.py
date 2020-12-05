from PyQt5 import QtWidgets
from TopMenu import TopMenu

class SubMenu(QtWidgets.QListWidget):
    def __init__(self, topMenu: TopMenu):
        super().__init__()

        self.__topMenu = topMenu

        self.__items = [
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

        # initialize SubMenu
        self.updateList(0)

        self.setFixedWidth(200)

    def updateList(self, index: int):
        self.clear()
        self.addItems(self.__items[index])
        self.setCurrentRow(0)

