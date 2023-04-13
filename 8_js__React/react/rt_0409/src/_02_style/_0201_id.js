import React from 'react'
import {useEffect} from 'react'

function _0201_id() {

    function init(){
        document.querySelector("#content").style.color = "red";
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <p id="content">getElementById() 메서드</p>
        </>
    )
}

export default _0201_id
