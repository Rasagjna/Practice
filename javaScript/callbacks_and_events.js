function attachEventListeners()
{
    let count = 0;
    document.getElementById("clickeMe").addEventListener("click",function xyz(){
        console.log("button clicked", ++count)
    })
}
attachEventListeners()


// why it is important to remove even listeners.
// 
