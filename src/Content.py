from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl
from TopMenu import TopMenu
from SubMenu import SubMenu
from SchoolHistory import SchoolHistory
from SchoolFacility import SchoolFacility
from SchoolLocation import SchoolLocation
from SchoolLink import SchoolLink
from Timeline import Timeline
from STEMSchool import STEMSchool

class Content(QStackedWidget):
    def __init__(self, subMenu: SubMenu):
        super().__init__()
        self.__subMenu = subMenu
        self.__indices = []
        t = 0
        for i in self.__subMenu._items:
            self.__indices.append(t)
            t += len(i)

        self.initUI()

    def initUI(self):
        self.__subMenu.subMenuChanged.connect(self.updateContent)

        self.addWidget(SchoolHistory())
        self.addWidget(SchoolFacility())

        schoolRewards = Timeline()
        # html = requests.request('GET', 'http://www.sy.caehs.kr/sub/info.do?m=010404&s=sy').text
        # schoolRewards, studentRewards = re.findall(r'(?<=\<tbody\>).*?(?=\<\/tbody\>)', html, re.DOTALL)

        # header = re.findall(r'(?<=\<th\>).?(?=\<\/th\>)', schoolRewards, re.DOTALL)
        # print(header)

        self.addWidget(schoolRewards)

        schoolLocation = SchoolLocation()
        self.addWidget(schoolLocation)

        # crawl school promotion videos from youtube
        self.addWidget(QWidget())
        # crawl school uniform
        self.addWidget(QWidget())
        # homepage link
        self.addWidget(SchoolLink())

        # crawl what introduces STEM school
        self.addWidget(STEMSchool())
        # crawl pictures
        self.addWidget(QWidget())

        # crawl regular clubs list
        self.addWidget(QWidget())
        # crawl autonomous clubs list
        self.addWidget(QWidget())
        # crawl clubs promotion videos from youtube
        self.addWidget(QWidget())
        # crawl club pictures
        self.addWidget(QWidget())

        # crawl percentage of students who go to universities
        self.addWidget(QWidget())
        # crawl rewards that students got
        self.addWidget(QWidget())
        # crawl status of students
        self.addWidget(QWidget())

        # crawl status of teachers
        self.addWidget(QWidget())

    def updateContent(self, topMenuIndex, subMenuIndex):
        self.setCurrentIndex(self.__indices[topMenuIndex] + subMenuIndex)

