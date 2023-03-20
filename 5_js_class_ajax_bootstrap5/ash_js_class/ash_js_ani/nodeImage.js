
import { ManagerGame } from "./managerGame.js";

export class NodeImage {
    constructor(x , y , w , h , imagePath){  
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.image = new Image();
        this.image.src = imagePath;
    }

    draw(x , y){
        this.x = x;
        this.y = y;
        ManagerGame.getInstance().ctx.drawImage(this.image , this.x , this.y , this.w , this.h);
    }
}