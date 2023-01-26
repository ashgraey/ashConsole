import { NodeAnimation } from "./nodeAnimation.js";
import { ManagerImage } from "./managerImage.js";

export class SkillSword{
    constructor(x , y , frame , type , direction){    
        this.x = x;
        this.y = y;
        this.frame = frame;
        this.type = type;    
        this.direction = direction;     
        this.nodeAnimation = this.getAnimation();
        this.once = false;
    }
    update(){
        
    }
    draw(){
        if(this.type == "loop"){
            this.nodeAnimation.playLoop(this.x , this.y , this.frame);  
        }else{
            this.once = this.nodeAnimation.playOnce(this.x , this.y , this.frame);  
        }
    }

    getAnimation(){
        if(this.direction == "left"){
            var list = [];
            var image = ManagerImage.getInstance().getImage("스킬_검_l_01");
            list.push(image);
            image = ManagerImage.getInstance().getImage("스킬_검_l_02");
            list.push(image);
            image = ManagerImage.getInstance().getImage("스킬_검_l_03");
            list.push(image);
            var nodeAnimation = new NodeAnimation(list);
            return nodeAnimation;
        }else if(this.direction == "right"){
            var list = [];
            var image = ManagerImage.getInstance().getImage("스킬_검_r_01");
            list.push(image);
            image = ManagerImage.getInstance().getImage("스킬_검_r_02");
            list.push(image);
            image = ManagerImage.getInstance().getImage("스킬_검_r_03");
            list.push(image);
            var nodeAnimation = new NodeAnimation(list);
            return nodeAnimation;
        }
    }
}