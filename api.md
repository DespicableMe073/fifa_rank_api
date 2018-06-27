世界杯排行榜有关操作
-----------

### 重新装载数据
#### 接口说明
> 清除当前数据并重新爬取
#### 接口地址
> /reloaddata
#### 返回格式
> JSON
#### 请求方式
> GET
#### 请求参数
无
#### 返回字段
| 返回字段 | 字段类型 | 说明                             |
|----------|----------|----------------------------------|
| status   | string      | 返回结果状态。OK：正常；FAILED：错误。当返回为错误时不反回data字段返回message字段 |
| code   | string   | 状态码 000000为成功 其他为失败                         |
| data     | string   | 数据                             |
| message  | string | 错误信息
| querytime | int | 执行命令用时

#### 接口示例
> 
#```json
{"code": "000000", "querytime": 0.09153699999999998, "status": "OK"}
#```
### 获取32强球队
#### 接口说明
> 分页获取32强球队列表
#### 接口地址
> /gettop32/<page>/<page_pre>
#### 返回格式
> JSON
#### 请求方式
> GET
#### 请求参数
| 参数 | 必选 | 类型   | 默认值 | 说明                                    |
|------|------|--------|--------|-----------------------------------------|
| page | ture | int | 1    | 页码                            |
| page_pre | true | int    | 10    | 每页条数 |
#### 返回字段
| 返回字段 | 字段类型 | 说明                             |
|----------|----------|----------------------------------|
| status   | string      | 返回结果状态。OK：正常；FAILED：错误。当返回为错误时不反回data字段返回message字段 |
| code   | string   | 状态码 000000为成功 其他为失败                         |
| data     | string   | 数据                             |
| message  | string | 错误信息

#### 接口示例
> 
#```json
{
	"code": "000000",
	"data": ["丹麦", "乌拉圭", "伊朗", "俄罗斯", "克罗地亚", "冰岛", "哥伦比亚", "哥斯达黎加", "埃及", "塞内加尔", "塞尔维亚", "墨西哥", "尼日利亚", "巴拿马", "巴西", "德国", "摩洛哥", "日本", "比利时", "沙特阿拉伯"],
	"status": "OK"
}
#```
### 获取每组净胜球最多球队
#### 接口说明
> 分页获取32强球队列表
#### 接口地址
> /getmaxgoallist
#### 返回格式
> JSON
#### 请求方式
> GET
#### 请求参数
无
#### 返回字段
| 返回字段 | 字段类型 | 说明                             |
|----------|----------|----------------------------------|
| status   | string      | 返回结果状态。OK：正常；FAILED：错误。当返回为错误时不反回data字段返回message字段 |
| code   | string   | 状态码 000000为成功 其他为失败                         |
| data     | string   | 数据                             |
| message  | string | 错误信息
| gname | string | 球队名
| goalnum | int | 净胜球数
|group| string |所在组别

#### 接口示例
> 
#```json
{
	"code": "000000",
	"data": [{
		"gname": "俄罗斯",
		"goalnum": 7,
		"group": "A"
	}, {
		"gname": "葡萄牙",
		"goalnum": 1,
		"group": "B"
	}, {
		"gname": "法国",
		"goalnum": 2,
		"group": "C"
	}, {
		"gname": "克罗地亚",
		"goalnum": 2,
		"group": "D"
	}, {
		"gname": "巴西",
		"goalnum": 2,
		"group": "E"
	}, {
		"gname": "墨西哥",
		"goalnum": 3,
		"group": "F"
	}, {
		"gname": "比利时",
		"goalnum": 6,
		"group": "G"
	}, {
		"gname": "塞内加尔",
		"goalnum": 0,
		"group": "H"
	}],
	"status": "OK"
}
#```
### 获取分差top3的比赛记录
#### 接口说明
> 获取分差top3
#### 接口地址
> /getfenchatop3
#### 返回格式
> JSON
#### 请求方式
> GET
#### 请求参数
无
#### 返回字段
| 返回字段 | 字段类型 | 说明                             |
|----------|----------|----------------------------------|
| status   | string      | 返回结果状态。OK：正常；FAILED：错误。当返回为错误时不反回data字段返回message字段 |
| code   | string   | 状态码 000000为成功 其他为失败                         |
| data     | string   | 数据                             |
| message  | string | 错误信息 |
| g1name | string | 主队名|
| g1score | int | 主队比分|
| g2name | string | 客队名|
|g2score | int |客队比分|
|gdatatime | string | 比赛时间|
|ggroup | string|所在组别|

