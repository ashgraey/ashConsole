import React from 'react'
import {useEffect} from 'react'
import "./_0202_class.css"

/*  
    [css 파일 임포트 방법]
        [주의] js 파일이 아니면 반드시 확장자명을 다써야한다 .css

        [예] import "./_0202_class.css"

    [주의]
        태그에 id 속성은 기존 css 와 이름이 같다
        하지만 class 는 예약어가 이미존재하기 때문에 className 으로 카멜식으로 변경되었다.

    [예시]
        <div className="content">
        </div>
*/

function _0202_class() {

    function init(){
        document.querySelectorAll(".content")[1].style.backgroundColor = "red";
    }
   
    useEffect(()=>{ 
        init();
    }, []);
  return (
    <>
        <div className="_0202content">
            <p>getElementsByClassName() 메서드1</p>
        </div>
        <div className="_0202content">
            <p>getElementsByClassName() 메서드2</p>
        </div>
    </>
  )
}

export default _0202_class
