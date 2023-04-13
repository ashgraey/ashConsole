import React from 'react'
import {useEffect} from 'react'

/*  
    <input> 은 사용불가능하다 반드시 쌍태그를 사용해야한다.
*/

function _0204_name() {
    function init(){
        let list = document.getElementsByName("subject");
        
        // 체크박스 체크로 변경
        for(let i=1; i<list.length; i++) {
            list[i].checked = true;
        }
    }
   
    useEffect(()=>{ 
        init();
    }, []);

    return (
        <>
            <h3 id="target">과목 선택</h3>
            HTML<input type="checkbox" name="subject" value="html"></input>
            CSS<input type="checkbox" name="subject" value="css"></input>
            JavaScript<input type="checkbox" name="subject" value="javascript"></input>
        </>
    )
}

export default _0204_name
