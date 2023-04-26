import React from 'react'
import {useRef} from 'react'
import {useState} from 'react'

function _0603_useRef와useState() {

    let number1 = 1;
    let NumberIncrease1 = () => {
        number1 += 1;
        console.log(number1);
    };

    const num2_ref = useRef(null);
    let NumberIncrease2 = () => {
        let num = Number(num2_ref.current.innerText);
        num2_ref.current.innerText = num + 1;
    };

    const [Num3 , setNum3] = useState(3);
    let NumberIncrease3 = () => {
        setNum3(Num3 + 1)
    };
    return (
    <>
        <hr></hr>
        <div>{number1}</div>
        <button onClick={NumberIncrease1}>Submit</button>
        
        <hr></hr>
        <div ref={num2_ref}>2</div>
        <button onClick={NumberIncrease2}>Submit</button>

        <hr></hr>
        <div >{Num3}</div>
        <button onClick={NumberIncrease3}>Submit</button>
    </>
    
  );
}

export default _0603_useRef와useState
