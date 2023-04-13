import React from 'react'
import {useEffect} from 'react'
/*
    [ useEffect() ]
        리엑트 제공하는 함수 , window.onload 와 비슷한 역활을 한다. 
        당장은 큰역활은 없으나 차차 기능을 익혀나간다. 
        이후는  window.onload 대신 useEffect 를 사용한다.


    [사용방법] 임포트 후 사용한다.
        [예] import {useEffect} from 'react'
    [주의점]
        구조가 조금 복잡해보여 잘 구분해서 사용한다.

            useEffect(()=>{ 
                init();
            }, []);



*/

function _0102_class() {

    function init(){
        let collection = document.getElementsByClassName("content")[0];
        console.log(collection.innerText);    
        document.getElementsByClassName("content")[1].innerText = "Hello, JavaScript";
    }

    useEffect(()=>{ 
        init();
    }, []);

    // window.onload = function() {
    //      init();
    // }

    return (
        <>
        <p class="content">getElementsByClassName() 메서드1</p>
        <p class="content">getElementsByClassName() 메서드2</p>
        <hr></hr>
        </>
    )
}

export default _0102_class
