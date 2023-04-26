import { ManagerGame } from "./managerGame.js";
import { ManagerImage } from "./managerImage.js";
export class NodeButton {
    constructor(normalImage , overImage){  
        this.normalImage = ManagerImage.getInstance().getImage(normalImage);
        this.overImage =  ManagerImage.getInstance().getImage(overImage);

        this.path = new Path2D(); // 충돌체크용
      
        document.addEventListener("mousemove", this.mouseOverEvent , true);
      
        this.mouseOver = false;
    }

    draw(x , y){
        if (this.mouseOver){
            this.overImage.draw(x , y);
        }else{
            this.normalImage.draw(x , y);
        }

        this.drawBox();
       
    }
    drawBox(){
        this.path.rect(this.normalImage.x, this.normalImage.y, this.normalImage.w, this.normalImage.h);
        ManagerGame.getInstance().ctx.stroke(this.path);
    }

    getMouseCollision(x , y){
        return ManagerGame.getInstance().ctx.isPointInPath(this.path , x , y);;
    }

    mouseOverEvent = (event) => {   
        var x = event.pageX;
        var y = event.pageY;
        this.mouseOver = this.getMouseCollision(x , y);
    }
}