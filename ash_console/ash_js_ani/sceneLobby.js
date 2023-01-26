import { ManagerButton } from "./managerButton.js";
import { ManagerGame } from "./managerGame.js";
import { ManagerImage } from "./managerImage.js";

export class SceneLobby{

    start(){       
        document.addEventListener("click", this.mouseClickEvent , true);
        
    }
    update(){}

    draw(){
        ManagerImage.getInstance().drawImage("로비_배경화면" , 0, 0); 
        ManagerButton.getInstance().drawButton("로비_버튼_start_on" , 820, 480); 
        ManagerButton.getInstance().drawButton("로비_버튼_공격증가_on" , 548, 178);
        ManagerButton.getInstance().drawButton("로비_버튼_체력증가_on" , 548, 350);
        ManagerButton.getInstance().drawButton("로비_버튼_이속증가_on" , 548, 522);
        ManagerButton.getInstance().drawButton("로비_버튼_뒤로가기_on" , 1180, 30);
    }

    mouseClickEvent = (event) => {    
        if(ManagerGame.getInstance().curSceneName != "lobby"){
            return;
        }   
        var x = event.pageX;
        var y = event.pageY;
        if(ManagerButton.getInstance().getButtonClick("로비_버튼_start_on" , x , y)){
            ManagerGame.getInstance().changeScene("select");
            event.stopImmediatePropagation();

        } 
        else if(ManagerButton.getInstance().getButtonClick("로비_버튼_뒤로가기_on" , x , y)){
            ManagerGame.getInstance().changeScene("title");
            event.stopImmediatePropagation();
        }
    }
}