from Timeline import Timeline
import requests
import re
import sqlite3

class SchoolHistory(Timeline):
    def __init__(self):
        super().__init__()

        url = 'http://sy.caehs.kr/sub/info.do?m=010401&s=sy'
        html = requests.request('GET', url).text
        data = re.findall(r'(?<=\<td\>).*?(?=</td>)', html, re.DOTALL)

        self.__history = []

        for i in range(0, len(data), 3):
            date = data[i] + '.' + data[i + 1]
            log = ' '.join(data[i + 2].split())
            self.__history.append((date, [log]))

        self.setTimeline(self.__history)

