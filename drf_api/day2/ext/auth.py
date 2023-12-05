from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
  
class myAuthentication(BaseAuthentication):
    def authenticate(self, request, *args, **kwargs):
        
        # 去用户认证：
        # 1.读取token
        # 2.校验合法性
        # 3.关于返回值
        #   3.1返回一个元组（11，22）   request.user request.auth
        #   3.2抛出异常                认证失败
        #   3.3null                   多个认证（不知道成功没有，给后面看）
        token = request.query_params.get("token")
        if token:
            return ("lijiajun",token)
        raise AuthenticationFailed({"code":"2020",'error' : "认证失败"})
