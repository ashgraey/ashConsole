// 서버 세팅 
var express = require("express");
var app = express();
var port = 3702;
var server = app.listen(port, function(){
	console.log("서버가 가동되었습니다" + port);
});

// ejs 세팅(views)
var ejs = require("ejs");
app.set("views", __dirname + "/views");
app.set("view engine", "ejs");
app.engine("ejs", ejs.renderFile);

// img폴더 경로 셋팅
app.use(express.static('./img'));	

// session 세팅
var session = require("express-session");
app.use(session({
	secret : "abcdefg",
	resave : false,
	saveUninitialized : false
}));

// router

require("./router/memberController")(app);
require("./router/bookController")(app);
require("./router/cartController")(app);

app.get("/", function(req, res){

	var log = req.session.log;
	var renderData = {	
		"log" : log
	};

    res.render("index.ejs", renderData); 
});