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
	database : "_node_jquery_ajax_bookshop"
};

//router
module.exports = function(app){

    app.get("/bookAllList", function(req, res){ 
        var log = req.session.log;
        
        var conn = mysql.createConnection(conn_info);
        var sql = "SELECT * FROM book ORDER BY bookNo ASC";
        conn.query(sql, function(error, rows) {
        var renderData = {
                "log" : log,
                "bookList" : rows
            };
            conn.end();
            res.render("book/bookAllList.ejs", renderData); 
        });
    });   

    app.get("/bookInfo", function(req, res){
        var log = req.session.log;
        var name = req.session.name;
        var bookNo = req.query.bookNo;

        var conn = mysql.createConnection(conn_info);
        var sql = "SELECT * FROM book WHERE bookNo = ?";
        var inputData = [bookNo];
        conn.query(sql, inputData, function(error, rows) {
            var renderData = {
                "log" : log,
                "name" : name,
                "book" : rows[0]
            };
            conn.end();
            res.render("book/bookInfo.ejs", renderData);
        });
    });

}