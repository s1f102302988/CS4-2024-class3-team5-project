from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def room(request, room_name):
    return render(request, "vote/room.html", {"room_name": room_name})
def index(request):
    return render(request, "vote/index.html")

def kinokotakenoko(request):
    return render(request, "vote/kinokotakenoko.html")

def loveormoney(request):
    return render(request, "vote/loveormoney.html")

def torokko(request):
    return render(request, "vote/torokko.html")

def room(request):
    return render(request, "vote/room.html")

 # きのこ vs たけのこ 用ビュー
@csrf_exempt
def vote_kinokotakenoko(request):
     """
     「きのこ vs たけのこ」に対する投票を受け付ける
     """
     if request.method == 'POST':
         try:
             data = json.loads(request.body)
             item = data.get('item')  # "kinoko" or "takenoko"

             if item not in ['kinoko', 'takenoko']:
                 return JsonResponse({'error': '無効な選択肢です。'}, status=400)

             # メモリ上に結果を保持
             if not hasattr(vote_kinokotakenoko, 'results'):
                 vote_kinokotakenoko.results = {'kinoko': 0, 'takenoko': 0}

             vote_kinokotakenoko.results[item] += 1

             total_votes = sum(vote_kinokotakenoko.results.values())
             kinoko_percentage = (vote_kinokotakenoko.results['kinoko'] / total_votes) * 100 if total_votes > 0 else 0
             takenoko_percentage = (vote_kinokotakenoko.results['takenoko'] / total_votes) * 100 if total_votes > 0 else 0

             return JsonResponse({
                 'kinoko_votes': vote_kinokotakenoko.results['kinoko'],
                 'takenoko_votes': vote_kinokotakenoko.results['takenoko'],
                 'kinoko': kinoko_percentage,
                 'takenoko': takenoko_percentage
             })
         except json.JSONDecodeError:
             return JsonResponse({'error': '不正なデータ形式です。'}, status=400)
     else:
         return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=405)


 # 愛 vs お金 用ビュー
@csrf_exempt
def vote_loveormoney(request):
     """
     「愛 vs お金」に対する投票を受け付ける
     """
     if request.method == 'POST':
         try:
             data = json.loads(request.body)
             item = data.get('item')  # "love" or "money"

             if item not in ['love', 'money']:
                 return JsonResponse({'error': '無効な選択肢です。'}, status=400)

             # メモリ上に結果を保持
             if not hasattr(vote_loveormoney, 'results'):
                 vote_loveormoney.results = {'love': 0, 'money': 0}

             vote_loveormoney.results[item] += 1

             total_votes = sum(vote_loveormoney.results.values())
             love_percentage = (vote_loveormoney.results['love'] / total_votes) * 100 if total_votes > 0 else 0
             money_percentage = (vote_loveormoney.results['money'] / total_votes) * 100 if total_votes > 0 else 0

             return JsonResponse({
                 'kinoko_votes': vote_loveormoney.results['love'],
                 'takenoko_votes': vote_loveormoney.results['money'],
                 'kinoko': love_percentage,
                 'takenoko': money_percentage
             })
         except json.JSONDecodeError:
             return JsonResponse({'error': '不正なデータ形式です。'}, status=400)
     else:
         return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=405)


 # トロッコ問題 用ビュー
@csrf_exempt
def vote_torokko(request):
     """
     「トロッコ問題」に対する投票を受け付ける
     """
     if request.method == 'POST':
         try:
             data = json.loads(request.body)
             item = data.get('item')  # "option1" or "option2"

             if item not in ['option1', 'option2']:
                 return JsonResponse({'error': '無効な選択肢です。'}, status=400)

             # メモリ上に結果を保持
             if not hasattr(vote_torokko, 'results'):
                 vote_torokko.results = {'option1': 0, 'option2': 0}

             vote_torokko.results[item] += 1

             total_votes = sum(vote_torokko.results.values())
             option1_percentage = (vote_torokko.results['option1'] / total_votes) * 100 if total_votes > 0 else 0
             option2_percentage = (vote_torokko.results['option2'] / total_votes) * 100 if total_votes > 0 else 0

             return JsonResponse({
                 'kinoko_votes': vote_torokko.results['option1'],
                 'takenoko_votes': vote_torokko.results['option2'],
                 'kinoko': option1_percentage,
                 'takenoko': option2_percentage
             })
         except json.JSONDecodeError:
             return JsonResponse({'error': '不正なデータ形式です。'}, status=400)
     else:
         return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=405)
