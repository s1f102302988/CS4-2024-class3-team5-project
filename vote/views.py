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



@csrf_exempt
def vote(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = data.get('item')

            if item not in ['kinoko', 'takenoko']:
                return JsonResponse({'error': '無効な選択肢です。'}, status=400)

            # 投票結果を仮に保存するロジック
            # 実際にはデータベースやキャッシュを利用してください
            if not hasattr(vote, 'results'):
                vote.results = {'kinoko': 0, 'takenoko': 0}

            vote.results[item] += 1

            # 結果を返す
            total_votes = vote.results['kinoko'] + vote.results['takenoko']
            kinoko_percentage = (vote.results['kinoko'] / total_votes) * 100 if total_votes > 0 else 0
            takenoko_percentage = (vote.results['takenoko'] / total_votes) * 100 if total_votes > 0 else 0

            return JsonResponse({
                'kinoko_votes': vote.results['kinoko'],
                'takenoko_votes': vote.results['takenoko'],
                'kinoko': kinoko_percentage,
                'takenoko': takenoko_percentage
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': '不正なデータ形式です。'}, status=400)
    else:
        return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=405)

