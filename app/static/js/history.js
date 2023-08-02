//// Boton Menu //////////////
(function(){
    let more = document.querySelectorAll('.article__link');

    for(let i=0; i<more.length; i++){
        more[i].addEventListener('click',()=>{
            more[i].parentNode.classList.toggle('active')
            console.log("clicko")
        })
    }
    
    
    let btnHistory = document.querySelector('.history__btn');
    const btnCloseHistory = document.querySelector('.history__btnClose')
    const historyParagraphs = document.querySelector('.history__principal')
    const main = document.querySelector('.body')
    
    
    btnHistory.addEventListener('click',()=>{
        historyParagraphs.style.display = 'flex';
        main.classList.add('bodyHidden');
    })
    btnCloseHistory.addEventListener('click',()=>{
        historyParagraphs.style.display = 'none';
        main.classList.remove('bodyHidden');
    })
           
})();