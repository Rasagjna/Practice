import { ADD_TO_CART, EMPTY_CART, REMOVE_FROM_CART } from "./constants"

export const addToCart = (data) =>{
    console.warn("action is called",data)
    return {
        type:ADD_TO_CART,
        data
    }
}

export const removeFromCart = (data) => {
    console.log("inside remove to cart",data)
    return {
        type: REMOVE_FROM_CART,
        data:data
    }
}

export const emptyCart = () => {
    console.log("inside remove to cart")
    return {
        type: EMPTY_CART,
       
    }
}