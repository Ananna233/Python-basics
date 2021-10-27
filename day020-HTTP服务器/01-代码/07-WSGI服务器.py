# 1-20.06
from wsgiref.simple_server import make_server

# demo_app 需要两个参数
# 第0个参数，表示环境（电脑的环境；请求路径相关的环境）
# 第1个参数，是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表，列表里只有一个元素，是一个二进制，表示返回给浏览器的数据
def demo_app(environ,start_response):
    # environ 是一个字典 保存了很多数据
    # path = environ['PATH_INFO']  # 获取用户请求路径
    #
    start_response('200 OK',[('Content-Type','text/html;charset=utf8')])
    return ['hello'.encode('utf8')]

if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('',8000,demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on",sa[0],"port",sa[1],'...')

    # 代码的作用是打开电脑的浏览器，并在浏览器里输入 http://localhost:8000/xyz?abc
    # import webbrowser
    # webbrowser.open('http://localhost:8000/xyz?abc')

    # 处理一次请求
    # httpd.handle_request()

    httpd.serve_forever()  # 服务器在后台一直运行