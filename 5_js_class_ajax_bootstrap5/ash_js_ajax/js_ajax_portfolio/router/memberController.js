

// ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
var mysql = require("mysql");
var conn_info = {
	host : "localhost",
	port : 3306,
	user : "root",
	password : "root",
	database : "_node_db_booshop" ,
    multipleStatements: true
};

var bodyParser = require("body-parser");
var urlencodedParser = bodyParser.urlencoded({extended : false});

//router
module.exports = function(app){
    app.get("/memberJoinForm", function(req, res){
   
        res.render("member/memberJoinForm.ejs");     
    });


	app.get("/memberLoginForm", function(req, res){
   
        res.render("member/memberLoginForm.ejs");     
    });
};