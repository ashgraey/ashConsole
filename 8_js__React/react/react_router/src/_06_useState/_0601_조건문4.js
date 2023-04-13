import React from 'react'

function _0601_조건문4() {
    let select =  Math.floor(Math.random() * 3);

 

  return (
    <>
        <div>{select == 0 ?  "선택0" : (select == 1 ? "선택1" : "선택2")}</div>
    </>
  )
}

export default _0601_조건문4
