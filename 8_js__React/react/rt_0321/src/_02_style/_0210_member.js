import React from 'react'
import {useEffect} from 'react'
import "./_0210_member.css"

function _0210_member() {
  return (
    <>
            <div id="join">
                <br></br><br></br>
                <font size="5" color="#3a3a3a"><b>회원가입</b></font>
                <hr width="300px" color="#196ab3"></hr>
                <br></br><br></br>

                <table>
                    <tr>
                        <td className="first">아이디</td>
                        <td className="second">
                            <input type="text" className="inputForm" id="data-memberId" placeholder="아이디를 입력해주세요." autoFocus="autofocus"></input>
                        </td>
                    </tr>
                    <tr>
                        <td className="first">비밀번호</td>
                        <td className="second">
                            <input type="password" className="inputForm" id="data-memberPw" placeholder="비밀번호를 입력해주세요"></input>
                        </td>
                    </tr>
                    <tr>
                        <td className="first">이름</td>
                        <td className="second">
                            <input type="text" className="inputForm" id="data-memberName" placeholder="이름을 입력해주세요"></input>
                        </td>
                    </tr>
                    <tr>
                        <td className="first">이메일</td>
                        <td className="second">
                            <input type="text" className="inputForm" id="data-memberEmail" placeholder="예:hong@itbook.com"></input>
                        </td>
                    </tr>
                    <tr height="150px">
                        <td colSpan="2" align="center">
                            <input type="image" id="btn-joinPro"src={"_0208_join.jpg"} ></input>
                        </td>
                    </tr>
                </table>
            </div>
    </>
  )
}

export default _0210_member
