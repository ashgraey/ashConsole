import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useLocation } from 'react-router'
import { useNavigate } from 'react-router';

import _0802_Header from "./_0802_Header"
import _0803_Nav from "./_0803_Nav"
import _0804_Footer from "./_0804_Footer"

function MemberInfo() {

    const location = useLocation();
    const navigate = useNavigate();

    const [member, setMember] = useState({});
    const [memberPw, setMemberPw] = useState("");
    const [memberName, setMemberName] = useState("");

    useEffect(() => {
        let id = location.state.id;
        let params = {
            id: id
        }
        axios.get(`http://localhost:3001/memberJson`, { params
      
    }).then((res) => {
        setMember(res.data[0]);
    }).catch(e => {
        console.log(e);
    })
      }, []);


      let onSubmit = (e) => {
        // form 페이지 이동 막기
        e.preventDefault();

        let id = location.state.id;
        axios.patch(`http://localhost:3001/memberJson/${id}`, {
            
            memberPw: memberPw,
            memberName: memberName

        }).then((res) => {
            alert("회원정보가 수정되었습니다.");

            navigate("/list")
        })
        .catch((e) => {
            console.log(e);
        });
    }


  return  (
    <>
      <_0802_Header></_0802_Header>
      <_0803_Nav></_0803_Nav>

      <div className="container" >
            <div className="row py-4 mb-2">
                <div className="text-center" > 
                    <h3 ><b>회원정보 수정</b></h3>
                </div>
            </div>
        </div>

        <div className="container" >
            <div className="row justify-content-xl-center">
                <div className="col-12 col-xl-4">
                    <div className="d-flex justify-content-center">
                        <form>
                            <label className="mt-4" style={{
                                fontSize: "15px",
                                color: "rgba(117, 117, 117, 0.973)",
                                fontWeight: "500"
                            }}>아이디</label>
                            <div className="input-group mt-2" >
                                <input type="text" className="form-control" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                
                                value={member.memberId || ""} readOnly>
                                </input>
                            </div>

                            <label className="mt-4" style={{
                                fontSize: "15px",
                                color: "rgba(117, 117, 117, 0.973)",
                                fontWeight: "500"
                            }}>비밀번호</label>
                            <div className="input-group mt-2" >
                                <input type="text" className="form-control" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                
                                value={member.memberPw || ""}
                                onChange={(e) => {
                                    setMemberPw(e.target.value);
                                    member.memberPw = e.target.value;
                                }}>
                                </input>
                            </div>

                            <label className="mt-4" style={{
                                fontSize: "15px",
                                color: "rgba(117, 117, 117, 0.973)",
                                fontWeight: "500"
                            }}>이름</label>
                            <div className="input-group mt-2" >
                                <input type="text" className="form-control" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                
                                value={member.memberName || ""}
                                onChange={(e) => {
                                    setMemberName(e.target.value);
                                    member.memberName = e.target.value;
                                }}>
                                </input>
                            </div>

                            <button className="w-100 btn btn-primary btn-lg mt-3 py-3" onClick={onSubmit}>회원정보 수정</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>


      <_0804_Footer></_0804_Footer>

   
    </>
  )
}

export default MemberInfo
