
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

    app.get("/bookMain", function(req, res){
   
        res.render("book/bookMain.ejs");     
    });

    app.post("/getBookListAll", urlencodedParser, function(req, res){
        var conn = mysql.createConnection(conn_info);
        var sql = "SELECT * FROM book ORDER BY bookSold DESC LIMIT 0, 18";
        conn.query(sql, function(error, rows) {
            var renderData = {
                "bookList" : rows
            };
            conn.end();
            res.json(renderData);
        });
        
    });

    app.post("/getLog", urlencodedParser, function(req, res){
        var result = 1;
        if(req.session.log == null){
            result = 0;
        }
        res.json(result);
    });

};