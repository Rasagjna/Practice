import React, { useEffect, useRef, useState } from 'react'

function useRefHook() {
    const [name,setName] = useState('')
    // const [renderCount, setRenderCount] = useState(0)
    const renderCount = useRef(0) // {current:0}
    const inputRef = useRef()
    const prevName = useRef('')
    useEffect(()=>{
      prevName.current = name
    },[name])

    useEffect(()=>{
        // setRenderCount(prevRenderzcount => prevRenderzcount+1)
        renderCount.current = renderCount.current+1
    })
    function focus() {
        // console.log(inputRef.current)
        inputRef.current.focus()
        inputRef.current.value = 'some value'
        appendChild

    }
  return (
    <>
    <input ref ={inputRef} value = {name} onChange={e=> setName(e.target.value)}/>
    <div> My name is {name} and it is used to be {prevName}</div>
    {/* <div>I rendered {renderCount.current} times</div> */}
    <button onClick={focus}>Focus</button>
    </>
  )
}

export default useRefHook
// Huge red flag with this is that, initially when the component renders setRenderCount state is set.
// This causes the useEffect to run again, causing the state to set again. And this loop continues infinitely.
// Thus we need to use Refs -> persists between renders.
//  Refs doesnot cause your component to update when changed. 
// completely outside coponent lifecycle
// biggest use case is:
// REFERENCE ELEMENTS INSIDE HTML
// PREV VALUE OF STATE****** PERSISTING VALUES ACROSS RENDERS WITHOUT ACTUALLY CAUSING RERENDER

