var $titleButton = document.querySelector("$title-button");
$titleButton.addEventListener("click", (e) => {
  new Game(); // Game class 호출
  console.log("!");
});
