from flask import Flask
from flask import json
from flaskr import load_data,group_serch
import time
import sqlite3


app = Flask(__name__)


# 重新导入数据
@app.route('/reloaddata',methods=['GET'])
def insert_data():
    start = time.clock()
    if load_data.insert_sqllite(load_data.get_contents()):
        end = time.clock()
        return json.dumps({'code':'000000',"status":"OK","querytime":end-start})
    else:
        return json.dumps({'code': '100001', "status": "FAILED", "message": "重新载入失败!"})


# 分页获取32强
@app.route('/gettop32/<page>/<page_pre>',methods=['GET'])
def get_top32(page,page_pre):
    if page.isdigit() & page_pre.isdigit():
        res = group_serch.serch_top32(int(page), int(page_pre))
        return json.dumps({'code': '000000', "status": "OK", "data":res})
    else:
        return json.dumps({'code': '100002', "status": "FAILED", "message": "错误的参数格式!"})


# 返回每个小组净胜球最多的球队
@app.route('/getmaxgoallist',methods=['GET'])
def get_max_goal_list():
    data = group_serch.max_goal_list()
    if data != None:
        return json.dumps({'code': '000000', "status": "OK", "data": data})
    else:
        return json.dumps({'code': '100002', "status": "FAILED", "message": "暂无排名!"})


# 返回分差top3的比赛记录
@app.route('/getfenchatop3',methods=['GET'])
def get_fencha_top3():
    data = group_serch.fencha_top3()
    if data != None:
        return json.dumps({'code': '000000', "status": "OK", "data": data})
    else:
        return json.dumps({'code': '100002', "status": "FAILED", "message": "暂无排名!"})


# 返回每个小组晋级的两只球队(排名优先级：积分、净胜球、球队名)；
@app.route('/getpromotionteam',methods=['GET'])
def get_promotion_team():
    data = group_serch.group_through_list()
    if data != None:
        return json.dumps({'code': '000000', "status": "OK", "data": data})
    else:
        return json.dumps({'code': '100002', "status": "FAILED", "message": "暂无排名!"})


if __name__ == '__main__':
    app.run()
