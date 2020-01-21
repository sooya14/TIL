
// 제이쿼리 
// 자바스크립트 코드를 실행하기 전에 브라우저가 html 을 전부 불러왔는지 확인

$(document).ready(function() {
    'use strict';

    paper.install(window);  // Paper.js 를 전역 스코프에 설치 
    paper.setup(document.getElementById('mainCanvas'));  // 연결 

    // TODO

    // 원 하나 생성 
    // var c = Shape.Circle(200, 200, 50);
    // c.fillColor = 'green';

    // 바둑판 
    // var c;
    // for(var x = 25; x < 400; x += 50) {
    //     for (var y =25; y < 400; y += 50) {
    //         c = Shape.Circle(x, y, 20);
    //         c.fillColor = 'green';
    //     }
    // }

    // 

    var c = Shape.Circle(200, 200, 80);
    c.fillColor = 'black';
    var text = new PointText(200, 200);
    text.justification = 'center';
    text.fillColor = 'white';
    text.fontSize = 20;
    text.content = 'hello world'; 

    var tool = new tool();  // 객체 => 객체를 만들면 이벤트핸들러(onMouseDown) 를 연결할 수 있음 
    
    tool.onMouseDown = function(event) {
        // var c = Shape.Circle(event.point.x, event.point.y, 20);
        var c = Shape.Circle(event.point, 20);
        c.fillColor = 'green';
    };

    paper.view.draw();  // 실제 화면에 그림 그리기 

});