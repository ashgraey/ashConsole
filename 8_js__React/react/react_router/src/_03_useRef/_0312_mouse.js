import React from 'react'
import {useEffect} from 'react'
import "./_0312_mouse.css"

function _0312_mouse() {

    function init(){
        let btn = document.querySelector("#btn");

        btn.addEventListener("mouseover", btnMouseOver);
        btn.addEventListener("mouseout", btnMouseOut);
    }

    function btnMouseOver() {
        let btn = document.querySelector("#btn");
        btn.style.background = "gray";
    }
    function btnMouseOut() {
        let btn = document.querySelector("#btn");
        btn.style.background = "tomato";
    }
    
    useEffect(()=>{ 
        init();
    }, []);


  return (
    <>
      <button id="_3012btn">GAME START</button>
    </>
  )
}

export default _0312_mouse
