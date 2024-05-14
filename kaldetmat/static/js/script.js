let pathName = window.location.pathname;

function hiddenNav(selector) {
    document.querySelector(selector).classList.add("hidden");
}

function activeNav(selector) {
    document.querySelector(selector).classList.add("active")
}

// show active navbar
if(pathName === "/") {
    activeNav(".home");
    activeNav(".footer-home-nav");
}

if(pathName === "/calculate/") {
    // nav header
    activeNav(".calculator");
    hiddenNav(".about");
    hiddenNav(".feedback");

    // nav footer
    activeNav(".footer-calculator-nav");
    hiddenNav(".footer-about-nav");
    hiddenNav(".footer-feedback-nav");
}