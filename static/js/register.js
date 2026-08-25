document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("registerForm");
    const button = document.getElementById("registerBtn");

    if (!form || !button) {
        return;
    }

    form.addEventListener("submit", function () {

        button.disabled = true;

        button.innerHTML = `
            <span>Creating Account...</span>
            <span>⏳</span>
        `;

    });

});