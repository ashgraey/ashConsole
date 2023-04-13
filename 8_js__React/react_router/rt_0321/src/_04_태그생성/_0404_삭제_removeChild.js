import React from 'react'
import {useRef} from 'react'
function _0404_삭제_removeChild() {


    const p1 = useRef();
    const target = useRef();

    function removeAllFunction() {
        let parent = target.current;
        parent.remove();
    }

    function removeChildFunction() {
        let parent = target.current;
        let child = p1.current;
        let delNode = parent.removeChild(child);

        console.log(delNode);
    }

    return (
        <>
        <div ref={target}>
            <p ref={p1}>첫번째 단락</p>
            <p >두번째 단락</p>
        </div>
        <button onClick={removeAllFunction}>removeAll()</button>
        <button onClick={removeChildFunction}>removeChild()</button>
        </>
  )
}

export default _0404_삭제_removeChild
