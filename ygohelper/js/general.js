// 窄屏下旋转背景图片
function resizeBackground() {
    var windowWidth = $(window).width();
    var windowHeight = $(window).height();
    if(windowWidth < windowHeight){
        $("body").css("background-image", 'url("../images/bg_t.jpg")');
    } else {
        $("body").css("background-image", 'url("../images/bg.jpg")');
    }
}