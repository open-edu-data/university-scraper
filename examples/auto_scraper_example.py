"""
University Homepage Scraper with AutoScraper
"""

from autoscraper import AutoScraper

url = 'https://www.xmu.edu.cn/xbyx/shkxxb.htm'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["经济学院"]

scraper = AutoScraper()

result = scraper.build(url, wanted_list)
print(result)
