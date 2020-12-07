from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class SchoolLink(QLabel):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setText('<a href="http://www.sy.caehs.kr/main.do">홈페이지</a>')
        self.setAlignment(Qt.AlignCenter)
        self.setOpenExternalLinks(True)

        self.setStyleSheet('''
            SchoolLink {
              font-size: 30px;
            }
        ''')

