import React, { useEffect, useState } from 'react'

function UseMemoHook() {
    const [number,setNumber] = useState(0)
    const [dark,setDark] = useState(false)
    //performance and memory overheads. Its saving the prev value in memory. Thus memory overhead.
    // UseMemo func is called each time the component rerenders. - performace overhead.
    // use case -> referential equality.
    const doubleNumber = useMemo(() => { return slowFunction(number)},[number])
    const themeStyles = useMemo(()=>{
        return {
            backgroundColor : dark? 'black':'white',
            colr:dark? 'white':'black'
        }
    },[dark])
    // {
    //     backgroundColor : dark? 'black':'white',
    //     colr:dark? 'white':'black'
    // }
    useEffect(()=>{
console.log('theme changed')
    },[themeStyles])
//  referential equality -> everytime thw component rerenders, 
// the new themestyle object gets created. The new theme style object is not same as the old theme style object eventhough they have exact same values
// they are at diff locations in memory. ***********
// 
  return (
   
    <>
    <input type="number" value ={number} onChange={e => setNumber(parseInt(
        e.target.value
    ))}/>
    <button onClick={()=>setDark(prevDark => !prevDark)}>Change Theme</button>
    <div style={themeStyles}>{doubleNumber}</div>
    </>
  )
}

function slowFunction(num){
    console.log('calling slow function')
    for(let i=0;i<=1000000000; i++){}
    return num*2
}

export default UseMemoHook
// Whenever the component rerenders because of state change or because of other component,
// the slow function is called each time, making it very slow and increasng the loading time.
// To avoid this, useMemo is used which is basically a caching mechanism.
// The function inside useMemo() runs only when there is change in the value inside dependency array simialr to useEffect.
//