import React from 'react'
import { useEffect} from 'react'


function _0101_id() {

    function init(){
        let element = document.getElementById("content");
        console.log(element.innerText);    
        document.getElementById("target").innerText = "Hello, JavaScript";
        
    }

    window.onload = function() {     
        init();
    }

    return (
        <>
            <p id="content">getElementById() 메서드</p>
            <p id="target"></p>
            <hr></hr>
        </>
    )
}

export default _0101_id
