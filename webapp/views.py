from django.shortcuts import render
from django.db.models import Max, F

from rates.models import Rate, Currency

def index(request, base='USD', target='EUR', months=24):

    currencies = Currency.objects.all().order_by('country_name')

    base_currency_code = base

    target_currency_code = target

    latest_rate_date = Rate.objects.all().aggregate(Max('rate_date'))

    base_rate = Rate.objects.all().filter(currency__currency_code=base_currency_code).filter(rate_date=latest_rate_date['rate_date__max']).select_related().first()

    rates = Rate.objects.all().filter(rate_date=latest_rate_date['rate_date__max']).annotate(ratio=F('per_dollar')/base_rate.per_dollar).select_related().order_by('currency__country_name')

    return render(request, 'webapp/index.html', context={
        'currencies': currencies,
        'base_currency_code': base_currency_code,
        'target_currency_code' : target_currency_code,
        'base_rate': base_rate,
        'rates': rates,
    })
