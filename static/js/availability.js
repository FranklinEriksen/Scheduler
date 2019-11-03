//none of this shit works. disregard for now

var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

var daySelectors = document.querySelector('form input');

function createHiddenTimeInputs( day ) {

	var d = document.createElement('div');

	var startLabel = document.createElement('p');
	startLabel.innerText = 'Start Time:';

	var startInput = document.createElements('input');
	startInput.type = 'text';
	
}

function updateTimeDisplay( day, b ) {

	var d = getElementById( day + '-times' );
	var b = getElementById( day + '-box' );

	if ( b.checked )
		d.style.display = 'block';
	else
		d.style.display = 'none';
}

getElementById('monday-box').addEventListener('click', updateTimeDisplay('monday'));
