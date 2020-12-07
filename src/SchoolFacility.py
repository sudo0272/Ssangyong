from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

class SchoolFacility(QTableWidget):
    def __init__(self):
        super().__init__()

        self.__facilities = (
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

        self.initUI()

    def initUI(self):
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setColumnCount(2)
        self.setColumnWidth(0, 200)
        self.setShowGrid(False)
        self.setFont(QFont('', 15))

        for i, j in enumerate(self.__facilities):
            self.insertRow(i)
            self.setItem(i, 0, QTableWidgetItem(j[0]))
            self.setItem(i, 1, QTableWidgetItem(str(j[1])))

        self.setStyleSheet('''
            #school-facility {
              width: 100%;
            }
        ''')

