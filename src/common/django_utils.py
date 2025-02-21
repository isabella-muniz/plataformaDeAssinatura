"""cOMMON DJANGO UTILITIES USED BY SEVERAL OTHER PACKAGES AND DJANGO"""
__all__=(
    'AsyncFormMixin',
    'AsyncModelFormMixin',
    'arender',

)

from django import forms
from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.shortcuts import render 


class AsyncFormMixin(forms.BaseForm):

    @sync_to_async
    def ais_valid(self: forms.BaseForm): #type: ignore
        return self.is_valid()
    #:

    @sync_to_async
    def arender(self: forms.BaseForm): #type ignore
        return self.render()
    #:
#:

class AsyncModelFormMixin(AsyncFormMixin):
    @sync_to_async
    def asave(self: forms.ModelForm): #type ignore
        return self.save()
    #:
#:

async def arender(*render_args, **render_kargs) -> HttpResponse:
    @sync_to_async
    def sync_call_render() -> HttpResponse:
        return render(*render_args, **render_kargs)
    return await sync_call_render()
#: