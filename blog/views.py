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

def post_detail(request, pk):
    print('post_detail request', request)
    print('post_detail pk', pk)

    # 이 view 함수의 매개변수로 전달되는 'pk'를 사용해서
    # 전달받은 'pk'갑싱 자신의 'pk' DB Column값과 같은 Post를 post변수에 지정
    # 이후 pk에 따라 /post-detail/에 접근했을 때, 다른 Post가 출력되는지 확
    # posts = Post.objects.filter(pk=pk)
    # post = posts[0]

    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
      return HttpResponse('없음')


    context = {
            'post': post,
        }


    return render(request, 'post_detail.html', context)


def post_add(request):
    # URL:    /posts/add
    # View: 이 함수
    # Template: post_add.html
    # form태그 내부에
    # input 한개, textarea한개, button[type=submit]한개

    #base.html의 nav 안에 /posts/add/로의 링크 하나 추가
    # 링크 텍스트: Post Add


    return render(request, 'post_add.html')







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
