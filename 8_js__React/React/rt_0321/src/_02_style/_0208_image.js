import React from 'react'
/*
    [리엑트 에서 이미지 적용방법]
        이미지 파일은 public 폴더에 위치시킨후 , 파일이름을 적용하면된다.
    [예시]    
        <input type="image" id="btn-joinPro"src={"_0208_join.jpg"} ></input>   
*/

function _0208_image() {
  return (
    <>
      <input type="image" id="btn-joinPro"src={"_0208_join.jpg"}  ></input>
      <hr></hr>
      <input type="image" id="btn-joinPro"src={"_0208_join.jpg"} width="200px" ></input>
    </>
  )
}

export default _0208_image
