from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class SchoolLocation(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setUrl(QUrl('http://ssangyonghsmap.kro.kr'))

