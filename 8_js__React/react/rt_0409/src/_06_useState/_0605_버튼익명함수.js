import React ,{useState} from 'react'

function _0605_버튼익명함수() {
    const [Arr2 , setArr2] = useState([100,200,300]);

    return (
        <>     
            <h2>{Arr2}</h2>

            <button onClick={()=>{
                let arr = [];
                arr = [...Arr2];
                arr.push(400);
                setArr2([...arr])
            }}>배열증가2</button>
             <hr></hr>

           
            {Arr2.map((v , i) =>{
                return <p key={i}>{v}</p>
            })}

            <hr></hr>


        </>
    )
}

export default _0605_버튼익명함수
