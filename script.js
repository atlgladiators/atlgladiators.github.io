document.addEventListener('DOMContentLoaded', function() {
    
    // Hero slider functionality
    const slides = document.querySelectorAll('.slide');
    
   // Initialize the first slide as active
   let currentSlide = 0; 
   const slideInterval = setInterval(nextSlide, 3000);

   function nextSlide() {
       slides[currentSlide].classList.remove('active');
       currentSlide = (currentSlide + 1) % slides.length; // Loop back to the first slide
       slides[currentSlide].classList.add('active');
   }

   // Sponsorship inquiry form submission (if applicable)
   const sponsorForm = document.querySelector('#sponsor-form');
   if (sponsorForm) {
       sponsorForm.addEventListener('submit', function(event) {
           event.preventDefault();
           const formData = new FormData(sponsorForm);
           // Process form data here
           alert('Thank you for your interest in sponsoring us!');
       });
   }
});
