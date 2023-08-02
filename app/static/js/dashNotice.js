const contentNotice = document.querySelector(".dashNotices__links")
const divNotices = document.querySelectorAll("#pestaña")
const linksNotice = document.querySelectorAll(".dashNotices__links button")

function activarPestañas(contenedor,pestañasDiv,linksBtn){
    contenedor.addEventListener("click",(e)=>{
        if(e.target.tagName == 'BUTTON'){
            pestañasDiv.forEach(pestaña=>{
                pestaña.classList.remove('active')
            })
            linksBtn.forEach(link=>{
                link.classList.remove('active')
            })
            pestañasDiv[parseInt(e.target.id)].classList.add("active")
            linksBtn[parseInt(e.target.id)].classList.add("active")    
        }
    })
}

activarPestañas(contentNotice,divNotices,linksNotice)
