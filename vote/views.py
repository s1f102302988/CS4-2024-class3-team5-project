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



@csrf_exempt  # 必要に応じてCSRFトークンを無効化（デバッグ用）
def vote(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # リクエストボディをJSONとして読み込む
            item = data.get('item')  # 'item'を取得

            if item not in ['kinoko', 'takenoko']:
                return JsonResponse({'error': '無効な選択肢です。'}, status=400)

            # ここでデータベースに投票を保存するロジックを追加
            print(f"選択されたアイテム: {item}")

            return JsonResponse({'message': '投票ありがとうございました！'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': '不正なデータ形式です。'}, status=400)
    else:
        return JsonResponse({'error': 'POSTメソッドを使用してください。'}, status=405)
