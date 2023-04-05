import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'

function _0608_select_useRef() {

      const mySelect = useRef();
      const result = useRef();
      function selectSub(){
          let select = mySelect.current.value;
          if (select == "0"){
            result.current.innerHTML = "선택한 과목 : "
          }else if (select == "1"){
            result.current.innerHTML = "선택한 과목 : HTML"
          }else if(select == "2"){
            result.current.innerHTML = "선택한 과목 : CSS"
          }else if(select == "3"){
            result.current.innerHTML = "선택한 과목 : JavaScript"
          }
      }

      function init(){
        selectSub();
      }
    
      useEffect(()=>{ 
          init();
      }, []);

      return (
        <div>
            <h4>과목을 선택하세요.</h4>
            <select ref={mySelect} onChange={selectSub}>
                <option value="0">과목</option>
                <option value="1">HTML</option>
                <option value="2">CSS</option>
                <option value="3">JavaScript</option>
            </select>
            <p ref={result}>선택한 과목 : </p>
        </div>
      )
}

export default _0608_select_useRef
