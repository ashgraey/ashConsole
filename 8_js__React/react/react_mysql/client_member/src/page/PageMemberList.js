import React from 'react'
import Header from '../layout/Header';
import Nav from '../layout/Nav';

import { useState } from "react";
import { useEffect } from 'react';
import axios from "axios";
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router';

function PageMemberList() {

  const navigate = useNavigate();
  const [memberJson, setMemberJson] = useState([]);

  useEffect(() => {
    axios
    .post("/memberListPro")
    .then((res) => {
      setMemberJson(res.data);
    })
    .catch((e) => {
      console.log(e);
    });
  }, []);

  let deleteMember = (value) => {
    console.log("value = " + value);
    navigate("/delete", {state: value});
  }

  return (
    <>
        <Header></Header>
        <Nav></Nav>
        <div className="d-flex justify-content-center">
        <div className="table-responsive">
          <table className="table table-bordered">
            <thead>
              <tr>
                <th>번호</th>
                <th>아이디</th>
                <th>비밀번호</th>
                <th>이름</th>  
                <th>삭제</th>
              </tr>
            </thead> 
            <tbody>
              {memberJson.map((v , i) =>{
                  return (
                  <tr key={i}>
                    <td>{i+1}</td>
                    <td>
                      <Link to="/info" state={{id:v.memberId}}>{v.memberId}</Link>
                    </td>
                    <td>{v.memberPw}</td>
                    <td>{v.memberName}</td>
                    <td>
                      <button className="btn btn-secondary" name={v.id}
                      onClick={(e )=> {deleteMember(v.memberId)}}>삭제</button>
                    </td>
                  </tr>
                  )
              })} 
            </tbody>           
          </table>
        </div>
      </div>
        
    </>
  )
}

export default PageMemberList
