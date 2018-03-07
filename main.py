from flask import Flask
from config import DevConfig


app=Flask(__name__)

#这样加载配置简单方便 ，不需要一项一项的添加和修改
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>hello word</h1>'

if __name__ == '__main__':
    app.run()