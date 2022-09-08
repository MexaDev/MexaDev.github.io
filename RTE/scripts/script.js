
var i;
//Check day of the week
function dayOfTheWeek(){
    switch (new Date().getDay()){
        case 0:
            day = "sunday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 1:
            day = "monday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 2:
            day = "tuesday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 3:
            day = "wednesday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 4:
            day = "thursday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 5:
            day = "friday";
            i = document.getElementById(day);
            i.classList.add("highLight")
            break;
          case 6:
            day = "saturday";
            i = document.getElementById(day);
            i.classList.add("highLight")
    }
    
}
