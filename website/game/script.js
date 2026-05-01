// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

// Mobile menu toggle
document.querySelector('.hamburger').addEventListener('click', function(){
    this.classList.toggle('active');
    document.querySelector('.nav-menu').classList.toggle('active');
});

// Close mobile menu when clicking a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', function(){
        document.querySelector('.hamburger').classList.remove('active');
        document.querySelector('.nav-menu').classList.remove('active');
    });
});

// Sticky header
window.addEventListener('scroll', function(){
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.padding = '15px 0';
    }
});

// Animation on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
}, { threshold: 0.1 });

// Observe all animated elements
document.querySelectorAll('.service-card, .portfolio-item, .about-text, .about-image').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

// Trigger animations
setTimeout(() => {
    document.querySelectorAll('.service-card, .portfolio-item, .about-text, .about-image').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
    });
}, 300);

console.log('James Becwar Portfolio Website Loaded Successfully!');