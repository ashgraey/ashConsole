import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'

import _0802_Header from "./_0802_Header"
import _0803_Nav from "./_0803_Nav"
import _0804_Footer from "./_0804_Footer"

function MemberList() {

    const [memberJson, setMemberJson] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:3001/memberJson`, {
      
    }).then((res) => {
        setMemberJson(res.data);
    }).catch(e => {
    
    })
      }, []);

    let deleteMember = (e) => {

      axios.delete(`http://localhost:3001/memberJson/${e.target.name}`, {

      }).then((res) => {
          alert("회원정보가 삭제되었습니다.");
          window.location.reload();
      })
      .catch((e) => {
          console.log(e);
      });


    }

  return  (
    <>
      <_0802_Header></_0802_Header>
      <_0803_Nav></_0803_Nav>
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
                      <Link to="/info" state={{id:v.id}}>{v.memberId}</Link>
                    </td>
                    <td>{v.memberPw}</td>
                    <td>{v.memberName}</td>
                    <td>
                      <button className="btn btn-secondary" name={v.id} onClick={deleteMember}>삭제</button>
                    </td>
                  </tr>
                  )
              })} 

              
            </tbody>           
          </table>
        </div>
      </div>
      <_0804_Footer></_0804_Footer>

   
    </>
  )
}

export default MemberList
