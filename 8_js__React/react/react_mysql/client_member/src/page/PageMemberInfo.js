import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useLocation } from 'react-router'
import { useNavigate } from 'react-router';

import Header from '../layout/Header';
import Nav from '../layout/Nav';

function PageMemberInfo() {

    const location = useLocation();
    const navigate = useNavigate();

    const [member, setMember] = useState({});
    const [memberPw, setMemberPw] = useState("");
    const [memberName, setMemberName] = useState("");

    useEffect(() => {
        let memberId = location.state.id;
       // console.log(location.state.id);
       
        let body = {
        memberId: memberId,
        };

        axios
        .post("/memberInfoPro" , body)
        .then((res) => {
        setMember(res.data[0]);
        })
        .catch((e) => {
        console.log(e);
        });

       
    }, []);

    let onSubmit = (e) => {
        // form 페이지 이동 막기
        e.preventDefault();

        let memberId = location.state.id;
       
        let body = {
            memberId: memberId,
            memberPw: member.memberPw,
            memberName : member.memberName
        };

        console.log(memberId);
        console.log(member.memberPw);
        console.log(member.memberName);

        axios
        .post("/memberUpdatePro" , body)
        .then((res) => {
            alert("정보를 수정했습니다.");
            navigate("/list");
        })
        .catch((e) => {
        console.log(e);
        });

    }

  return (
    <>
    <Header></Header>
    <Nav></Nav>

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
    </>
  )
}

export default PageMemberInfo
