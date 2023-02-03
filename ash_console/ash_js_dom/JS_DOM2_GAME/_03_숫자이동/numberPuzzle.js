var nodeList = [];
var body = document.body;
var table = document.createElement("table");

var nodeEvent = function(e) {
    var target = e.target;

    if(target.textContent != "") {
        var y = 0;
        var x = 0;
        for(var i=0; i<nodeList.length; i++) {
            for(var j=0; j<nodeList[i].length; j++) {
                if(target.textContent == nodeList[i][j].textContent) {
                    y = i;
                    x = j;
                    break;
                }
            }
        }
        
        var yy = -1;
        var xx = -1;
        for(var i=-1; i<=1; i++) {
            if(0 <= y + i && y + i < 5) {
                if(nodeList[y + i][x].textContent == "") {
                    yy = y + i;
                    xx = x;
                }
            }
            if(0 <= x + i && x + i < 5) {
                if(nodeList[y][x + i].textContent == "") {
                    yy = y;
                    xx = x + i;
                }
            }
        }

        if(yy > -1 && xx > -1) {
            var text = nodeList[y][x].textContent;
            nodeList[y][x].textContent = "";
            nodeList[yy][xx].textContent = text;
        }
    }
}

function setNumber() {
    var numList = [];
    // 5 * 5 배열에 순차적으로 값 생성
    for(var i=0; i<25; i++) {
        numList.push(i);
    }

    // 셔플
    for(var i=0; i<100; i++) {
        var r = Math.floor(Math.random() * 25);

        var temp = numList[0];
        numList[0] = numList[r];
        numList[r] = temp;
    }

    // 배열의 값이 0인 블럭에 "" 빈공백 삽입하기
    var index = 0;
    for(var i=0; i<nodeList.length; i++) {
        for(var j=0; j<nodeList[i].length; j++) {
            if(numList[index] == 0) {
                nodeList[i][j].textContent = "";
            } else {
                nodeList[i][j].textContent = numList[index];
            }
            
            index += 1;
        }
    }
}

function init() {
    
    for(var i=0; i<5; i++) {
        var line = document.createElement("tr");
        nodeList.push([]);
        for(var j=0; j<5; j++) {
            var node = document.createElement("td");
            node.addEventListener("click", nodeEvent);
            line.append(node);
            nodeList[i].push(node);
        }
        table.append(line);
    }
    body.append(table);

    setNumber();
}

init();