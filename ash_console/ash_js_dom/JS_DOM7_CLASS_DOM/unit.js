
export class Unit{
    constructor(a , b , c ){
        this.name = a;
        this.health = b;
        this.power = c;
    }

    attack(other){
        other.health -= this.power;
    }

    checkDead(){
        if(this.health <= 0){
            this.health = 0;
            return true;
        }
        return false;
    }
}