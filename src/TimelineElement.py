from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from typing import *

class TimelineElement(QWidget):
    def __init__(self, title: str, logs: List[str]):
        super().__init__()

        self.__title = title;
        self.__logs = logs

        self.initUI()

    def initUI(self):
        self.__container = QVBoxLayout()

        self.__header = QLabel(self.__title)
        self.__header.setObjectName('timeline-element-header')
        self.__container.addWidget(self.__header)

        self.__items: List[QLabel] = []
        for log in self.__logs:
            self.__items.append(QLabel(log, objectName='timeline-element-item'))
            self.__container.addWidget(self.__items[-1])

        self.setLayout(self.__container)

        with open('TimelineElement.qss') as f:
            self.setStyleSheet(f.read())

