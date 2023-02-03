function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 캔버스 삭제
    drawPlayer(); // 호출
}

function drawPlayer(){
    ctx.beginPath();

    ctx.rect(0, 0, 100, 100);
    ctx.fillStyle = "blue";
    ctx.fill();

    ctx.closePath();
}

//-------------------------------------------------
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d"); 
setInterval(draw, 10); // 100frame