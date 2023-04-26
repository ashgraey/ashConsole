// bodyParser (app.post)
var bodyParser = require("body-parser");
var urlencodedParser = bodyParser.urlencoded({extended : false});

// mysql 아래 명령어를 db상에서 반드시 실행해야한다.  
// ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
var mysql = require("mysql");
var conn_info = {
	host : "localhost",
	port : 3306,
	user : "root",
	password : "root",
	database : "_node_jquery_ajax_bookshop",
    multipleStatements: true    // 여러 쿼리를 ;를 기준으로 한번에 보낼 수 있게 해줌.
};

//router
module.exports = function(app){

    app.get("/memberJoin", function(req, res){ 

        var log = req.session.log;
        var renderData = {	
            "log" : log
        };

        res.render("member/memberJoin.ejs", renderData);
    });

    app.post("/checkIdPro", urlencodedParser, function(req, res){ 
        var memberId = req.body.memberId;

        var conn = mysql.createConnection(conn_info);
        var sql = "SELECT COUNT(*) FROM member WHERE memberId=?";
        var inputData = [memberId];
        conn.query(sql, inputData, function(error, rows){
            var json = JSON.stringify(rows);
            var data = JSON.parse(json);
            var count = data[0]["COUNT(*)"];

            conn.end();

            var responseData = {};
            responseData.count = count;
            res.json(responseData);

        });
    });
    
    app.post("/memberJoinPro", urlencodedParser, function(req, res){
        var memberId = req.body.memberId;
        var memberPw = req.body.memberPw;
        var memberName = req.body.memberName;
        var memberPhone = req.body.memberPhone;
        var memberGender = req.body.memberGender;
        var memberInterest = req.body.memberInterest;
        var memberAddress = req.body.memberAddress;
        var memberEmail = req.body.memberEmail;

        var conn = mysql.createConnection(conn_info);

        var sql = "INSERT INTO member (memberId, memberPw, memberName, memberPhone, memberGender, memberInterest, memberAddress, memberEmail) VALUES(?, ?, ?, ?, ?, ?, ?, ?)";
        var inputData = [memberId, memberPw, memberName, memberPhone, memberGender, memberInterest, memberAddress, memberEmail];
        conn.query(sql, inputData, function(error){
            conn.end();
            res.json("");
        });
    });

    app.get("/memberLogin", function(req, res){ 
        var log = req.session.log;
    
        var renderData = {	
            "log" : log
        };

        res.render("member/memberLogin.ejs", renderData); 
    });    

    app.post("/memberLoginPro", urlencodedParser, function(req, res){ 
        var memberId = req.body.memberId;
        var memberPw = req.body.memberPw;

        var conn = mysql.createConnection(conn_info);
        var sql = "SELECT COUNT(*) FROM member WHERE memberId = ? AND memberPw = ?";
        var inputData = [memberId, memberPw];
        conn.query(sql, inputData, function(error, rows) {
            var json = JSON.stringify(rows);
            var data = JSON.parse(json);

            var count = data[0]["COUNT(*)"];
            if(count == 1) {
                req.session.log = memberId;
            }
            conn.end();

            var responseData = {};
            responseData.count = count;
            res.json(responseData);
            
        });
    });  

    app.post("/memberLogout", urlencodedParser, function(req, res){ 

        req.session.log = null;
        req.session.name = null;

    
        res.json("");
    });  
}