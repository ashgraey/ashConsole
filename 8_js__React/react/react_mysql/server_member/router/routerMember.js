// mysql 아래 명령어를 db상에서 반드시 실행해야한다.  
// ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
let mysql = require("mysql");
let conn_info = {
	host : "localhost",
	port : 3306,
	user : "root",
	password : "root",
	database : "react_member_202304"
};

//router
module.exports = function(app){
    app.post("/loginPro", function(req, res) {
        let memberPw = req.body.memberPw;
        let memberId = req.body.memberId;
       
        let conn = mysql.createConnection(conn_info);
        let sql = "select * from member_json where memberId=? and memberPw=?";
        let inputData = [memberId, memberPw];
        conn.query(sql, inputData, function(error, rows) {

            let json = JSON.stringify(rows);
            let data = JSON.parse(json);
            conn.end();
            res.json(data);
        });
    });

    app.post("/memberListPro", function(req, res) {
        let conn = mysql.createConnection(conn_info);
        let sql = "select * from member_json";
        conn.query(sql, function(error, rows) {

            let json = JSON.stringify(rows);
            let data = JSON.parse(json);
            console.log(data);
            conn.end();
            res.json(data);
        });
    });

    app.post("/memberInfoPro", function(req, res) {
        let memberId = req.body.memberId;

        let conn = mysql.createConnection(conn_info);
        let sql = "select * from member_json where memberId=?";
        let inputData = [memberId];
        conn.query(sql, inputData, function(error, rows) {

            let json = JSON.stringify(rows);
            let data = JSON.parse(json);
        
            conn.end();
            res.json(data);
        });
    });
    app.post("/memberUpdatePro", function(req, res) {
        let memberId = req.body.memberId;
        let memberPw = req.body.memberPw;
        let memberName = req.body.memberName;

        let conn = mysql.createConnection(conn_info);
        let inputData = [memberPw, memberName, memberId];
        let sql = "UPDATE member_json SET memberPw=?, memberName=? WHERE memberId = ?";
        conn.query(sql, inputData, function(error) {
            console.log(error)     
            conn.end();
            res.json("");
        });
    });
    app.post("/deletePro", function(req, res) {
        let memberId = req.body.memberId;

        let conn = mysql.createConnection(conn_info);
        let inputData = [memberId];
        let sql = "DELETE FROM member_json WHERE memberId = ?";
        conn.query(sql, inputData, function(error) {
            console.log(error)     
            conn.end();
            res.json("");
        });
    });
    app.post("/joinPro", function(req, res) {
        let memberId = req.body.memberId;
        let memberPw = req.body.memberPw;
        let memberName = req.body.memberName;

        let conn = mysql.createConnection(conn_info);
        let inputData = [memberId, memberPw, memberName];
        let sql = "insert into member_json (memberId, memberPw, memberName) values(?, ?, ?)";
        conn.query(sql, inputData, function(error) {
            console.log(error)     
            conn.end();
            res.json("");
        });
    });
}