import Entity from "./Entity.js"
import {randomInt, randomChoice, removeDir, directions} from "./utils.js"
import {baitArt, baitArt_left, baitArt_right} from "./Artwork.js"
class Bait extends Entity {
    constructor(speed, pos_max_w, pos_max_h) {
        super(
            0,
            0,
            64,
            64,
            baitArt,
            speed,
            1
        )
        this.x = randomInt(0, pos_max_w - this.width);
        this.y = randomInt(0, pos_max_h - this.height);
        this.dir = randomChoice(directions);
        this.moveSc = 0;
        this.hitbox = [this.x, this.y, this.width, this.height];
    }
    randomMove() {
        this.art = baitArt;
        if(this.dir == "up") {
            this.y -= this.speed;
        }
        if(this.dir == "down") {
            this.y += this.speed;
        }
        if(this.dir == "right") {
            this.art = baitArt_right;
            this.x += this.speed;
        }
        if(this.dir == "left") {
            this.art = baitArt_left;
            this.x -= this.speed;
        }
        this.moveSc += randomInt(1, 3);
        if(this.moveSc >= 16) {
            this.dir = randomChoice(removeDir(this.dir));
            this.moveSc = 0;
        }
    }
    draw(context, background) {
        super.draw(context, background)
        this.randomMove();
        this.hitbox = [this.x + 5, this.y, this.width - 5, this.height];
        //context.strokeRect(this.hitbox[0], this.hitbox[1], this.hitbox[2], this.hitbox[3]);
    }
}

export default Bait;