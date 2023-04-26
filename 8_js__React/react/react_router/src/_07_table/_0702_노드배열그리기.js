import React from 'react'

import {useEffect} from 'react'
import {useRef} from 'react'
import {useState} from 'react'

import "./_0702_노드배열그리기.css"

function _0702_노드배열그리기() {
    const center = useRef();
    let tdList = [];

    let clickEvent = function(e) {
        for(let i=0; i<tdList.length; i++) {
            if(e.target.innerText == tdList[i].innerText) {
                alert(i);
            }
        }
    }
   
    function init(){
        
        let table = document.createElement("table");
        let tr = document.createElement("tr");
        
        for(let i=0; i<5; i++) {
            let td = document.createElement("td");
            td.className = "_0702td";
            td.addEventListener("click", clickEvent);
            td.innerText = i;
            tr.append(td);  
            
            tdList.push(td);
        }
        table.append(tr);
        center.current.append(table);
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

export default _0702_노드배열그리기
