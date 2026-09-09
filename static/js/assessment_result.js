/* =========================================
   SMART CAREER
   ASSESSMENT RESULT
========================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {


        const performanceFill =
            document.querySelector(
                ".performance-fill"
            );


        if (!performanceFill) {
            return;
        }


        /*
        =========================================
        ANIMATE PERFORMANCE BAR
        =========================================
        */

        const targetWidth =
            performanceFill.style.width;


        performanceFill.style.width = "0%";


        setTimeout(
            function () {

                performanceFill.style.width =
                    targetWidth;

            },
            200
        );


    }
);