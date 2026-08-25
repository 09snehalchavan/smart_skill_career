document.addEventListener("DOMContentLoaded", function () {

    const matchBars = document.querySelectorAll(".match-fill");

    matchBars.forEach(function (bar) {

        let percentage = parseFloat(
            bar.getAttribute("data-percentage")
        );

        if (isNaN(percentage)) {
            percentage = 0;
        }

        percentage = Math.max(
            0,
            Math.min(100, percentage)
        );

        setTimeout(function () {
            bar.style.width = percentage + "%";
        }, 200);

    });

});