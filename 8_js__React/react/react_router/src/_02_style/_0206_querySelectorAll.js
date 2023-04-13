import React from 'react'
import {useEffect} from 'react'

function _0206_querySelectorAll() {
    function init(){
        let list = document.querySelectorAll("p.content");
        for(let i=0; i<list.length; i++) {
            list[i].style.fontWeight = "bold";
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);


  return (
    <>
        <p class="content">querySelectorAll() 메서드1</p>
        <p class="content">querySelectorAll() 메서드2</p>
    </>
  )
}

export default _0206_querySelectorAll
