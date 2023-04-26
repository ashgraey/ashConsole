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

    // 장바구니 수량증가
    app.post("/priceUp", urlencodedParser, function(req, res) {
        var cartNo = Number(req.body.cartNo);
       
        var conn = mysql.createConnection(conn_info);
        var sql = "UPDATE cart SET cartBuyCount = cartBuyCount + 1 WHERE cartNo = ?";
        var inputData = [cartNo];
        conn.query(sql, inputData, function(error) {
            conn.end();
            res.json("");
        });
    });

    // 장바구니 수량감소
    app.post("/priceDown", urlencodedParser, function(req, res) {
        var cartNo = Number(req.body.cartNo);
        
        var conn = mysql.createConnection(conn_info);
        var sql = "UPDATE cart SET cartBuyCount = cartBuyCount - 1 WHERE cartNo = ?";
        var inputData = [cartNo];
        conn.query(sql, inputData, function(error) {
            conn.end();
            res.json("");
        });
    });

    app.post("/addCart", urlencodedParser, function(req, res) { 
        var log = req.session.log;

        if(log == null) {
            res.json("no");
        } else {

            var conn = mysql.createConnection(conn_info);
            
            var cartMemberId = log;
            var cartBookName = req.body.bookName;
            var cartBuyCount = Number(req.body.buyCount);
            var cartBookImage = req.body.bookImage;
            var cartBuyBookPrice = Number(req.body.buyPrice);
            
            var sql = "INSERT INTO cart (cartMemberId, cartBookName, cartBuyCount, cartBookImage, cartBuyBookPrice) VALUES(?, ?, ?, ?, ?)";
            var inputData = [cartMemberId, cartBookName, cartBuyCount, cartBookImage, cartBuyBookPrice];
            conn.query(sql, inputData, function(error) {
                conn.end();
               
                res.json("yes");
            });

            
        }
    });

    // app.post("/cartInfo", urlencodedParser, function(req, res) {
    app.get("/cartInfo", function(req, res) {
        var log = req.session.log;
        var name = req.session.name;

        if(log == null) {
            res.redirect("/");
        } else {
            var conn = mysql.createConnection(conn_info);
            var sql1 = "SELECT SUM(cartBuyCount * cartBuyBookPrice) FROM cart WHERE cartMemberId = ?";
            var inputData = [log];
            conn.query(sql1, inputData, function(error, rows) {
                var json = JSON.stringify(rows);
                var data = JSON.parse(json);
                var total = data[0]["SUM(cartBuyCount * cartBuyBookPrice)"];

                sql2 = "SELECT * FROM cart WHERE cartMemberId = ? ORDER BY cartNo ASC";
                inputData = [log];
                conn.query(sql2, inputData, function(error, rows) {
                    var renderData = {	
                        "log" : log,
                        "name" : name,
                        "total" : total,
                        "cartList" : rows
                    };
    
                    conn.end();
                    res.render("cart/cartInfo.ejs", renderData); 
                });
            });
            
        }
    });

    app.post("/deleteCart", urlencodedParser, function(req, res) {
        var log = req.session.log;
        var name = req.session.name;

        var cartNo = Number(req.body.cartNo);

        var conn = mysql.createConnection(conn_info);
        var sql = "DELETE FROM cart WHERE cartNo = ?";
        var inputData = [cartNo];
        conn.query(sql, inputData, function(error) {

            //--------------------------------------------------------------------------
            var sql1 = "SELECT SUM(cartBuyCount * cartBuyBookPrice) FROM cart WHERE cartMemberId = ?";
            var inputData = [log];
            conn.query(sql1, inputData, function(error, rows) {
                var json = JSON.stringify(rows);
                var data = JSON.parse(json);
                var total = data[0]["SUM(cartBuyCount * cartBuyBookPrice)"];

                var sql2 = "SELECT * FROM cart WHERE cartMemberId = ? ORDER BY cartNo ASC";
                inputData = [log];
                conn.query(sql2, inputData, function(error, rows) {
                    var renderData = {	
                        "log" : log,
                        "name" : name,
                        "total" : total,
                        "cartList" : rows
                    };
    
                    conn.end();
                    res.json(renderData);
                });
            });
            //--------------------------------------------------------------------------

        });
    });


}