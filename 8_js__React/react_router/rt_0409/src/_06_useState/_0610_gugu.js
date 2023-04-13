import React from 'react'
import {useEffect} from 'react'
import {useRef} from 'react'
import {useState} from 'react'

function _0610_gugu() {
    
    const [first, setFirst] = useState(Math.ceil(Math.random() * 9));
    const [second, setSecond] = useState(Math.ceil(Math.random() * 9));
    const [value, setValue] = useState('');
    const inputNumber = useRef(null);

  return (
    <>
      <div style={{ textAlign:"center"}}>
        <div>{first} 곱하기 {second}는 ?</div>
        <br></br>
        <input type="text" ref={inputNumber} value={value} onChange={(e) => setValue(e.target.value)}></input>
        <br></br>
        <br></br>
        <button onClick={(e) =>{   
            let result = first * second;
            if(result == value){
                alert("정답");
            }else{
                alert("오답")
            }
            setValue("");
            setFirst(Math.ceil(Math.random() * 9));
            setSecond(Math.ceil(Math.random() * 9));
            inputNumber.current.focus();
        }}>입력</button>
      </div>
    </>
  )
}

export default _0610_gugu
