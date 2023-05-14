from django.shortcuts import render
from .models import Table
from django.views.generic import ListView
from django.db.models import Q


class SearchResults(ListView):
    """Класс, отвечающий за отображения страницы с результатами поиска"""

    model = Table
    template_name = 'filter/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Table.objects.filter(
            Q(company_name__icontains=query) | Q(country_company__icontains=query) | Q(aid_form__icontains=query) | Q(aid_name__icontains=query) | Q(mnn__icontains=query) | Q(dru__icontains=query)
        )
        return object_list


def main_page(request):
    """Функция получения данных о заказе из базы данных"""
    farma_info = Table.objects.all()
    farma_company_unique = Table.objects.values('company_name',).distinct()
    farma_company_country_unique = Table.objects.values('country_company',).distinct()
    farma_aid_form_unique = Table.objects.values('aid_form',).distinct()
    farma_aid_name_unique = Table.objects.values('aid_name',).distinct()
    farma_mnn_unique = Table.objects.values('mnn',).distinct()
    farma_dru_unique = Table.objects.values('dru',).distinct()

    company_name = ''

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        if company_name != '':
            farma_info = Table.objects.filter(company_name=company_name)
        else:
            farma_info = Table.objects.all()

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