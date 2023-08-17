from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from .models import YourModel
from accounts.models import Influencer
from django.core import serializers

# Create your views here.
def first_index(request):
    logout(request)
    return render(request, "first-index.html")

def InfluHome(request):
    return render(request, "InfluHome.html")

def AdvHome(request):
    influencers = Influencer.objects.all()    
    return render(request, 'AdvHome.html', {'influencers': influencers})

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details(request, pk):
    item = get_object_or_404(YourModel, pk=pk)
    
    # query = request.GET.get('q')
    # if query and query in item.body:
    #     return redirect('search-results', q=query)
    
    context = {'item': item}
    return render(request, 'portfolio-details.html', context)

def portfolio_details01(request):
    return render(request, "portfolio-details01.html")

def TermOfUse_A(request):
    return render(request, "TermOfUse_A.html")

def PrivacyPolicy_A(request):
    return render(request, "PrivacyPolicy_A.html")

def TermOfUse_I(request):
    return render(request, "TermOfUse_I.html")

def PrivacyPolicy_I(request):
    return render(request, "PrivacyPolicy_I.html")

from django.http import JsonResponse

def get_influencer_data(request):
    influencer_name = request.GET.get('influencer', None)
    
    influencer = Influencer.objects.get(username=influencer_name)  # 여기서는 인플루언서 이름으로 조회
    
    influencer_data = {
        '게시글': influencer.media_count,
        '팔로워 수': influencer.followers_count,
        '팔로우 수': influencer.follows_count,
        # ... 추가 필드들
    }
    
    return JsonResponse(influencer_data)