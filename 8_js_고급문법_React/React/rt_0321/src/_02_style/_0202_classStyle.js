import React from 'react'
import {useEffect} from 'react'

/*
    [리엑트에서 내부스타일 사용해서 속성변경]

        기본의 css 문법을 사용하면 에러가 발생한다.
        [예] 
            style="display: none"

        [리엑트 스타일 문법 ]
            style = {}  안에 json 문법으로 {key : value , key : value , ... } 를 사용해야한다. 
        [예] 
            style={{display:"none"}}
*/

function _0202_classStyle() {

    function init(){
        document.querySelectorAll(".content")[1].style.backgroundColor = "red";
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
        <div>
            <p className="content" 
            style={{ border: "1px solid black" , fontSize: "20px" }}>
                getElementsByClassName() 메서드1</p>
        </div>
        <div>
            <p className="content" 
            style={{ border: "1px solid black"}}>
                getElementsByClassName() 메서드2</p>
        </div>
    </>
  )
}

export default _0202_classStyle
