// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Ignore empty/hash-only links like href="#"
        if (!href || href === '#') return;

        let target = null;
        try {
            target = document.querySelector(href);
        } catch {
            // Invalid selector; ignore
            return;
        }

        // Only prevent default when we can actually scroll to something
        if (!target) return;

        e.preventDefault();
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Contact form handling
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const nameEl = document.getElementById('name');
        const emailEl = document.getElementById('email');
        const subjectEl = document.getElementById('subject');
        const messageEl = document.getElementById('message');

        // If the expected fields are missing, do nothing (avoid runtime errors)
        if (!nameEl || !emailEl || !subjectEl || !messageEl) return;

        const formData = {
            name: nameEl.value,
            email: emailEl.value,
            subject: subjectEl.value,
            message: messageEl.value
        };

        console.log('Form submitted:', formData);
        alert('Thank you for your message! I will get back to you soon.');
        this.reset();
    });
}

// Add active class to nav link based on current page
document.addEventListener('DOMContentLoaded', function () {
    const currentLocation = window.location.pathname;
    const menuItems = document.querySelectorAll('.nav-link');

    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });
});