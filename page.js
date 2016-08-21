$(document).ready(function() {

	const MS_PER_DAY = 86400000;

	var utcStart = Date.UTC(2016, 7, 15);
	var startDate = new Date(utcStart);

	var utcNow = Date.now();
	var nowDate = new Date(utcNow);

	var utcEnd = utcStart + (21 * MS_PER_DAY);
	var endDate = new Date(utcEnd);

	console.log('Start date: '.concat(startDate));
	console.log('Now: '.concat(nowDate));
	console.log('End Date: '.concat(endDate));

	var daysUntil = Math.floor((utcEnd - utcNow) / MS_PER_DAY);
	var startFormatted = "".concat(startDate.getFullYear(), '-', startDate.getMonth()+1, '-', startDate.getDate()+1);
	var result = "".concat('Started on ', startFormatted, ', so there are ', daysUntil, ' days remaining.');

	$('#time').text(result);

	//get a reference to the canvas
	var ctx = $('#background')[0].getContext("2d");

	ctx.canvas.width  = window.innerWidth;
	ctx.canvas.height = window.innerHeight;

	var xstart = $('#background').width();
	xstart = xstart/2;

	var ystart = $('#background').height();
	ystart = ystart/2;
	 
	//draw a circle
	ctx.beginPath();
	ctx.moveTo(xstart, ystart);
	ctx.arc(xstart, ystart, window.innerWidth, 0, (((utcNow - utcStart) / (utcEnd - utcStart))*2*Math.PI)); 
	ctx.closePath();
	ctx.fillStyle = '#8CDD81';
	ctx.fill();

});