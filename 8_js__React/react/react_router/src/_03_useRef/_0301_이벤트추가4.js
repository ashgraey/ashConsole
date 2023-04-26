import React from 'react'
import {useEffect} from 'react'

/*
    [리엑트 버튼으로 인자전달]
        리엑트에서 onClick 에 함수를 연결할때는 기본적으로 ()를 붙이지않는다.
        () 가 없기때문에 인자도 전달할수가 없다.
        인자를 전달하기 위해서는 구조를 변경해야한다.

    [예시]
        아래와 같은 모양으로는 인자를 전달할수없다. 소괄호가 없다.
        <button onClick={testClick}>버튼으로 인자전달</button>

    [변경된예시]
        조금 구조가 복잡해보이지만 (e) => { 여기에 함수작성 } 의 모양으로 바꿔야한다.
    
        <button onClick= {(e) => {testClick(1,2)}}>버튼으로 인자전달</button>
*/

function _0301_이벤트추가4() {
    
    function testClick(a , b){
        alert(a);
        alert(b);
    }
   
    return (
        <>  
            {/* <button onClick={testClick}>버튼으로 인자전달</button> */}
            <button onClick= {(e) => {testClick(1,2)}}>버튼으로 인자전달</button>
        </>
    )
}

export default _0301_이벤트추가4
