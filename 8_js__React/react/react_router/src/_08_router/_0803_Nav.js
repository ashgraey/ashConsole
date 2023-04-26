import React from 'react'
import { Link } from 'react-router-dom'

function _0803_Nav() {

  return (
    <>

    <h3>로그 = {window.sessionStorage.getItem("log")}</h3>
      <div className="container bg-light">
          <div className="">
              <div className="d-flex justify-content-center justify-content-xl-center">
                  <div className="">
                      <div className="">
                       {window.sessionStorage.getItem("log") === "null" || window.sessionStorage.getItem("log") === null? 

                        <ul className="nav">
                          <li className="nav-link"><Link to="/" className="nav-item">메인화면</Link></li>
                          <li className="nav-link"><Link to="/join" className="nav-item">회원가입</Link></li>
                          <li className="nav-link"><Link to="/login" className="nav-item">로그인</Link></li>
                        </ul>
                       : 
                          <ul className="nav">
                            <li className="nav-link"><Link to="/" className="nav-item">메인화면</Link></li>
                            <li className="nav-link"><Link to="/list" className="nav-item">회원목록</Link></li>
                            <li className="nav-link"><Link to="/logout" className="nav-item">로그아웃</Link></li>
                          </ul>
                       }
                      </div>
                  </div>
              </div>
          </div>
      </div>
    </>
  )
}

export default _0803_Nav
