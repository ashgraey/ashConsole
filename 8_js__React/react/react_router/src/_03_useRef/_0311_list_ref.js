import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
import "./_0311_list.css"

function _0311_list_ref() {
   
    let isShow = false;
    const list = useRef(null);
    const menu = useRef(null);

    function init(){
        list.current.addEventListener("click", displayList);
    }

    function displayList() {
        if(isShow == false) {
            menu.current.style.display = "block";            // 노출 처리
            list.innerHTML = "목차 닫기";   
            isShow = true;
        } else {
            menu.current.style.display = "none";             // 숨김 처리
            list.innerHTML = "목차 보기";   
            isShow = false;
        }
    }
    
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <a href="" ref={list}>목차 보기</a>
            <hr></hr>
            <ul ref={menu}>
                <li>메뉴1</li>
                <li>메뉴2</li>
                <li>메뉴3</li>
                <li>메뉴4</li>
            </ul>
        </>
    )
}

export default _0311_list_ref
