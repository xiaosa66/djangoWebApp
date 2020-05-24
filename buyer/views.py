from django.shortcuts import render, HttpResponse, redirect
from seller import models


# Create your views here.

# 首页视图函数
def index(request):
    # 轮播图上展示的商品
    # 所有商品
    all_goods_obj_list = models.Goods.objects.all()
    lb_goods_obj_list = all_goods_obj_list[0:3]  # 使用列表切片
    # print(all_goods_obj_list)
    # print(lb_goods_obj_list)
    # 获取苹果对象中的第一张图片
    # ret = lb_goods_obj_list[0].goodsimage_set.first()
    # print(ret,type(ret))
    # print(ret.image_address.name,type(ret.image_address.name))
    # 获取每一个商品的第一张图片的路径
    # for goods_obj in lb_goods_obj_list:
    #     goodsimage_obj = goods_obj.goodsimage_set.first()
    #     # print(goodsimage_obj,type(goodsimage_obj))
    #     ret = goodsimage_obj.image_address.name
    #     print(ret, type(ret))

    return render(request, 'buyer/index_1.html',
                  {'lb_goods_obj_list': lb_goods_obj_list, 'all_goods_obj_list': all_goods_obj_list})


# 商品详情
def goods_detail(request):
    # 1. 获取id
    ids = request.GET.get('id')
    # 2. 根据id查询数据库
    goods_obj = models.Goods.objects.get(id=ids)
    # 3. 将数据盛放到页面上进行显示。
    return render(request, 'buyer/goods_details_1.html', {'goods_obj': goods_obj})


from buyer import models as buyer_models


# 注册功能
def register(request):
    if request.method == 'POST':
        # 1. 获取表单提交的内容
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        userpass = request.POST.get('userpass')
        # 2. 保存到数据库
        user_obj = buyer_models.User()
        user_obj.name = username
        user_obj.nickname = nickname
        user_obj.password = userpass
        user_obj.save()
        # 3. 跳转到登录界面
        return HttpResponse('注册成功了...')
    else:
        # get 请求。
        return render(request, 'buyer/register_1.html')


def login(request):
    if request.method == 'POST':
        # 1. 获取表单提交的内容
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 2. 根据用户名和密码查询数据库
        user_obj = buyer_models.User.objects.filter(name=username, password=password)
        # 注意如果是空的QuerySet对象，则转换成False。
        if user_obj:
            # 如果查出来数据则表示输入正确，返回首页
            return redirect('/buyer/index/')
        else:
            # 如果不能查询出来则提示用户用户名或者密码错误。
            pass

    return render(request, 'buyer/login_1.html')
