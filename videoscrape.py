import requests as re
from selectolax.parser import HTMLParser

class Videoscraper:
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Connection': 'keep-alive',
        'Range': 'bytes=0-',
        'Referer': 'https://wecima.movie/',
        'Sec-Fetch-Dest': 'video',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    def __init__(self):
        self.base_url = "https://wecima.movie/watch/%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D9%85%D8%B3%D9%84%D8%B3%D9%84-{series}-%D9%85%D9%88%D8%B3%D9%85-{season}-%D8%AD%D9%84%D9%82%D8%A9-{episode}-/"

    def parse(self, series,season,episode):
        series = series.replace(" ","-")
        # Format the URL with the series name
        url = self.base_url.format(series=series,season=season,episode=episode)

        # Send the GET request with headers
        resp = re.get(url=url, headers=self.headers).text

        # Parse the response HTML
        parser = HTMLParser(resp)

        # Locate the download link
        download_element = parser.css_first("ul.List--Download--Wecima--Single li:nth-child(1) a")
        
        downlink = download_element.attributes['href'].strip()
        print(downlink)
        return downlink



