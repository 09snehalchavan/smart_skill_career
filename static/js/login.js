/* =====================================================
   SMART CAREER - LOGIN PAGE JS
===================================================== */

document.addEventListener("DOMContentLoaded", function () {

    const loginForm = document.querySelector(".login-form");
    const loginButton = document.getElementById("loginBtn");

    if (!loginForm || !loginButton) {
        return;
    }


    /* ===============================
       LOGIN BUTTON LOADING
    =============================== */

    loginForm.addEventListener("submit", function () {

        loginButton.disabled = true;

        const buttonText =
            loginButton.querySelector(".btn-text");

        const buttonArrow =
            loginButton.querySelector(".btn-arrow");


        if (buttonText) {
            buttonText.textContent = "Logging in...";
        }


        if (buttonArrow) {
            buttonArrow.textContent = "⏳";
        }

    });

});