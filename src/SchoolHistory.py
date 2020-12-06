from Timeline import Timeline
import requests
import re

class SchoolHistory(Timeline):
    def __init__(self):
        super().__init__()

        self.__url = 'http://sy.caehs.kr/sub/info.do?m=010401&s=sy'
        self.__html = requests.request('GET', self.__url).text
        self.__data = re.findall(r'(?<=\<td\>).*?(?=</td>)', self.__html, re.DOTALL)

        self.__history = []

        for i in range(0, len(self.__data), 3):
            date = self.__data[i] + '.' + self.__data[i + 1]
            log = ' '.join(self.__data[i + 2].split())
            self.__history.append((date, [log]))

        self.setTimeline(self.__history)

