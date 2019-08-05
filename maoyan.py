# 导入requests模块，python http库
import requests
# 导入etree，用xpath提取数据
from lxml import etree
# 导入json模块
import json

# 自定义函数，请求网页信息
def getOnePage(page):
    # 把网址附给变量url
    url = f'https://maoyan.com/board/4?offset={page*10}'
    # 使用西刺免费高匿代理服务器，避免ip被封和赔偿
    free_proxies = {"http": "http://222.189.190.89: 9999"}
    # 加入头部信息，告诉服务器这是浏览器访问，最简单的反爬措施
    # 查找user-agent：在浏览器页面按F12，找到Network，刷新一下，在request headers下找到user-agent
    # 复制下来后以字典的形式赋值给变量user_agent
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    # 调用get(url)函数，返回数据
    r = requests.get(url, proxies = free_proxies, headers = user_agent)
    # 打印一下，以text的形式，已做分析之用
    # print(r.text)
    # 函数最后都要返回值，相当于把这个返回值赋给了这个函数，调用函数最后得到的就是这个返回值
    return r.text

# 自定义函数，提取信息
def parse(text):
    # 初始化， 标准化
    html = etree.HTML(text)
    # 提取电影名称，用xpath语法，xpath返回的是列表
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    # 打印names，分析用
    # print(names)
    # 提取电影上映时间
    releasetimes = html.xpath('//p[@class="releasetime"]/text()')
    # print(releasetimes)
    
    # 创建一个空字典
    item = {}

    # zip是拉链函数，让两个列表的元素成对出现
    for name, releasetime in zip(names, releasetimes):
        item['name'] = name
        item['releasetime'] = releasetime
        # parse()变成生成器
        yield item

# 定义函数保存数据到文件
def save2File(data):
        # 创建json格式的文件，'a'的含义是打开用于写入，如果存在就写在末尾，防止替换
        with open('movie.json', 'a', encoding = 'utf-8') as f:
                # 把字典，列表，等转化成字符串
                data = json.dumps(data, ensure_ascii=False) + ',\n'
                f.write(data)

def run():
        # 爬取1到10页数据
        for n in range(0, 10):
                text = getOnePage(n)
                # parse()是生成器，items也是，需要for循环迭代出里面的数据
                items = parse(text)
                # 把生成器的内容迭代出
                for item in items:
                        print(item)
                        save2File(item)

if __name__ == '__main__':
        run()

