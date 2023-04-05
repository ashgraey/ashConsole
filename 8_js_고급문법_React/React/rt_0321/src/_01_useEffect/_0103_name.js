import React from 'react'
import {useEffect} from 'react'


function _0103_name() {

    function init() {
        let list = document.getElementsByName("subject");
        let size = list.length;
        console.log(size);
        
        let element = document.getElementById("target");
        let text = element.innerText + size;
        element.innerText = text;
    }

    useEffect(()=>{ 
        init();
    }, []);


    // window.onload = function() {
    //     init();
    // }


    return (
        <>
            <h3 id="target">선택 가능한 과목 수 : </h3>
            HTML<input type="checkbox" name="subject" value="html"></input>
            CSS<input type="checkbox" name="subject" value="css"></input>
            JavaScript<input type="checkbox" name="subject" value="javascript"></input>
            <hr></hr>
        </>
    )
}

export default _0103_name
