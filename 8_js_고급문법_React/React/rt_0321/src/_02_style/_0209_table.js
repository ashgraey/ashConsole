import React from 'react'

/*
    [리엑트에서 table]
        [1] 기존html 과 달리 tbody , thead , tfoot 등의 태그를 사용하지않으면 경고가 뜨지만 무시해도된다.

        [2] colspan 이나 rowspan 이 카멜식으로 변경되었다. 
            [예시] colSpan , rowSpan
*/

function _0209_table() {
  return (
    <>
       <h3>회원가입</h3>
            <table border="1">
                <tr>
                    <td>아이디</td>
                    <td><input id="data-id"></input></td>
                </tr>
                <tr>
                    <td>비밀번호</td>
                    <td><input id="data-pw"></input></td>
                </tr>
                <tr>
                    <td colSpan="2"><button id="btn-joinPro">회원가입</button></td>
                </tr>
            </table>

        <br></br>
        <button id="btn-mainPage">메인메뉴</button>
    </>
  )
}

export default _0209_table
