from django.shortcuts import render, get_object_or_404
from .models import Table
from django.template import loader
from django.http import HttpResponse


def main_page(request):
    farma_info = Table.objects.all()
    # farma_info_company_name = farma_info.company_name
    # farma_info_reg_date = farma_info.reg_date
    # farma_info_country = farma_info.country_company
    # farma_info_aid_form = farma_info.aid_form
    # farma_info_aid_name = farma_info.aid_name
    # farma_info_mnn = farma_info.mnn
    # farma_info_dru = farma_info.dru
    
    context = {
        'farma_info': farma_info,
        # 'farma_info_company_name': farma_info_company_name,
        # 'farma_info_reg_date': farma_info_reg_date,
        # 'farma_info_country': farma_info_country,
        # 'farma_info_aid_form': farma_info_aid_form,
        # 'farma_info_aid_name': farma_info_aid_name,
        # 'farma_info_mnn': farma_info_mnn,
        # 'farma_info_dru': farma_info_dru

        
    }

    return render(request, 'filter/main_page.html', context)
