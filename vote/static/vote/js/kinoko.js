document.querySelector('.btn-primary').onclick = function (e) {
  e.preventDefault(); // フォームのデフォルト送信を防ぐ

  // 選択されたラジオボタンの値を取得
  const selectedItem = document.querySelector('input[name="item"]:checked');
  if (!selectedItem) {
      alert("投票対象を選択してください！");
      return;
  }

  // 投票データをWebSocket経由で送信
  const vote = selectedItem.value; // "kinoko" または "takenoko"
  chatSocket.send(JSON.stringify({ message: vote }));

  // UIをリセット（必要に応じて）
  alert(`"${vote}" に投票しました！`);
  document.querySelector('form').reset();
};

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);

  // 投票データを更新
  document.querySelector('#chat-log').value += `きのこ: ${data.kinoko}票, たけのこ: ${data.takenoko}票\n`;
};
