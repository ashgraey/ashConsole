import { ManagerGame } from "./managerGame.js";

export class SceneStage{

    start(){  
        
        this.curStage = ManagerGame.getInstance().getCurStage();
        this.curStage.start();
    }
   
    update(){
        this.curStage.update();
    }

    draw(){
        this.curStage.draw();
    }

    
}