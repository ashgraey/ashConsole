import React from 'react'

import {useEffect} from 'react'
import {useRef} from 'react'
import {useState} from 'react'

import './_0701_노드한개그리기.css'

function _0701_노드한개그리기() {

    const center = useRef();
    let check = false;

    let nodeEvent = function(e) {
        if(check == false) {
            e.target.innerText = "눌렀음!";
        } else {
            e.target.innerText = "";
        }
        check = !check;
    }
   
    function init(){
        let node = document.createElement("td");
        node.className = "_0701td";
        center.current.append(node) ;
        node.addEventListener("click", nodeEvent);
        
    
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <div ref={center}>

            </div>
        </>
    )
}

export default _0701_노드한개그리기
