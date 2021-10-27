# 1.21.10

import json
from wsgiref.simple_server import make_server

def show_login():
    return '欢迎来到登录'

def show_register():
    return '注册啦~~~~'

def show_index():
    return '欢迎来到首页'
# ......像这样一个个封装起来
def show_text():
    return json.dumps({'name': 'zhangsan', 'age': 18})

url ={
    '/login':show_login,
    '/register':show_register,
    '/index':show_index,
    '/text':show_text
}

def demo_app(environ, start_response):
    # environ 是一个字典 保存了很多数据
    status_code = '200 OK'
    # QUERY_STRING 获取客户端GET请求方式传递的参数
    # print(environ.get('QUERY_STRING'))  # name=zhangsan&age=19

    path = environ['PATH_INFO']  # 请求路径
    method = url.get(path)
    if method:
        response_body =method()
    else:
        status_code = '404 Not Found'
        response_body = '页面走丢了'



    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response_body.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8080, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], '...')

    httpd.serve_forever()
