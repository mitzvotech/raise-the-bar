$("#new_contact_save").click(function () {
	contact_data = {
		"first_name": $("#id_first_name").val(),
		"last_name": $("#id_last_name").val(),
		"email": $("#id_email").val(),
		"phone_number": $("#id_phone_number").val(),
		"firm": $("#firm_id").val()
	}
	$.ajax({
		type:"post",
		url:"/addcontact", 
		data:contact_data,
		dataType:'json',
		headers: {'X-CSRFToken': $.cookie('csrftoken')}
	}).done(function(data){
		data = data.split(",")
		console.log(data)
		if (data[1] != "False") {
			$("#contact-select").prepend("<option value='" + data[0] + "'>" + $("#id_last_name").val() + ", " + $("#id_first_name").val() + "</otion>")
			$("#contact-select").val(data[0])
		}
		$("#new_contact_modal").modal("hide")
	})
	$("#new_contact_modal").modal("hide")
})

$(function() {
	$( "#id_reminder_date" ).datepicker();
});

$("#new_reminder_save").click(function () {
	$("#note_form").append(
		hiddenInput("reminder_date",$("#id_reminder_date").val()) + 
		hiddenInput("reminder_content",$("#id_reminder_content").val())
		// This is going to append the input values as hidden inputs to the 
		// #note-form
	)
	$("#new_reminder_modal").modal("hide");
})

function hiddenInput (tag, value) {
	return "<input type='hidden' name='" + tag + "' value='" + value + "'>"
}