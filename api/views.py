from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponse, HttpRequest
from api.models import Company, Vacancy


def company_list(request):
    if request.method =='GET':
        # companies = Company.objects.filter(name='')
        # companies = Company.objects.filter(name__startswith='')
        # companies = Company.objects.filter(name__endswith='')
        # companies = Company.objects.filter(name__exact='')
         companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    data ={
        'companies': companies_json,
    }
    return JsonResponse(data)

def vacancy_list(request):
    if request.method == 'GET':


       vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    obj = {
        'vacancies': vacancies_json,
    }
    return JsonResponse(obj)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(vacancy.to_json())

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(company.to_json())


def company_vacancy(request, id):
    try:
      com = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = com.vacancy_set.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(vacancies_json, safe=False)


def vacancies_top(request):
        vacancies = Vacancy.objects.all().order_by('-salary')[:10];
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)




