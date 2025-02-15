import React, { useEffect, useState } from 'react'

function List({getitems}) {
    const [items,setItems] = useState([])
    useEffect(()=>{
    setItems(getitems())
    console.log('updating items')
    },[getitems])
  return (
    items.map(item => <div key = {item}> {item}</div>)
  )
}

export default List