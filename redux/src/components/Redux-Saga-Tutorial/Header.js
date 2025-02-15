import { useSelector } from "react-redux"

export const Header = ()=>{
    const result = useSelector((state)=>state.cartData);
    console.log("data in header",result);
return(
    <div className="header">
        <div className="cart-div">
            <span>{result.length}</span>
            <img src="https://pngimg.com/uploads/shopping_cart/shopping_cart_PNG38.png"></img>
        </div>

    </div>
)
}