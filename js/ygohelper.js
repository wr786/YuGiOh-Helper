// 造成伤害
function doDamage() {
    var dmg = parseInt($("#dmg").val());
    if(dmg < 0) {   // 对P1造成伤害
        var lpMax = parseInt($("#p1fm").text());
        var lpCur = parseInt($("#p1fz").text());
        lpCur += dmg;
        lpCur = Math.max(lpCur, 0);
        $("#player1").progress({percent: 100 * lpCur / lpMax});
        $("#p1fz").text(lpCur);
    } else if(dmg > 0) {
        var lpMax = parseInt($("#p2fm").text());
        var lpCur = parseInt($("#p2fz").text());
        lpCur -= dmg;
        lpCur = Math.max(lpCur, 0);
        $("#player2").progress({percent: 100 * lpCur / lpMax});
        $("#p2fz").text(lpCur);
    }
}

// 重设LP
function recoverLP() {
    var lpMax = parseInt($("#lpMAX").val());
    if(lpMax > 0) {
        $("#p1fm").text(lpMax);
        $("#p1fz").text(lpMax);
        $("#p2fm").text(lpMax);
        $("#p2fz").text(lpMax);
        $("#player1").progress({percent: 100});
        $("#player2").progress({percent: 100});
    }
}

// 骰1d6
function rollDice() {
    var diceNum = Math.floor((Math.random()*6)+1);
    $("#diceNotice").removeClass("hidden");
    $("#diceNum").text(diceNum);
}

// 投硬币
function tollCoin() {
    var coinSide = Math.floor((Math.random()*100)+1) > 50? "正面": "反面";
    $("#coinNotice").removeClass("hidden");
    $("#coinSide").text(coinSide);
}