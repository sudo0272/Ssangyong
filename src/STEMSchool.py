from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout

class STEMSchool(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        container = QVBoxLayout()

        title = QLabel('과학중점고등학교란?')
        title.setObjectName('stemschool-title')
        content = QLabel('기존의 다른 고등학교와는 달리 수학·과학 교육에 중점을 둔 고등학교입니다. 과학고와는 다르지만 최소 과학실 4개와 수학교실 2개를 갖추게 되어 심도있는 수업이 가능하다는 장점이 있습니다.  수학·과학이 수업단위에서 차지하는 비율은 과학 고등학교 60%, 일반계 고등학교는 30%, 과학중점 고등학교 45% 입니다. 1학년 때 연간 60시간 이상의 과학체험활동과 함께 한국과학창의재단에서 제작한 과학교양, 과학융합 과목을 추가로 이수하게 되고, 2학년 때부터 과정에 따라 실험, 탐구 중심의 교육을 받게 됩니다. 또한 과학중점학교는 자율학교로 지정되어 시설비로 5억 원, 매년 1억 5천만 원의 운영비를 지원받습니다. (위키백과)')
        content.setObjectName('stemschool-content')
        content.setWordWrap(True)

        container.addWidget(title)
        container.addWidget(content)
        container.addStretch()

        self.setLayout(container)

        with open('./STEMSchool.qss') as f:
            self.setStyleSheet(f.read())

