import { ManagerGame } from "./managerGame.js";
import { ManagerImage } from "./managerImage.js";
import { ManagerButton } from "./managerButton.js";

export class SceneTitle{
    start(){
        
        document.addEventListener("click", this.mouseClickEvent , true);
    }
    update(){
      
    }
    draw(){
        ManagerImage.getInstance().drawImage("타이틀_배경화면" , 0, 0);   
        ManagerImage.getInstance().drawImage("타이틀_제목" , 400, 30); 
        ManagerButton.getInstance().drawButton("타이틀_버튼_게임시작_on" , 540, 630);   
    }

    mouseClickEvent = (event) => {    
        if(ManagerGame.getInstance().curSceneName != "title"){
            return;
        }     
        var x = event.pageX;
        var y = event.pageY;
        
        if(ManagerButton.getInstance().getButtonClick("타이틀_버튼_게임시작_on" , x , y)){
            ManagerGame.getInstance().changeScene("lobby");
            event.stopImmediatePropagation();
        } 
    }
    
}