//main.js에서 game.js 불러오기
//현재 예제에서는 main.js와 game.js 파일은
//같은 경로에 있다는 것을 가정

import { Game } from "./game.js"; // game.js 안에 있는 class game
var $titleButton = document.querySelector("#title-button");
$titleButton.addEventListener("click", (event) => {
  new Game(); // game 클래스 호출
});
