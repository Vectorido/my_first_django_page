from django.shortcuts import render


# Create your views here.
def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'guinness_records/guinnessworldrecords.html', context=context)
