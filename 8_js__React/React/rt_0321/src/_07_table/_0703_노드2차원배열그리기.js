import React from 'react'

import {useEffect} from 'react'
import {useRef} from 'react'
import {useState} from 'react'

import "./_0703_노드2차원배열그리기.css"

function _0703_노드2차원배열그리기() {
    const center = useRef();
    let tableList = [];

    let clickEvent = function(e) {
        for(let i=0; i<tableList.length; i++) {
            for(let j=0; j<tableList[i].length; j++) {
                if(e.target.innerText == tableList[i][j].innerText) {
                    alert(i + ", " + j);
                }
            }
        }
    }
   
    function init(){
        
        let table = document.createElement("table");
        let num = 1;
        for(let i=0; i<5; i++) {
            let tempTr = document.createElement("tr");
            let trList = [];
            for(let j=0; j<5; j++) {
                let td = document.createElement("td");
                td.className = "_0703td";
                td.addEventListener("click", clickEvent);

                td.innerText = num;
                tempTr.append(td);  

                num += 1;
                trList.push(td);
            }
            
            table.append(tempTr);
            tableList.push(trList);
        }
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

export default _0703_노드2차원배열그리기
