$( document ).ready(() => {
    // function will get executed 
    // on click of submit button

    $("#add-chap-btn").click(function(ev) {
        $('#add-chap-btn').attr("disabled", true);
        ev.preventDefault();
        for(let i = 0; i < $(this).val(); i++){
            let chapter_clone = $('#chapter-container').clone(true);
            chapter_clone.addClass('loading');
            chapter_clone.appendTo('#horizontal-scroll');
            console.log(eval($(this).val())+1)
            let chapter = eval($(this).val())+1
            $('.loading .chapter').text('Chapter ' + chapter)
            console.log($('.loading .chapter'));
            
        }

        $('input').addClass('skeleton');
        //$('input').attr('disabled', true);
        $('input').css('color', 'transparent');
        if($('textarea')){
            $('textarea').attr('disabled', true);
            $('.loading textarea').css('color', 'transparent');
        }
        
        $('button').attr('disabled', true);
        $('button').css('color', 'transparent');
        $('button').addClass('skeleton-footer');
        
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

    $("#voice-over-btn").click(function(ev) {
        
        $('#voice-over-btn').attr("disabled", true);
        
        $('#create-form2').css("display", "none");
        $('#skeleton-container').css("display", "flex");

        $('input').addClass('skeleton');
        //$('input').attr('disabled', true);
        $('input').css('color', 'transparent');
        if($('textarea')){
            $('textarea').attr('disabled', true);
            $('.loading textarea').css('color', 'transparent');
        }
        
        $('button').attr('disabled', true);
        $('button').css('color', 'transparent');
        $('button').addClass('skeleton-footer');
        
        ev.preventDefault();
        let url = '/create/stage3'
        $.ajax({
            type: "POST",
            url: url,
            data: $('#form-voice-over').serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('#voice-over-btn').attr("disabled", false);
                window.location.href = url;
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#voice-over-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });

    $("#regenerate-btn").click(function(ev) {
        console.log("regenerate button clicked ...")
        console.log($('#form-regenerate'))
        $('#regenerate-btn').attr("disabled", true);
        
        $('input').addClass('skeleton');
        //$('input').attr('disabled', true);
        $('input').css('color', 'transparent');
        if($('textarea')){
            $('textarea').attr('disabled', true);
            $('.loading textarea').css('color', 'transparent');
            $('.loading textarea').attr('disabled', true);
        }
        
        $('button').attr('disabled', true);
        $('button').css('color', 'transparent');
        $('button').addClass('skeleton-footer');
        
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