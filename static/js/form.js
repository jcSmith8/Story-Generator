let edit_btns = document.querySelectorAll('.edit-btn')
let edit_area = document.querySelector('.story')
const container = document.querySelector(".container");
const cardTemplate = document.getElementById("card-template");
let form = $("#form-2");
console.log("loading scripts ...")
console.log($('#overlay-btn'))

edit_btns.forEach((btn)=>{
    btn.addEventListener('click', ()=>{
        edit_area.disabled = false
    })
})

$( document ).ready(() => {
    // function will get executed 
    // on click of submit button
    $("#add-chap-btn").click(function(ev) {
        $('#add-chap-btn').attr("disabled", true);
        ev.preventDefault();
        let url = '/create/stage2'
        $.ajax({
            type: "POST",
            url: url,
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({chapter:true}),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('#add-chap-btn').attr("disabled", false);
                window.location.reload();
            },
            error: function(data) {
                  
                // Some error in ajax call
                //alert("some Error");
                $('#add-chap-btn').attr("disabled", false);
            }
        });
    });
    $("#create-btn").click(function(ev) {
        $('#create-btn').attr("disabled", true);
        //ev.preventDefault();
        $('#skeleton-container').css("display", "block");
        $('#create-form').css("display", "none");
        let form = $("#form-create");
        let url = '/create/stage2'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(response) {
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
               
                $('#create-btn').attr("disabled", false);
                console.log(response)
                window.location.href = url
                
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#create-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });
    $('#overlay-btn').attr("disabled", true);
});

// the selector will match all input controls of type :checkbox
    // and attach a click event handler 
    $(document).on('click', 'input[type="checkbox"]', function() {      
        $('input[type="checkbox"]').not(this).prop('checked', false);   
        $('#overlay-btn').attr("disabled", false);
    });

    $("#overlay-btn").click(function(ev) {
        //ev.preventDefault();
        $('#overlay-btn').attr("disabled", true);
        let form = $("#form-2");
        let url = '/create/stage4';
        let overlay_music = $("input:checkbox:checked").val();
        console.log("music overlay: "+ overlay_music)
        $.ajax({
            type: "POST",
            url: url,
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({overlay:overlay_music}),
            success: function(data) {
                  
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                window.location.href = 'stage4'
                $('#overlay-btn').attr("disabled", false);
            },
            error: function(data) {
                  
                // Some error in ajax call
                //alert("some Error");
                $('#overlay-btn').attr("disabled", false);
            }
        });
    });