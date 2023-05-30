let edit_btns = document.querySelectorAll('.edit-btn')
let edit_area = document.querySelector('.story')

edit_btns.forEach((btn)=>{
    btn.addEventListener('click', ()=>{
        edit_area.disabled = false
    })
})