// var display = document.querySelectorAll("p");
// let btn = document.querySelectorAll("button");

// function hide(){
//     for (let i = 0; i < display.length; i++)
//     display[i].classList.add("display_hidden");
// }
// function show(){
//     for (let i = 0; i < display.length; i++)
//     display[i].classList.remove("display_hidden");
// }
// function toggle(){
//     for (let i = 0; i < display.length; i++)
//     display[i].classList.toggle("display_hidden")
// }
// function background(){
//     let back = document.querySelector("html");
//     back.classList.toggle("bg")
// }
// function test(){
//     const i = document.getElementById("head");
//     i.innerHTML = "This Heading is now Changed!";
// }
// function modButton(){
//     for (let j = 0; j < btn.length; j++)
//     btn[j].classList.toggle("btn")
//     for (let i = 0; i < btn.length; i++)
//     btn[i].classList.toggle("btn-primary")

// }
// function customBtn(){
//     for (let i = 0; i < btn.length; i++)
//     btn[i].classList.toggle("customButton")
// }
// function hideButton(){
//     for (let i = 0; i < btn.length; i++)
//     btn[i].classList.toggle("display_hidden");
// }
let counter = document.getElementById("counter");
let num = 0;

const add = () => {
    let i = document.getElementById("add");
    num ++;
    counter.innerHTML = num;
    console.log(num);
}

const subtract = () => {
    let i = document.getElementById("subtract");
    num --;
    counter.innerHTML = num;
    console.log(num);
}