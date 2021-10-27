# 1-20.07
from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    # environ 是一个字典 保存了很多数据
    status_code = '200 OK'
    # 状态码:  RESTFUL ==》 前后端分离
    # 2XX : 请求响应成功
    # 3XX : 重定向
    # 4XX : 客户端的错误  404 客户端访问了一个不存在的地址  405:请求方式不被允许
    # 5XX : 服务器的错误。

    path = environ['PATH_INFO']  # 请求路径
    if path == '/login':
        response_body = '欢迎来到登录'
    elif path == '/register':
        response_body = '注册啦~~~~'
    elif path == '/index':
        response_body = '欢迎来到首页'
    elif path == '/':
        response_body = 'Hello World'
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
