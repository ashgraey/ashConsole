
import { ManagerImage } from "./managerImage.js";
import { ManagerButton } from "./managerButton.js";
import { SceneTitle } from "./sceneTitle.js";
import { SceneLobby } from "./sceneLobby.js";
import { SceneSelect } from "./sceneSelect.js";
import { SceneStage } from "./sceneStage.js";
import { StageCastle } from "./stageCastle.js";
import { StageBoss } from "./stageBoss.js";
import { ManagerKey } from "./managerKey.js";


export class ManagerGame{
    static instance = new ManagerGame()
    static getInstance(){
        return this.instance;
    }

    start(ctx){
        this.ctx = ctx;
        ManagerKey.getInstance().start();
        ManagerImage.getInstance().start();
        ManagerButton.getInstance().start();
        
        this.sceneList =  {};
        this.setScene();

        this.curScene = null;
        this.curSceneName = "";

        this.stageList= {};
        this.setStage();
        this.stageLevel = 1;
        this.curStageName = "stageCastle";
           
        this.changeScene("title");
    }

    update(){
        if(this.curScene != null){
            this.curScene.update();
           
        }
    }
    draw(){
        if(this.curScene != null){
            this.curScene.draw();
           
        }   
    }

    
    changeScene(sceneName){
        if(this.curSceneName == sceneName){
            return;
        }
        this.curScene = this.sceneList[sceneName];        
    
        if(this.curScene != null){
            this.curSceneName = sceneName;
            this.curScene.start();
        }
    }

    getCurStage(){
        return this.stageList[this.curStageName];
    }

    setScene(){
        this.sceneList["title"] = new SceneTitle();
        this.sceneList["lobby"] = new SceneLobby();
        this.sceneList["select"] = new SceneSelect();
        this.sceneList["stage"] = new SceneStage();
    }

    setStage(){
        this.stageList["stageCastle"] = new StageCastle();
        this.stageList["stageBoss"] = new StageBoss() ; // 아직안만듬
       
    }
}