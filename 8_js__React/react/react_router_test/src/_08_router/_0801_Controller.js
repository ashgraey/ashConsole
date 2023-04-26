import React from 'react'
import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Main from './Main';
import MemberLoginForm from './MemberLoginForm';

function _0801_Controller() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Main></Main>}></Route>
                    <Route path="/login" element={<MemberLoginForm></MemberLoginForm>}></Route>
                    {/* 
                <Route path="/join" element={<MemberJoinForm></MemberJoinForm>}></Route>
                <Route path="/list" element={<MemberList></MemberList>}></Route>
                <Route path="/info" element={<MemberInfo></MemberInfo>}></Route>
                <Route path="/logout" element={<MemberLogout></MemberLogout>}></Route>
                 */}
                </Routes>
            </BrowserRouter>


        </>
    )
}

export default _0801_Controller