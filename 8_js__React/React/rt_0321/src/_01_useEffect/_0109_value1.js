import React from 'react'
import {useEffect} from 'react'

function _0109_value1() {

    function init(){
        let element = document.querySelector("#name");
        console.log(element.value);
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
      <input type="text" id="name" value="김철수"></input>
    </>
  )
}

export default _0109_value1
