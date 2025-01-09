document.addEventListener('DOMContentLoaded', function() {
    const backgrounds = [
        'url(https://embed.pixiv.net/spotlight.php?id=1387&lang=ja)',
        'url(https://d2dcan0armyq93.cloudfront.net/photo/odai/600/463d21d3442cc99c60fe2626ceb37f0e_600.jpg)',
        'url(https://i.pinimg.com/originals/f7/a6/71/f7a671cb4901f216c931840fad3ce49a.jpg)',
    ];
    let currentIndex = 0;
    const backgroundElement = document.querySelector('.background');

    function nextBackground() {
        currentIndex = (currentIndex + 1) % backgrounds.length;
        backgroundElement.style.backgroundImage = backgrounds[currentIndex];
    }

    setInterval(nextBackground, 3000); // 3秒ごとに切り替え

    // 初回背景画像設定
    backgroundElement.style.backgroundImage = backgrounds[currentIndex];
});
