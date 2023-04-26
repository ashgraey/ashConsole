import React from 'react'
import {useEffect} from 'react'

/*  
    [리엑트에서 this(현재클릭된버튼)를 인자로 함수에 전달하는 방법]

    [주의] 아래와 같이 this를 직접 전달하면 에러발생한다.
        <h3 onClick={(e) =>{changeColor(this, 'red')}}>클릭하면 글자 색상이 바뀝니다.</h3>

    [변경] e.target으로 전달해야한다.
         <h3 onClick={(e) =>{changeColor(e.target, 'red')}}>클릭하면 글자 색상이 바뀝니다.</h3>
*/
function _0308_this() {
    function changeColor(elem, color) {
        console.log(elem)
        elem.style.color = color;
    }

    function init(){
        let test2 = document.querySelector("#test2");
        test2.addEventListener("click", (e) => {changeColor(e.target , "blue")});
    }
    
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            {/* <h3 onClick={(e) =>{changeColor(this, 'red')}}>클릭하면 글자 색상이 바뀝니다.</h3> */}
            <h3 onClick={(e) => {changeColor(e.target, 'red')}}>클릭하면 글자 색상이 바뀝니다1.</h3>
            <h3 id="test2">클릭하면 글자 색상이 바뀝니다2.</h3>
        </>
    )
}

export default _0308_this
