//script
const d = new Date();
let day = d.getDay();


function show(){
var element = document.getElementsByClassName('elem');
console.log(element);
element[day].style.display = 'block';
}