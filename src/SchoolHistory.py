from Timeline import Timeline
import requests
import re
import sqlite3

class SchoolHistory(Timeline):
    def __init__(self):
        super().__init__()

        self.setTimeline([
            ('2020.9.1', ['제7대 고미영 교장 취임']),
            ('2020.1.3', ['제14회 졸업식(455명, 졸업생 누계 6,842명)']),
            ('2017.3.1', ['제6대 강혜옥 교장 취임']),
            ('2011.3.1', ['과학중점학교 운영(교육부)']),
            ('2004.5.20', ['개교식']),
            ('2004.3.4', ['제1회 입학식(14학급)']),
            ('2002.1.15', ['천안쌍용고등학교 설립인가(36학급)'])
        ])

