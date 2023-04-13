import React, { useEffect } from 'react'
import { useNavigate } from 'react-router';

function MemberLogout() {

    const navigate = useNavigate();

    useEffect(() => {
        window.sessionStorage.setItem("log", null);
        navigate("/")
      }, []);

  return (
    <>
      
    </>
  )
}

export default MemberLogout
