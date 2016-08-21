$(document).ready(function() {
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
	ctx.arc(xstart, ystart, window.innerWidth, (1.5*Math.PI), 2); 
	ctx.closePath();
	ctx.fillStyle = '#93DB70';
	ctx.fill();

});