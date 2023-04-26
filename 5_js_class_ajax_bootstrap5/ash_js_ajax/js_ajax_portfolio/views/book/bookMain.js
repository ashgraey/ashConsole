function drawBanner(){
    var text = '';
    text += 
    `<div class="my-5">
        <img src="/banner01.jpg" class="img-fluid">
    </div>;`;
    var $banner = document.querySelector("#banner");
    $banner.innerHTML = text;
}


function drawContentTitle(){
    var text = '';
    text += 
    `<div class="container" >
        <div class="row py-4 mb-4">
            <div class="text-center" > 
                <h3 ><b>전체상품</b></h3>
            </div>
        </div>
    </div>`;
    var $contentTitle = document.querySelector("#contentTitle");
    $contentTitle.innerHTML = text;
}

function drawContent(bookList){
        
    var text = '';
    var k = 0;
    for(var i = 0; i < 3; i++){
        text += 
        `<div class="container">
            <div class="row mb-5 gy-3">`;
                for(var j = 0; j < 6; j++){
                    var book = bookList[k];
                    var bookInfoToken = book.bookInfo.split("|");
                    var bookInfo = bookInfoToken[0] + "|" + bookInfoToken[1];
                    k += 1;
                    text += 
                    `<div class="col-12 col-sm-6 col-xl-2">
                        <div class="d-flex justify-content-center">
                            <div class="card col-10 border-0">
                                <img class="card-img-top border" src=${book.bookImage}>
                                <div class="card-body px-0">
                                    <div class="card-text " style="font-size:14px; color: rgba(0, 0, 0, 0.973); font-weight: 500;">${book.bookName}</div>
                                    <div class="card-text " style="font-size:12px; color: rgba(162, 162, 162, 0.973); font-weight: 500;">${bookInfo}</div>
                                    <div class="card-text " style="font-size:14px; color: rgba(0, 0, 0, 0.973); font-weight: 500;">${book.bookPrice}원</div>
                                </div>
                            </div>
                        </div>
                    </div>`;
                }
            text += 
            `</div>
        </div>`;
    }
        
    var $content = document.querySelector("#content");
    $content.innerHTML = text;

}

function drawBookMain(){
    jQuery.ajax({
        type: "post",
        url: "getBookListAll",
        data: {},
        
        success: function(data) {
            //console.log(data);
            var bookList = data.bookList;
            drawBanner();
            drawContentTitle();
            drawContent(bookList);            
        }
    });
}  