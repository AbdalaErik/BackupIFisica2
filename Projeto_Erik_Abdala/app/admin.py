from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

# admin.site.register(Area)
# admin.site.register(Subarea)
admin.site.register(Topico)
admin.site.register(Fisico)
admin.site.register(Invencao)
admin.site.register(Questao)
admin.site.register(Questionario)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(QuestionarioRespondido)

class SubareaInline(admin.TabularInline):

    model = Subarea

    form = SubareaForm

    extra = 1

class AreaAdmin(admin.ModelAdmin):

    inlines = [SubareaInline]

class TopicoInline(admin.TabularInline):

    model = Topico

    form = TopicoForm

    extra = 1

class SubareaAdmin(admin.ModelAdmin):

    inlines = [TopicoInline]
    
admin.site.register(Area, AreaAdmin)
admin.site.register(Subarea, SubareaAdmin)