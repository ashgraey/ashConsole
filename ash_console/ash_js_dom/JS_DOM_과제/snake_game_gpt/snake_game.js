const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

// Set canvas dimensions
canvas.width = 500;
canvas.height = 500;

// Set the size of each block
const blockSize = 10;

// Initialize the snake
let snake = [];
for (let i = 5; i >= 0; i--) {
  snake.push({ x: i, y: 0 });
}

// Set the starting direction
let direction = "right";

// Draw the snake on the canvas
function drawSnake() {
  snake.forEach((block) => {
    ctx.fillRect(
      block.x * blockSize,
      block.y * blockSize,
      blockSize,
      blockSize
    );
  });
}

// Clear the canvas
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Move the snake in the specified direction
function moveSnake() {
  let x = snake[0].x;
  let y = snake[0].y;

  switch (direction) {
    case "right":
      x++;
      break;
    case "left":
      x--;
      break;
    case "up":
      y--;
      break;
    case "down":
      y++;
      break;
  }

  // Add the new head to the front of the snake
  snake.unshift({ x, y });

  // Remove the tail of the snake
  snake.pop();
}

// The main game loop
function gameLoop() {
  clearCanvas();
  drawSnake();
  moveSnake();

  setTimeout(gameLoop, 100);
}

// Listen for arrow key presses to change the direction of the snake
document.onkeydown = function (event) {
  switch (event.keyCode) {
    case 37:
      if (direction !== "right") direction = "left";
      break;
    case 38:
      if (direction !== "down") direction = "up";
      break;
    case 39:
      if (direction !== "left") direction = "right";
      break;
    case 40:
      if (direction !== "up") direction = "down";
      break;
  }
};

gameLoop();