#### 接口示例
> 
#```json
{
	"code": "000000",
	"data": [{
		"g1name": "塞尔维亚",
		"g1score": 0,
		"g2name": "巴西",
		"g2score": 5,
		"gdatatime": "2018-06-28 02:00:00",
		"ggroup": "E"
	}, {
		"g1name": "英格兰",
		"g1score": 6,
		"g2name": "巴拿马",
		"g2score": 1,
		"gdatatime": "2018-06-24 20:00:00",
		"ggroup": "G"
	}, {
		"g1name": "俄罗斯",
		"g1score": 5,
		"g2name": "沙特阿拉伯",
		"g2score": 0,
		"gdatatime": "2018-06-14 23:00:00",
		"ggroup": "A"
	}],
	"status": "OK"
}
#```
### 获取小组晋级列表
#### 接口说明
> 获取每组晋级的前两只队伍 排名根据积分/净胜球等
#### 接口地址
> /getpromotionteam
#### 返回格式
> JSON
#### 请求方式
> GET
#### 请求参数
无
#### 返回字段
| 返回字段 | 字段类型 | 说明                             |
|----------|----------|----------------------------------|
| status   | string      | 返回结果状态。OK：正常；FAILED：错误。当返回为错误时不反回data字段返回message字段 |
| code   | string   | 状态码 000000为成功 其他为失败                         |
| data     | string   | 数据                             |
| message  | string | 错误信息
|gname |string|球队名|
|group|string|组别|
|score|int|积分|
|truescore |int |净胜球数

#### 接口示例
> 
#```json
{
	"code": "000000",
	"data": [{
		"gname": "俄罗斯",
		"group": "A",
		"score": 6,
		"truescore": 7
	}, {
		"gname": "乌拉圭",
		"group": "A",
		"score": 6,
		"truescore": 4
	}, {
		"gname": "葡萄牙",
		"group": "B",
		"score": 4,
		"truescore": 1
	}, {
		"gname": "西班牙",
		"group": "B",
		"score": 1,
		"truescore": 0
	}, {
		"gname": "法国",
		"group": "C",
		"score": 6,
		"truescore": 2
	}, {
		"gname": "丹麦",
		"group": "C",
		"score": 2,
		"truescore": 0
	}, {
		"gname": "克罗地亚",
		"group": "D",
		"score": 3,
		"truescore": 2
	}, {
		"gname": "尼日利亚",
		"group": "D",
		"score": 3,
		"truescore": 1
	}, {
		"gname": "巴西",
		"group": "E",
		"score": 4,
		"truescore": 2
	}, {
		"gname": "哥斯达黎加",
		"group": "E",
		"score": 0,
		"truescore": -1
	}, {
		"gname": "墨西哥",
		"group": "F",
		"score": 3,
		"truescore": 3
	}, {
		"gname": "瑞典",
		"group": "F",
		"score": 3,
		"truescore": 1
	}, {
		"gname": "比利时",
		"group": "G",
		"score": 6,
		"truescore": 6
	}, {
		"gname": "英格兰",
		"group": "G",
		"score": 3,
		"truescore": 3
	}, {
		"gname": "日本",
		"group": "H",
		"score": 2,
		"truescore": 0
	}, {
		"gname": "塞内加尔",
		"group": "H",
		"score": 1,
		"truescore": 0
	}],
	"status": "OK"
}
#```
