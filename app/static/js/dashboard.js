const activePage = window.location.pathname;
const linksSideBar = document.querySelectorAll(".sideMenu__link");

linksSideBar.forEach(link=>{
    let regex = /\/[a-zA-Z]+\//g;
    let url = activePage.match(regex)

    if(link.href.includes(`${url}`) || link.href.includes(`${activePage}`)){
        link.classList.add('sideMenu__link--active')
    }
})

const linksInteriores = document.querySelectorAll(".dashBlog__links a");

linksInteriores.forEach(link=>{
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active')
    }
})

const links2Interiores = document.querySelectorAll(".dashNotices__links a");

links2Interiores.forEach(link=>{
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active')
    }
})

const links3Interiores = document.querySelectorAll(".dashFixture__links a");

links3Interiores.forEach(link=>{
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active')
    }
})