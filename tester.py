import json, urllib, os
import pymongo
import requests
from mitmproxy import ctx

from pymongo import MongoClient



class DedaoMongodb(object):
    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client.test
        self.collection = self.db.dedao_book
    def update_book(self, book_info):
        self.collection.insert(book_info)
def save_file(url,file_name,file_path):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print ('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)


        #拼接图片名（包含路径）
        filename = '{}/{}'.format(file_path,file_name)
        if os.path.exists(filename):
            print(filename,'已存在')
        else:
           #下载图片，并保存到文件夹中

            urllib.request.urlretrieve(url,filename=filename)
    except IOError as e:
        print ('文件操作失败'),e
    except Exception as e:
        print ('错误 ：',e)

def conn(data):
    client = MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.dedao
    collection.create_index([('id', pymongo.ASCENDING)])
    collection.update_one({'id':data.get('id')}, {'$set':data}, True)


def response(flow):
    # global collection
    #url = 'https://entree.igetget.com/odob/v2/theme/list'
    url = 'https://entree.igetget.com/ebook2/v1/ebook/list'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'id': book.get('id'),
                'cover': book.get('cover'),
                'epub': book.get('epub'),
                'operating_title': book.get('operating_title'),
                'other_content': book.get('other_content'),
                'other_share_summary': book.get('other_share_summary'),
                'book_filename': book.get('book_filename'),
                'book_name': book.get('book_name'),
                'book_intro': book.get('book_intro'),
                'sell_seven_day':book.get('sell_seven_day'),
                'publish_time':book.get('publish_time'),
                'price':book.get('price'),
                'b_special_price':book.get('b_special_price'),
                'current_price':book.get('current_price"')


            }

            ctx.log.info(str(data))
            print('downloading ' + book.get('operating_title'))
            book_name = book.get('operating_title') + '.epub'
            book_cover = str(book.get('sell_seven_day')) + '_' +book.get('operating_title') + '.jpeg'
            url = book.get('epub')
            url_cover = book.get('cover')
            #r = requests.get(url)
            #r_cover = requests.get(url_cover)

            #save_file(url,book_name,'book')
            save_file(url_cover,book_cover,'book_cover')
            # with open(book_name, "wb") as code:
            #     code.write(r.content)
            # with open(book_cover,'wb') as file:
            #     file.write(r_cover.content)
            conn(data=data)

            