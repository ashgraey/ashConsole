import React from 'react'
import { useEffect } from 'react';
function _0502_timeout1() {

    let num = 0;
    function addNumber(){
        num += 1;
        alert(num)
    }

    function init(){
        setTimeout(addNumber, 3000);
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
      
    </>
  )
}

export default _0502_timeout1
