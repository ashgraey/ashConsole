import React from 'react'
import "./_0406_종합.css"
function _0406_종합() {

    function addReply() {

        // table을 변수로 저장
        let list = document.querySelector("#list");

        // input창에 사용자가 입력한 값을 가지고 온다.
        let value = document.querySelector("#reply").value;
        // 사용자가 입력하지 않고 버튼을 눌렀을 때에 대한 예외처리
        if(value == "") {
            alert("댓글을 입력해주세요.");

            // 함수 강제 종료
            return;
        }

        let tr = document.createElement("tr");
        
        // 답글 추가하기
        let td = document.createElement("td");
        td.setAttribute("class", "_0406replyList");
        // td.classList = "replyList";
        td.innerText = value;
        tr.append(td);

        // 삭제 버튼 추가하기
        td = document.createElement("td");
        let delSpan = document.createElement("span");
        delSpan.innerText = "X";
        delSpan.setAttribute("class", "_0406removeList");
        delSpan.addEventListener("click", delReply);
        td.append(delSpan);
        tr.append(td);

        list.append(tr);

        document.querySelector("#reply").value = "";
        document.querySelector("#reply").focus();
    }

    function delReply() {
        // table을 가지고 옴
        let list = document.querySelector("#list");

        let removeList = document.querySelectorAll("._0406removeList");
        for(let i=0; i<removeList.length; i++) {
            if(this == removeList[i]) {
                // table의 자식 요소(tr)
                list.children[i].remove();
            }
        }
    }

    return (
    <>
        <table>
            <tr>
                <td>
                    댓글 <input id="reply" type="text"></input>
                    <button onClick={addReply}>등록</button>
                </td>
            </tr>
        </table>

        <table id="list">
        </table>

    </>
  )
}

export default _0406_종합
