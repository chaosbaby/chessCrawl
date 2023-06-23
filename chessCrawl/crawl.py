import asyncio
import os
import sqlite3

# 创建一个 SQLite 数据库连接
conn = sqlite3.connect("test.db")
c = conn.cursor()

from chessCrawl import dbraw, playParser


# 定义一个异步函数来读取文件内容并写入数据库
async def process_file(filename):
    with open(filename, "r", encoding="GBK") as file:
        content = file.read()
        jsonData = playParser.convert_to_json(content)
        query, values = dbraw.toSqlPairs(jsonData, "chess_play")
        try:
            c.execute(query, values)
        except Exception as e:
            print(">>>>>")
            print(filename)
            print(e)
            print(query, values)
        print(filename)


# 定义一个异步函数来处理所有的文件
async def process_files(root):
    for file in os.listdir(root):
        if file.endswith(".txt"):
            filename = os.path.join(root, file)
            await process_file(filename)


# 定义一个异步函数来处理所有的目录
async def process_directories(dir):
    for root, directories, _ in os.walk(dir):
        await asyncio.gather(*[process_files(os.path.join(root, directory)) for directory in directories])


dir = "/home/chaos/GB2312"
# dir = "/home/chaos/GB2312/err"
# 运行异步函数并等待它们完成
asyncio.run(process_files(dir))

# 提交所有的更改并关闭数据库连接
conn.commit()
conn.close()
