import { tentaclesArt, turboTentaclesArt } from "./Artwork.js";
import Entity from "./Entity.js"
class Player extends Entity {
    constructor(x, y, speed) {
        super(x, y, 64, 64, tentaclesArt, speed, 1)
        this.keystrokes = {}
        this.stamina = 60;
    }
    movementCheck() {
        this.art = tentaclesArt;
        this.turboModifier = 1;
        if((this.keystrokes["ShiftLeft"] || this.keystrokes["Button7"]) && this.stamina > 0) {
            this.art = turboTentaclesArt;
            this.turboModifier = 3;
        }
        if(this.keystrokes["KeyA"] || this.keystrokes["ArrowLeft"] || this.keystrokes["Axe0"] == -1) {
            this.x -= this.speed * this.turboModifier;
            if((this.keystrokes["ShiftLeft"] || this.keystrokes["Button7"]) && this.stamina > 0) {
                this.stamina--;
            }
        }
        if(this.keystrokes["KeyD"] || this.keystrokes["ArrowRight"] || this.keystrokes["Axe0"] == 1) {
            this.x += this.speed * this.turboModifier;
            if((this.keystrokes["ShiftLeft"] || this.keystrokes["Button7"]) && this.stamina > 0) {
                this.stamina--;
            }								
        }
        if(this.keystrokes["KeyW"] || this.keystrokes["ArrowUp"] || this.keystrokes["Axe1"] == -1) {
            this.y -= this.speed * this.turboModifier;
            if((this.keystrokes["ShiftLeft"] || this.keystrokes["Button7"]) && this.stamina > 0) {
                this.stamina--;
            }								
        }
        if(this.keystrokes["KeyS"] || this.keystrokes["ArrowDown"] || this.keystrokes["Axe1"] == 1) {
            this.y += this.speed * this.turboModifier;
            if((this.keystrokes["ShiftLeft"] || this.keystrokes["Button7"]) && this.stamina > 0) {
                this.stamina--;
            }								
        }
    }
    hit() {
        this.isAlive = false;
        console.log("hithit");
    }
    scored() {
        this.stamina += 60;
    }
    draw(context, background) {
        super.draw(context, background);
        this.movementCheck();
        this.hitbox = [this.x + 10, this.y + 5, this.width - 10, this.height - 5];
        //context.strokeRect(this.hitbox[0], this.hitbox[1], this.hitbox[2], this.hitbox[3]);
    }
}

export default Player;