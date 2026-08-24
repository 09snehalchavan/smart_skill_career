document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("profileForm");
    const saveButton = document.getElementById("saveProfileBtn");

    if (!form || !saveButton) {
        return;
    }

    form.addEventListener("submit", function () {

        const buttonText = saveButton.querySelector(".btn-text");
        const loader = saveButton.querySelector(".btn-loader");

        saveButton.disabled = true;

        if (buttonText) {
            buttonText.style.display = "none";
        }

        if (loader) {
            loader.style.display = "inline";
        }

    });

});