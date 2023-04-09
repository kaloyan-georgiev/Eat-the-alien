//loading art
var background = new Image(960, 540);
background.src = "small_art\\background3.png"

var tentaclesArt = new Image(64, 64);
tentaclesArt.src = "small_art\\alien2_1.png";
var turboTentaclesArt = new Image(64, 64);
turboTentaclesArt.src = "small_art\\alien2_3.png"

var enemyArt = new Image(64, 64);
enemyArt.src = "small_art\\alien3.png";
var enemyImmature = new Image(64, 64);
enemyImmature.src = "small_art\\alien3_1.png";

var baitArt_left = new Image(64, 64);
baitArt_left.src = "small_art\\alien5.png"
var baitArt_right = new Image(64, 64);
baitArt_right.src = "small_art\\alien5_1.png"
var baitArt = new Image(64, 64);
baitArt.src = "small_art\\alien5_2.png"

var splashParticle_bait = new Image(80, 80);
splashParticle_bait.src = "small_art\\bait_eat1.png"
var splashParticle_player = new Image(96, 96);
splashParticle_player.src = "small_art\\tentacles_die.png"

export {background, tentaclesArt, turboTentaclesArt, enemyArt, enemyImmature, baitArt_left, baitArt_right, baitArt, splashParticle_bait, splashParticle_player}