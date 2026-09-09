/* =========================================
   ASSESSMENT QUESTIONS PAGE
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const assessmentPage =
        document.querySelector(".assessment-page");


    if (!assessmentPage) {
        return;
    }


    /*
    =========================================
    ERROR MESSAGE
    =========================================
    */

    const errorMessage =
        document.querySelector(".assessment-error");


    if (errorMessage) {

        errorMessage.setAttribute(
            "role",
            "alert"
        );

    }

});