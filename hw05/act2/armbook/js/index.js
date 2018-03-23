$(document).ready(function() {
    // Registration validation
    $('#regForm').submit(function(event) {
        event.preventDefault();
        var valid = true;
        if($('#reg_email').val()!=$('#reg_email_confirmation').val()){
            valid=false;
        }
        if($('#email').val()==""){
            valid=false;
        }
        if(($('#email').val()).search("@")==-1){
            valid=false;
        }
        if($('#password').val()==""){
            valid=false;
        }
          if(valid == false){
            $("#message").css( "color", "red" )
            $("#message").html("The credentials you inserted were not valid");
        }
        var data = $('#regForm').serialize();
        $.post( "registration.php", data)
            .done(function( data ) {
                if(data.search("False - ") != -1){
                    $("#message").css( "color", "red" )
                    $("#message").html(data.substring(data.search(" - ")+3,data.length));
                }else if(data.search("True - ") != -1){
                    $("#message").css( "color", "green" )
                    $("#message").html(data.substring(data.search(" - ")+3,data.length));
                }else{
                    $("#message").css( "color", "red" )
                    $("#message").html("There was an error adding your user, contact the administrator");
                }
        });
    });
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var data = $('#loginForm').serialize();
        $.post( "login.php", data)
            .done(function( data ) {
                if(data.search("False - ") != -1){
                    $("#loginMsg").css( "color", "red" )
                    $("#loginMsg").html(data.substring(data.search(" - ")+3,data.length));
                }else if(data.search("True - ") != -1){
                    window.location.href = '/home.php';
                }else{
                    $("#loginMsg").css( "color", "red" )
                    $("#loginMsg").html("There was an error logging you in, contact the administrator");
                }
        });
    });
});