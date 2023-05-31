let edit_btns = document.querySelectorAll('.edit-btn')
let edit_area = document.querySelector('.story')
let form = $("#form-2");

edit_btns.forEach((btn)=>{
    btn.addEventListener('click', ()=>{
        edit_area.disabled = false
    })
})

$( document ).ready(() => {
    // function will get executed 
    // on click of submit button
    $("#add-chap-btn").click(function(ev) {
        ev.preventDefault();
        var form = $("#form-2");
        var url = '/create/stage2'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data) {
                  
                // Ajax call completed successfully
                alert("Form Submited Successfully");
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
            }
        });
    });
});