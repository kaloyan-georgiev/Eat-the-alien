import { tentaclesArt, turboTentaclesArt } from "./Artwork.js";
class Entity {
    constructor(x, y, width, height, art, speed, turboModifier) {
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.isMoving = false;
        this.isAlive = true;
        this.art = art;
        this.width = width;
        this.height = height;
        this.hitbox = [this.x, this.y, this.width, this.height];
        this.turboModifier = turboModifier

    }
    borderCheck(background) {
        if(this.x > background.width - this.width) {
            this.x -= this.speed * this.turboModifier;
        }
        else if(this.x < 0) {
            this.x += this.speed * this.turboModifier;
        }
        if(this.y > background.height - this.height) {
            this.y -= this.speed * this.turboModifier;
        }
        else if(this.y < 0) {
            this.y += this.speed * this.turboModifier;
        }					
    }
    collisionCheck(object2) {
        if(((this.hitbox[0] > object2.hitbox[0]) && (this.hitbox[0] < object2.hitbox[0] + object2.hitbox[2])) || ((this.hitbox[0] < object2.hitbox[0]) && (this.hitbox[0] + this.hitbox[2] > object2.hitbox[0]))) {
            if((this.hitbox[1] > object2.hitbox[1] && this.hitbox[1] < object2.hitbox[1] + object2.hitbox[3]) || (this.hitbox[1] < object2.hitbox[1] && this.hitbox[1] + this.hitbox[3] > object2.hitbox[1])) {
                return true;
            }
        }
        return false;
    }
    draw(context, background) {
        this.borderCheck(background);
        context.drawImage(this.art, this.x, this.y);
        this.hitbox = [this.x + 10, this.y + 5, this.width - 10, this.height - 5];
        //context.strokeRect(this.hitbox[0], this.hitbox[1], this.hitbox[2], this.hitbox[3]);
    }
}

export default Entity;