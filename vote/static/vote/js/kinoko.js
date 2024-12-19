const socket = new WebSocket('ws://127.0.0.1:8000/ws/vote/'); 

const form = document.querySelector('form');
const radioButtons = document.querySelectorAll('input[name="item"]');
const submitButton = document.querySelector('button[type="submit"]');

const resultContainer = document.createElement('div');
resultContainer.id = "vote-results";
resultContainer.style.marginTop = "30px";
resultContainer.style.fontSize = "1.2rem";
form.parentElement.appendChild(resultContainer);

socket.onopen = function () {
  console.log("WebSocket接続が確立されました。");
};

socket.onmessage = function (event) {
  const data = JSON.parse(event.data);

  updateResults(data);
};

socket.onerror = function (error) {
  console.error("WebSocketエラー: ", error);
};

form.addEventListener('submit', function (e) {
  e.preventDefault(); 

  let selectedValue = null;
  radioButtons.forEach((radio) => {
    if (radio.checked) {
      selectedValue = radio.value;
    }
  });

  if (selectedValue) {
    socket.send(JSON.stringify({
      action: 'vote',
      item: selectedValue
    }));

    submitButton.disabled = true;
    submitButton.innerText = "投票中...";
    setTimeout(() => {
      submitButton.disabled = false;
      submitButton.innerText = "投票";
    }, 2000);
  } else {
    alert("どちらかに投票してください！");
  }
});

function updateResults(data) {
  const kinokoCount = data.kinoko || 0;
  const takenokoCount = data.takenoko || 0;
  const total = kinokoCount + takenokoCount;

  const kinokoPercent = total ? ((kinokoCount / total) * 100).toFixed(1) : 0;
  const takenokoPercent = total ? ((takenokoCount / total) * 100).toFixed(1) : 0;

  resultContainer.innerHTML = `
    <h3>現在の投票結果</h3>
    <p>🍄 きのこ: ${kinokoCount} 票 (${kinokoPercent}%)</p>
    <p>🎋 たけのこ: ${takenokoCount} 票 (${takenokoPercent}%)</p>
    <p>合計投票数: ${total} 票</p>
  `;
}
