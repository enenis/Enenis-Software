let menu=document.querySelector("#menu-icon")
let navbar=document.querySelector(".navbar")

menu.addEventListener("click",function() {
    navbar.classList.toggle("active")
})


window.onscroll= () => {
    navbar.classList.remove("active")
}


function SendMail(){
    var params={
        from_name : document.getElementById("fullName").value,
        email_id : document.getElementById("email_id").value,
        message : document.getElementById("message").value
    }
    emailjs.send("service_6e6vlup","template_kd02p4d",params).then(function(res){
        alert("Success! " + res.status);
    });
}


function reloadPage()
 {
  window.location.reload()
 }