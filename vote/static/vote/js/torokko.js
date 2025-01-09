const chatSocket = new WebSocket('ws://localhost:8000/ws/vote/torokko/');

// 投票ボタンが押された時の処理
const voteButton = document.querySelector('#vote-button');
voteButton.onclick = function () {
  const selectedItem = document.querySelector('input[name="item"]:checked');
  if (selectedItem) {
    // 選択された項目をサーバーに送信
    chatSocket.send(JSON.stringify({ 'message': selectedItem.value }));
  } else {
    alert('項目を選択してください！');
  }
};

// サーバーからメッセージを受け取った時の処理
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);

  if (data.kinoko !== undefined && data.takenoko !== undefined) {
    const total = data.kinoko + data.takenoko;

    // 投票数から割合を計算
    const kinokoPercentage = total ? (data.kinoko / total) * 100 : 50;
    const takenokoPercentage = total ? (data.takenoko / total) * 100 : 50;

    // 進捗バーの更新
    const kinokoBar = document.querySelector('#kinoko-bar');
    kinokoBar.style.width = kinokoPercentage + '%';
    kinokoBar.textContent = `愛: ${data.kinoko}票`;

    const takenokoBar = document.querySelector('#takenoko-bar');
    takenokoBar.style.width = takenokoPercentage + '%';
    takenokoBar.textContent = `お金: ${data.takenoko}票`;
  }
};

// WebSocketが閉じられた時の処理
chatSocket.onclose = function () {
  console.error('WebSocketが予期せず閉じられました');
};

chatSocket.onopen = function () {
  console.log('WebSocketが接続されました');
};

chatSocket.onerror = function (error) {
  console.error('WebSocketエラー:', error);
};

document.querySelector('#vote-button').onclick = function () {
  const selectedItem = document.querySelector('input[name="item"]:checked');
  if (selectedItem) {
    const voteType = 'torokko'; // ここを投票種別に応じて変更
    chatSocket.send(JSON.stringify({ 
      'type': voteType, 
      'message': selectedItem.value 
    }));
  } else {
    alert('項目を選択してください！');
  }
};


if (chatSocket.readyState === WebSocket.OPEN) {
  chatSocket.send(JSON.stringify({ 'message': selectedItem.value }));
} else {
  console.error('WebSocketが接続されていません');
}