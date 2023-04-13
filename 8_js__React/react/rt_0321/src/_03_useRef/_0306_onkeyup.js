import React from 'react'
import {useEffect} from 'react'

function _0306_onkeyup() {
    function init(){
        document.querySelector("#myInput").addEventListener("keyup", keyupFunction);
    }
 
    function keyupFunction() {
        let element = document.querySelector("#myInput");
        element.value = element.value.toUpperCase();
    }
   
    useEffect(()=>{ 
        init();
    }, []);
  return (
    <>
      
      <input type="text" id="myInput" placeholder="영어소문자를 입력하세요."></input>
    </>
  )
}

export default _0306_onkeyup
