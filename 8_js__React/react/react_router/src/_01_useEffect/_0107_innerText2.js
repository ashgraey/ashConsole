import React from 'react'
import {useEffect} from 'react'

function _0107_innerText2() {

    function init(){
        document.querySelector("#name").innerText = "김철수";
        document.querySelector("#age").innerText = 10;
    }
   
    useEffect(()=>{ 
        init();
    }, []);
  return (
    <>
      
    </>
  )
}

export default _0107_innerText2
