

import { NodeImage } from "./nodeImage.js";

export class ManagerImage {
    static instance = new ManagerImage()
    static getInstance(){
        return this.instance;
    }

    start(){
       
        this.imageList = {};        
        this.setImageList();
    }


    setImageList(){
        this.setImage("타이틀_배경화면" , 0, 0, 1280, 720 , "img/타이틀/타이틀_배경화면.png");
        this.setImage("타이틀_제목" , 0, 0, 530, 239 , "img/타이틀/타이틀_제목.png");
        this.setImage("타이틀_버튼_게임시작_on" , 0, 0, 200, 70 , "img/타이틀/타이틀_버튼_게임시작_on.png");
        this.setImage("타이틀_버튼_게임시작_off" , 0, 0, 200, 70 , "img/타이틀/타이틀_버튼_게임시작_off.png");


        this.setImage("로비_배경화면" , 0, 0, 1280, 720 , "img/로비/로비_배경화면.jpg");

        this.setImage("로비_버튼_start_on" , 0, 0, 400, 140 , "img/로비/로비_버튼_start_on.png");
        this.setImage("로비_버튼_start_off" , 0, 0, 400, 140 , "img/로비/로비_버튼_start_off.png");
        this.setImage("로비_버튼_공격증가_on" , 0, 0, 130, 130 , "img/로비/로비_버튼_공격증가_on.png");
        this.setImage("로비_버튼_공격증가_off" , 0, 0, 130, 130 , "img/로비/로비_버튼_공격증가_off.png");
        this.setImage("로비_버튼_체력증가_on" , 0, 0, 130, 130 , "img/로비/로비_버튼_체력증가_on.png");
        this.setImage("로비_버튼_체력증가_off" , 0, 0, 130, 130 , "img/로비/로비_버튼_체력증가_off.png");
        this.setImage("로비_버튼_이속증가_on" , 0, 0, 130, 130 , "img/로비/로비_버튼_이속증가_on.png");
        this.setImage("로비_버튼_이속증가_off" , 0, 0, 130, 130 , "img/로비/로비_버튼_이속증가_off.png");
        
        this.setImage("로비_버튼_뒤로가기_on" , 0, 0, 40, 40 , "img/로비/로비_버튼_뒤로가기_on.png");
        this.setImage("로비_버튼_뒤로가기_off" , 0, 0, 40, 40 , "img/로비/로비_버튼_뒤로가기_off.png");
        

        this.setImage("셀렉트_배경화면" , 0, 0, 1280, 720 , "img/셀렉트/셀렉트_배경화면.png");
        this.setImage("셀렉트_버튼_뒤로가기_on" , 0, 0, 40, 40 , "img/셀렉트/셀렉트_버튼_뒤로가기_on.png");
        this.setImage("셀렉트_버튼_뒤로가기_off" , 0, 0, 40, 40 , "img/셀렉트/셀렉트_버튼_뒤로가기_off.png");
        this.setImage("셀렉트_버튼_01_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_01_on.png");
        this.setImage("셀렉트_버튼_01_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_01_off.png");
        this.setImage("셀렉트_버튼_02_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_02_on.png");
        this.setImage("셀렉트_버튼_02_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_02_off.png");
        this.setImage("셀렉트_버튼_03_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_03_on.png");
        this.setImage("셀렉트_버튼_03_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_03_off.png");
        this.setImage("셀렉트_버튼_04_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_04_on.png");
        this.setImage("셀렉트_버튼_04_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_04_off.png");
        this.setImage("셀렉트_버튼_05_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_05_on.png");
        this.setImage("셀렉트_버튼_05_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_05_off.png");
        this.setImage("셀렉트_버튼_06_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_06_on.png");
        this.setImage("셀렉트_버튼_06_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_06_off.png");
        this.setImage("셀렉트_버튼_07_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_07_on.png");
        this.setImage("셀렉트_버튼_07_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_07_off.png");
        this.setImage("셀렉트_버튼_08_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_08_on.png");
        this.setImage("셀렉트_버튼_08_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_08_off.png");
        this.setImage("셀렉트_버튼_09_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_09_on.png");
        this.setImage("셀렉트_버튼_09_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_09_off.png");      
        this.setImage("셀렉트_버튼_10_on" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_10_on.png");
        this.setImage("셀렉트_버튼_10_off" , 0, 0, 100, 100 , "img/셀렉트/셀렉트_버튼_10_off.png");

 
        this.setImage("스테이지01_파란배경" , 0, 0, 1280, 720 , "img/스테이지01/스테이지01_파란배경.jpg");
        this.setImage("스테이지01_왕실배경" , 0, 0, 1280, 720 , "img/스테이지01/스테이지01_왕실배경.png");
        this.setImage("스테이지01_구름1" , 0, 0, 250, 110 , "img/스테이지01/스테이지01_구름1.png");
        this.setImage("스테이지01_구름2" , 0, 0, 350, 150 , "img/스테이지01/스테이지01_구름2.png");
        this.setImage("스테이지01_구름3" , 0, 0, 200, 100 , "img/스테이지01/스테이지01_구름3.png");
        this.setImage("스테이지01_구름4" , 0, 0, 380, 200 , "img/스테이지01/스테이지01_구름4.png");

        this.setImage("player_idle_r_01" , 0, 0, 350, 420 , "img/플레이어/player_idle_r_01.png");
        this.setImage("player_idle_r_02" , 0, 0, 350, 420 , "img/플레이어/player_idle_r_02.png");
        this.setImage("player_idle_r_03" , 0, 0, 350, 420 , "img/플레이어/player_idle_r_03.png");

        this.setImage("player_work_r_01" , 0, 0, 350, 420 , "img/플레이어/player_work_r_01.png");
        this.setImage("player_work_r_02" , 0, 0, 350, 420 , "img/플레이어/player_work_r_02.png");
        this.setImage("player_work_r_03" , 0, 0, 350, 420 , "img/플레이어/player_work_r_03.png");
        this.setImage("player_work_r_04" , 0, 0, 350, 420 , "img/플레이어/player_work_r_04.png");

        this.setImage("player_idle_l_01" , 0, 0, 350, 420 , "img/플레이어/player_idle_l_01.png");
        this.setImage("player_idle_l_02" , 0, 0, 350, 420 , "img/플레이어/player_idle_l_02.png");
        this.setImage("player_idle_l_03" , 0, 0, 350, 420 , "img/플레이어/player_idle_l_03.png");

        this.setImage("player_work_l_01" , 0, 0, 350, 420 , "img/플레이어/player_work_l_01.png");
        this.setImage("player_work_l_02" , 0, 0, 350, 420 , "img/플레이어/player_work_l_02.png");
        this.setImage("player_work_l_03" , 0, 0, 350, 420 , "img/플레이어/player_work_l_03.png");
        this.setImage("player_work_l_04" , 0, 0, 350, 420 , "img/플레이어/player_work_l_04.png");

        this.setImage("스킬_검_r_01" , 0, 0, 300, 300 , "img/스킬/스킬_검_r_01.png");
        this.setImage("스킬_검_r_02" , 0, 0, 300, 300 , "img/스킬/스킬_검_r_02.png");
        this.setImage("스킬_검_r_03" , 0, 0, 300, 300 , "img/스킬/스킬_검_r_03.png");

        this.setImage("스킬_검_l_01" , 0, 0, 300, 300 , "img/스킬/스킬_검_l_01.png");
        this.setImage("스킬_검_l_02" , 0, 0, 300, 300 , "img/스킬/스킬_검_l_02.png");
        this.setImage("스킬_검_l_03" , 0, 0, 300, 300 , "img/스킬/스킬_검_l_03.png");

    
        this.setImage("사이클롭스_가만히_l_01" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_l_01.png");
        this.setImage("사이클롭스_가만히_l_02" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_l_02.png");
        this.setImage("사이클롭스_가만히_l_03" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_l_03.png");

        this.setImage("사이클롭스_가만히_r_01" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_r_01.png");
        this.setImage("사이클롭스_가만히_r_02" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_r_02.png");
        this.setImage("사이클롭스_가만히_r_03" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_가만히_r_03.png");

        this.setImage("사이클롭스_이동_l_01" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_l_01.png");
        this.setImage("사이클롭스_이동_l_02" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_l_02.png");
        this.setImage("사이클롭스_이동_l_03" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_l_03.png");
        this.setImage("사이클롭스_이동_l_04" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_l_04.png");
        this.setImage("사이클롭스_이동_l_05" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_l_05.png");

        this.setImage("사이클롭스_이동_r_01" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_r_01.png");
        this.setImage("사이클롭스_이동_r_02" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_r_02.png");
        this.setImage("사이클롭스_이동_r_03" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_r_03.png");
        this.setImage("사이클롭스_이동_r_04" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_r_04.png");
        this.setImage("사이클롭스_이동_r_05" , 0, 0, 270, 320 , "img/사이클롭스/사이클롭스_이동_r_05.png");

    }

    setImage(imageName , x , y , w , h , imagePath){
        var nodeImage = new NodeImage(x , y , w , h , imagePath);
        this.imageList[imageName] = nodeImage;
    }

    getImage(imageName){
        return this.imageList[imageName];
    }

    drawImage(imageName , x , y){
        var nodeImage = this.imageList[imageName];     
        if(nodeImage == null){
            return;
        }  
        nodeImage.draw(x , y);

    }

    // drawText(posx , posy , px , color , text){
    //     //    var font = "serif";
    //     ManagerGame.getInstance().ctx.fillStyle = color;
    //     ManagerGame.getInstance().ctx.font = (px + "px 맑은고딕");
    //     ManagerGame.getInstance().ctx.fillText(text , posx, posy);
    // }

}