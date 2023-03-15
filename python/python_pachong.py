from urllib.request import urlopen
import re


# if has Chinese, apply decode()
html = urlopen(
    "https://mofanpy.com/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)


res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
# Page title is:  Scraping tutorial 1 | 莫烦Python

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])

# Page paragraph is:
#  这是一个在 <a href="https://mofanpy.com/">莫烦Python</a>
#  <a href="https://mofanpy.com/tutorials/scraping">爬虫教程</a> 中的简单测试.

