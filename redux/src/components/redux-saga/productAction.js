import { PRODUCT_LIST } from "./constants"

export const productList = () =>{
    // let data = "hello, How are you"
    // let data = await fetch('https://jsonplaceholder.typicode.com/todos/1')
    // .then(response => response.json())
    // .then(json => console.log(json))
    // console.warn("PRODUCT action is called",data)
    return {
        type:PRODUCT_LIST,
        // data: "apple"
    }
}