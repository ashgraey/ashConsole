import React from 'react'
import {useEffect} from 'react'
function _0110_value2() {


    function init(){
        document.getElementById("content").value = "반가워요";
    }
   
    useEffect(()=>{ 
        init();
    }, []);


  return (
    <>
      <input type="text" id="content" value="안녕하세요"></input>
    </>
  )
}

export default _0110_value2
