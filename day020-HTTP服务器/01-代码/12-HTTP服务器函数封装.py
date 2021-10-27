# 1.21.10

import json
from wsgiref.simple_server import make_server

def show_login():
    return '欢迎来到登录'

def show_register():
    return '注册啦~~~~'

# ......像这样一个个封装起来

def demo_app(environ, start_response):
    # environ 是一个字典 保存了很多数据
    status_code = '200 OK'
    # QUERY_STRING 获取客户端GET请求方式传递的参数
    # print(environ.get('QUERY_STRING'))  # name=zhangsan&age=19

    path = environ['PATH_INFO']  # 请求路径
    if path == '/':
        response_body = 'Hello World'
    elif path == '/login':
        response_body = show_login()
    elif path == '/register':
        response_body = show_register()
    elif path == '/index':
        response_body = '欢迎来到首页'
    elif path == '/test':
        response_body = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        with open('笔记.txt','r',encoding='utf8') as file:
            response_body = file.read()
    elif path.split('.')[-1] == 'html':
        try:
            with open('htmlPages/'+path,'r',encoding='utf8') as file:
                    response_body = file.read()
        except FileNotFoundError:
            status_code = '404 Not Found'
            response_body = '文件未找到~~~'
    elif path == '/info':
        name = 'Jack'
        with open('htmlPages/info.html','r',encoding='utf8') as file:
            response_body = file.read().format(username=name)
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
