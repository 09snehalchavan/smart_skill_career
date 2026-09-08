/* =========================================
   SMART CAREER
   SKILL ASSESSMENT JAVASCRIPT
========================================= */


document.addEventListener(
    "DOMContentLoaded",
    function () {


        /* =====================================
           GET ELEMENTS
        ====================================== */

        const form =
            document.getElementById(
                "assessmentForm"
            );


        const questionCards =
            document.querySelectorAll(
                ".question-card"
            );


        const progressFill =
            document.getElementById(
                "progressFill"
            );


        const progressText =
            document.getElementById(
                "progressText"
            );


        const completionMessage =
            document.getElementById(
                "completionMessage"
            );


        /* =====================================
           UPDATE PROGRESS
        ====================================== */

        function updateProgress() {


            let answered = 0;


            questionCards.forEach(
                function (card) {


                    const selected =
                        card.querySelector(
                            'input[type="radio"]:checked'
                        );


                    const status =
                        card.querySelector(
                            ".answered-status"
                        );


                    if (selected) {

                        answered++;


                        if (status) {

                            status.textContent =
                                "Answered";

                            status.style.color =
                                "#16a34a";

                        }

                    } else {

                        if (status) {

                            status.textContent =
                                "Not answered";

                            status.style.color =
                                "#94a3b8";

                        }

                    }

                }
            );


            const total =
                questionCards.length;


            let percentage = 0;


            if (total > 0) {

                percentage =
                    (answered / total) * 100;

            }


            /* Update progress bar */

            if (progressFill) {

                progressFill.style.width =
                    percentage + "%";

            }


            /* Update progress text */

            if (progressText) {

                progressText.textContent =
                    answered +
                    " / " +
                    total;

            }


            /* Completion message */

            if (
                total > 0 &&
                answered === total
            ) {

                completionMessage.textContent =
                    "All questions answered. You can submit your assessment.";

                completionMessage.style.color =
                    "#16a34a";

            } else {

                completionMessage.textContent =
                    "Please answer all questions before submitting.";

                completionMessage.style.color =
                    "#64748b";

            }

        }


        /* =====================================
           OPTION CLICK
        ====================================== */

        const options =
            document.querySelectorAll(
                ".option"
            );


        options.forEach(
            function (option) {


                option.addEventListener(
                    "click",
                    function () {


                        const radio =
                            option.querySelector(
                                'input[type="radio"]'
                            );


                        const questionCard =
                            option.closest(
                                ".question-card"
                            );


                        if (!radio ||
                            !questionCard) {

                            return;

                        }


                        /* Remove previous selection */

                        const cardOptions =
                            questionCard.querySelectorAll(
                                ".option"
                            );


                        cardOptions.forEach(
                            function (item) {

                                item.classList.remove(
                                    "selected"
                                );

                            }
                        );


                        /* Select current option */

                        option.classList.add(
                            "selected"
                        );


                        radio.checked = true;


                        /* Update progress */

                        updateProgress();

                    }
                );

            }
        );


        /* =====================================
           FORM SUBMIT VALIDATION
        ====================================== */

        if (form) {


            form.addEventListener(
                "submit",
                function (event) {


                    let unanswered = [];


                    questionCards.forEach(
                        function (card, index) {


                            const selected =
                                card.querySelector(
                                    'input[type="radio"]:checked'
                                );


                            if (!selected) {

                                unanswered.push(
                                    index
                                );

                            }

                        }
                    );


                    /* =================================
                       IF QUESTIONS ARE UNANSWERED
                    ================================== */

                    if (
                        unanswered.length > 0
                    ) {


                        event.preventDefault();


                        completionMessage.textContent =
                            "Please answer all questions before submitting.";


                        completionMessage.style.color =
                            "#dc2626";


                        /* Scroll to first unanswered */

                        const firstUnanswered =
                            questionCards[
                            unanswered[0]
                            ];


                        if (firstUnanswered) {


                            firstUnanswered.scrollIntoView(
                                {
                                    behavior: "smooth",
                                    block: "center"
                                }
                            );


                            /* Add temporary highlight */

                            firstUnanswered.style.borderColor =
                                "#dc2626";


                            setTimeout(
                                function () {

                                    firstUnanswered.style.borderColor =
                                        "#e5e7eb";

                                },
                                1500
                            );

                        }

                    }

                }
            );

        }


        /* =====================================
           INITIAL PROGRESS
        ====================================== */

        updateProgress();


    }
);