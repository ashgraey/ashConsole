function drawPlayer(){
    ctx.beginPath(); // 열기

    ctx.rect(0, 0, 100, 100); // x, y, whidth, height
    ctx.fillStyle = "blue"; // 색상
    ctx.fill(); // 그려라

    ctx.closePath(); // 닫기
}

//-------------------------------------------------
var canvas = document.getElementById("myCanvas"); // canvas는 도화지
var ctx = canvas.getContext("2d"); // ctx로 그림을 그린다.
drawPlayer();