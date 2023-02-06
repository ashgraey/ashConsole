function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // 캔버스 삭제
  drawPlayer(); // 캔버스 생성
}

function drawPlayer() {
  ctx.beginPath();

  ctx.rect(0, 0, 100, 100);
  ctx.fillStyle = "blue";
  ctx.fill();

  ctx.closePath();
}

//-------------------------------------------------
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
setInterval(draw, 10); // 100프레임

// 애니메이션의 기본 원리
// 그리기 -> 지우기 -> 그리기 -> 지우기.. 계속 반복하면서 움직은 모양 연출
