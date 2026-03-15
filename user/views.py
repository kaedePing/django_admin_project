from datetime import datetime
import json

from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
# from rest_framework.settings import api_settings
from rest_framework_jwt.settings import api_settings

# Create your views here.
from django_admin_project import settings
from menu.models import SysMenu, SysMenuSerializer
from role.models import SysRole
from user.models import SysUser
from user.serializers import SysUserSerializer


class LoginView(View):

    def buildTreeMenu(self, sysMenuList):
        resultMenuList: list[SysMenu] = list()
        for menu in sysMenuList:
            # 寻找子节点
            for e in sysMenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点，添加到集合
            if menu.parent_id == 0:
                resultMenuList.append(menu)
        return resultMenuList

    def post(self, request):

        username = request.GET.get('username')
        password = request.GET.get('password')

        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            # 生成用户的JWT载荷
            payload = jwt_payload_handler(user)
            # 将载荷编码为JWT token字符串
            token = jwt_encode_handler(payload)

            roleList = SysRole.objects.raw(
                "SELECT id ,NAME FROM sys_role WHERE id IN (SELECT role_id FROM sys_user_role WHERE user_id=" + str(
                    user.id) + ")")

            print(roleList)

            # 获取当前用户所有的角色，逗号隔开
            roles = ",".join([role.name for role in roleList])

            menuSet: set[SysMenu] = set()

            for row in roleList:
                print(row.id, row.name)
                menuList = SysMenu.objects.raw(
                    "SELECT * FROM sys_menu WHERE id IN (SELECT menu_id FROM sys_role_menu WHERE role_id=" + str(
                        row.id) + ")")
                for row2 in menuList:
                    print(row2.id, row2.name)
                    menuSet.add(row2)

            print(menuSet)

            menuList: list[SysMenu] = list(menuSet)  # set转list
            sorted_menuList = sorted(menuList)  # 根据order_num排序

            # 构造菜单树
            sysMenuList: list[SysMenu] = self.buildTreeMenu(sorted_menuList)
            print(sysMenuList)
            serializerMenuList = list()
            for sysMenu in sysMenuList:
                serializerMenuList.append(SysMenuSerializer(sysMenu).data)

        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'info': '用户名或密码错误'})
        return JsonResponse({'code': 200, 'token': token, 'user': SysUserSerializer(user).data, 'info': '登录成功',
                             'menuList': serializerMenuList,
                             'roles': roles})


class TestView(View):

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token != None and token != '':

            query_obj = SysUser.objects.all()
            list_obj = list(query_obj.values())

            return JsonResponse({'code': 200, 'info': '测试', 'data': list_obj})
        else:
            return JsonResponse({'code': 401, 'info': '没有访问权限'})


class JwtTestView(View):
    def get(self, request):
        # 查询指定用户名和密码的用户
        user = SysUser.objects.get(username='python222', password='123456')

        # 获取JWT配置的载荷处理函数和编码函数
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        # 生成用户的JWT载荷
        payload = jwt_payload_handler(user)
        # 将载荷编码为JWT token字符串
        token = jwt_encode_handler(payload)

        # 返回包含token的JSON响应
        return JsonResponse({'code': 200, 'token': token})


class SaveView(View):
    def post(self, request):
        # 解析请求体中的 JSON 数据
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        if data['id'] == -1:
            # 添加新用户逻辑（当前为 pass，可补充创建 SysUser 并 save）
            pass
        else:
            # 修改现有用户
            obj_sysUser = SysUser(
                id=data['id'],
                username=data['username'],
                password=data['password'],
                avatar=data['avatar'],
                email=data['email'],
                phonenumber=data['phonenumber'],
                login_date=data['login_date'],
                status=data['status'],
                create_time=data['create_time'],
                update_time=data['update_time'],
                remark=data['remark']
            )
            # 更新修改时间为当前日期
            obj_sysUser.update_time = datetime.now().date()
            # 保存到数据库
            obj_sysUser.save()

        # 返回成功响应
        return JsonResponse({'code': 200})

class PwdView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        oldPassword = data['oldPassword']
        newPassword = data['newPassword']
        print(1111111111111111111111111)
        print(id)
        print(oldPassword)
        print(newPassword)
        obj_user = SysUser.objects.get(id=id)
        if obj_user.password == oldPassword:
            obj_user.password = newPassword
            obj_user.update_time = datetime.now().date()
            obj_user.save()
            return JsonResponse({'code': 200})
        else:
            return JsonResponse({'code': 500, 'errorInfo': '原密码错误！'})

class ImageView(View):

    def post(self, request):
        file = request.FILES.get('avatar')
        print("file:", file)
        if file:
            file_name = file.name
            suffixName = file_name[file_name.rfind("."):]
            new_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + suffixName
            file_path = str(settings.MEDIA_ROOT) + "\\userAvatar\\" + new_file_name
            print("file_path:", file_path)
            try:
                with open(file_path, 'wb') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                return JsonResponse({'code': 200, 'title': new_file_name})
            except:
                return JsonResponse({'code': 500, 'errorInfo': '上传头像失败'})


class AvatarView(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        avatar = data['avatar']
        obj_user = SysUser.objects.get(id=id)
        obj_user.avatar = avatar
        obj_user.save()
        return JsonResponse({'code': 200})