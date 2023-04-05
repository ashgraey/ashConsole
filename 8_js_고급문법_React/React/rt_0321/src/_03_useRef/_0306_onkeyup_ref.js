import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
function _0306_onkeyup_ref() {
    const myInput = useRef(null);

    function init(){
        myInput.current.addEventListener("keyup", keyupFunction);
    }
 
    function keyupFunction() {
        myInput.current.value = myInput.current.value.toUpperCase();
    }
   
    useEffect(()=>{ 
        init();
    }, []);
  return (
    <>
      
      <input type="text" ref={myInput} placeholder="영어소문자를 입력하세요."></input>
    </>
  )
}

export default _0306_onkeyup_ref
