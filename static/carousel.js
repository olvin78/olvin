document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector('.carousel');
    const nextBtn = document.querySelector('.next-btn');
    const prevBtn = document.querySelector('.prev-btn');
    const itemWidth = document.querySelector('.carousel-item').offsetWidth + 20; // Ajusta para el margen

    let scrollAmount = 0;

    nextBtn.addEventListener('click', () => {
        const maxScroll = carousel.scrollWidth - carousel.clientWidth;
        scrollAmount += itemWidth;
        if (scrollAmount > maxScroll) scrollAmount = 0; // Resetea al inicio al llegar al final
        carousel.scrollTo({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });

    prevBtn.addEventListener('click', () => {
        scrollAmount -= itemWidth;
        if (scrollAmount < 0) scrollAmount = maxScroll; // Resetea al final al llegar al inicio
        carousel.scrollTo({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });
});

///aca est para el caroucel de portafolios

const portfolioCarousel = document.querySelector('.portfolio-carousel');
let scrollPosition = 0;
const itemWidth = portfolioCarousel.querySelector('.portfolio-item').offsetWidth + 20; // Width of each item + gap
const visibleItems = 1;
const totalItems = portfolioCarousel.querySelectorAll('.portfolio-item').length;
const carouselWidth = itemWidth * totalItems;

function rotateCarousel() {
    scrollPosition += itemWidth;
    if (scrollPosition >= carouselWidth) {
        scrollPosition = 0;
        // Reset position to show the first three items again
    }
    portfolioCarousel.style.transform = `translateX(-${scrollPosition}px)`;
}

// Rotar cada 3 segundos
setInterval(rotateCarousel, 2000);
//aca es el codigo para el carousel de el portafolio
// JavaScript for Automatic Carousel
    
