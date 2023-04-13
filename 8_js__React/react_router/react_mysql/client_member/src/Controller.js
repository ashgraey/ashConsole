import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import PageMain from './page/PageMain';
import PageMemberLoginForm from './page/PageMemberLoginForm';
import PageMemberList from './page/PageMemberList';
import PageLogout from './page/PageLogout';
import PageMemberInfo from './page/PageMemberInfo';
import PageDeleteMember from './page/PageDeleteMember';
import PageMemberJoinForm from './page/PageMemberJoinForm';

function Controller() {
  return (
    <>
      <BrowserRouter>
          <Routes>
              <Route path="/" element={<PageMain></PageMain>}></Route>
              <Route path="/loginForm" element={<PageMemberLoginForm></PageMemberLoginForm>}></Route>
              <Route path="/list" element={<PageMemberList></PageMemberList>}></Route>
              <Route path="/logout" element={<PageLogout></PageLogout>}></Route>
              <Route path="/info" element={<PageMemberInfo></PageMemberInfo>}></Route>
              <Route path="/delete" element={<PageDeleteMember></PageDeleteMember>}></Route>
              <Route path="/joinForm" element={<PageMemberJoinForm></PageMemberJoinForm>}></Route>
          </Routes>
      </BrowserRouter>
    </>
  )
}

export default Controller
