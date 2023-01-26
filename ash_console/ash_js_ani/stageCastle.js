import { ManagerImage } from "./managerImage.js";
import { UnitPlayer } from "./unitPlayer.js";
import { UnitCyclops } from "./unitCyclops.js";
export class StageCastle{
    start(){  
        this.cloudList = []
        this.setCloudList();
        this.player = new UnitPlayer();
        this.monsterList = [];

        var monster = new UnitCyclops();
        monster.setTarget(this.player);
        this.monsterList.push(monster);

        var monster = new UnitCyclops();
        monster.setTarget(this.player);
        this.monsterList.push(monster);
    }
   
    update(){
        this.cloudListMove();
        this.player.update();
        for(var i = 0; i < this.monsterList.length; i++){
            this.monsterList[i].update();
        }
    }

    draw(){
        ManagerImage.getInstance().drawImage("스테이지01_파란배경" , 0, 0);   
        for(var i = 0; i < this.cloudList.length; i++){
            var cloud = this.cloudList[i];
            ManagerImage.getInstance().drawImage(cloud.name , cloud.x, cloud.y);   
        }
        ManagerImage.getInstance().drawImage("스테이지01_왕실배경" , 0, 0);   

        let drawList = []

        for(var i = 0; i < this.monsterList.length; i++){
            drawList.push(this.monsterList[i]);
          //  this.monsterList[i].draw();
        }
        drawList.push(this.player);
       // this.player.draw();

       drawList.sort(function (a, b) {
            if (a.z > b.z) {
                return 1;
            }else{
                return -1;
            }
       });

       for(var i = 0; i < drawList.length; i++){
            drawList[i].draw();
       }
    }
        
    

    setCloudList(){
        for(var i = 0; i < 4; i++){
            var rnum = i + 1;
            var cloudName = "스테이지01_구름" + rnum;
            var rx = Math.random() * 3000 - 1500;
            var ry = Math.random() * 200 - 100;
            var speed = 1 / 3 + Math.random() * 1 / 2;
            var cloud = {"name" : cloudName , "x" : rx , "y" : ry , "speed" : speed};
            this.cloudList.push(cloud);
        }
    }

    cloudListMove(){
        for(var i = 0; i < this.cloudList.length; i++){
            this.cloudList[i].x -= this.cloudList[i].speed;
            if (this.cloudList[i].x < -1000){
                this.cloudList[i].x = 1400;
                this.cloudList[i].y = Math.random() * 200 - 100;
                this.cloudList[i].speed =  1 / 3 + Math.random() * 1 / 2;
            }
        }
    }
}