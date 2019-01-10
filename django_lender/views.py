from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    """Respond to requests on the home route.

    :input: request: request object
    :return: render the home template
    """
    return render(request, 'generic/home.html')
