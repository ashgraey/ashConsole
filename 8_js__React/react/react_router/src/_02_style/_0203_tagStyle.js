import React from 'react'
import {useEffect} from 'react'

function _0203_tagStyle() {

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
            <p style={{ border: "1px solid black"}} >getElementsByTagName() 메서드1</p>
            <p style={{ border: "1px solid black" , color : "red"}} >getElementsByTagName() 메서드2</p>
            <p style={{ border: "1px solid black"}} >getElementsByTagName() 메서드3</p>
        </>
    )
}

export default _0203_tagStyle
