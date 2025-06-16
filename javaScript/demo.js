let arr = ["a","b","c"]
arr.forEach((val,idx,arr)=>{
    console.log(val.toUpperCase(),idx,arr)
})
//OR
const uppercase = (val,idx,arr)=>{
    console.log(val.toUpperCase(),idx,arr)
}

arr.forEach(uppercase)

// higherorder functions are the functions which take the functions as the argumentd,or return the functions.

// MAP - creates a new array unlike for each
// the value the callback returns are used to form new array.

let nums = [67, 52, 39]
nums.map((val)=> console.log(val)
)

let newArr = nums.map((val) => val*val)
console.log(newArr) // new arary create..

// filter -> condition: true (stores in new array)

let arr1 = [1,2,3,4,5,6,7]
let evenArr= arr1.filter((num)=>{
    return num%2 == 0
})
console.log(arr1, evenArr)

// performs some operation and reduces the array to a single value. It returns the single value.
const output = arr1.reduce((res,curr) => {
    return res+curr
}, 10) // give initial value. 
console.log(output)

const output1 = arr1.reduce((prev,curr) => {
    return prev > curr ? prev:curr;
},0) // largest element in the array.


// DOM - DOCUMENT OBJECT MODEL
// window object is created by the browser automatically. It is browser's object not javascript's object.
// it is global object with lots of properties and methods.

// window.console.log()
// all the elements in the html are converted into a object called document.
 
// window.document - model. representation of html
// tree like structure
// each node is an object


console.log(document)
console.dir(document.body,document.title)
// dynamic changes/manipulation 

 // link the script tag at the bottom of the body
 //HTML COLLECTION - getElementsByClass

 // null -when there is no such id, and empty html collection when there is no such class.

 // getElementById, getElementsByClass, getElementsByTagName

 // querySelector - can pass id,class or tagname 
 // let firstEl = document.querySelector("p") : myClass
 // let allEl = document.querySelectorAll("p") 
// let allEl = document.querySelector(".myclass")

// properties

/*

tagName: return tag for element nodes
innerText: pure text
innerHTMl : HTML+text 
textContent : gives text content even for the hidden elements.

*/

let newBtn = document.createElement("button")
newBtn.innerText = "click me"
console.log(newBtn)

/*
For example if you want to add button at the end of li 
<div>
<ul>
<li> </li>
<li> </li>
<li> </li>
</ul>
</div>
*/

let div = document.querySelector("div")
div.append(newBtn) // added at last.
div.prepend(newBtn) // at beginning

div.before(newBtn); // before the div
div.after(newBtn); // after the div

let newHeading = document.createElement("h1");
newHeading.innerHTML = "<i>Hi, Iam new! </i>"

document.querySelector("body").prepend(newHeading)

let para = document.querySelector("p");
para.classList.add("newClass")
para.remove();

// the change in the state of a object is known as an event.
// inline event handling - writing within the tags.
 
let btn1 = document.querySelector("div");
//priority given to the javascript rsther than inline event handling.
div.onmouseover=(e)=>{
    // we can access the event object with an argument.
    console.log("here")
}

// EVENT LISTENERS

// addEventListener(event,callback)
const handler3 = (event)=>{
    console.log("button 1 was clicked - 3")
}
btn1.addEventListener("click",()=>{
    console.log("button 1 was clicked")
})

btn1.addEventListener("click",(event)=>{
    console.log("button 1 was clicked - 2")
})

btn1.addEventListener("click", handler3)

btn1.addEventListener("click",(event)=>{
    console.log("button 1 was clicked - 4")
})

btn1.removeEventListener("click",handler3);

