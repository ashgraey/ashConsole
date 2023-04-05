import React from 'react'
import {useEffect} from 'react'

function _0205_querySelector() {
    function init(){
        let element = document.querySelector("div > p");
        // 테두리 변경
        element.style.border = "1px solid black";
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
      <div>
        <p>div안의 p태그</p>
      </div>
      <p>p태그</p>
    </>
  )
}

export default _0205_querySelector
