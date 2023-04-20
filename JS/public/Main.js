import {background, tentaclesArt, turboTentaclesArt, enemyArt, enemyImmature, baitArt_left, baitArt_right, baitArt, splashParticle_bait, splashParticle_player} from "./Artwork.js"
import Player from "./Player.js"
import Bait from "./Bait.js"
import Enemy from "./Enemy.js"
import {randomInt, randomChoice, Timer} from "./utils.js"
//background, tentaclesArt, turboTentaclesArt, enemyArt, enemyImmature, baitArt_left, baitArt_right, baitArt, splashParticle_bait, splashParticle_player
var canvas; 
var context;
var gamepad = 0;
window.addEventListener("gamepadconnected", (e) => {
    gamepad = navigator.getGamepads()[0];
    console.log(
        "Gamepad connected at index %d: %s. %d buttons, %d axes.",
        e.gamepad.index,
        e.gamepad.id,
        e.gamepad.buttons.length,
        e.gamepad.axes.length
    );
});

window.addEventListener("gamepaddisconnected", (e) => {
    gamepad = 0;
    console.log(
        "Gamepad disconnected from index %d: %s",
        e.gamepad.index,
        e.gamepad.id
    );
});

window.onload = function() {
    var score = 0;
    function main() {
        console.log("Hello World!");
        canvas = document.getElementById("gameCanvas");
        context = canvas.getContext("2d");
        context.strokeStyle = "#FF0000";
        var FPS = 60;      
        function Particle(art, x, y, time) {
            this.art = art;
            this.x = x;
            this.y = y;
            this.time = time * FPS;
            var self = this;
            this.draw = function() {
                if(self.time > 0) {
                    context.drawImage(self.art, self.x, self.y);
                    self.time--;
                }
            }
            
        }
    
        
        function trunctate(number, places) {
            return Math.round(number * (10 ** places)) / (10 ** places)
        }
        
        //Initializing variables
        var enemySpeed = 2.8;
        var enemySpeed_modifier = 0.4;
        var maxEnemies = 6;
        var baitSpeed = 2;
        var tentacles = new Player(0 ,0, 2.5);
        var bait = new Bait(baitSpeed, background.width, background.height);
        var enemies = [new Enemy(enemySpeed, false, canvas.width, canvas.height, FPS), new Enemy(enemySpeed, false, background.width, background.height, FPS)];
        var i;
        var effects = [];
        var summonTimer = new Timer(FPS);
        var gameTimer = new Timer(FPS);
        var endScreenTimer = new Timer(FPS);
        var afterGameTimer = new Timer(FPS);

        context.font = "normal normal 700 20px sans-serif"
        
        // Registering keystrokes
        onkeydown = onkeyup = function (e) {
            tentacles.keystrokes[e.code] = (e.type == "keydown");
            console.log(e.code);
        }



        function mainLoop() {
            context.drawImage(background, 0, 0);
            //Gamepad support
            if(gamepad != 0) {
                tentacles.keystrokes["Axe0"] = gamepad.axes[0];
                tentacles.keystrokes["Axe1"] = gamepad.axes[1];
                tentacles.keystrokes["Button7"] = gamepad.buttons[7].pressed;
                //console.log(tentacles.keystrokes);
            }
            // Drawing player
            if(tentacles.isAlive) {
                tentacles.draw(context, background)
            }
            else if(afterGameTimer.ticks == 0 && afterGameTimer.seconds == 0){
                effects.push(new Particle(splashParticle_player, tentacles.x, tentacles.y, 2))
                afterGameTimer.tick();
            }
            else {
                afterGameTimer.tick();
            }
            //Adding new enemies
            summonTimer.tick();
            if(summonTimer.seconds == 10 && enemies.length < maxEnemies) {
                enemySpeed -= enemySpeed_modifier;
                enemySpeed_modifier -= 0.1
                enemies.push(new Enemy(enemySpeed, false, background.width, background.height, FPS));
                summonTimer.reset();
            }
            else if(enemies.length >= maxEnemies && summonTimer.seconds == 1) {
                for(i = 0; i < maxEnemies; i++) {
                    enemies[i].speed += 0.01;
                }
                summonTimer.reset();
            }
            //Player - Bait Collision check
            if(tentacles.collisionCheck(bait) && tentacles.isAlive) {
                tentacles.scored();
                score += 1
                effects.push(new Particle(splashParticle_bait, bait.x, bait.y, 3));
                baitSpeed += 0.1;
                bait = new Bait(baitSpeed, background.width, background.height);
            }
            //Drawing bait

            bait.draw(context, background);
            //Drawing enemies and collision check
            for(i = 0; i < enemies.length; i++) {
                enemies[i].draw(context, background);
                if(tentacles.collisionCheck(enemies[i])) {
                    tentacles.hit();
                }
            }
            //Draw effects
            for(i = 0; i < effects.length; i++) {
                effects[i].draw();
                if(effects[i].time <= 0) {
                    effects.splice(i, 1);
                }
            }
            //Display time
            if(tentacles.isAlive) {
                gameTimer.tick();
            }
            context.fillStyle = "#FF0000";
            let timeText = "Your time is " + gameTimer.seconds + " seconds"
            context.fillText(timeText, canvas.width - context.measureText(timeText).width - 1, 21);
            context.fillText("Your score is " + score, 1, 21);
            //Display stamina
            context.fillStyle = "#00FF00";
            let staminaText = "Your Stamina is " + tentacles.stamina
            context.fillText(staminaText, canvas.width / 2 - context.measureText(staminaText).width / 2, 21);
            //End screen
            if(afterGameTimer.seconds >= 2) {
                context.fillStyle = "#05668D";
                context.fillRect(0, 0, canvas.width, canvas.height);
                context.fillStyle = "#FF0000";
                let timeText = "Your time was " + gameTimer.seconds + " seconds"
                context.fillText(timeText, canvas.width / 2 - context.measureText(timeText).width / 2, 200);
                let scoreText = "Your score was " + score
                context.fillText(scoreText, canvas.width / 2 - context.measureText(scoreText).width / 2, 240);
                context.fillStyle = "#00FF00";
                let netText = "Your net score is " + trunctate(score * 10 / gameTimer.seconds, 2)
                context.fillText(netText, canvas.width/2 - context.measureText(netText).width / 2, 280 );
                endScreenTimer.tick();
            }
            // Loop
            if(endScreenTimer.seconds < 2) {
                setTimeout(mainLoop, 1000 / FPS);
            }
            else {
                score = 0;
                main();
            }
        }
        mainLoop();
    }
    /*var playerName = prompt("Enter your name to keep your score on the site");
    if(playerName != null) {
        document.cookie = "playerName=" + playerName;
        document.cookie = "score=" + score;
    }*/
    main();
}