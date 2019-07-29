# html下载器
from urllib import request
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        sessions = requests.session()
        sessions.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                            'Chrome/75.0.3770.142 Safari/537.36'
        resp = sessions.get(url)
        resp.encoding = 'utf-8'
        if resp.status_code != 200:
            return None
        return resp.text.encode('utf-8')

