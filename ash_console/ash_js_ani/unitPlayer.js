
import { NodeAnimation } from "./nodeAnimation.js";
import { ManagerImage } from "./managerImage.js";
import { ManagerKey } from "./managerKey.js";
import { SkillSword } from "./skillSword.js";

export class UnitPlayer{
    constructor(){
        this.x = 100;
        this.y = 100;
        this.centerx = this.x + 180;
        this.centery = this.y + 210;
        this.z = this.y + 420;
        this.speed = 2;
        this.direction = "right";

        this.animationList = {};
        this.animationName = "player_idle_l";
        this.setAnimation();

        this.skillSwordList = [];
    }
    update(){     
        this.centerx = this.x + 180;
        this.centery = this.y + 210;
        this.z = this.y + 420;
        var d = ManagerKey.getInstance().getKeyStay("KeyD");
        var a = ManagerKey.getInstance().getKeyStay("KeyA");
        var w = ManagerKey.getInstance().getKeyStay("KeyW");
        var s = ManagerKey.getInstance().getKeyStay("KeyS");

        var j = ManagerKey.getInstance().getKeyOnce("KeyJ");
        var k = ManagerKey.getInstance().getKeyOnce("KeyK");

        if(d){
            this.animationName = "player_work_r"; 
            this.direction  = "right";
            this.x += this.speed;
        }
        if(a){
            this.animationName = "player_work_l"; 
            this.direction  = "left";
            this.x -= this.speed;
        }

        if(w){
            if(this.direction == "right"){
                this.animationName = "player_work_r"; 
            }else if(this.direction == "left"){
                this.animationName = "player_work_l"; 
            }
            this.y -= this.speed;
        }       
        if(s){
            if(this.direction == "right"){
                this.animationName = "player_work_r"; 
            }else if(this.direction == "left"){
                this.animationName = "player_work_l"; 
            }
            this.y += this.speed;
        }
        
        if(d == false && a == false && w == false && s == false)
        {
            if(this.direction == "right"){
                this.animationName = "player_idle_r"; 
            }else if(this.direction == "left"){
                this.animationName = "player_idle_l"; 
            }
        }


        if(j){
           // console.log(j);
           if(this.direction == "left"){
              // var skillSword = new SkillSword(this.x + 200 , this.y , 30, "once" , "right");
               var skillSword = new SkillSword(this.x - 130 , this.y + 100 , 8, "once" , this.direction );
               this.skillSwordList.push(skillSword);

           }else if(this.direction == "right"){
                var skillSword = new SkillSword(this.x + 130 , this.y + 100 , 8, "once" , this.direction );
                this.skillSwordList.push(skillSword);
           }
        }
        
        for(var i = 0; i < this.skillSwordList.length; i++){
            if(this.skillSwordList[i].once == true){
                this.skillSwordList.splice(i , 1);
                break;
            }else{
                this.skillSwordList[i].update();
            }
        }
        
    }
    draw(){
        this.animationDraw(this.x , this.y , 20 , "loop");

        for(var i = 0; i < this.skillSwordList.length; i++){
            this.skillSwordList[i].draw();
        }
    }

    setAnimation(){
        var list = [];
        var image = ManagerImage.getInstance().getImage("player_idle_l_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_idle_l_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_idle_l_03");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["player_idle_l"] = nodeAnimation;

        var list = [];
        image = ManagerImage.getInstance().getImage("player_idle_r_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_idle_r_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_idle_r_03");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["player_idle_r"] = nodeAnimation;

        var list = [];
        image = ManagerImage.getInstance().getImage("player_work_l_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_l_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_l_03");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_l_04");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["player_work_l"] = nodeAnimation;

        var list = [];
        image = ManagerImage.getInstance().getImage("player_work_r_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_r_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_r_03");
        list.push(image);
        image = ManagerImage.getInstance().getImage("player_work_r_04");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["player_work_r"] = nodeAnimation;

        
    }

    animationDraw( x , y , frame , type){
        var nodeAnimation = this.animationList[this.animationName];
        if(nodeAnimation == null){
            return;
        }
        if(type == "loop"){
            nodeAnimation.playLoop(x , y , frame);
        }else if(type == "once"){
           // nodeAnimation.playOnce(x , y , frame);
        }
    } 

   
}