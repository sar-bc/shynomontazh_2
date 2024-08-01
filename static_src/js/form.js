$(function($) {
//================================    
    $('#form_login').submit(function(e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success : function(response){
                console.log('ok - ', response)
                if(response.status === 201){
                    // window.location.reload()
                    window.location.href = '/'
                }else if (response.status === 400) {
                    $('.alert-danger').text(response.error).removeClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
            }
        })
    })
//================================
    $('#form_reg').submit(function(e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success : function(response){
                console.log('ok - ', response)
                if(response.status === 201){
                    // window.location.reload()
                    window.location.href = 'users/confirm_email'
                }else if (response.status === 400) {
                    // $('.alert-danger').text(response.error).removeClass('d-none')
                    let obj = JSON.parse(response.error);
                    console.log(obj);
                    //error_email
                    if(obj.email){
                        $('.error_email').text(obj.email[0]['message']).removeClass('d-none')
                    }else{
                        $('.error_email').text("").addClass('d-none')
                    }
                    if(obj.username){
                        $('.error_username').text(obj.username[0]['message']).removeClass('d-none')
                    }else{
                        $('.error_username').text("").addClass('d-none')
                    }
                    //error_phone
                    if(obj.phone){
                        $('.error_phone').text(obj.phone[0]['message']).removeClass('d-none')
                    }else{
                        $('.error_phone').text("").addClass('d-none')
                    }
                    //error_password2
                    if(obj.password2){
                        // console.log(obj);
                        err = new Array();
                        for (let i = 0; i < obj.password2.length; i++) {
                            err[i] = obj.password2[i]['message'];
                        }
                        // console.log(obj.password2[0]['message'])
                        $('.error_password2').text(err).removeClass('d-none')
                    }else{
                        $('.error_password2').text("").addClass('d-none')
                    }
                }
            },
            error: function (response) {
                console.log('err - ', response)
            }
        })
    })  
//===============================
$('#show_pass_enter').click(function(e){
    // console.log("press")
    if ($('#password').attr('type') == 'password'){
        $('#password').attr('type', 'text');
    }else{
        $('password').attr('type', 'password');
    }
})     
//================================
    $('#show_pass').click(function(e){
        // console.log("press")
        if ($('#id_new_password1').attr('type') == 'password'){
            $('#id_new_password1').attr('type', 'text');
            $('#id_new_password2').attr('type', 'text');
        }else{
            $('#id_new_password1').attr('type', 'password');
            $('#id_new_password2').attr('type', 'password');
        }
    })    
//==============================    
$('#show_pass_reg').click(function(e){
    // console.log("press")
    if ($('#id_password1').attr('type') == 'password'){
        $('#id_password1').attr('type', 'text');
        $('#id_password2').attr('type', 'text');
    }else{
        $('#id_password1').attr('type', 'password');
        $('#id_password2').attr('type', 'password');
    }
}) 
//================================
$('#show_pass_change').click(function(e){
    // console.log("press")
    if ($('#id_old_password').attr('type') == 'password'){
        $('#id_old_password').attr('type', 'text');
        $('#id_new_password1').attr('type', 'text');
        $('#id_new_password2').attr('type', 'text');
    }else{
        $('#id_old_password').attr('type', 'password');
        $('#id_new_password1').attr('type', 'password');
        $('#id_new_password2').attr('type', 'password');
    }
})    
//============================== 
//form_change_password
$('#form_change_password').submit(function(e){
    e.preventDefault()
    $.ajax({
        type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success : function(response){
                console.log('ok - ', response)
                if(response.status === 201){
                 $('.response').text(response.response).removeClass('d-none')
                setTimeout(function () {
                    window.location.reload()
                }, 3000);
                    // window.location.reload()
                    // window.location.href = '/'
                }else if (response.status === 400) {
                    // $('.alert-danger').text(response.error).removeClass('d-none')
                    let obj = JSON.parse(response.error)
                    // console.log(obj)
                    if(obj.old_password){
                        // console.log(obj.old_password[0]['message'])
                        //error_old
                        $('.error_old').text(obj.old_password[0]['message']).removeClass('d-none')
                    }else{
                        $('.error_old').text("").addClass('d-none')
                    }
                    if(obj.new_password2){
                        // console.log(obj.new_password2[0]['message'])
                        //error_password2
                        $('.error_password2').text(obj.new_password2[0]['message']).removeClass('d-none')
                    }else{
                        $('.error_password2').text("").addClass('d-none')
                    }

                }
    
            },
            error: function (response) {
                console.log('err - ', response)
            }

    })

})
//================================
//form_username_edit
$('#form_username_edit').submit(function(e){
    e.preventDefault()
    $.ajax({
        type: this.method,
        url: this.action,
        data: $(this).serialize(),
        dataType: 'json',
        success : function(response){
            console.log('ok - ', response)
            if(response.status === 201){
                 $('.response').text(response.response).removeClass('d-none')
                setTimeout(function () {
                    window.location.reload()
                }, 3000);
            }else if (response.status === 400) {
                $('.error_username').text(response.error).removeClass('d-none')
                setTimeout(function(){
                $('.error_username').addClass('d-none')
                }, 3000)
            }
            
        },
        error: function (response) {
            console.log('err - ', response)
        }

    })

})
//=================================
//form_phone_edit
$('#form_phone_edit').submit(function(e){
    e.preventDefault()
    $.ajax({
        type: this.method,
        url: this.action,
        data: $(this).serialize(),
        dataType: 'json',
        success : function(response){
            console.log('ok - ', response)
            if(response.status === 201){
                 $('.response').text(response.response).removeClass('d-none')
                setTimeout(function () {
                    window.location.reload()
                }, 3000);
            }else if (response.status === 400) {
                $('.error_phone').text(response.error).removeClass('d-none')
                 setTimeout(function(){
                $('.error_phone').addClass('d-none')
                }, 3000);
            }
        },
        error: function (response) {
            console.log('err - ', response)
        }

    })

})
//==================================
})