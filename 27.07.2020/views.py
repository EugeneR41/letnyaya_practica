from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_http_methods(['GET', 'PUT', 'POST'])
def simple_route(request, something=None):
    if request.method == 'GET' and something is None:  # если get запрос с правильным указание ссылки, то вернем 200
        return HttpResponse(content='', status=200)
    elif request.method in ['POST', 'PUT']:     # если запрос post или put, то вернем 405 иначе 404
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)


@require_http_methods(['GET'])
def slug_route(request, first=None, second=None):
    if second is None:
        return HttpResponse(content=first, status=200)
    else:
        return HttpResponse(status=404)


@require_http_methods(['GET'])
def sum_route(request, first, second):
    if first.isdigit and second.isdigit:  # Если два инта, то ссумируем и возвращаем 200 иначе 404
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=404)


@require_http_methods(['GET'])
def sum_get_method(request):
    first = request.GET.get('a')
    second = request.GET.get('b')

    if first.isdigit and second.isdigit:  # как и в предыдущей функции, только сначала ищем а и б
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)


@require_http_methods(['POST'])
def sum_post_method(request):
    first = request.POST.get('a')
    second = request.POST.get('b')

    if first.isdigit and second.isdigit:  # как и в предыдущей функции
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)


