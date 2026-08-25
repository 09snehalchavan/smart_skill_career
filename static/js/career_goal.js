document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("careerGoalForm");
    const saveButton = document.getElementById("saveGoalBtn");

    if (!form || !saveButton) {
        return;
    }

    form.addEventListener("submit", function () {

        saveButton.disabled = true;

        saveButton.innerHTML = `
            <span>⏳</span>
            Saving...
        `;

    });

});