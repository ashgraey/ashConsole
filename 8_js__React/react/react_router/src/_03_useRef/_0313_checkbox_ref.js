import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
function _0313_checkbox_ref() {
    const checkList = useRef([]);
    const checkAll = useRef(null);

    function init(){
        for(let i=0; i<checkList.current.length; i++) {
            checkList.current[i].addEventListener("click", checkValue);
        }

        checkAll.current.addEventListener("click" , checkValueAll);
    }


    function checkValueAll(){
        if (checkAll.current.checked == true){
            for(let i=0; i<checkList.current.length; i++) {           
                checkList.current[i].checked = true;  
            }
        }else{
            for(let i=0; i<checkList.current.length; i++) {
                checkList.current[i].checked = false;               
            }
        }
    }

    function checkValue() {
        let count = 0;
        for(let i=0; i<checkList.current.length; i++) {
            if(checkList.current[i].checked) {
                count += 1;
            }
        }

        if(count == checkList.current.length) {
            checkAll.current.checked = true;
        } else {
            checkAll.current.checked = false;
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);


    return (
        <>
            <input type="checkbox" ref={checkAll} />전체선택 <br />

            <input type="checkbox" className="subject" ref={(e) => checkList.current[0] = e} ></input>수학
            <input type="checkbox" className="subject" ref={(e) => checkList.current[1] = e} />영어
            <input type="checkbox" className="subject" ref={(e) => checkList.current[2] = e} />국어
        </>
    )
}

export default _0313_checkbox_ref
