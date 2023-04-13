import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
import {useState} from 'react'

function _0609_select_useState() {

      const mySelect = useRef();
      let [Result, setResult] = useState(0);
      function selectSub(){
          let select = mySelect.current.value;
          if (select == "1"){
            setResult("HTML")
          }else if(select == "2"){
            setResult("CSS")
          }else if(select == "3"){
            setResult("JavaScript")
          }else{
            setResult("");
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
            <p id="selected">선택한 과목 : {Result}</p>
        </div>
      )
}

export default _0609_select_useState
