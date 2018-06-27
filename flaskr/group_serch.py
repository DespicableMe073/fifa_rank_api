import sqlite3



# 分页查询32强
def serch_top32(page,page_pre):
    try:
        result = []
        con = sqlite3.connect("data.db3")
        cur = con.cursor()
        cur.execute('select  DISTINCT  g1name  from groupsinfo order by g1name limit ? offset ?*?', (page_pre,page_pre,page-1,))
        reqdata = cur.fetchall()
        for i in reqdata:
            result.append(i[0])
        return result
    except Exception as e:
        return e.strerror

    finally:
        con.close()

# 查询每组净胜球第一
def max_goal_list():
    try:
        result = []
        con = sqlite3.connect("data.db3")
        cur = con.cursor()
        cur.execute('select t.g1name,t.ggroup,max(t.gscore) as score from (select g1name,ggroup,sum(g1score-g2score) as gscore from groupsinfo group by ggroup,g1name) as t group by ggroup ')
        reqdata = cur.fetchall()
        for i in reqdata:
            result.append({"group":i[1],"gname":i[0],"goalnum":i[2]})
        return result
    except Exception as e:
        return e.strerror

    finally:
        con.close()


# 查询分差最大的三场比赛
def fencha_top3():
    try:
        result = []
        con = sqlite3.connect("data.db3")
        cur = con.cursor()
        cur.execute(
            'select abs(g1score-g2score) as fencha,g1name,g2name,ggroup,gdatetime,g1score,g2score  from groupsinfo order by fencha desc,gdatetime desc limit 0,3')
        reqdata = cur.fetchall()
        for i in reqdata:
            result.append({"g1name": i[1], "g2name": i[2], "ggroup": i[3],"g1score":i[5],"g2score":i[6],"gdatatime":i[4]})
        return result
    except Exception as e:
        return e.strerror

    finally:
        con.close()


# 返回每个小组晋级的两只球队(排名优先级：积分、净胜球、球队名)；
def group_through_list():
    try:
        groups = ['A','B','C','D','E','F','G','H']
        result = []
        con = sqlite3.connect("data.db3")
        cur = con.cursor()
        for i in groups:
            reqdata = cur.execute("select ggroup,g1name,sum(g1score-g2score)  as truescore, sum(case   when g1score>g2score then 3 when g1score=g2score then 1 when g1score<g2score then 0  end)  as score1 from groupsinfo   where ggroup=? "
                                  "  group by g1name order by ggroup asc,score1 desc,truescore desc limit 2",(i,))
            for j in reqdata:
                result.append({"group":j[0],"gname":j[1],"score":j[3],"truescore":j[2]})
        return result
    except Exception as e:
        return e.strerror
    finally:
        con.close()


if __name__ == "__main__":
    # print(serch_top32(1,10))
    pass