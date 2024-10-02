from datetime import date
from django.shortcuts import render
from .forms import DataCollectionForm
from django.http import JsonResponse
from .models import UserData
from django.db.models import Avg, Count, F


def data_collection_view(request):
    if request.method == "POST":
        form = DataCollectionForm(request.POST)
        if form.is_valid():
            # Save the form data to the UserData model
            form.save()

            # Optionally, you can redirect to a success page or show a message
            return render(request, 'done.html')
    else:
        form = DataCollectionForm()
        return render(request, 'data_collection.html', {'form': form})
    
    return render(request, 'data_collection.html', {'form': form})




def graph_view(request):
    # a) Quantos técnicos da AFI nasceram na década de 1970?
    afi_1970s = UserData.objects.filter(unit_area='AFI', birth_date__year__gte=1970, birth_date__year__lt=1980).count()

    # b) Quantos técnicos existem no total (presentes) na ASB?
    asb_total = UserData.objects.filter(unit_area='ASB').count()

    # c) Idade média dos colaboradores da AAS? 
    current_year = date.today().year
    aas_mean_age = UserData.objects.filter(unit_area='AAS').annotate(
        age=current_year - F('birth_date__year')
    ).aggregate(mean_age=Avg('age'))['mean_age']

    # d) Quantos técnicos da AII entraram no Banco antes de 2010?
    aii_pre_2010 = UserData.objects.filter(unit_area='AII', year_joined__lt=2010).count()

    # e) Quantas mulheres/homens existem na UATP?
    uatp_women = UserData.objects.filter(unit_area='UATP', gender='F').count()
    uatp_men = UserData.objects.filter(unit_area='UATP', gender='M').count()

    # f) Em que ano entraram os membros da Direção para o Banco?
    direcao_years = UserData.objects.filter(unit_area='DIR').values_list('year_joined', flat=True)

    context = {
        'afi_1970s': afi_1970s,
        'asb_total': asb_total,
        'aas_mean_age': aas_mean_age,
        'aii_pre_2010': aii_pre_2010,
        'uatp_women': uatp_women,
        'uatp_men': uatp_men,
        'direcao_years': list(direcao_years),
    }
    return render(request, 'graph.html', context)

from django.http import JsonResponse
from django.db.models import Count

from django.http import JsonResponse
from django.db.models import Count


def bar_chart_data_view(request):
    # Available areas from the DAS_CHOICES field of the UserData model
    areas = [choice[0] for choice in UserData.DAS_CHOICES]

    # Define decades dynamically (1970, 1980, ..., 2020)
    decades = [(1970 + i * 10) for i in range(6)]  # From 1970 to 2020

    # Initialize a dictionary to store counts per area for each category
    data_per_area = {
        'decade': {},
        'department': {},
        'gender': { 'Masculino': {}, 'Feminino': {} },
        'function': { 'Estagiário': {}, 'Técnico': {}, 'Coordenador': {}, 'Direção': {} },
    }

    # Calculate counts for decades
    for area in areas:
        counts_per_decade = []
        for decade in decades:
            count = UserData.objects.filter(
                unit_area=area,
                birth_date__year__gte=decade,
                birth_date__year__lt=decade + 10
            ).count()
            counts_per_decade.append(count)
        
        data_per_area['decade'][area] = counts_per_decade

    # Count users per department
    for area in areas:
        count = UserData.objects.filter(unit_area=area).count()
        data_per_area['department'][area] = count

    # Count users by gender
    for area in areas:
        data_per_area['gender']['Masculino'][area] = UserData.objects.filter(gender='M', unit_area=area).count()
        data_per_area['gender']['Feminino'][area] = UserData.objects.filter(gender='F', unit_area=area).count()

    # Count users by function
    for func, func_name in [('E', 'Estagiário'), ('T', 'Técnico'), ('C', 'Coordenador'), ('D', 'Direção')]:
        for area in areas:
            data_per_area['function'][func_name][area] = UserData.objects.filter(function=func, unit_area=area).count()

    # Prepare the response data
    data = {
        'decades': decades,
        'data_per_area': data_per_area
    }

    return JsonResponse(data)


