/* =====================================================
   SMART CAREER - GLOBAL JAVASCRIPT
===================================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* ===============================
       MOBILE NAVIGATION
    =============================== */

    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    if (menuToggle && navMenu) {

        menuToggle.addEventListener("click", function () {

            navMenu.classList.toggle("active");

            if (navMenu.classList.contains("active")) {
                menuToggle.innerHTML = "✕";
            } else {
                menuToggle.innerHTML = "☰";
            }

        });


        /* Close menu after clicking link */

        const navLinks = navMenu.querySelectorAll("a");

        navLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                navMenu.classList.remove("active");

                menuToggle.innerHTML = "☰";

            });

        });

    }


    /* ===============================
       AUTO HIDE MESSAGES
    =============================== */

    const messages = document.querySelectorAll(".message");

    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.transition = "0.4s ease";
            message.style.opacity = "0";
            message.style.transform = "translateY(-10px)";

            setTimeout(function () {
                message.remove();
            }, 400);

        }, 5000);

    });

});