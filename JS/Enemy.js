import Entity from "./Entity.js"
import {randomInt, randomChoice, removeDir, directions} from "./utils.js"
import {enemyArt, enemyImmature} from "./Artwork.js"
class Enemy extends Entity {
    constructor(speed, isMature, pos_max_w, pos_max_h, FPS) {
        super(10, 10, 64, 64, enemyArt, speed, 1)
        this.isMature = isMature;
        this.x = randomInt(0, pos_max_w - this.width);
        this.y = randomInt(0, pos_max_h - this.height);
        this.moveSc = 0;
        this.lifetime = 0;
        this.dir = randomChoice(directions);
        this.FPS = FPS;
        // 0-up, 1-down, 2 - right, 3 -left
        this.hitbox = [this.x, this.y, this.width, this.height];
    }
    randomMove() {
        if(this.dir == "up") {
            this.y -= this.speed;
        }
        if(this.dir == "down") {
            this.y += this.speed;
        }
        if(this.dir == "right") {
            this.x += this.speed;
        }
        if(this.dir == "left") {
            this.x -= this.speed;
        }
        this.moveSc += randomInt(1, 9);
        if(this.moveSc >= 128) {
            this.dir = randomChoice(removeDir(this.dir));
            this.moveSc = 0;
        }
    }
    collisionCheck(other) {
        if(this.isMature) {
            return super.collisionCheck(other);
        }
        else {
            return false;
        }
    }
    draw(context, background) {
        if(this.isMature) {
            this.randomMove();
            this.borderCheck(background);
            context.drawImage(this.art, this.x, this.y);
            this.hitbox = [this.x + 10, this.y, this.width - 20, this.height];
            //context.strokeRect(this.hitbox[0], this.hitbox[1], this.hitbox[2], this.hitbox[3]);
        }
        else {
            this.lifetime++;
            context.drawImage(enemyImmature, this.x, this.y);
            //context.strokeRect(this.hitbox[0], this.hitbox[1], this.hitbox[2], this.hitbox[3]);
            if(this.lifetime == 2 * this.FPS) {
                this.isMature = true;
            }
        }
    }
}

export default Enemy;