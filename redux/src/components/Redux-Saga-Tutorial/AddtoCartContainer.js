import React, { useEffect } from 'react'
import { addToCart, emptyCart, removeFromCart } from '../redux-saga/action'
import {useDispatch, useSelector} from 'react-redux';
import { productList } from '../redux-saga/productAction';
function AddtoCartContainer() {
    const dispatch = useDispatch();
    let data = useSelector((state)=>state.productData);
    console.log("data in main component",data)

    const product = {
        name:"i phone",
        category:"mobile",
        price: 1000,
        color:"red"
    }
    useEffect(()=>{
      dispatch(productList())
    },[])
  return (
    <div>
   <div><button onClick={()=> dispatch(addToCart(product))}> Add to cart</button></div>
   <div><button onClick={()=> dispatch(removeFromCart(product.name))}> Remove from cart</button></div>
   <div><button onClick={()=> dispatch(emptyCart())}> Empty cart</button></div>
   {/* <div><button onClick={()=> dispatch(productList())}> Call product List</button></div> */}
   <div className='product-container'>
    {
      data.map((item)=> <div className="product-item">
      <h1>{item.title}</h1>
      <h1>{item.id}</h1>
      <button onClick={()=> dispatch(addToCart(product))}>add to cart</button>
      <button>remove from cart</button>
      </div>
      )
    }
  </div> 
  </div>
 
 

  )
}

export default AddtoCartContainer