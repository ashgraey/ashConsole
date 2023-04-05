import React from 'react'
import {useEffect} from 'react'
function _0601_조건문5() {
    let select =  Math.floor(Math.random() * 3);

    function init(){
      console.log(select);
    }
   
    useEffect(()=>{ 
        init();
    }, []);



    return (
      <>
          <div>
            {select == 0 && "선택0"} 
            {select == 1 && "선택1"} 
            {select == 2 && "선택2"}
          </div>
      </>
    )
}

export default _0601_조건문5
