let edit_btns = document.querySelectorAll('.edit-btn')
let edit_area = document.querySelector('.story')
let form = $("#form-2");
console.log("loading scripts ...")
console.log($("#overlay-btn"))

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
                location.reload();
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
            },
            error: function(data) {
                  
                // Some error in ajax call
                //alert("some Error");
            }
        });
    });

});

// the selector will match all input controls of type :checkbox
    // and attach a click event handler 
    $("input:checkbox").on('click', function() {
        // in the handler, 'this' refers to the box clicked on
        var $box = $(this);
        if ($box.is(":checked")) {
        // the name of the box is retrieved using the .attr() method
        // as it is assumed and expected to be immutable
        var group = "input:checkbox[name='" + $box.attr("name") + "']";
        // the checked state of the group/box on the other hand will change
        // and the current value is retrieved using .prop() method
            $(group).prop("checked", false);
        $box.prop("checked", true);
        } else {
            $box.prop("checked", false);
        }
    });

    $("#overlay-btn").click(function(ev) {
        ev.preventDefault();
        let form = $("#form-2");
        let url = '/create/stage3'
        let overlay = $("input:checkbox:checked").val()
        $.ajax({
            type: "POST",
            url: url,
            contentType: "application/json",
            data: {overlay:overlay},
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