const paths = document.querySelectorAll('#map-container path');
 	const infoBox = document.querySelector('#info-box');


// Add event listeners to each path element
	paths.forEach((path) => {
	path.addEventListener('mouseover', (e) => {
    // Get the title attribute value of the path element
		const areaTitle = e.target.getAttribute('title');

			if(areaTitle==null)
			{
				infoBox.innerHTML = ` <h2>No Information<h2>
	    `;

			}
			else{
     // Set the innerHTML of the info-box element to display the table of information
			 infoBox.innerHTML = `
      ${areaTitle}
	    `;
	    	}
    // Show the info-box element
	     infoBox.style.display = 'block';
	   });

	   path.addEventListener('mouseout', () => {
     // Hide the info-box element
     infoBox.innerHTML = "<h2>Discover Mumbai:</h2><em><p>Our interactive map of Mumbai allows you to explore the vibrant city in a whole new way. You can click on each point of interest to learn more about it. Whether you're a tourist planning your trip to Mumbai or a local looking to discover something new, our map is the perfect tool to help you navigate the city with ease. Explore the streets of Mumbai, find hidden gems, and uncover the city's rich culture and history today!</p></em>";
  });
});