from urllib.request import urlopen


# if has Chinese, apply decode()
html = urlopen(
    "https://mofanpy.com/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)
