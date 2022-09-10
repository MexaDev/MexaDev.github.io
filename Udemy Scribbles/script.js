const first = () => {
    const greet = 'Hi';
    const second = () => {
        alert(greet);
    }
    return second;
}

function first(){
    var greet = 'Hi';
    function second(){
        alert(greet);
    }
    return second;
}

const newFunc = first();
newFunc();