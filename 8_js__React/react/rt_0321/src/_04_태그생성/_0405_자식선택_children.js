import React from 'react'
import { useEffect } from 'react';
import {useRef} from 'react'

function _0405_자식선택_children() {

    const list = useRef();

    function init(){


        
        for(let i=0; i<4; i++) {
            console.log(list.current.children[i].innerText);
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
        <h4>과일 목록</h4>
            <div ref={list}>
                <li>사과</li>
                <li>바나나</li>
                <li>딸기</li>
                <li>포도</li>
            </div>
        </>
    )
}

export default _0405_자식선택_children
