import React from 'react'
import {useEffect} from 'react'
import "./_0311_list.css"

function _0311_list() {
   
    let isShow = false;
    
    function init(){
        let list = document.querySelector("#list");
        list.addEventListener("click", displayList);
    }

    function displayList() {
        let list = document.querySelector("#list");
        if(isShow == false) {
            document.querySelector("#menu").style.display = "block";            // 노출 처리
            list.innerHTML = "목차 닫기";   
            isShow = true;
        } else {
            document.querySelector("#menu").style.display = "none";             // 숨김 처리
            list.innerHTML = "목차 보기";   
            isShow = false;
        }
    }
    
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <a href="#" id="list">목차 보기</a>
            <hr></hr>
            <ul id="menu">
                <li>메뉴1</li>
                <li>메뉴2</li>
                <li>메뉴3</li>
                <li>메뉴4</li>
            </ul>
        </>
    )
}

export default _0311_list
