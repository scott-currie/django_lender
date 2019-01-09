from django.shortcuts import render


def home_view(request):
    """Respond to requests on the home route.

    :input: request: request object
    :return: render the home template
    """
    return render(request, 'generic/home.html')
