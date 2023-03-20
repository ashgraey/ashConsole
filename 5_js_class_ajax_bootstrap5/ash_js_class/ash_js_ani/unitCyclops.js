
import { NodeAnimation } from "./nodeAnimation.js";
import { ManagerImage } from "./managerImage.js";

export class UnitCyclops{
    constructor(){
        this.x = Math.floor(Math.random() * 600 + 600);
        this.y = Math.floor(Math.random() * 300 + 100);
        this.centerx = this.x + 135;
        this.centery = this.y + 160;
        this.z = this.y + 320;
        this.speed = 1;
        this.direction = "left";

        this.animationList = {};
        this.animationName = "사이클롭스_가만히_l";
        this.setAnimation();

        this.ai = 0;
        this.aiDelay = 100;
        this.startTime = 0;

    }
    update(){     
        this.centerx = this.x + 135;
        this.centery = this.y + 160;
        this.z = this.y + 320;
        this.startTime += 1;
       if(this.startTime >= this.aiDelay){

            this.aiAction();

            this.startTime = 0;
       }
       if(this.target == null){
            this.ai = "idle";
            this.animationName = "사이클롭스_가만히_l";
            return;
       }

       if(this.ai == "idle"){
            if(this.direction == "left"){
                this.animationName = "사이클롭스_가만히_l";
            }else if(this.direction == "right"){

                this.animationName = "사이클롭스_가만히_r";
            }
       }else if(this.ai == "moveleft"){
            this.direction = "left";
            this.animationName = "사이클롭스_이동_l";
            this.x -= this.speed;
       }else if(this.ai == "moveright"){
            this.direction = "right";
            this.animationName = "사이클롭스_이동_r";
            this.x += this.speed;
       }else if(this.ai == "moveup"){
            if(this.direction == "left"){
                this.animationName = "사이클롭스_이동_l";
            }else if(this.direction == "right"){
                this.animationName = "사이클롭스_이동_r";
            }
            this.y -= this.speed;
       }else if(this.ai == "movedown"){
            if(this.direction == "left"){
                this.animationName = "사이클롭스_이동_l";
            }else if(this.direction == "right"){
                this.animationName = "사이클롭스_이동_r";
            }
            this.y += this.speed;
       }else if(this.ai == "skill"){
            
       }
        
    }
    aiAction(){
        if(this.target.centerx < this.centerx && this.target.centerx + 300 >= this.centerx){
            this.direction = "left";
            var r = Math.floor(Math.random() * 2);
            if( r == 0){
                if(this.target.centery < this.centery){
                    this.ai = "moveup";
                }else {
                    this.ai = "movedown";
                }
            }else{
                this.ai = "skill";
            }
       } if(this.target.centerx < this.centerx && this.target.centerx + 300 < this.centerx){
            this.direction = "left";
            var r = Math.floor(Math.random() * 2);
            if( r == 0){
                this.ai = "moveleft";
            }else{
                this.ai = "idle";
            }
       } if(this.target.centerx >= this.centerx && this.target.centerx - 300 <= this.centerx){
            this.direction = "right";
            var r = Math.floor(Math.random() * 2);
            if( r == 0){
                if(this.target.centery < this.centery){
                    this.ai = "moveup";
                }else {
                    this.ai = "movedown";
                }
            }else{
                this.ai = "skill";
            }
       } if(this.target.centerx >= this.centerx && this.target.centerx - 300 > this.centerx){
            this.direction = "right";
            var r = Math.floor(Math.random() * 2);
            if( r == 0){
                this.ai = "moveright";
            }else{
                this.ai = "idle";
            }
       }
    }

    draw(){
        this.animationDraw(this.x , this.y , 20 , "loop");

        
    }
    setTarget(player){
        this.target = player;
    }


    setAnimation(){
        var list = [];
        var image = ManagerImage.getInstance().getImage("사이클롭스_가만히_l_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_가만히_l_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_가만히_l_03");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["사이클롭스_가만히_l"] = nodeAnimation;

        var list = [];
        var image = ManagerImage.getInstance().getImage("사이클롭스_가만히_r_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_가만히_r_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_가만히_r_03");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["사이클롭스_가만히_r"] = nodeAnimation;

        var list = [];
        var image = ManagerImage.getInstance().getImage("사이클롭스_이동_l_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_l_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_l_03");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_l_04");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_l_05");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["사이클롭스_이동_l"] = nodeAnimation;

        var list = [];
        var image = ManagerImage.getInstance().getImage("사이클롭스_이동_r_01");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_r_02");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_r_03");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_r_04");
        list.push(image);
        image = ManagerImage.getInstance().getImage("사이클롭스_이동_r_05");
        list.push(image);
        var nodeAnimation = new NodeAnimation(list);
        this.animationList["사이클롭스_이동_r"] = nodeAnimation;

        
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