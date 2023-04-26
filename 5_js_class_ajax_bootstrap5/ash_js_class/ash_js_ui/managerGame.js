import { ManagerKey } from "./managerKey.js";
import { ManagerImage } from "./managerImage.js";
import { ManagerButton } from "./managerButton.js";
import { ManagerScene } from "./managerScene.js";
import { ManagerPlayer } from "./managerPlayer.js";
import { ManagerStage } from "./managerStage.js";


export class ManagerGame{
    static instance = new ManagerGame()
    static getInstance(){
        return this.instance;
    }

    start(ctx){
        this.ctx = ctx;
        ManagerKey.getInstance().start();
        ManagerImage.getInstance().start(); // imageDB setting
        ManagerButton.getInstance().start();
        ManagerScene.getInstance().start(); // sceneDB setting
        ManagerStage.getInstance().start();
        ManagerPlayer.getInstance().start();
        ManagerScene.getInstance().changeScene("title"); // curScene이 title인지 아닌지 검사, title이면 return 계속 타이틀 화면을 유지
    }

    update(){
        ManagerScene.getInstance().update();
    }
    
    draw(){
        ManagerScene.getInstance().draw();
    }

}