import React from 'react'

/*
    [리엑트의 버튼사용법]
        [기존 예시] <button onclick="clickMe()">버튼</button>
    [변경점]
        [1] onclick 이 카멜식으로 onClick 으로 변경
        [2] "" 안에 함수명을적었던 방식에서 , {} 안에 적는것으로 변경
*/
function _0301_이벤트추가1() {
    
    function clickMe() {
        alert("클릭!");
    }
   
    return (
        <>
            {/* <button onclick="clickMe()">버튼</button> */}
            <button onClick={clickMe}>버튼</button>
        </>
    )
}

export default _0301_이벤트추가1
