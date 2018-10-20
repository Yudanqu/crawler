import urllib.request
import random

url = "http://www.baidu.com"

# headers = {
# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
# }

# req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(req)

agentsList = [
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"
]

agentStr = random.choice(agentsList)

req = urllib.request.Request(url)
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(len(data))
print(type(data))
print(data)