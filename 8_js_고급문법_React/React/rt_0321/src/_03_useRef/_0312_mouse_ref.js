import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
import "./_0312_mouse.css"

function _0312_mouse_ref() {

    const btn = useRef(null);

    function init(){

        btn.current.addEventListener("mouseover", btnMouseOver);
        btn.current.addEventListener("mouseout", btnMouseOut);
    }

    function btnMouseOver() {
        btn.current.style.background = "gray";
    }
    function btnMouseOut() {
        btn.current.style.background = "tomato";
    }
    
    useEffect(()=>{ 
        init();
    }, []);


  return (
    <>
      <button id="_0312btn" ref={btn}>GAME START</button>
    </>
  )
}

export default _0312_mouse_ref
