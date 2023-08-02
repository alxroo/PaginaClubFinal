const contentBlog = document.querySelector(".dashBlog__links")
const divBlog = document.querySelectorAll("#pestañaBlog")
const linksBlog = document.querySelectorAll(".dashBlog__links button")

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
            guardar = parseInt(e.target.id)    
            
        }
    })
}

activarPestañas(contentBlog,divBlog,linksBlog)
