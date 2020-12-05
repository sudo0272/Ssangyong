from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from TimelineElement import TimelineElement
from typing import *

class Timeline(QWidget):
    def __init__(self, items: List[Tuple[str, List[str]]]):
        super().__init__()

        self.__items = items

        self.initUI()

    def initUI(self):
        self.__container = QVBoxLayout()

        self.__timelineElements: List[TimelineElement] = []
        for item in self.__items:
            self.__timelineElements.append(TimelineElement(item[0], item[1]))
            self.__container.addWidget(self.__timelineElements[-1])

        self.__container.addStretch()

        self.setLayout(self.__container)

        with open('Timeline.qss') as f:
            self.setStyleSheet(f.read())

