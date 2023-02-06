
import {Hero} from './hero.js';
import {Wolf} from './monster.js';
import {Tiger} from './monster.js';
import {Bat} from './monster.js';

export class Game{
    constructor(){
        this.$lobbyButton= document.querySelector('#lobby-button');
        this.$battleButton = document.querySelector('#battle-button');
        this.$lobbyButton.addEventListener('click', this.onLobbyMenuInput);
        this.$battleButton.addEventListener('click', this.onBattleMenuInput);

        this.$titleMenu = document.querySelector('#title-menu');
        this.$lobbyMenu = document.querySelector('#lobby-menu');
        this.$battleMenu = document.querySelector('#battle-menu');

        this.$heroName = document.querySelector('#hero-name');
        this.$heroHealth = document.querySelector('#hero-health');
        this.$heroPower = document.querySelector('#hero-power');

        this.$monsterName = document.querySelector('#monster-name');
        this.$monsterHealth = document.querySelector('#monster-health');
        this.$monsterPower = document.querySelector('#monster-power');


        this.hero = new Hero("용사", 50 , 15);
        this.updateHeroStat();

        this.monster = null;
        this.changeScreen('lobby');

    }
    onLobbyMenuInput = (event) => {
        var $menuInput = document.querySelector('#lobby-input');
        var input = $menuInput.value;
        if (input == "1"){
           this.changeScreen('battle');
           this.setRandomMonster();
           this.updateMonsterStat();
           var txt = "몬스터와 전투에 돌입합니다";
           alert(txt);
        }else if(input == "2"){
            this.hero.health = 50;
            this.updateHeroStat();
            alert("체력을 모두 회복합니다.")
        }else if(input == "3"){
            alert("게임을 종료합니다.");
            this.hero = null;
            this.updateHeroStat();
            this.changeScreen("title");
        }
    } 
    onBattleMenuInput = (event) => {
        var $menuInput = document.querySelector('#battle-input');
        var input = $menuInput.value;

        if(input == 4){
            alert("전투에서 도망칩니다.");
            this.monster = null;
            this.updateMonsterStat();
            this.changeScreen("lobby");
            return;
        }
        if(input == 1){
            this.hero.attack(this.monster);
            this.updateMonsterStat();
            var txt = this.hero.name + "은" + this.monster.name + "에게" + this.hero.power + "의 데미지를 줍니다.";    
            alert(txt);   
            
            this.monster.attack(this.hero);
            var txt = this.monster.name + "은" + this.hero.name + "에게" + this.monster.power + "의 데미지를 줍니다.";
            this.updateHeroStat();
            alert(txt);

        }else if(input == 2){

        }else if(input == 3){

        }          
        if(this.monster.checkDead()){
            alert("전투에서 승리합니다.");
            this.monster = null;
            this.updateMonsterStat();
            this.changeScreen("lobby");
        }      
        else if(this.hero.checkDead()){
            alert("용사가 전투에서 패배했습니다. 게임오버");
            this.hero = null;    
            this.updateHeroStat();
            this.monster = null;
            this.updateMonsterStat();
            this.changeScreen("title");
            
        }
    } 

    updateHeroStat() {
        if (this.hero === null) {
          this.$heroName.textContent = '';
          this.$heroHealth.textContent = '';
          this.$heroPower.textContent = '';
          return;
        }
        this.$heroName.textContent = this.hero.name;
        this.$heroHealth.textContent = this.hero.health;
        this.$heroPower.textContent = this.hero.power;
    }
    updateMonsterStat(){
        if (this.monster === null) {
            this.$monsterName.textContent = '';
            this.$monsterHealth.textContent = '';
            this.$monsterPower.textContent = '';
            return;
          }
          this.$monsterName.textContent = this.monster.name;
          this.$monsterHealth.textContent = this.monster.health;
          this.$monsterPower.textContent = this.monster.power;
    }


    getRandomNumber(size){
        return Math.floor(Math.random() * size);
    }

    setRandomMonster(){
        var index = this.getRandomNumber(3);
        if(index == 0){
             this.monster = new Wolf("늑대" , 30, 5);
         }
         else if(index == 1){
             this.monster = new Bat("박쥐" , 20, 4);
         }
         else if(index == 2){
             this.monster = new Tiger("호랑이" , 40, 7);
         }
    }

    changeScreen(screen) {
        if (screen === 'title') {
          this.$titleMenu.style.display = 'block';
          this.$lobbyMenu.style.display = 'none';
          this.$battleMenu.style.display = 'none';
        } else if (screen === 'lobby') {
          this.$titleMenu.style.display = 'none';
          this.$lobbyMenu.style.display = 'block';
          this.$battleMenu.style.display = 'none';
        } else if (screen === 'battle') {
          this.$titleMenu.style.display = 'none';
          this.$lobbyMenu.style.display = 'none';
          this.$battleMenu.style.display = 'block';
        }
    }
    
}