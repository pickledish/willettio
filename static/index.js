$(document).ready(function() {

	const lengthOfSlide = 600;
	const lengthOfHidden = 400;
	var isHidden = true;

	function slideCover () {
		$('#sidebar').transition({x: 0}, lengthOfSlide, 'ease');
		isHidden = true;
		// Returns the sidebar object so that we can queue stuff to it later
		return $('#sidebar');
	};

	function showContent(name) {
		$('#sidebar').transition({x: '-70%'}, lengthOfSlide, 'ease');
		$('.content').hide();
		$(name).show();
		
		isHidden = false;
		// Returns the sidebar object in case we need to queue stuff to it later
		return $('#sidebar');
	};

	$('#sideContent h1').click(function() {
		slideCover();
	});

	$('li').click(function() {

		// Figure out what div we should be showing when it reveals again
		var idee = $(this).attr('id');
		var name = idee.concat('Content');
		var fullName = '#'.concat(name);

		if (isHidden) {
			showContent(fullName);
		} else {
			slideCover().queue(function() {
				showContent(fullName);
				$(this).dequeue();
			});
		};
	});

});