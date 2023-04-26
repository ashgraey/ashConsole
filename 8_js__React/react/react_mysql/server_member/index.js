// 서버 셋팅
let express = require("express");
let app = express();
let port = 3502;
let server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// body-parser 설정
app.use(express.json());
app.use(express.urlencoded({extended: true}));

// path 설정
const path = require("path");

// 폴더 설정
app.use(express.static(path.join(__dirname, "../client_member/build")));

// 라우터
require("./router/routerMember")(app);


app.get("/", function(req, res){
    res.sendFile(path.join(__dirname, "../client_member/build/index.html")); 
});

app.get("*", function(req, res){
    res.sendFile(path.join(__dirname, "../client_member/build/index.html")); 
});
