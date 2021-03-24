# -*- coding = utf-8 -*-
# @author tangwenbo
# @File spider
# @date 2021/2/23 16:29

# 引入第三方库
from bs4 import BeautifulSoup  # 网页解析
import re  # 正则库,文字匹配
import urllib.request, urllib.error  # 制定url,获取网页数据
import xlwt  # excel操作
import sqlite3  # SQLite数据库
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xlsx"
    saveData(savepath, datalist)
    saveData2DB("movie.db", datalist)
    print(datalist)


# 创建正则表达式对象,表示筛选条件
findInfoLink = re.compile(r'<a href="(.*?)">')
# 获取图片地址,并忽略换行符
findImg = re.compile(r'<img.*src="(.*?)"', re.S)
# 主标题
findTitle = re.compile(r'<span class="title">(.*?)</span>', re.S)
# 其他标题
findTitleOther = re.compile(r'<span class="other">(.*?)</span>', re.S)
# 演员信息
findPerformer = re.compile(r'<p class="">(.*?)</p>', re.S)
# 评分
findRatingNum = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>', re.S)
# 简介
findDesc = re.compile(r'<span class="inq">(.*?)</span>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for offset in range(0, 10):
        limit = offset * 25
        url = baseurl + str(limit)
        html = askUrl(url)
        # 解析网页内容
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []  # 保存需要的信息
            item = str(item)

            infoLink = re.findall(findInfoLink, item)[0]
            data.append(infoLink)
            imgUrl = re.findall(findImg, item)[0]
            data.append(imgUrl)
            title = re.findall(findTitle, item)
            if len(title) > 1:
                for twoTitle in title:
                    data.append(twoTitle.replace("\xa0", "").replace("/", "", 1))
            else:
                data.append(title[0])
                data.append("暂无")
            titleOther = re.findall(findTitleOther, item)[0]
            data.append(titleOther.replace("\xa0", "").replace("/", "", 1))
            performer = re.findall(findPerformer, item)[0]
            data.append(
                performer.replace("\xa0", "").replace("\n", "").replace("<br/>", "").strip().replace("/", "", 1))
            ratingNum = re.findall(findRatingNum, item)[0]
            data.append(ratingNum)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            desc = re.findall(findDesc, item)
            if len(desc) > 0:
                data.append(desc[0])
            else:
                data.append("暂无")
            datalist.append(data)
    return datalist


# 保存数据到excel
def saveData(savepath, dataList):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
    sheet.write(0, 0, "电影详情链接")
    sheet.write(0, 1, "电影封面")
    sheet.write(0, 2, "电影名称")
    sheet.write(0, 3, "外国名称")
    sheet.write(0, 4, "其他名称")
    sheet.write(0, 5, "演员简介")
    sheet.write(0, 6, "豆瓣评分")
    sheet.write(0, 7, "评论人数")
    sheet.write(0, 8, "电影简介")
    for i in range(0, len(dataList)):
        data = dataList[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    workbook.save(savepath)


def saveData2DB(dbPath, dataList):
    init_db(dbPath)
    connect = sqlite3.connect(dbPath)
    cursor = connect.cursor()
    for data in dataList:
        cursor.execute("""
        insert into movie (info_url,img_url,china_name,out_name,other_name,performer_desc
        ,rating_num,judge,desc) values (?,?,?,?,?,?,?,?,?)
        """, data)
    connect.commit()
    connect.close()


def init_db(dbPath):
    connect = sqlite3.connect(dbPath)
    cursor = connect.cursor()
    createSql = """
    create table IF NOT EXISTS movie (
    id integer primary key AUTOINCREMENT not null  ,
    info_url text not null,
    img_url text not null,
    china_name text ,
    out_name text ,
    other_name text ,
    performer_desc text ,
    rating_num real ,
    judge real,
    desc text
    )
    """
    cursor.execute(createSql)
    connect.commit()
    connect.close()


# 获取单一页面
def askUrl(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
        }
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        return html
    except urllib.error.URLError as e:
        print("获取网页信息失败,原因:%s" % e)
        pass


if __name__ == '__main__':
    main()
