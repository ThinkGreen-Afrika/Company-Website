document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navbarNav = document.querySelector('.navbar-nav');

    hamburger.addEventListener('click', function() {
        navbarNav.classList.toggle('active');
        hamburger.classList.toggle('active');
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Timer functionality
function updateTimer() {
    const eventDate = new Date("2024-12-31T00:00:00").getTime();
    const now = new Date().getTime();
    const distance = eventDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("days").textContent = days.toString().padStart(2, '0');
    document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
    document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
    document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');
}

setInterval(updateTimer, 1000);
updateTimer(); // Call immediately to set initial values

// const testimonials = [
//     {
//       name: "Anne M.",
//       position: "Back-End Developer",
//       image: "/static/images/anne.jpg",
//       text: "The diversity of perspectives in the roundtable discussions has been eye-opening. It's expanded my vision."
//     },
//     {
//         name: "Paul Pierce",
//         position: "Lead Designer",
//         image: "/static/images/Leroy.jpg",
//         text: "The tools and frameworks shared here helped me structure my business for rapid growth. Incredible resource!"
//       },
//    {
//         name: "Pascal O.",
//         position: "Front-End Developer",
//         image: "/static/images/Pasacal.jpg",
//         text: "The Founder's RoundTable changed my entire approach to scaling. Their expert discussions are pure gold!"
//       },
    
//   ];
  
//   const testimonialContainer = document.querySelector('.testimonial-container');
//   const prevBtn = document.querySelector('.prev-btn');
//   const nextBtn = document.querySelector('.next-btn');
//   const sliderDots = document.querySelector('.slider-dots');
  
//   let currentIndex = 0;
  
//   function createTestimonialCard(testimonial) {
//     return `
//       <div class="testimonial-card">
//         <div class="testimonial-content">
//           <img src="${testimonial.image}" alt="${testimonial.name}" class="testimonial-image">
//           <p class="testimonial-text">${testimonial.text}</p>
//           <p class="testimonial-name">${testimonial.name}</p>
//           <p class="testimonial-position">${testimonial.position}</p>
//         </div>
//       </div>
//     `;
//   }
  
//   function updateSlider() {
//     testimonialContainer.innerHTML = '';
//     for (let i = currentIndex; i < currentIndex + 3; i++) {
//       const index = i % testimonials.length;
//       testimonialContainer.innerHTML += createTestimonialCard(testimonials[index]);
//     }
//     updateDots();
//   }
  
//   function updateDots() {
//     sliderDots.innerHTML = '';
//     for (let i = 0; i < testimonials.length; i++) {
//       const dot = document.createElement('span');
//       dot.classList.add('dot');
//       if (i === currentIndex) dot.classList.add('active');
//       dot.addEventListener('click', () => {
//         currentIndex = i;
//         updateSlider();
//       });
//       sliderDots.appendChild(dot);
//     }
//   }
  
//   prevBtn.addEventListener('click', () => {
//     currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
//     updateSlider();
//   });
  
//   nextBtn.addEventListener('click', () => {
//     currentIndex = (currentIndex + 1) % testimonials.length;
//     updateSlider();
//   });
  
  updateSlider();
  
  document.querySelector('.newsletter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = e.target.querySelector('input[type="email"]').value;
    alert(`Thank you for subscribing with: ${email}`);
  });

  document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration-form');
    const photoUpload = document.getElementById('photo-upload');
    const profilePhoto = document.getElementById('profile-photo');
    const fileInputs = document.querySelectorAll('input[type="file"]');

    photoUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profilePhoto.src = e.target.result;
            }
            reader.readAsDataURL(file);
        }
    });

    fileInputs.forEach(input => {
        input.addEventListener('change', function(event) {
            const fileName = event.target.files[0]?.name || 'No file chosen';
            event.target.nextElementSibling.textContent = fileName;
        });
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        console.log('Form submitted');
        const formData = new FormData(form);
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }
    });
});

    document.addEventListener('DOMContentLoaded', function() {
        const form = document.getElementById('otp-form');
        const inputs = form.querySelectorAll('input[type="text"]');
        const emailDisplay = document.getElementById('email');
        let userEmail = ''; // This should be set from your registration process
    
        function setupInputs() {
            inputs.forEach((input, index) => {
                input.addEventListener('input', function(e) {
                    if (e.inputType === "insertText") {
                        this.value = this.value.replace(/[^0-9]/g, '');
                        if (this.value && index < inputs.length - 1) {
                            inputs[index + 1].focus();
                        }
                    }
                });
    
                input.addEventListener('keydown', function(e) {
                    if (e.key === 'Backspace' && !this.value && index > 0) {
                        inputs[index - 1].focus();
                    }
                });
    
                input.addEventListener('paste', handlePaste);
            });
        }
    
        function handlePaste(e) {
            e.preventDefault();
            const pastedData = e.clipboardData.getData('text').slice(0, inputs.length);
            inputs.forEach((input, index) => {
                if (index < pastedData.length) {
                    input.value = pastedData[index];
                }
            });
            if (inputs[inputs.length - 1].value) {
                inputs[inputs.length - 1].focus();
            }
        }
    
        function validateOTP(otp) {
            return /^\d{4}$/.test(otp);
        }
    
        async function sendOTPToEmail(email) {
            try {
                const response = await fetch('/api/send-otp', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email }),
                });
                if (!response.ok) {
                    throw new Error('Failed to send OTP');
                }
                const data = await response.json();
                return data.message; 
            } catch (error) {
                console.error('Error sending OTP:', error);
                throw error;
            }
        }
    
        async function verifyOTP(otp) {
            try {
                const response = await fetch('/api/verify-otp', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email: userEmail, otp }),
                });
                if (!response.ok) {
                    throw new Error('OTP verification failed');
                }
                const data = await response.json();
                return data.verified;
            } catch (error) {
                console.error('Error verifying OTP:', error);
                throw error;
            }
        }
    
        function displayEmail() {
            // This function should be called after the user has entered their email during registration
            if (userEmail) {
                const maskedEmail = userEmail.replace(/(\w{2})[\w.-]+@([\w.]+\w)/, "$1***@$2");
                emailDisplay.textContent = maskedEmail;
            }
        }
    
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const otp = Array.from(inputs).map(input => input.value).join('');
            
            if (validateOTP(otp)) {
                try {
                    const isVerified = await verifyOTP(otp);
                    if (isVerified) {
                        alert('OTP verified successfully!');
                        // Redirect or perform next steps after successful verification
                    } else {
                        alert('Invalid OTP. Please try again.');
                    }
                } catch (error) {
                    alert('An error occurred during verification. Please try again.');
                }
                form.reset();
                inputs[0].focus();
            } else {
                alert('Please enter a valid 4-digit OTP.');
            }
        });
    
        setupInputs();
        displayEmail(); // Call this after setting userEmail from your registration process
    
        // If you need to trigger OTP sending from this page:
        // sendOTPToEmail(userEmail).then(() => {
        //     alert(`An OTP has been sent to your email.`);
        // }).catch(() => {
        //     alert('Failed to send OTP. Please try again.');
        // });
    });

// Function to check if an element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }
  
  // Function to animate counting
  function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      obj.innerHTML = Math.floor(progress * (end - start) + start) + obj.innerHTML.replace(/\d+/g, '');
      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    };
    window.requestAnimationFrame(step);
  }
  
  // Get the stats section
  const statsSection = document.querySelector('.stats-section');
  
  // Get all stat items
  const statItems = document.querySelectorAll('.stat-item span');
  
  // Function to start animation if elements are in viewport
  function checkScroll() {
    if (isInViewport(statsSection) && !statsSection.classList.contains('counted')) {
      statItems.forEach((item) => {
        const text = item.innerHTML;
        const number = parseInt(text.match(/\d+/)[0]);
        animateValue(item, 0, number, 2000); // 2000ms duration
      });
      statsSection.classList.add('counted');
    }
  }
  
  // Listen for scroll events
  window.addEventListener('scroll', checkScroll);
  
  // Initial check in case elements are already in viewport on page load
  checkScroll();

  document.querySelectorAll('input[type="file"]').forEach((input) => {
    input.addEventListener('change', function() {
        const fileName = this.files.length > 0 ? this.files[0].name : 'No file chosen';
        this.nextElementSibling.textContent = fileName;
    });
});
