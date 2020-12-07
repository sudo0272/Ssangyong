from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl
from Menu import Menu
from SchoolHistory import SchoolHistory
from SchoolFacility import SchoolFacility
from SchoolLocation import SchoolLocation
from SchoolLink import SchoolLink
from Timeline import Timeline
from STEMSchool import STEMSchool
from SchoolRewards import SchoolRewards
from StudentRewards import StudentRewards

class Content(QStackedWidget):
    def __init__(self, menu: Menu):
        super().__init__()

        self.__menu = menu

        self.initUI()

    def initUI(self):
        self.__menu.menuChanged.connect(self.updateContent)

        self.addWidget(SchoolHistory())
        self.addWidget(SchoolFacility())
        self.addWidget(SchoolRewards())
        self.addWidget(StudentRewards())
        self.addWidget(SchoolLocation())
        self.addWidget(SchoolLink())
        self.addWidget(STEMSchool())

    def updateContent(self, menuIndex):
        self.setCurrentIndex(menuIndex)

