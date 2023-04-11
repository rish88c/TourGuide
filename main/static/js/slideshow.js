var slideshow = document.querySelector('.slideshow');
var images = slideshow.querySelectorAll('img');
var currentImage = 0;
var slideshowTimer;

function nextImage() {
  images[currentImage].style.opacity = 0;
  currentImage = (currentImage + 1) % images.length;
  images[currentImage].style.opacity = 0.8;
}

function startSlideshow() {
  slideshowTimer = setInterval(nextImage, 3000);
}

function stopSlideshow() {
  clearInterval(slideshowTimer);
}

startSlideshow();

//slideshow.addEventListener('mouseover', stopSlideshow);
//slideshow.addEventListener('mouseout', startSlideshow);