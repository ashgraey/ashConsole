import React from 'react';
import ReactDOM from 'react-dom/client';

 /* 확장자명 .js만 생략가능 다른 확장자는 생략불가능하다 [예] .css */ 
import _0101_id from './_01_useEffect/_0101_id';
import _0102_class from './_01_useEffect/_0102_class';
import _0103_name from './_01_useEffect/_0103_name';
import _0104_tag from './_01_useEffect/_0104_tag';
import _0105_querySelector from './_01_useEffect/_0105_querySelector';
import _0106_querySelectorAll from './_01_useEffect/_0106_querySelectorAll';
import _0107_innerText1 from './_01_useEffect/_0107_innerText1';
import _0107_innerText2 from './_01_useEffect/_0107_innerText2';
import _0108_innerHTML1 from './_01_useEffect/_0108_innerHTML1';
import _0108_innerHTML2 from './_01_useEffect/_0108_innerHTML2';
import _0109_value1 from './_01_useEffect/_0109_value1';
import _0110_value2 from './_01_useEffect/_0110_value2';

import _0201_id from './_02_style/_0201_id';
import _0202_class from './_02_style/_0202_class';
import _0202_classStyle from './_02_style/_0202_classStyle';
import _0203_tag from './_02_style/_0203_tag';
import _0203_tagStyle from './_02_style/_0203_tagStyle';
import _0204_name from './_02_style/_0204_name';
import _0205_querySelector from './_02_style/_0205_querySelector';
import _0206_querySelectorAll from './_02_style/_0206_querySelectorAll';
import _0207_textContent from './_02_style/_0207_textContent';
import _0208_image from './_02_style/_0208_image';
import _0209_table from './_02_style/_0209_table';
import _0210_member from './_02_style/_0210_member';

import _0301_이벤트추가1 from './_03_useRef/_0301_이벤트추가1';
import _0301_이벤트추가2 from './_03_useRef/_0301_이벤트추가2';
import _0301_이벤트추가3 from './_03_useRef/_0301_이벤트추가3';
import _0301_이벤트추가4 from './_03_useRef/_0301_이벤트추가4';
import _0302_onblur from './_03_useRef/_0302_onblur';
import _0303_onchange from './_03_useRef/_0303_onchange';
import _0304_onfocus from './_03_useRef/_0304_onfocus';
import _0305_oninput1 from './_03_useRef/_0305_oninput1';
import _0305_oninput2 from './_03_useRef/_0305_oninput2';
import _0306_onkeydown from './_03_useRef/_0306_onkeydown';
import _0306_onkeyup from './_03_useRef/_0306_onkeyup';
import _0307_onclick1 from './_03_useRef/_0307_onclick1';
import _0307_onclick2 from './_03_useRef/_0307_onclick2';
import _0307_onclick3 from './_03_useRef/_0307_onclick3';
import _0307_onclick4 from './_03_useRef/_0307_onclick4';
import _0307_onclick5 from './_03_useRef/_0307_onclick5';
import _0308_this from './_03_useRef/_0308_this';
import _0309_cart from './_03_useRef/_0309_cart';
import _0310_light from './_03_useRef/_0310_light';
import _0311_list from './_03_useRef/_0311_list';
import _0312_mouse from './_03_useRef/_0312_mouse';
import _0313_checkbox_ref from './_03_useRef/_0313_checkbox_ref';

