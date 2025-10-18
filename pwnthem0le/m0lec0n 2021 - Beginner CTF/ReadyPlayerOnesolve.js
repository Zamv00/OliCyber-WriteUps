computermovement = function() { };

PADDLE_HEIGHT2 = (10/600)*screenH;   
PADDLE_HEIGHT1 = (240/600)*screenH;  
paddle2Y = (250/600)*screenH;

var _easyWinInterval = setInterval(() => {
  if (typeof ballY === "number" && typeof PADDLE_HEIGHT1 === "number") {
    var target = ballY - (PADDLE_HEIGHT1/2);
    target = Math.max(0, Math.min(screenH - PADDLE_HEIGHT1, target));
    paddle1Y = target;
  }
}, 20);


welcome = false;
showingWinScreen = false;

(function pollFlag(n=0){
  if (typeof result !== "undefined" && result) {
    console.log("Flag:", result);
    return;
  }
  if (n > 100) return; 
  setTimeout(()=>pollFlag(n+1),100);
})();

// giochi normalmente
//ptm{1_l1k3d_w0nd3rw4ll}
