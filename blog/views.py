import os
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def post_list(request):


    #Template을 찾을 경로에서
    # post_list.html을 찾아서
    # 그 파일을 text로 만들어서 httpResponse 형태로 돌려준다
    # 위 기능을 하는 shortcut 함수

    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)

def post_detail(request):
    post = Post.objects.all()[0]
    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)










    # 상위폴더(blog)의
    # 상위폴더(djangogirls)의
    # 하위폴더 (templates)의
    # 하위파일(post_list.html)내용을 read()한 결과를 HttpResponse에 인자로 전달

    # 경로이동
    # os.path.abspath(__file__) <- 현재 파일의 절대 경로를 리턴해줌
    # os.path.dirname : 경로 중 디렉토리명만 얻기
    # os.path.join : 경로를 병합하여 새 경로 생

    # 파일열기
    # open

    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # root_dir_path = os.path.dirname(blog_dir_path)
    # templates_dir_path = os.path.join(root_dir_path, 'templates')
    # post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')
    #
    # f = open(post_list_html_path, 'rt')
    # html = f.read()
    # f.close()
    #
    # print(cur_file_path)
    #
    #
    #
    # return HttpResponse(
    #     html)
