// Toggle between showing and hidding the navigation menu links when the user clicks on the hamburger / bar icon

function myFunction(){
    var x = document.getElementById("myLinks");
    if (x.style.display === "block"){
        x.style.display = "none";
    }else{
        x.style.display = "block";
    }
}
