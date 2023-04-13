import React , {useState} from 'react' // , 를 사용해 여러개의 내용을 한줄로 import 할수있다. 
/*
    [useState 로 배열사용법]

    [useState 배열 출력법]
*/
function _0604_Array() {

    const [Arr1 , setArr1] = useState([10,20,30]);
    const [Arr2 , setArr2] = useState([100,200,300]);

    function arrAdd1(number){
        Arr1.push(number);
        console.log(Arr1);
        setArr1(Arr1);
    }

    function arrAdd2(number){
        let arr = [];
        arr = [...Arr2];
        arr.push(400);
        setArr2([...arr])
    }


    return (
        <>

            <button onClick={(e) => {arrAdd1(40)}}>배열증가1</button>
            <h2>{Arr1}</h2>

             <hr></hr>


            <button onClick={(e) => {arrAdd2(400)}}>배열증가2</button>
            <h2>{Arr2}</h2>
            <hr></hr>


            <h2>반복문사용법(map)</h2>
            {Arr2.map((v , i) =>{
                return <p key={i}>{v}</p>
            })}

            <hr></hr>


        </>
    )
}

export default _0604_Array
