import React from 'react'
import {useState} from 'react'

function _0602_useState() {

    const [Temp , setTemp] = useState(0);
    /*
        1. 첫번째 인자 : 변수의 이름
        2. 두번째 인자 : State를 바꿔주는 함수
        3. useState 함수인자 : State의 초기 Type, 값

        state의 값이 바뀌어도 화면을 재랜더링(새로고침)시킬필요가없다. 

        1. state의 값을 바꿀때는 항상 set을 사용해야한다. 
        2. set를 html 태그의 on속성 호출 : 함수로 감싸주어야한다. 
    */

    return (
        <>
            {Temp}
            <br></br>
            <button onClick={function(){ setTemp(Temp + 1)}}>증가1</button>
            <br></br>
            <button onClick={() => setTemp(Temp + 1)}>증가2</button>
        </>
    )
}

export default _0602_useState
