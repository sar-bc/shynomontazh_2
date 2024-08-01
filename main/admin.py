from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.forms.widgets import SplitDateTimeWidget

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageForm(forms.ModelForm):
    body = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = ('title', 'slug', 'body')


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    form = PageForm


class RecordForm(forms.ModelForm):
    event_date = forms.DateField(widget=AdminDateWidget(), label='Дата')
    # event_time = forms.TimeField(widget=AdminTimeWidget())

    class Meta:
        model = Recording_Time
        fields = ['avto']


class RecordingAdmin(admin.ModelAdmin):
    form = RecordForm

    class Meta:
        model = Recording_Time
        fields = ['avto']


admin.site.register(Recording_Time, RecordingAdmin)
admin.site.register(Time)
admin.site.register(UserMessage)
admin.site.register(Page, PageAdmin)
