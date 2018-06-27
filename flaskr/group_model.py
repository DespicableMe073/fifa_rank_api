import datetime
import random

class GroupModel(object):

    def __init__(self,gdate,gtime,g1name,score,g2name,ggroupname,gposition):

        self.g1name = g1name
        self.g2name = g2name
        self.groupname = ggroupname
        self.gposition = gposition
        self.gdate = datetime.datetime.strptime('2018'+'-'+gdate.split('月')[0]+'-'+gdate.split('月')[1].split('日')[0]+' '+gtime, "%Y-%m-%d %H:%M")
        scores = score.split('-')
        if len(scores[0]) == 0:
            self.g1score = str(random.randint(0, 5))
            self.g2score = str(random.randint(0, 5))
        else:
            self.g1score,self.g2score = scores



# 测试
    def __str__(self):

        print(self.gdate,self.groupname,self.g1name,self.g2name,self.g1score,self.g2score)
        return ""

