
let modalDone = document.querySelector('.modalDone-content');
//let body = document.querySelector('body');
$(document).ready(function() {

	//E-mail Ajax Send
	$("form").submit(function() { //Change
		var th = $(this);
		$.ajax({
			type: "POST",
			url: "mail.php", //Change
			data: th.serialize()
		}).done(function() {
			// alert("Your application is accepted! Ваша заявка принята!");
			modalDone.style.display="block";
			body.style.overflow="hidden";
			setTimeout(function() {
				// Done Functions
				th.trigger("reset");
				modalDone.style.display="none";
				body.style.overflow="auto";
			}, 3100);
		});
		return false;
	});

});