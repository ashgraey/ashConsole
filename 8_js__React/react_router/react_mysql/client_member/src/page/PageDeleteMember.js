import React from 'react';
import { useEffect } from 'react';
import { useLocation } from 'react-router';
import { useNavigate } from 'react-router';
import axios from "axios";

function PageDeleteMember() {

  const navigate = useNavigate();
  const location = useLocation();
  
  useEffect(() => {
    // console.log(location.state);

    let body = {
      memberId: location.state
    }

    axios
    .post("/deletePro", body)
    .then((res) => {
      alert("회원정보가 삭제되었습니다.");
      navigate("/list");
    })
    .catch((e) => {
      console.log(e);
    });


  }, []);


  return (
    <>
      
    </>
  )
}

export default PageDeleteMember
