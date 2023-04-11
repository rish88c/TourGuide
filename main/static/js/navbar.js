window.addEventListener
('scroll', function()
    {
		var nav = document.querySelector('nav');
		var distanceY = window.pageYOffset || document.documentElement.scrollTop;
		var opaqueAfter = window.innerHeight;

		if (distanceY > opaqueAfter) {
		    nav.classList.add('opaque');
		} else {
			nav.classList.remove('opaque');
		}
    }
);