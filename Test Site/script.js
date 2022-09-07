var display = document.querySelectorAll("p");

function hide(){
    for (let i = 0; i < display.length; i++)
    display[i].classList.add("display_hidden");
}
function show(){
    for (let i = 0; i < display.length; i++)
    display[i].classList.remove("display_hidden");
}
function toggle(){
    for (let i = 0; i < display.length; i++)
    display[i].classList.toggle("display_hidden")
}
function background(){
    let back = document.querySelector("html");
    back.classList.toggle("bg")
}
function test(){
    const i = document.getElementById("head");
    i.innerHTML = "This Heading is now Changed!";
    alert("TEST")
}
