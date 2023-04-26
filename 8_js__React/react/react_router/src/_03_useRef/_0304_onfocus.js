import React from 'react'
import {useEffect} from 'react'

function _0304_onfocus() {

    function init(){
        let element = document.querySelector("#myInput");
        console.log(element);

        element.addEventListener("focus", focusFunction);
        element.addEventListener("blur", blurFunction);
    }
    function focusFunction() {
        let element = document.querySelector("#myInput");
        element.style.background = "lightgray";
    }
    
    function blurFunction() {
        let element = document.querySelector("#myInput");
        element.style.background = "";
    }
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
        <input type="text" id="myInput"></input>
    </>
  )
}

export default _0304_onfocus
