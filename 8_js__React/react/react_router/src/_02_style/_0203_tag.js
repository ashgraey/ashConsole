import React from 'react'
import {useEffect} from 'react'
import "./_0203_tag.css"

function _0203_tag() {
    function init(){
        let collection = document.getElementsByTagName("p");
        // 배경색상 변경
        for(let i=0; i<collection.length; i++) {
            collection[i].style.backgroundColor = "yellow";
        }
    }

    useEffect(()=>{ 

        init();

    }, []);
    
    return (
        <>
            <p className="_0203p">getElementsByTagName() 메서드1</p>
            <p className="_0203p">getElementsByTagName() 메서드2</p>
            <p className="_0203p">getElementsByTagName() 메서드3</p>
        </>
    )
}

export default _0203_tag
