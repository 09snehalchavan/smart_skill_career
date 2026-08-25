document.addEventListener("DOMContentLoaded", function () {

    const progressBar = document.querySelector(".main-progress-fill");

    if (!progressBar) {
        return;
    }

    let percentage = parseFloat(
        progressBar.getAttribute("data-percentage")
    );

    if (isNaN(percentage)) {
        percentage = 0;
    }

    percentage = Math.max(
        0,
        Math.min(100, percentage)
    );

    setTimeout(function () {
        progressBar.style.width = percentage + "%";
    }, 200);

});