import requests
import re

url = 'http://www.columbia.edu/~fdc/sample.html'

page = requests.get(url).text
headings = re.findall(r'<h3.*?>(.*?)</h3>', page)
print(headings)
