$( document ).ready(() => {
    $('#overlay-btn').attr("disabled", true);
    // the selector will match all input controls of type :checkbox
    // and attach a click event handler 
    $(document).on('click', 'input[type="checkbox"]', function() {      
        $('input[type="checkbox"]').not(this).prop('checked', false);
        if($("input:checkbox:checked").val()){
            $('#overlay-btn').attr("disabled", false);
        }else{
            $('#overlay-btn').attr("disabled", true);
        }   
        
    });
    $("#add-chap-btn").click(function(ev) {
        ev.preventDefault();
        $('#add-chap-btn').attr("disabled", true);
        
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
        
        let url = '/create/stage3'
        $.ajax({
            type: "POST",
            url: url,
            data: $('#form-chapter').serialize(),
            success: function(data) {
                console.log(data)
                // Ajax call completed successfully
                alert("Form Submited Successfully");
                $('#add-chap-btn').attr("disabled", false);
                window.location.href = url;
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#add-chap-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });

    $(".voice-btn").click(function(ev) {
        ev.preventDefault();
        form = $('#form-voice-'+ $(this).val())
        $('.voice-btn').attr("disabled", true);
        console.log($(this).val());
        console.log(form);
        console.log(form.serialize());

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
        
        let url = '/create/stage3'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('.voice-btn').attr("disabled", false);
                window.location.href = '/create/stage3';
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('.voice-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });


    $("#combine-voice-btn").click(function(ev) {
        ev.preventDefault();
        form = $('#form-combine-voice');
        $('#combine-voice-btn').attr("disabled", true);
        console.log($(this).val());
        console.log(form);
        console.log(form.serialize());

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
        
        let url = '/create/stage3'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                alert("Form Submited Successfully");
                $('.voice-btn').attr("disabled", false);
                window.location.href = '/create/stage3';
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('.voice-btn').attr("disabled", false);
                window.location.reload();
            }
        });
    });

    $("#music-btn").click(function(ev) {
        ev.preventDefault();
        form = $('#form-music');
        $('#music-btn').attr("disabled", true);
        
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
       
        let url = '/create/stage3'
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data) {
                
                // Ajax call completed successfully
                //alert("Form Submited Successfully");
                $('#music-btn').attr("disabled", false);
                window.location.href = '/create/stage3';
            },
            error: function(data) {
                  
                // Some error in ajax call
                alert("some Error");
                $('#music-btn').attr("disabled", false);
                window.location.href = '/create/stage3';
            }
        });
    });

    $("#overlay-btn").click(function(ev) {
        ev.preventDefault();
        //ev.preventDefault();
        $('#overlay-btn').attr("disabled", true);
        let form = $("#form-2");
        let url = '/create/stage4';
        let overlay_music = $("input:checkbox:checked").val();
        console.log("music overlay: "+ overlay_music)

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
});