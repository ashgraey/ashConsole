import React from 'react'
import {useEffect} from 'react'
import "./_0309_cart.css"

/*
    [Console 창에 뜨는 table 관련 오류는 무시한다.]
*/

function _0309_cart() {
    function init(){
        let subImgs = document.querySelectorAll(".sub1");
        for(let i=0; i<subImgs.length; i++) {

            /* 자동으로 e 변수에 이벤트가 저장된다. */
            subImgs[i].addEventListener("click", changeImg1);
        }

        
        subImgs = document.querySelectorAll(".sub2");
        for(let i=0; i<subImgs.length; i++) {
            /* 정확하게 직접 전달하는방법 */
            subImgs[i].addEventListener("click", (e) =>{changeImg2(e.target)});
        }
    }
    function changeImg1(e) {
        let mainImg = document.querySelector("#main");
        let clickImg = e.target.src;
        console.log(e);
        mainImg.setAttribute("src", clickImg);
    }

    function changeImg2(target) {
        let mainImg = document.querySelector("#main");
        let clickImg = target.src;
        console.log(target);
        mainImg.setAttribute("src", clickImg);
    }

    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <h1 id="heading">간식 종류</h1>
            <table>
                <tr>
                    <td rowSpan="5">
                        <img src="images/snack1.jpg" id="main" width="200px" height="200px"></img>
                    </td>
                    <td>상품명 : 삼립 미니꿀약과</td>
                </tr>
                <tr>
                    <td>판매가 : 20,000원</td>
                </tr>
                <tr>
                    <td>배송비 : 3,000원</td>
                </tr>
                <tr>
                    <td>수량 : <input type="number" value="1"></input></td>
                </tr>
                <tr>
                    <td><button>장바구니 담기</button></td>
                </tr>
                <tr>
                    <td colSpan="2">
                        <img src="images/snack1.jpg" className="_0309sub1" ></img>
                        <img src="images/snack2.jpg" className="_0309sub1"></img>
                        <img src="images/snack3.jpg" className="_0309sub1"></img>
                    </td>


                </tr>

                <tr>
                    <td colSpan="2">
                        <img src="images/snack1.jpg" className="_0309sub2" ></img>
                        <img src="images/snack2.jpg" className="_0309sub2"></img>
                        <img src="images/snack3.jpg" className="_0309sub2"></img>
                    </td>                   
                </tr>
            </table>

        </>
    )
}

export default _0309_cart
