from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def request_info(request):
    # POST 요청 시 세션에 값 저장
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            request.session['demo'] = message

    context = {
        'request_method': request.method,
        'path': request.path,
        'full_path': request.build_absolute_uri(),
        'client_ip': request.META.get('REMOTE_ADDR'),
        'user_agent': request.META.get('HTTP_USER_AGENT'),
        'get_data': request.GET,
        'post_data': request.POST,
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else '',
        'session_data': request.session.get('demo', '없음'),
    }
    return render(request, 'pybo/request_info.html', context)