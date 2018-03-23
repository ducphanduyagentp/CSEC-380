$( document ).ready(function() {
    $( "#update_prof" ).submit(function( event ) {
        if($("#url").val() == ""){
            $("#update").html("Please insert a value");
        }else{
            $.get( "change_photo.php?type=profile&url=" + $("#url").val(), function( data ) {
                $("#update").html(data);
                if(data.indexOf("successfully") >= 0){
                    location.reload();
                }
            });
        }
        event.preventDefault();
    });
});