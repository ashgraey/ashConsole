

export class ManagerKey {
    static instance = new ManagerKey();
    static getInstance(){
        return this.instance;
    }

    start(){
        
        this.keyStayList = {"KeyD" : false , "KeyA" : false , "KeyW" : false , "KeyS" : false };
        this.keyOnceList = {"KeyJ" : "ready" , "KeyK" : "ready"};

        document.addEventListener("keydown", (e) => {
            this.keyStayList[e.code] = true;

            if(this.keyOnceList[e.code] == "ready"){
                this.keyOnceList[e.code] = "push";
            }

        }, false);

        document.addEventListener("keyup", (e) => {
            this.keyStayList[e.code] = false;

            if(this.keyOnceList[e.code] == "wait"){
                this.keyOnceList[e.code] = "ready";
            }
        }, false);

    }

    // key 값 반환 메소드
    getKeyStay(key){
        return this.keyStayList[key];
      
    }

    // 공격 버튼, keyUp 상태에선 공격이 안 나가도록
    // unitPlayer에 연결 시켜야함
    getKeyOnce(key){
        if(this.keyOnceList[key] == "push"){
            this.keyOnceList[key]  = "wait";
            return true;
        }else{
            return false;
        }
        
    }
  
}