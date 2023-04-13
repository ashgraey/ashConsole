import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
function _0310_light_ref() {

    const light = useRef(null);

    function init(){

        // 하나의 선택자에 여러개의 이벤트를 적용할 수 있다.
        light.current.addEventListener("mouseover", changeOn);
        light.current.addEventListener("mouseout", changeOff);
    }
    
    function changeOn() {
        light.current.src = "images/light_on.jpg";
    }
    
    function changeOff() {
        light.current.src = "images/light_off.jpg";
    }

    useEffect(()=>{ 
        init();
    }, []);

    
    return (
    <>
       <img src="images/light_off.jpg" ref={light} width="300px"></img>
    </>
  )
}

export default _0310_light_ref
