import { ADD_TO_CART, EMPTY_CART, REMOVE_FROM_CART } from "./constants"

export const cartData = (data=[],action)=>{
    // console.warn("reducer called")
    // if(action.type === ADD_TO_CART)
    // {
    //  return data   
    // } else{
    //     return "no action called"
    // }
    // return 100
    switch(action.type){
        case ADD_TO_CART:
            console.log("ADD_TO_CART condition",action)
            return [action.data,...data]

        case REMOVE_FROM_CART:
            console.log("REMOVE_FROM_CART  condition",action)
            data.length = data.length? data.length-1: []
            return [...data]

        case EMPTY_CART:
            console.log("EMPTY CART CONSOLE",action)
            data= []
            return [...data]
        default:
            return data
    }
}