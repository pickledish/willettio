$(document).ready(function($) {

	$("#greekRow").hide();
	$("#entryRow").hide();

	$("#showGreek").on('click', function(event) {
		$("#greekRow").show();
		$("#showMatrixEntry").prop("disabled",true);
	});

	$("#showMatrixEntry").on('click', function(event) {

		var en = parseInt(document.getElementById('n').value);
		if (isNaN(en)) {en = -1};

		$("#matrixA").css({
			width: String(2*en) + "em",
			height: String(1+en) + "em"
		});
		$("#matrixb").css({
			width: "2em",
			height: String(1+en) + "em"
		});
		$("#entryRow").show();
		$("#showGreek").prop("disabled",true);
	});

	$('#calculate').on('click', function(event) {

		event.preventDefault();
		$("#bottom").html("Thank you for the input! Calculating ... <br/> <div class=\"loading\"></div>")

		var en = parseInt(document.getElementById('n').value);
		if (isNaN(en)) {en = -1};

		var alph = parseFloat(document.getElementById('alpha').value);
		if (isNaN(alph)) {alph = -1};

		var bet = parseFloat(document.getElementById('beta').value);
		if (isNaN(bet)) {bet = -1};

		var gamm = parseFloat(document.getElementById('gamma').value);
		if (isNaN(gamm)) {gamm = -1};

		var mA = String(document.getElementById('matrixA').value);

		var mb = String(document.getElementById('matrixb').value);

		$.ajax({
			type: "POST",
			url: "/",
			headers: { "cache-control": "no-cache" },
			data: {n : en, alpha : alph, beta : bet, gamma : gamm, matrixA : mA, matrixb : mb},
			dataType: "html",
			success: function(html){
				$("#bottom").html(html);
			}
		});
	});

	$('div').on('click', '#rerun', function(event) {

		event.preventDefault();

		var keepRows = document.getElementById('keepRows').value;
		if (keepRows == "") {keepRows = "no"};

		$("#bottom").html("Thank you for the input! Calculating ... <br/> <div class=\"loading\"></div>")

		$.ajax({
			type: "POST",
			url: "/rerun/",
			headers: { "cache-control": "no-cache" },
			data: {keep : keepRows},
			dataType: "html",
			success: function(html){
				$("#bottom").html(html);
			}
		});
	});

});