import { ADD_TO_CART, EMPTY_CART, PRODUCT_LIST, REMOVE_FROM_CART, SET_PRODUCT_LIST } from "./constants"

export const productData = (data=[],action)=>{
    // console.warn("reducer called")
    // if(action.type === ADD_TO_CART)
    // {
    //  return data   
    // } else{
    //     return "no action called"
    // }
    // return 100
    switch(action.type){
        // case PRODUCT_LIST:
        //     console.log("PRODUCT LIST condition",action)
        //     return [action.data,...data]
        case SET_PRODUCT_LIST:
            console.log("PRODUCT LIST condition",action)
            return [...action.data]

        default:
            return data
    }
}