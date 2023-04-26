export class Unit {
  constructor(a, b, c) {
    this.name = a;
    this.health = b;
    this.power = c;
  }

  // 들어오는 인자의 값에 따라 this가 다른 의미로 씌어진다.
  // other == hero => this == monster
  // orther == monser => this = hero
  attack(other) {
    other.health -= this.power;
  }

  skill1Attack(monster) {
    monster.health -= this.power * 1.5;
  }

  skill2Attack(monster) {
    monster.health -= this.power * 2;
  }

  // this가 객체 그 자체
  checkDead() {
    if (this.health <= 0) {
      this.health = 0;
      return true;
    }
    return false;
  }
}
