const pars = document.querySelectorAll("p")
function hide(){
    var display = document.getElementById("demo");
    display.classList.add("display_hidden");
}
function show(){
    var display = document.getElementById("demo");
    display.classList.remove("display_hidden");
}
console.log(pars)