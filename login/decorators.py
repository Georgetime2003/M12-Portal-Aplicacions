def grup_propi(func):
    def comprobar_grup(request, *args, **kwargs):
        pk = kwargs["pk"]
        if pk != request.user.id:
            return HttpResponse('Unauthorized', status=401)
        return func(request, *args, **kwargs)
    return comprobar_grup