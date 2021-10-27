# 1-20.06
from wsgiref.simple_server import make_server

def demo_app(environ,start_response):
    # environ 是一个字典 保存了很多数据
    # path = environ['PATH_INFO']  # 请求路径
    #
    start_response('200 OK',[('Content-Type','text/html;charset=utf8')])
    return ['hello'.encode('utf8')]

if __name__ == '__main__':
    httpd = make_server('',8000,demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on",sa[0],"port",sa[1],'...')

    httpd.serve_forever()