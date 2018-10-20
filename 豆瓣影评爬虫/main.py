import urllib.request
import random
import re

agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 ",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
]
agentStr = random.choice(agentsList)

url = r"https://movie.douban.com/review/best/"

req = urllib.request.Request(url)
# 向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)

response = urllib.request.urlopen(req)

html = response.read().decode("utf-8")

with open(r"F:/python实战/豆瓣电影爬虫/file1.html", "w") as f:
    f.write(html)

re_a = re.compile(r'<div xmlns:(.*?)</div>.*?</div>', re.S)
result = re_a.findall(html)
with open(r"F:/python实战/豆瓣电影爬虫/file2.html", "w") as f:
    for i in range(len(result)):
        f.write(result[i]+'\n**********************\n')
print(len(result))

re_title = re.compile('<img alt="(.*?)"')
re_author = re.compile('class="name">(.*?)</a>')
re_comment_title = re.compile('<h2>(.*?)>(.*?)</a>')
re_comment_body = re.compile('<div class="short-content">(.*?)&nbsp', re.S)

# print(result[2])
# print(type(result[2]))


with open(r"F:/python实战/豆瓣电影爬虫/file3.txt", "w") as ff:
    for i in range(len(result)):
        # print(type(result[i]))
        ff.write("title:" + re_title.findall(result[i])[0] + '\n')
        # print(re_title.findall(result[i]))
        # print(type(re_title.findall(result[i])))
        ff.write("author:" + re_author.findall(result[i])[0] + '\n')
        ff.write("comment_title:" + re_comment_title.findall(result[i])[0][1] + '\n')
        ff.write("comment_body:" + re.sub(r'\s', '', re_comment_body.findall(result[i])[0].strip()) + '\n\n')
        # print(re_comment_body.findall(result[i])[0].strip())
        # print(type(re_comment_body.findall(result[i])[0]))