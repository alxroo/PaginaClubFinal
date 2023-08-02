const btnDelBlog = document.querySelectorAll('#btnBlogDelete')
const activePageUrl = window.location.pathname;

btnDelBlog.forEach(boton =>{
  boton.addEventListener('click',(e)=>{
    const atributo = boton.getAttribute('data-Atributo')
    e.preventDefault()
    Swal.fire({
      title: '¿Estas seguro de eliminar registro?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        if(activePageUrl=='/dashNotice/seeNotice'){
          location.href = `/dashNotice/deleteNotice/${atributo}`;
        }
        if(activePageUrl=='/dashBlog/seeBlog'){
          location.href = `/dashBlog/deleteBlog/${atributo}`;
        }
        if(activePageUrl=='/dashFixture/addTeam'){
          location.href = `/dashFixture/deleteTeam/${atributo}`;
        }
        if(activePageUrl=='/dashFixture/versus'){
          location.href = `/dashFixture/deleteVersus/${atributo}`;
        }
      }
    })

  })
})