
// comment-box
function myFunction(whatever) {
    var x = document.getElementById(whatever);
    // whatever.addEventListener("click", x); 
    console.log(x)
    if (x.style.display === "none") {
        x.style.display = "block";
        console.log('it works??')
    } else {
        x.style.display = "none"
    }
    console.log('here')
}



//SOLVED - HEART BUTTON

function toggleColor(element){
    var btn = document.getElementById("btnh1");
    element.addEventListener("click", btn); 
    if (element.style.color == "red"){
        element.style.color = "grey";
        console.log('pleasework')
    }
    else {
        element.style.color = "red";
    }
    console.log("besweettome")


}




//SOLVED - HEART BUTTON

function toggleColor(element){
    var btn = document.getElementById("btnh1");
    element.addEventListener("click", btn); 
    if (element.style.color == "red"){
        element.style.color = "grey";
        console.log('pleasework')
    }
    else {
        element.style.color = "red";
    }
    console.log("besweet")


}



// function Toggle2(i){
//     var btn = document.getElementsByClassName("btn");
//     var btn_r = (btn.style.color == "grey"); 
//     i.classList.toggle("red"); 
// }

// function Toggle2(i){
//     var btn = document.getElementById("btnh1"); 
//     var btn_g = btn.style.color == "grey";
//     var btn_r = btn.style.color =="red";
//     if ( btn_r === false){
//         i.classList.toggle(btn_g);
//         console.log('grey')
//     } else {
//         i.classList.toggle(btn_r); 
//         console.log('red')
//     }
//     console.log('workng?')
// }