import React, { useState } from 'react'

function Main() {

  // ****USESTATE HOOK ****// 
    const [count,setCount] = useState(()=>{console.log("only on first render"); return 4 }) // when state changes component rerenders
    // when there is complex, slow computation intially, then alwayts use functional state as it only renders once.
    const [state,setState] = useState({count:4,theme: "red"}) 
    const count1 = state.count
    const theme = state.theme
    
    function decrementCount() {
        setCount(prevCount => prevCount-1)
        // completely overrides the old state. to update the state spread out the previous state and then update

        // setState(prevState =>{
        //   return {count:prevState.count-1}
        // })
      // ****************************************************************
        setCount(prevState=>{
          return {...prevState,count:prevState-1}
        })
    }
    function incrementCount(){
        setCount(prevCount => prevCount+1)
    }
  return (
    <div><button onClick={incrementCount}> + </button>
    {/* <span>{count}</span> */}
    <span>{count1}</span>
    <span>{theme}</span>
    <button onClick={decrementCount}> - </button>
    </div>
  )
}

export default Main