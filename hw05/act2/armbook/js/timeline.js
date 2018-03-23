$(document).ready(function () {
	var f = 'jqueryui';
	var id_to_get = $("#id_to_get").val();
	$.fn.editable.defaults.mode = 'popup';
	$('#school').editable();
	$('#phone').editable();
	$('#screen_name').editable();
	$('#interests').editable();
	$('#statUpdate').keypress(function (e) {
		if (e.which == 13) {
			$.get("add_comment.php?id=" + id_to_get + "&comment=" + $('#statUpdate').val(), function (data) {
				location.reload();
			});
			return false;

		}
	});
});