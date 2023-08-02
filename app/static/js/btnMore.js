let more = document.querySelectorAll('.article__link');

for(let i=0; i<more.length; i++){
    more[i].addEventListener('click',()=>{
        more[i].parentNode.classList.toggle('active')
    })
}