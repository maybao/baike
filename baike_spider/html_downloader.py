# html下载器
from urllib import parse
from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

# if __name__ == '__main__':
#     text = HtmlDownloader().download('https://baike.baidu.com/item/Python/407313')
#     print(text)
