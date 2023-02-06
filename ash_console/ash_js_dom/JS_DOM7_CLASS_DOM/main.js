//main.js에서 play.js 불러오기
//현재 예제에서는 main.js와 play.js 파일은 
//같은 경로에 있다는 것을 가정

import {Game} from './game.js';
var $titleButton = document.querySelector('#title-button');
$titleButton.addEventListener('click', (event) => {
    new Game();
});
