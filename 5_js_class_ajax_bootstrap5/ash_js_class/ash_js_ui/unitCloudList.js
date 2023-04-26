import { ManagerImage } from "./managerImage.js";
// var bg1 = { x: 0, y: 500, w: 400, h: 500, img: new Image(), speed: 0.5 };
// bg1["img"].src = "image/stage_01.png";
// var bg2 = { x: 0, y: 0, w: 400, h: 500, img: new Image(), speed: 0.5 };
// bg2["img"].src = "image/stage_01.png";
// var bg3 = { x: 0, y: -500, w: 400, h: 500, img: new Image(), speed: 0.5 };
// bg3["img"].src = "image/stage_01.png";

export class UnitCloudList{
    constructor(){  
        this.cloudList = [];
        for(var i = 0; i < 4; i++){
            var rnum = i + 1;
            // 문자 + 숫자 = 문자 + 문자 = 스테이지01_구름1
            var cloudName = "스테이지01_구름" + rnum;
            var rx = Math.random() * 3000 - 1500;
            var ry = Math.random() * 200 - 100;
            var speed = 1 / 3 + Math.random() * 1 / 2;
            var cloud = {"name" : cloudName , "x" : rx , "y" : ry , "speed" : speed};
            this.cloudList.push(cloud);
        }
    }
   
    update(){
        for(var i = 0; i < this.cloudList.length; i++){
            this.cloudList[i].x -= this.cloudList[i].speed;
            if (this.cloudList[i].x < -1000){
                this.cloudList[i].x = 1400;
                this.cloudList[i].y = Math.random() * 200 - 100;
                this.cloudList[i].speed =  1 / 3 + Math.random() * 1 / 2;
            }
        }
       
    }

    draw(){
        ManagerImage.getInstance().managerImageDraw("스테이지01_파란배경" , 0, 0);   
        for(var i = 0; i < this.cloudList.length; i++){
            var cloud = this.cloudList[i];
            ManagerImage.getInstance().managerImageDraw(cloud.name , cloud.x, cloud.y);   
        }
        ManagerImage.getInstance().managerImageDraw("스테이지01_왕실배경" , 0, 0);   
    }
   
}