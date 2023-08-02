const activePage = window.location.pathname;

const navbarLinks = document.querySelectorAll(".header__navLinks .navLink");

navbarLinks.forEach(link=>{

        if(link.href.includes(`${activePage}`)){
            if(activePage != "/"){
                link.classList.add('navLink--active')
            }else{
                navbarLinks[0].classList.add('navLink--active')
            }
        }


        
    
})