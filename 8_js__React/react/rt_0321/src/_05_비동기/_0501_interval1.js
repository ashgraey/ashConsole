import React from 'react'
import { useEffect } from 'react';
function _0501_interval1() {

    let num = 0;
    let auto = null;
    function addNumber(){
        num += 1;
        console.log("num: " + num);
    }

    function init(){
             
        // setInterval(함수(){}, 밀리세컨드)
        // 해당 시간간격만큼 해당 함수를 호출함(애니메이션)
        // clearInterval() : 생성된 setInterval함수를 종료시키는 함수
        auto = setInterval(addNumber, 100);     // 0.1초 간격으로 addNumber함수 호출
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <h1>일정 시간 간격으로 값 증감시키기</h1>
            <button onClick={(e) => {clearInterval(auto)}}>증가 정지</button>  
        </>
    )
}

export default _0501_interval1
