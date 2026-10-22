// Aggiungi qui il tuo JavaScript per funzionalità aggiuntive

document.addEventListener("DOMContentLoaded", function () {
    const link = document.getElementById("privacy-link");
    const modal = document.getElementById("privacy-modal");
    const closeButton = document.getElementById("privacy-close");
    const closeButtonBottom = document.getElementById(
        "privacy-close-button"
    );

    if (!link || !modal || !closeButton || !closeButtonBottom) {
        return;
    }

    let previousFocus = null;

    function openModal(event) {
        event.preventDefault();

        previousFocus = document.activeElement;
        modal.classList.add("is-open");
        modal.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";

        closeButton.focus();
    }

    function closeModal() {
        modal.classList.remove("is-open");
        modal.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";

        if (previousFocus) {
            previousFocus.focus();
        }
    }

    link.addEventListener("click", openModal);
    closeButton.addEventListener("click", closeModal);
    closeButtonBottom.addEventListener("click", closeModal);

    modal.addEventListener("click", function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (
            event.key === "Escape" &&
            modal.classList.contains("is-open")
        ) {
            closeModal();
        }
    });
});
