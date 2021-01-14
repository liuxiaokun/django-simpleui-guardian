from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):

    def process_request(self, request):
        print("md1  process_request 方法。", id(request))  # 在视图之前执行

    def process_response(self, request, response):  # 基于请求响应
        print("md1  process_response 方法！", id(request))  # 在视图之后
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("md1  process_view 方法！")  # 在视图之前执行 顺序执行
        # return view_func(request)


class MD2(MiddlewareMixin):

    def process_request(self, request):
        print("md2  process_request 方法。", id(request))  # 在视图之前执行

    def process_response(self, request, response):  # 基于请求响应
        print("md2  process_response 方法！", id(request))  # 在视图之后
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("md2  process_view 方法！")  # 在视图之前执行 顺序执行
        # return view_func(request)
