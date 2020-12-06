from Timeline import Timeline
import requests
import re
from typing import *

class SchoolHistory(Timeline):
    def __init__(self):
        super().__init__()

        html: str = self.__scrap()
        history = self.__parse(html)

        self.setTimeline(history)

    def __scrap(self) -> str:
        url = 'http://sy.caehs.kr/sub/info.do?m=010401&s=sy'

        html = requests.request('GET', url).text

        return html

    def __parse(self, html) -> List[Tuple[str, List[str]]]:
        data = re.findall(r'(?<=\<td\>).*?(?=</td>)', html, re.DOTALL)

        history = []
        for i in range(0, len(data), 3):
            date = data[i] + '.' + data[i + 1]
            log = ' '.join(data[i + 2].split())
            history.append((date, [log]))

        return history

