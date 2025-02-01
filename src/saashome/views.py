from django.http import HttpResponse
import pathlib

from django.shortcuts import render
from visits.models import PageVisits



def my_home_page(request,*args ,**kwargs):
    new_title="hello new world"
    queryset=PageVisits.objects.all()


    my_new_context={
        "new_context":new_title,
        "queryset":queryset.count()
    }
    html_template="home.html"
    PageVisits.objects.create()

    return render(request, html_template,my_new_context)


# this_dir=pathlib.Path(__file__).resolve().parent
def home_page_view(request,*args,**kwargs):
    # print(this_dir)
    my_title="what ur"

    my_context={
        "my_page":my_title
    }
    html_="""<!DOCTYPE html>
<html>
    <body>
        <h1>{my_page} anything....???</h1>
    </body>
</html>

""".format(**my_context)
    # html_file_path=this_dir / "home.html"
    # html_=html_file_path.read_text()
    
    return HttpResponse(html_)