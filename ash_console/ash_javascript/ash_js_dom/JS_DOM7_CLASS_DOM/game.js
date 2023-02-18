// 데이터 클래스 import
import { Hero } from "./hero.js";
import { Wolf } from "./monster.js";
import { Tiger } from "./monster.js";
import { Bat } from "./monster.js";

export class Game {
  // 생성자(초기화)
  constructor() {
    this.$lobbyButton = document.querySelector("#lobby-button");
    this.$battleButton = document.querySelector("#battle-button");
    this.$lobbyButton.addEventListener("click", this.onLobbyMenuInput);
    this.$battleButton.addEventListener("click", this.onBattleMenuInput);

    this.$titleMenu = document.querySelector("#title-menu");
    this.$lobbyMenu = document.querySelector("#lobby-menu");
    this.$battleMenu = document.querySelector("#battle-menu");

    this.$heroName = document.querySelector("#hero-name");
    this.$heroHealth = document.querySelector("#hero-health");
    this.$heroPower = document.querySelector("#hero-power");

    this.$monsterName = document.querySelector("#monster-name");
    this.$monsterHealth = document.querySelector("#monster-health");
    this.$monsterPower = document.querySelector("#monster-power");

    this.hero = new Hero("용사", 50, 15, 30);
    this.updateHeroStat();

    this.monster = null;
    this.changeScreen("lobby");
  }

  // lobby menu
  onLobbyMenuInput = (event) => {
    var $menuInput = document.querySelector("#lobby-input");
    // input = lobby-input.value값을 가져옴
    var input = $menuInput.value;
    // 1.던전
    if (input == "1") {
      // css style display : none으로 화면 출력 조절
      this.changeScreen("battle");
      // monster data setting
      this.setRandomMonster();
      // setting 된 data를 html에 삽입
      this.updateMonsterStat();
      var txt = "몬스터와 전투에 돌입합니다";
      alert(txt);

      // 2.휴식
    } else if (input == "2") {
      // hero Object의 health 값 조정
      this.hero.health = 50;
      // html에 반영
      this.updateHeroStat();
      alert("체력을 모두 회복합니다.");

      // 3.종료
    } else if (input == "3") {
      alert("게임을 종료합니다.");
      // hero Object 초기화
      this.hero = null;
      // html에 반영
      this.updateHeroStat();
      // title 화면을 출력
      this.changeScreen("title");
    }
  };

  // $battleButton 클릭 시 발생하는 event
  onBattleMenuInput = (event) => {
    var $menuInput = document.querySelector("#battle-input");
    // battle-input에 입력 받은 값 => input
    var input = $menuInput.value;

    if (input == 4) {
      alert("전투에서 도망칩니다.");
      this.monster = null;
      this.updateMonsterStat();
      this.changeScreen("lobby");
      return; // 이벤트 종료
    }
    if (input == 1) {
      // hero에는 attack() 메소드가 없다.
      // 그럼에도 실행되는것은 hero의 부모인 unit클래스의 메소드를 상속 받고 있기때문에
      // hero Object.attack()이 실행될 수 있다. 상속 관계
      this.hero.attack(this.monster);
      // monster data 최신화
      this.updateMonsterStat();
      // alert txt
      var txt =
        this.hero.name +
        "은" +
        this.monster.name +
        "에게" +
        this.hero.power +
        "의 데미지를 줍니다.";
      alert(txt);

      this.monster.attack(this.hero);
      var txt =
        this.monster.name +
        "은" +
        this.hero.name +
        "에게" +
        this.monster.power +
        "의 데미지를 줍니다.";
      this.updateHeroStat();
      alert(txt);
    } else if (input == 2) {
      // 용사 -> 몬스터 어택
      this.hero.skill1Attack(this.monster);
      this.updateMonsterStat();
      var txt =
        this.hero.name +
        "은" +
        this.monster.name +
        "에게" +
        this.hero.power * 1.5 +
        "의 스킬1 데미지를 줍니다.";
      alert(txt);

      // 몬스터 => 용사
      this.monster.attack(this.hero);
      var txt =
        this.monster.name +
        "은" +
        this.hero.name +
        "에게" +
        this.monster.power +
        "의 데미지를 줍니다.";
      this.updateHeroStat();
      alert(txt);
    } else if (input == 3) {
      // 용사 -> 몬스터 어택
      this.hero.skill2Attack(this.monster);
      this.updateMonsterStat();
      var txt =
        this.hero.name +
        "은" +
        this.monster.name +
        "에게" +
        this.hero.power * 2 +
        "의 스킬2 데미지를 줍니다.";
      alert(txt);

      // 몬스터 => 용사
      this.monster.attack(this.hero);
      var txt =
        this.monster.name +
        "은" +
        this.hero.name +
        "에게" +
        this.monster.power +
        "의 데미지를 줍니다.";
      this.updateHeroStat();
      alert(txt);
    }

    // monster checkDead()
    if (this.monster.checkDead()) {
      alert("전투에서 승리합니다.");
      this.monster = null;
      this.updateMonsterStat();
      this.changeScreen("lobby");

      // checkDead()
    } else if (this.hero.checkDead()) {
      alert("용사가 전투에서 패배했습니다. 게임오버");
      this.hero = null;
      this.updateHeroStat();
      this.monster = null;
      this.updateMonsterStat();
      this.changeScreen("title");
    }
  };

  // hero data를 html에 삽입
  updateHeroStat() {
    if (this.hero === null) {
      this.$heroName.textContent = "";
      this.$heroHealth.textContent = "";
      this.$heroPower.textContent = "";
      return;
    }
    this.$heroName.textContent = this.hero.name;
    this.$heroHealth.textContent = this.hero.health;
    this.$heroPower.textContent = this.hero.power;
  }
  // moster data를 html에 삽입
  updateMonsterStat() {
    if (this.monster === null) {
      this.$monsterName.textContent = "";
      this.$monsterHealth.textContent = "";
      this.$monsterPower.textContent = "";
      return;
    }
    // construct에서 모두 초기화 해놓은 상태
    // html txt node에 update된 정보를 넣음
    this.$monsterName.textContent = this.monster.name;
    this.$monsterHealth.textContent = this.monster.health;
    this.$monsterPower.textContent = this.monster.power;
  }

  getRandomNumber(size) {
    return Math.floor(Math.random() * size);
  }

  setRandomMonster() {
    // 랜덤값을 index로 받아옴
    var index = this.getRandomNumber(3);
    // monster 데이터 세팅
    if (index == 0) {
      this.monster = new Wolf("늑대", 30, 5);
    } else if (index == 1) {
      this.monster = new Bat("박쥐", 20, 4);
    } else if (index == 2) {
      this.monster = new Tiger("호랑이", 40, 7);
    }
  }

  // 배경화면 change
  changeScreen(screen) {
    if (screen === "title") {
      this.$titleMenu.style.display = "block";
      this.$lobbyMenu.style.display = "none";
      this.$battleMenu.style.display = "none";
    } else if (screen === "lobby") {
      this.$titleMenu.style.display = "none";
      this.$lobbyMenu.style.display = "block";
      this.$battleMenu.style.display = "none";
    } else if (screen === "battle") {
      this.$titleMenu.style.display = "none";
      this.$lobbyMenu.style.display = "none";
      this.$battleMenu.style.display = "block";
    }
  }
}
