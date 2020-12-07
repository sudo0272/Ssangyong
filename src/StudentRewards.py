from requests import request
from Timeline import Timeline
import re

class StudentRewards(Timeline):
    def __init__(self):
        super().__init__()

        html = request('GET', 'http://www.sy.caehs.kr/sub/info.do?m=010404&s=sy').text
        data = re.findall(r'(?<=\<tbody\>).*?(?=\<\/tbody\>)', html, re.DOTALL)[1]
        headers = re.findall(r'(?<=\<th\>).*?(?=\<\/th\>)', data, re.DOTALL)
        items = []
        for i in headers:
            items.append([i, []])

        contentGroup = re.findall(r'(?<=\<tr\>).*?(?=\<\/tr\>)', data, re.DOTALL)[1:]
        for i in contentGroup:
            rewards = re.findall(r'(?<=\<p style="margin-top: 0pt; margin-bottom: 0pt;"\>).*?(?=\<\/p\>)', i, re.DOTALL)

            for index, item in enumerate(rewards):
                items[index][1].append(item)

        self.setTimeline(items)

