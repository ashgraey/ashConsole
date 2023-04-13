import _0802_Header from "./_0802_Header"
import _0803_Nav from "./_0803_Nav"
import _0804_Footer from "./_0804_Footer"

import { useState } from "react";
import { useRef } from 'react'
import axios from "axios";
import { useNavigate } from 'react-router';

function MemberJoinForm() {

    const navigate = useNavigate();

    let [memberId, setMemberId] = useState("");
    let [memberPw, setMemberPw] = useState("");
    let [memberName, setMemberName] = useState("");
    let [msgIdState, setMsgIdState] = useState("");
    let [msgPwState, setMsgPwState] = useState("");
    let [msgPw2State, setMsgPw2State] = useState("");
    let [msgNametate, setMsgNameState] = useState("");
    let [idCheck, setIdcheck] = useState(false);
    let [idButtonPush, setIdButtonPush] = useState(false);


    const memberIdRef = useRef(null);
    const memberPwRef = useRef(null);
    const memberPw2Ref = useRef(null);
    const memberNameRef = useRef(null);
    const checkAllRef = useRef(null);
    const checkListRef = useRef([]);


    let onSubmit = (e) => {
        // form 페이지 이동 막기
        e.preventDefault();

        console.log(idButtonPush);
        if(idButtonPush == false) {
            alert("아이디 중복확인을 해주세요.");
            return;
        }
        if(checkAllRef.current.checked == false) {
            alert("약관 전체동의가 필요합니다.");
            return;
        }

        axios.post('http://localhost:3001/memberJson', {
            
            memberId: memberId,
            memberPw: memberPw,
            memberName: memberName

        }).then((res) => {
            alert("회원가입을 축하합니다.");

            navigate("/login")
        })
        .catch((e) => {
            console.log(e);
        });
    }


    // 아이디 유효성 검사
    let getOnChangeInputId = (e) => {
        setMemberId(e.target.value);

        let userIdCheck = RegExp(/^[A-Za-z0-9_\-]{6,20}$/); // 영어 숫자 조합 6~20글자 
        if(userIdCheck.test(memberIdRef.current.value)) {
            setMsgIdState("");
            setIdcheck(true);

        } else {
            let msgId = "6자리 이상의 영문 혹은 숫자를 조합";
            setMsgIdState(msgId);
            setIdcheck(false);
        }

        setIdButtonPush(false);
    }

    // 아이디 중복검사
    let checkId = (e) => {
        // form 페이지 이동 막기
        e.preventDefault();

        // 아이디 유효성
        if(idCheck == false) {
            alert("6자리 이상의 영문 혹은 숫자를 조합");
            memberIdRef.current.value = "";
            memberIdRef.current.focus();
            return;
        }

        let params = {
            memberId: memberIdRef.current.value
        }

        axios.get(`http://localhost:3001/memberJson`,{params})
        .then((res) => {
            console.log(res.data);

            if(res.data.length == 0) {
                alert("사용할 수 있는 아이디입니다.");
                setIdButtonPush(true);
                memberPwRef.current.focus();
            } else {
                alert("아이디가 중복됩니다.");
                setIdButtonPush(false);
                memberIdRef.current.value = "";
                memberIdRef.current.focus();
            }
        })
        .catch((e) => {
            console.log(e);
        });
    }

    // 비밀번호 유효성 검사
    let getOnChangeInputPw = (e) => {
        setMemberPw(e.target.value);

        let passwdCheck = RegExp(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^*()\-_=+\\\|\[\]{};:\'",.<>\/?]).{8,16}$/);
        if(passwdCheck.test(memberPwRef.current.value)) {
            setMsgPwState("");
        } else {
            let msgPw = "영문 대문자와 소문자, 숫자, 특수문자를 하나 이상 포함하여 8~16자 조합";
            setMsgPwState(msgPw);
        }
    }

    // 비밀번호 재입력 유효성 검사
    let getOnChangeInputPwCheck = (e) => {
        if(memberPwRef.current.value == memberPw2Ref.current.value) {
            setMsgPw2State("");
        } else {
            let msgPw2 = "동일한 비밀번호를 입력해주세요.";
            setMsgPw2State(msgPw2);
        }
    }

    // 이름 유효성 검사
    let getOnChangeInputName = (e) => {
        setMemberName(e.target.value);

        let nameCheck = RegExp(/^[가-힣]{2,6}$/);
        if(nameCheck.test(memberNameRef.current.value)) {
            setMsgNameState("");
        } else {
            let msgName = "2~6글자의 한글만 입력";
            setMsgNameState(msgName);
        }
    }

    // 전체 체크박스
    let checkAll = (e) => {
        if(checkAllRef.current.checked == true) {
            for(let i=0; i<checkListRef.current.length; i++) {           
                checkListRef.current[i].checked = true;  
            }
        } else {
            for(let i=0; i<checkListRef.current.length; i++) {
                checkListRef.current[i].checked = false;               
            }
        }
    }

    // 체크박스 검사
    let checkValue = (e) => {
        let count = 0;
        for(let i=0; i<checkListRef.current.length; i++) {
            if(checkListRef.current[i].checked) {
                count += 1;
            }
        }

        if(count == checkListRef.current.length) {
            checkAllRef.current.checked = true;
        } else {
            checkAllRef.current.checked = false;
        }
    }

    return (
        <>
        <_0802_Header></_0802_Header>
        <_0803_Nav></_0803_Nav>

         <div className="container" >
            <div className="row py-4 mb-2">
                <div className="text-center" > 
                    <h3 ><b>회원가입</b></h3>
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
                                <input type="text" className="form-control" placeholder="아이디를 입력하세요" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                ref={memberIdRef}
                                onChange={getOnChangeInputId}>
                                </input>
                                <button className="btn btn-secondary" onClick={checkId}>중복확인</button>
                            </div>
                            <div style={{
                                width: "480px",
                                color: "#B3130B",
                                fontSize: "12px"
                            }}>{msgIdState}</div>

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
                                onChange={getOnChangeInputPw}>
                                </input>
                            </div>
                            <div style={{
                                width: "480px",
                                color: "#B3130B",
                                fontSize: "12px"
                            }}>{msgPwState}</div>

                            <label className="mt-4" style={{
                                fontSize: "15px",
                                color: "rgba(117, 117, 117, 0.973)",
                                fontWeight: "500"
                            }}>비밀번호 확인</label>
                            <div className="input-group mt-2">
                                <input type="text" className="form-control" placeholder="비밀번호를 입력하세요" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                ref={memberPw2Ref}
                                onChange={getOnChangeInputPwCheck}>
                                </input>
                            </div>
                            <div style={{
                                width: "480px",
                                color: "#B3130B",
                                fontSize: "12px"
                            }}>{msgPw2State}</div>

                            <label className="mt-4" style={{
                                fontSize: "15px",
                                color: "rgba(117, 117, 117, 0.973)",
                                fontWeight: "500"
                            }}>이름</label>
                            <div className="input-group mt-2">
                                <input type="text" className="form-control" placeholder="이름을 입력하세요" style={{
                                    height: "40px",
                                    width: "250px",
                                    fontSize: "15px"
                                }}
                                ref={memberNameRef}
                                onChange={getOnChangeInputName}>
                                </input>
                            </div>
                            <div style={{
                                width: "480px",
                                color: "#B3130B",
                                fontSize: "12px"
                            }}>{msgNametate}</div>

                            <div className="form-check py-3">
                                <label className="form-check-label">
                                    <input className="form-check-input" type="checkbox" 
                                    ref={checkAllRef}
                                    onClick={checkAll}>
                                    </input>
                                전체동의</label>
                            </div>

                            <ul className="list-group">
                                <li className="list-group-item py-3">
                                    <input type="checkbox" className="form-check-input me-1" ref={(e) => checkListRef.current[0] = e} onClick={checkValue}></input>
                                    <label style={{
                                        fontSize: "15px",
                                        color: "rgba(0, 0, 0, 0.973)",
                                        fontWeight: "500"
                                    }}>이용약관 동의</label>
                                </li>
                                <li className="list-group-item py-3">
                                    <input type="checkbox" className="form-check-input me-1" ref={(e) => checkListRef.current[1] = e} onClick={checkValue}></input>개인정보취급 동의
                                </li>
                                <li className="list-group-item py-3">
                                    <input type="checkbox" className="form-check-input me-1" ref={(e) => checkListRef.current[2] = e} onClick={checkValue}></input>만14세 입니다.
                                </li>
                            </ul>

                            <button className="w-100 btn btn-primary btn-lg mt-3 py-3" onClick={onSubmit}>가입</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <_0804_Footer></_0804_Footer>
        </>
    )
}

export default MemberJoinForm
