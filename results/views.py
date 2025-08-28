from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Max
from django.utils import timezone
from .models import PollingUnit, AnnouncedPUResults, Ward, LGA


def polling_unit_result(request, pu_id):
    polling_unit = get_object_or_404(PollingUnit, uniqueid=pu_id)
    results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid=pu_id)
    return render(request, 'results/polling_unit_result.html', {
        'polling_unit': polling_unit,
        'results': results
    })


def lga_results(request):
    lgas = LGA.objects.all()
    results = None
    selected_lga = None

    if request.method == 'POST':
        lga_id = request.POST.get('lga')
        if lga_id:
            lga_id = int(lga_id)
            selected_lga = LGA.objects.get(lga_id=lga_id)
            pus = PollingUnit.objects.filter(
                lga_id=lga_id).values_list('uniqueid', flat=True)
            results = (AnnouncedPUResults.objects
                       .filter(polling_unit_uniqueid__in=pus)
                       .values('party_abbreviation')
                       .annotate(total_score=Sum('party_score'))
                       .order_by('party_abbreviation'))

    return render(request, 'results/lga_results.html', {
        'lgas': lgas,
        'results': results,
        'selected_lga': selected_lga
    })


def add_polling_unit_results(request):
    wards = Ward.objects.all()
    parties = ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP']

    if request.method == 'POST':
        polling_unit_name = request.POST.get('polling_unit_name')
        ward_id = request.POST.get('ward')
        entered_by_user = request.POST.get('entered_by_user', 'admin')

        ward = Ward.objects.filter(ward_id=ward_id).first()
        if not ward:
            return render(request, 'results/add_polling_unit_results.html', {
                'wards': wards,
                'parties': parties,
                'error': 'Selected ward does not exist.'
            })

        new_uniqueid = (PollingUnit.objects.aggregate(
            Max('uniqueid'))['uniqueid__max'] or 0) + 1

        new_pu = PollingUnit.objects.create(
            uniqueid=new_uniqueid,
            polling_unit_id=0,
            ward_id=ward.ward_id,
            lga_id=ward.lga_id,
            polling_unit_name=polling_unit_name
        )

        for party in parties:
            score = request.POST.get(party)
            if score:
                AnnouncedPUResults.objects.create(
                    polling_unit_uniqueid=new_pu.uniqueid,
                    party_abbreviation=party,
                    party_score=int(score),
                    entered_by_user=entered_by_user,
                    date_entered=timezone.now()
                )

        return redirect('polling_unit_result', pu_id=new_pu.uniqueid)

    return render(request, 'results/add_polling_unit_results.html', {
        'wards': wards,
        'parties': parties
    })
