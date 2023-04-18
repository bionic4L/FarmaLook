from django.shortcuts import render
from .models import Table


def main_page(request):
    farma_info = Table.objects.all()
    farma_company_unique = Table.objects.values('company_name',).distinct()
    farma_company_country_unique = Table.objects.values('country_company',).distinct()
    farma_aid_form_unique = Table.objects.values('aid_form',).distinct()
    farma_aid_name_unique = Table.objects.values('aid_name',).distinct()
    farma_mnn_unique = Table.objects.values('mnn',).distinct()
    farma_dru_unique = Table.objects.values('dru',).distinct()

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        farma_info = Table.objects.filter(company_name=company_name)


        context1 = {
            'farma_info': farma_info,
            'farma_company_unique': farma_company_unique,
            'farma_company_country_unique': farma_company_country_unique,
            'farma_aid_form_unique': farma_aid_form_unique,
            'farma_aid_name_unique': farma_aid_name_unique,
            'farma_mnn_unique': farma_mnn_unique,
            'farma_dru_unique': farma_dru_unique,
        }

    # return render(request, 'filter/main_page.html', context)
        return render(request, 'filter/main_page.html', context1)
    else:
        farma_info = Table.objects.all()
        context2 = {
            'farma_info': farma_info,
            'farma_company_unique': farma_company_unique,
            'farma_company_country_unique': farma_company_country_unique,
            'farma_aid_form_unique': farma_aid_form_unique,
            'farma_aid_name_unique': farma_aid_name_unique,
            'farma_mnn_unique': farma_mnn_unique,
            'farma_dru_unique': farma_dru_unique,
        }
        return render(request, 'filter/main_page.html', context2)