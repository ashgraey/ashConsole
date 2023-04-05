import React from 'react'

function _0601_조건문1() {
  let Flag = true;

    function getFlag(Flag){
        if(Flag){
            return "참입니다.";
        }else{
            return "거짓입니다."
        }
    }

    return (
      <>
          <div>{getFlag(Flag)}</div>
      </>
    )
}

export default _0601_조건문1