import _0302_onblur_ref from './_03_useRef/_0302_onblur_ref';
import _0303_onchange_ref from './_03_useRef/_0303_onchange_ref';
import _0304_onfocus_ref from './_03_useRef/_0304_onfocus_ref';
import _0305_oninput1_ref from './_03_useRef/_0305_oninput1_ref';
import _0305_oninput2_ref from './_03_useRef/_0305_oninput2_ref';
import _0306_onkeydown_ref from './_03_useRef/_0306_onkeydown_ref';
import _0306_onkeyup_ref from './_03_useRef/_0306_onkeyup_ref';
import _0307_onclick1_ref from './_03_useRef/_0307_onclick1_ref';
import _0307_onclick2_ref from './_03_useRef/_0307_onclick2_ref';
import _0307_onclick3_ref from './_03_useRef/_0307_onclick3_ref';
import _0307_onclick4_ref from './_03_useRef/_0307_onclick4_ref';
import _0307_onclick5_ref from './_03_useRef/_0307_onclick5_ref';
import _0308_this_ref from './_03_useRef/_0308_this_ref';
import _0309_cart_ref from './_03_useRef/_0309_cart_ref';
import _0310_light_ref from './_03_useRef/_0310_light_ref';
import _0311_list_ref from './_03_useRef/_0311_list_ref';
import _0312_mouse_ref from './_03_useRef/_0312_mouse_ref';

import _0401_추가_appendChild from './_04_태그생성/_0401_추가_appendChild';
import _0402_추가_append from './_04_태그생성/_0402_추가_append';
import _0403_추가_append from './_04_태그생성/_0403_추가_append';
import _0404_삭제_removeChild from './_04_태그생성/_0404_삭제_removeChild';
import _0405_자식선택_children from './_04_태그생성/_0405_자식선택_children';
import _0406_종합 from './_04_태그생성/_0406_종합';
import _0406_종합_ref from './_04_태그생성/_0406_종합_ref';

import _0501_interval1 from './_05_비동기/_0501_interval1';
import _0502_timeout1 from './_05_비동기/_0502_timeout1';

import _0601_조건문1 from './_06_useState/_0601_조건문1';
import _0601_조건문2 from './_06_useState/_0601_조건문2';
import _0601_조건문3 from './_06_useState/_0601_조건문3';
import _0601_조건문4 from './_06_useState/_0601_조건문4';
import _0601_조건문5 from './_06_useState/_0601_조건문5';
import _0602_useState from './_06_useState/_0602_useState';
import _0603_useRef와useState from './_06_useState/_0603_useRef와useState';
import _0604_Array from './_06_useState/_0604_Array';
import _0605_버튼익명함수 from './_06_useState/_0605_버튼익명함수';
import _0606_삼항연산자 from './_06_useState/_0606_삼항연산자';
import _0607_리스트 from './_06_useState/_0607_리스트';
import _0608_select_useRef from './_06_useState/_0608_select_useRef';
import _0609_select_useState from './_06_useState/_0609_select_useState';
import _0610_gugu from './_06_useState/_0610_gugu';
import _0611_끝말잇기 from './_06_useState/_0611_끝말잇기';

import _0701_노드한개그리기 from './_07_table/_0701_노드한개그리기';
import _0702_노드배열그리기 from './_07_table/_0702_노드배열그리기';
import _0703_노드2차원배열그리기 from './_07_table/_0703_노드2차원배열그리기';

/*
[npm install react-router-dom@6]
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
*/

import _0801_Controller from './_08_router/_0801_Controller';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(

  <React.Fragment>
    <_0801_Controller></_0801_Controller>
  </React.Fragment>

);


  /*
    [리액트 에서 태그 그리는 방법]
      [1] import React from 'react';
      [2]  <React.Fragment></React.Fragment> 사이에 태그작성 
  */

  /*
    [예외1] 태그가 한개일경우는   <React.Fragment></React.Fragment>  를 생략할수있다.    
    [예시] 
      <div>안녕</div>
  */

  /*
    [예외2] <React.Fragment> 는 <> </> 으로 변경가능 
    [예시]
    <>
      <div>안녕</div>
      <div>하이</div>
    </>
  */

  /*
    [기본함수 단축생성]
      rcfe 이후 enter 
  */

  /*
    [리액트 jsx 문법]
      기존의 html 에서의 단일태그는 더이상 사용할수없다.
      <input></input> 반드시 쌍태그로 작성해야한다. 
      <input/> 이와같이 축약할수는 있으나 본예제에서는 헷갈리지않도록 쌍태그만 사용한다. 
  */


