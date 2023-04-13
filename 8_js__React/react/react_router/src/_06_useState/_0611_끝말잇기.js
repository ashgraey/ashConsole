import React from 'react'
import {useState} from 'react'
import {useRef} from 'react'

function _0611_끝말잇기() {
    const [word, setWord] = useState('거미');
    const [value, setValue] = useState('');
    const [result, setResult] = useState('');
    const inputText = useRef(null);

  return (
    <>
      <div>{word}</div>
        <input
          ref={inputText}
          value={value}
          onChange={(e) => setValue(e.currentTarget.value)}
        />
        <button onClick={(e) => {
            if (word[word.length - 1] === value[0]) {
                setResult('정답');
                setWord(value);
                setValue('');
                inputText.current.focus();
                } else {
                setResult('오답');
                setValue('');
                inputText.current.focus();
                }
        }}>입력!</button>
      <div>{result}</div>
    </>
  )
}

export default _0611_끝말잇기
