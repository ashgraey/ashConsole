import React ,{useState} from 'react'
function _0607_리스트() {
    const [Content , setContent] = useState("");
    const [ContentList , setContentList] = useState([]);

    const onSubmit = () => {
        let arr = [...ContentList]
        arr.push(Content);
        setContentList([...arr]);
        setContent("");
    }

    return (
        < >    
            <input type="text" value={Content} onChange={(event) =>{
                    console.log(event.currentTarget.value);
                    setContent(event.currentTarget.value);

                }
            }></input>

            <button
                onClick={()=>{
                    onSubmit();
                    
                }}
            >제출</button>

            {ContentList.map((v , i) =>{
                return (<div key={i}>{i + 1} : {v}</div>)
            })}

        </>
    )
}

export default _0607_리스트
