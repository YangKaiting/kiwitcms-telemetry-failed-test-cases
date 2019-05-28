from django.shortcuts import render
from django.db.models import Count, Q, FloatField
from django.db.models.functions import Cast

from .forms import SearchProductForm
from tcms.testplans.models import TestPlan
from tcms.testruns.models import TestRun, TestExecution
from tcms.management.models import Product

def example(request):
    """An example view of Telemetry plugin"""
    return render(request, 'telemetryPlugin/example.html')

def get(request, template_name='telemetryPlugin/failed_test_case_by_projects.html'):
    searched_product_id = None
    if request.method == 'POST':
        form = SearchProductForm(request.POST)
        if form.is_valid():
            searched_product_name = form.cleaned_data['name_product']
            searched_products = Product.objects.filter(name__icontains=searched_product_name)
            if searched_products is not None:
                searched_product_id = [sp.id for sp in searched_products]
    else:
        form = SearchProductForm()

    # to get all the products' id
    all_products = Product.objects.all().order_by()
    all_product_id = [ap.id for ap in all_products]

    if searched_product_id is None:
        selected_or_all_product_id = all_product_id
    else:
        selected_or_all_product_id = searched_product_id
    
    projects = []
    for each_product_id in selected_or_all_product_id:
        cases = TestExecution.objects.filter(run__plan__product__id=each_product_id) \
        .values('case','case__summary').order_by('case') \
        .annotate(count=Count('case')) \
        .annotate(fail=Count('status', filter=Q(status=5))) \
        .annotate(FailurePercentage=(Count('status', filter=Q(status=5))*1.0/Count('case'))*100.0) \
        .annotate(SuccessPercentage=(1-(Count('status', filter=Q(status=5))*1.0/Count('case')))*100.0)

        per_project = {
            'product_id': Product.objects.values('name').get(pk=int(each_product_id)),
            'cases': cases,
        }
        projects.append(per_project) 

    data = {
        'form': form,
        'projects': projects,
    }

    return render(request, template_name, data)
