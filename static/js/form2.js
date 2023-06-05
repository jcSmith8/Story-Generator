$( document ).ready(() => {
    // function will get executed 
    // on click of submit button

    $("#add-chap-btn").click(function(ev) {
        $('#add-chap-btn').attr("disabled", true);
        
        for(let i = 0; i < $(this).val() ; i++){
            let chapter_clone = $('#chapter-container-skeleton').clone(true)
            console.log(chapter_clone)
            chapter_clone.appendTo('#horizontal-skeleton')
        }
        
        $('#skeleton-container').css("display", "block");
        $('#create-form2').css("display", "none");
        ev.preventDefault();
        let url = '/create/stage2'
        $.ajax({
            type: "POST",
            url: url,
            data: $('#form-chapter').serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('#add-chap-btn').attr("disabled", false);
                window.location.reload();
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#add-chap-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });

    $("#regenerate-btn").click(function(ev) {
        console.log("regenerate button clicked ...")
        console.log($('#form-regenerate'))
        $('#regenerate-btn').attr("disabled", true);
        
        for(let i = 0; i < $(this).val() ; i++){
            let chapter_clone = $('#chapter-container-skeleton').clone(true)
            console.log(chapter_clone)
            chapter_clone.appendTo('#horizontal-skeleton')
        }
        
        $('#skeleton-container').css("display", "block");
        $('#create-form2').css("display", "none");
        ev.preventDefault();
        let url = '/create/stage2'
        $.ajax({
            type: "POST",
            url: url,
            data: $('#form-regenerate').serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('#regenerate-btn').attr("disabled", false);
                window.location.reload();
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#regenerate-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });
    
});