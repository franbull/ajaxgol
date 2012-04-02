var x=0;
console.log('imported ok');
function init() {
   console.log('in init');
   ctx = document.getElementById('canvas').getContext('2d');
   return setInterval(draw, 100);
   ctx.font = '20pt Arial';
}
function draw() {
    console.log('in draw');
    if ( x < 1000 ) {
        ctx.clearRect(0,0,400,400);
        ctx.strokeRect(0,0,400,400);
        for (var i = 0; i < 2; i++) {
            drawAGuy([10 * i , x]);
        }
        ctx.fillText(x, 380, 390);
        x += 1;
    }
}
function drawAGuy(coords){
    ctx.fillRect(coords[0], coords[1], 5, 5);   
}
