import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
import "./_0309_cart.css"

/*
    [Console 창에 뜨는 table 관련 오류는 무시한다.]

    [useRef 배열로 사용법] 

*/

function _0309_cart_ref() {

    const sub1 = useRef([]);
    const main = useRef(null);

    function init(){
        for(let i=0; i < sub1.current.length; i++) {

            sub1.current[i].addEventListener("click", changeImg1);
        }   
    }
    function changeImg1(e) {
        let mainImg = main.current;
        let clickImg = e.target.src;
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
                        <img src="images/snack1.jpg" ref={main} width="200px" height="200px"></img>
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
                        <img src="images/snack1.jpg" className="_0309sub1" ref={(e) => {sub1.current[0] = e}} ></img>
                        <img src="images/snack2.jpg" className="_0309sub1" ref={(e) => {sub1.current[1] = e}}></img>
                        <img src="images/snack3.jpg" className="_0309sub1" ref={(e) => {sub1.current[2] = e}}></img>
                    </td>


                </tr>

                
            </table>

        </>
    )
}

export default _0309_cart_ref
