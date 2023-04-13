import React from 'react'
import {useEffect} from 'react'

function _0108_innerHTML2() {
    function init(){
        document.querySelector("#name").innerHTML = "이름 : <span style='color:blue'>김철수</span>";
        document.querySelector("#age").innerHTML = "나이 : <span>10</span>";
    }
   
    useEffect(()=>{ 
        init();
    }, []);

  return (
    <>
        <h4>학생 명단</h4>
        <p id="name"></p>
        <p id="age"></p>
    </>
  )
}

export default _0108_innerHTML2
