import React from 'react'
import { useEffect } from 'react';
import {useRef} from 'react'

function _0403_추가_append() {

    const list = useRef(null);

    
    function init(){
        let stList = [
            {"name":"Hong", "age":21},
            {"name":"Kim", "age":22},
            {"name":"Park", "age":23}
        ];

        for(let i=0; i<stList.length; i++) {
            let p = document.createElement("p");
            p.append(`이름 : ${stList[i]["name"]}, 나이 : ${stList[i].age}`);

            list.current.append(p);
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <h4>학생 명단</h4>
            <div ref={list}></div>
        </>
    )
}

export default _0403_추가_append
