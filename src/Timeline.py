from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from TimelineElement import TimelineElement
from typing import *

class Timeline(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def setTimeline(self, items: List[Tuple[str, List[str]]]):
        self.__items = items

        for item in self.__items:
            self.__timelineElements.append(TimelineElement(item[0], item[1]))
            self.__container.addWidget(self.__timelineElements[-1])

        self.__container.addStretch()

    def initUI(self):
        self.__container = QVBoxLayout()

        self.__timelineElements: List[TimelineElement] = []

        self.setLayout(self.__container)

        with open('Timeline.qss') as f:
            self.setStyleSheet(f.read())

