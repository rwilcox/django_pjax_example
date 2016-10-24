from django.http import HttpResponse
from django.template import loader, Context, Template

def index( request ):
    template = loader.get_template( 'django_pjax_example/index.html' )
    
    return HttpResponse( template.render( {}, request ) )

def name_form( request ):
    template = None
    
    if 'message/partial' in request.META['HTTP_ACCEPT']:
        template = loader.get_template( 'django_pjax_example/name_form_partial.html' )
    else:
        template = loader.get_template( 'django_pjax_example/name_form.html' )
    
    return HttpResponse( template.render( Context( {"query_params": request.GET } ) ) )

