import React ,{useState} from 'react'
function _0606_삼항연산자() {
    const [Temp , setTemp] = useState(false);
    return (
        <div >      
            {Temp ? <h1>Temp</h1>: null}
            <button
                onClick={()=>{
                    setTemp(!Temp);
                }}
            >
                클릭
            </button>
        </div>
    )
}

export default _0606_삼항연산자
