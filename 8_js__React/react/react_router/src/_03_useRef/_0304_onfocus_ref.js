import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'

function _0304_onfocus_ref() {

    const myInput = useRef(null);

    function init(){
        
        myInput.current.addEventListener("focus", focusFunction);
        myInput.current.addEventListener("blur", blurFunction);
    }
    function focusFunction() {
        myInput.current.style.background = "lightgray";
    }
    
    function blurFunction() {
        myInput.current.style.background = "";
    }
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
        <input ref={myInput} type="text" ></input>
    </>
  )
}

export default _0304_onfocus_ref
