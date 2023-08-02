//////////////////////////////////////////////
// Boton cerrar MsgAlerts
(function(){
    const btnClose = document.querySelector(".msgAlert__close")
    const alertMsg = document.querySelector(".msgAlert");

    if(btnClose != null){
        btnClose.addEventListener("click",()=>{
            alertMsg.classList.add("active")
        })
    }
    
           
})();