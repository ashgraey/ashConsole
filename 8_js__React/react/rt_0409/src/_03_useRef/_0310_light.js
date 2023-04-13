import React from 'react'
import {useEffect} from 'react'

function _0310_light() {

    function init(){
        let light = document.querySelector("#light");
        console.log(light);

        // 하나의 선택자에 여러개의 이벤트를 적용할 수 있다.
        light.addEventListener("mouseover", changeOn);
        light.addEventListener("mouseout", changeOff);
    }
    
    function changeOn() {
        let light = document.querySelector("#light");
        light.src = "images/light_on.jpg";
    }
    
    function changeOff() {
        let light = document.querySelector("#light");
        light.src = "images/light_off.jpg";
    }

    useEffect(()=>{ 
        init();
    }, []);

    
    return (
    <>
       <img src="images/light_off.jpg" id="light" width="300px"></img>
    </>
  )
}

export default _0310_light
