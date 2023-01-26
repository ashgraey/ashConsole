
export class NodeAnimation {
    constructor(imageList){
        this.imageList = imageList
        this.index = 0;
        this.frameTime = 0;
        this.size = imageList.length;
    }

    playLoop(x , y , frameDelay ){
        this.frameTime += 1;  
        if(this.frameTime >= frameDelay){
            this.frameTime = 0;
            this.index += 1;
            if(this.index >= this.size){
                this.index = 0;
            }        
        }
        this.draw(x, y);
    }
    playOnce(x , y , frameDelay){
        this.frameTime += 1; 
        if(this.frameTime >= frameDelay){
            this.frameTime = 0;        
            this.index += 1;     
        }
        if(this.index < this.size){   
            this.draw(x, y);           
            return false;     
        }else{       
            return true;
        }
        
    }
    draw(x , y){
        var nodeImage = this.imageList[this.index];     
        if(nodeImage == null){
            return;
        }  
        nodeImage.draw(x , y);  
    }
  
}