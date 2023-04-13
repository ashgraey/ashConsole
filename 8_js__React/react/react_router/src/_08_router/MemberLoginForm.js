import React from 'react'
import _0802_Header from './_0802_Header'
import _0803_Nav from './_0803_Nav'
import _0804_Footer from './_0804_Footer'

import { useState } from "react";
import { useRef } from 'react'
import axios from "axios";
import { useNavigate } from 'react-router';

function MemberLoginForm() {

  const navigate = useNavigate();

  let [memberId, setMemberId] = useState("");
  let [memberPw, setMemberPw] = useState("");

  const memberIdRef = useRef(null);
  const memberPwRef = useRef(null);

  let onSubmit = (e) => {
    // form 페이지 이동 막기
    e.preventDefault();

    let params = {
      memberId: memberId,
      memberPw: memberPw
    }

    axios.get('http://localhost:3001/memberJson', 
    {params}
    ).then((res) => {
        console.log(memberId);
        console.log(memberPw);

        console.log(res.data);
        if(res.data.length == 0) {
          alert("아이디와 비밀번호를 확인해주세요.");
        } else {
          alert("로그인 성공!");
          window.sessionStorage.setItem("log", memberId);
          navigate("/list")
        }

    })
    .catch((e) => {
        console.log(e);
    });
}

  return (
    <>
        <_0802_Header></_0802_Header>
        <_0803_Nav></_0803_Nav>    
          <div className="container" >
              <div className="row py-4 mb-2">
                  <div className="text-center" > 
                      <h3 ><b>로그인</b></h3>
                  </div>
              </div>
          </div>

          <div className="container">
            <div className="row justify-content-xl-center">
                <div className="col-12 col-xl-4">
                    <div className="d-flex justify-content-center">
                      <form>
                        <label className="mt-4" style={{
                          fontSize: "15px",
                          color: "rgba(117, 117, 117, 0.973)",
                          fontWeight: "500"
                          }}>아이디</label>

                          <div className="input-group mt-2">
                            <input type="text" className="form-control" placeholder="비밀번호를 입력하세요" style={{
                                height: "40px",
                                width: "250px",
                                fontSize: "15px"
                            }}
                            ref={memberIdRef}
                            onChange={e => {setMemberId(e.target.value)}}>
                            </input>
                          </div>

                        <label className="mt-4" style={{
                          fontSize: "15px",
                          color: "rgba(117, 117, 117, 0.973)",
                          fontWeight: "500"
                          }}>비밀번호</label>

                          <div className="input-group mt-2">
                            <input type="text" className="form-control" placeholder="비밀번호를 입력하세요" style={{
                                height: "40px",
                                width: "250px",
                                fontSize: "15px"
                            }}
                            ref={memberPwRef}
                            onChange={e => {setMemberPw(e.target.value)}}>
                            </input>
                          </div> 

                          <button className="w-100 btn btn-primary btn-lg mt-3 py-3" onClick={onSubmit}>로그인</button>
                      </form>
                    </div>
                </div>
            </div>
          </div>

        <_0804_Footer></_0804_Footer>
    </>
  )
}

export default MemberLoginForm
