$( document ).ready(() => {
    // function will get executed 
    // on click of submit button
    
    $("#create-btn").click(function(ev) {
        $('#create-btn').attr("disabled", true);
        ev.preventDefault();

        $('#create-form').css("display", "none");
        $('#skeleton-container').css("display", "flex");
        
        
        //$('textarea').attr('disabled', true);
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

    $("#random-set-btn").click(function(ev) {
        $('#random-set-btn').attr("disabled", true);
        ev.preventDefault();
        $('#create-btn').attr("disabled", true);
      
        $('input').addClass('skeleton');
        //$('input').attr('disabled', true);
        $('input').css('color', 'transparent');
        if($('textarea')){
            $('textarea').addClass('skeleton');
            $('textarea').css('color', 'transparent');
        }
        
        $('button').attr('disabled', true);
        $('button').css('color', 'transparent');
        $('button').addClass('skeleton-footer');
        let form = $("#random-set-form");
        let url = '/create'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(response) {
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
               
                $('#random-set-btn').attr("disabled", false);
                console.log(response)
                window.location.href = url
                
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#random-set-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });
    
});

