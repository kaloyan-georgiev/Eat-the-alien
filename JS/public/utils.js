function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

function randomChoice(array) {
    return array[randomInt(0, array.length)];
}
function removeDir(direction) {
    switch(direction) {
        case "up":
            return ["down", "right", "left"];
        case "down":
            return ["up", "right", "left"];
        case "right":
            return ["down", "up", "left"];
        case "left":
            return ["down", "right", "up"];
    }

}
class Timer {
    constructor(CPS) {
        this.CPS = CPS
        this.ticks = 0;
        this.seconds = 0;
    }
    tick() {
        this.ticks++;
        if(this.ticks == this.CPS) {
            this.seconds++;
            this.ticks = 0;
        }
    }
    reset() {
        this.ticks = 0;
        this.seconds = 0;
    }
}
var directions = ["down", "right", "up", "left"];
export {randomInt, randomChoice, removeDir, Timer, directions}