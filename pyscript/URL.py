"""
ath	/page.html
script_root	/myapplication
base_url	http://www.example.com/myapplication/page.html
url	http://www.example.com/myapplication/page.html?x=y
url_root	http://www.example.com/myapplication/
"""

url = "/photos/tag?123"
tags = url.replace("/photos/tag?","")

print(tags)