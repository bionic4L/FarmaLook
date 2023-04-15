from django.contrib import admin
from .models import Table


class FilterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company_name', 'reg_date', 'country_company', 'aid_form', 'aid_name', 'mnn', 'dru')
    list_editable = ('company_name','country_company', 'aid_form', 'aid_name', 'mnn', 'dru',)
    search_fields = ('company_name',)
    list_filter = ('reg_date',)
    empty_value_display = '-пусто-'


admin.site.register(Table)
