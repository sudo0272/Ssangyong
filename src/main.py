from PyQt5.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QApplication
from TopMenu import TopMenu
from SubMenu import SubMenu
from Timeline import Timeline
import requests
import re
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        container = QHBoxLayout()

        topMenu = TopMenu()
        subMenu = SubMenu(topMenu)
        content = QStackedWidget()

        schoolHistory = Timeline()

        # crawl school history
        url = 'http://sy.caehs.kr/sub/info.do?m=010401&s=sy'
        html = requests.request('GET', url).text
        data = re.findall(r'(?<=\<td\>).*?(?=</td>)', html, re.DOTALL)

        history = []
        for i in range(0, len(data), 3):
            date = data[i] + '.' + data[i + 1]
            log = ' '.join(data[i + 2].split())
            history.append((date, [log]))

        schoolHistory.setTimeline(history)

        content.addWidget(schoolHistory)

        container.addWidget(topMenu)
        container.addWidget(subMenu)
        container.addWidget(content)

        self.setLayout(container)

        with open('Window.qss') as f:
            self.setStyleSheet(f.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.show()
    app.exec_()

