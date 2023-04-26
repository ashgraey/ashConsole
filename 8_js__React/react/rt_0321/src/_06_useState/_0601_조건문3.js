import React from 'react'

function _0601_조건문3() {
    let select =  Math.floor(Math.random() * 3);

    function getFlag(){
      console.log(select);
      if(select == 0){
          return "선택0";
      }else if(select == 1){
          return "선택1"
      }else{
          return "선택2";
      }
  }

  return (
    <>
        <div>{getFlag()}</div>
    </>
  )
}

export default _0601_조건문3
