let a = document.querySelector(".wrap2").style.display = "none"

let container = document.querySelector('.wrap2');
function show(ele1, ele2, display1, display2){
    document.querySelector(".wrap2").style.display = "block";
    document.querySelector(ele1).style.display = display1;
    document.querySelector(ele2).style.display = display2;
    
}
document.querySelector("#one").onclick = function(e){
    e.preventDefault()
    document.querySelector("#p1").src = 'design_resources/user-icon.svg';
    document.querySelector("#lockIcon").src = 'design_resources/lock-icon.svg';
    document.querySelector('#one').style.borderBottomColor = 'hsla(358, 97%, 31%, 1)';
    document.querySelector('#three').style.borderBottomColor = 'grey';
    show(".container", ".container2", "block", "none")
}
document.querySelector("#three").onclick = function(e){
    e.preventDefault()
    document.querySelector("#p1").src = 'design_resources/Vector (1).svg';
    document.querySelector("#lockIcon").src = 'design_resources/Vectorlock.png';
    document.querySelector('#three').style.borderBottomColor = 'hsla(358, 97%, 31%, 1)';
    document.querySelector('#one').style.borderBottomColor = 'grey';
    show(".container", ".container2", "none", "block")
    let pas = document.querySelector("#newPass");
    let pas1 = document.querySelector("#oldPass");
    let pas2 = document.querySelector("#newPass2");
    let but = document.querySelector("#butt")
    but.onclick = function(e){
        e.preventDefault();
        let old = 'okay' //pass old account here
        if (pas1.value == old){
            if (pas.value.length >= 8 && pas2.value.length >= 8){
                if (pas.value == pas2.value){
                    alert("password changed successfully.");
                    old = pas.value; //update the database
                }
                else{
                    alert("password doesn't match. Try again")
                }
            }
            else{
                alert("Password must be greater that 8")
            }
        }
        else{
            alert("Invalid password")
        }
    }
}