from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont
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

        # school facility
        facilities = (
            ('일반 교실', 39),
            ('특수 교육 지원실', 3),
            ('과학실', 4),
            ('수학실', 3),
            ('컴퓨터실', 1),
            ('음악실', 1),
            ('미술실', 1),
            ('기술가정실', 1),
            ('진로상담실', 1),
            ('시청각실', 1),
            ('문헌정보실', 1),
            ('상담실', 1),
            ('보건실', 1),
            ('위클래스', 1),
            ('집중학습실', 1),
            ('비룡실', 3),
            ('창조관', 1),
            ('교무실', 8),
            ('여직원휴게실', 1),
            ('남직원휴게실', 1),
            ('샤워실', 2),
            ('교장실', 1),
            ('행정실', 1),
            ('장애인화장실', 2),
            ('학생화장실', 8),
            ('직원화장실', 8),
            ('급식실', 1),
            ('조리실', 1),
            ('학생탈의실', 2),
            ('서고', 1),
            ('창고', 1),
            ('기계실', 1),
            ('승강기', 1),
            ('서버실', 1),
            ('소회의실', 1),
            ('학생회의실', 1)
        )

        schoolFacility = QTableWidget()
        schoolFacility.setObjectName('school-facility')
        schoolFacility.horizontalHeader().hide()
        schoolFacility.verticalHeader().hide()
        schoolFacility.setColumnCount(2)
        schoolFacility.setColumnWidth(0, 200)
        schoolFacility.setShowGrid(False)
        schoolFacility.setFont(QFont('', 15))

        for i, j in enumerate(facilities):
            schoolFacility.insertRow(i)
            schoolFacility.setItem(i, 0, QTableWidgetItem(j[0]))
            schoolFacility.setItem(i, 1, QTableWidgetItem(str(j[1])))

        content.addWidget(schoolFacility)

        content.setCurrentIndex(1)

        # crawl school rewards
        # show location
        # crawl school promotion videos from youtube
        # crawl school uniform
        # homepage link

        # crawl what introduces STEM school
        # crawl pictures

        # crawl regular clubs list
        # crawl autonomous clubs list
        # crawl clubs promotion videos from youtube
        # crawl club pictures

        # crawl percentage of students who go to universities
        # crawl rewards that students got
        # crawl status of students

        # crawl status of teachers

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

