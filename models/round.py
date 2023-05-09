import datetime
# a mettre dans tournament ?


class Round:
    def __init__(self, name, matches={}, start_time=None, end_time=None,score={}):
        self.name = name
        self.matches = matches or []
        self.start_time = start_time
        self.end_time = end_time
        self.score = score
        
    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
