import React, { useEffect } from 'react'
import { useNavigate } from 'react-router';
function PageLogout() {
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

export default PageLogout
