// Initialize AOS Animation
AOS.init({
    once: true,
    offset: 100,
});

// Typed.js Animation for Hero Section
const typingElement = document.querySelector('.typing');
if (typingElement) {
    new Typed('.typing', {
        strings: ['Python-Django Developer', 'Web Developer', 'Graphics Designer', 'Video Editor'],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true,
        backDelay: 1500
    });
}

// Mobile Navbar Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.innerHTML = navLinks.classList.contains('active') 
            ? '<i class="fas fa-times"></i>' 
            : '<i class="fas fa-bars"></i>';
    });
}

// Progress Bar Animation on Scroll
const progressBars = document.querySelectorAll('.progress');

const animateProgress = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const progressBar = entry.target;
            const targetWidth = progressBar.getAttribute('data-width');
            const percentText = progressBar.parentElement.previousElementSibling.querySelector('.percent-text');
            
            // Animate width
            progressBar.style.width = targetWidth;

            // Animate Percentage Number
            let currentWidth = 0;
            const targetValue = parseInt(targetWidth);
            const duration = 1500; // ms
            const interval = 20; // ms
            const step = targetValue / (duration / interval);
            
            const timer = setInterval(() => {
                currentWidth += step;
                if (currentWidth >= targetValue) {
                    currentWidth = targetValue;
                    clearInterval(timer);
                }
                if (percentText) {
                    percentText.innerText = Math.round(currentWidth) + '%';
                }
            }, interval);

            // Stop observing once animated
            observer.unobserve(progressBar);
        }
    });
};

const progressObserver = new IntersectionObserver(animateProgress, {
    root: null,
    threshold: 0.5,
});

progressBars.forEach(bar => {
    progressObserver.observe(bar);
});

// Prepare elements for printing
window.addEventListener('beforeprint', () => {
    // 1. Force progress bars to target width
    const bars = document.querySelectorAll('.progress');
    bars.forEach(bar => {
        bar.style.width = bar.getAttribute('data-width');
        const percentText = bar.parentElement.previousElementSibling.querySelector('.percent-text');
        if (percentText) {
            percentText.innerText = bar.getAttribute('data-width');
        }
    });
});
