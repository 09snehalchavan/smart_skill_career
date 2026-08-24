document.addEventListener("DOMContentLoaded", function () {

    const ratingBars = document.querySelectorAll(".rating-fill");

    ratingBars.forEach(function (bar) {

        let rating = parseFloat(
            bar.getAttribute("data-rating")
        );

        if (isNaN(rating)) {
            rating = 0;
        }

        rating = Math.max(0, Math.min(5, rating));

        const percentage = (rating / 5) * 100;

        setTimeout(function () {
            bar.style.width = percentage + "%";
        }, 200);

    });

});