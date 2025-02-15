import React, { useState,useEffect } from 'react'

function UseEffectHook() {
    const [resourceType,setResourceType] = useState('posts')
    const [items,setItems] = useState([])
    const [windowWWidth,setWindowwidth] = useState(window.innerWidth)
    useEffect(()=>{
        fetch(`https://jsonplaceholder.typicode.com/${resourceType}`)
        .then(response => response.json())
        .then(json => setItems(json))
        // console.log('render')
    },[resourceType]) // dependency array -> whatever the values passed insdie the array,
    // whenevr they change, the hook is going to run.
    //empty means that, on mount.
    const handleResize =()=>
    {
        setWindowwidth(window.innerWidth)
    }
useEffect(()=>{
    window.addEventListener('resize',handleResize)

    // clean up whatever we did last time. Fist return is run.
    return() => {
        window.removeEventListener('resize',handleResize)
    }
},[])

  return (
    <>
     {/* <div>
    <button onClick={()=> setResourceType('posts')}>Posts</button>
    <button onClick={()=> setResourceType('users')}>Users</button>
    <button onClick={()=> setResourceType('comments')}>Comments</button>
   </div>
   <h1>{resourceType}</h1>
   {items.map(item =>{
    return <pre>{JSON.stringify(item)} </pre>
   })} */}

   <div>
{windowWWidth}
   </div>
    </>
  
  )
}

export default UseEffectHook