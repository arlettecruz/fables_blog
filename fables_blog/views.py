# views.py

from django.http import HttpResponse


def index(request):
    welcome_page = """
    <html>
        <body>
            <h1 style="text-align:center">Welcome to Fables of the World</h1>
            <p style="font-size:200%">Share the stories from around the world that unite us. </p>
            <p style="font-size:200%; text-align:left; color:blue">Because human spirit is universal,
             regardless of origin and time.</p>
        </body>
    </html>
    """
    return HttpResponse(welcome_page)
