function showToast(msg) {
    const toast = document.getElementById("toast");
    toast.innerText = msg;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 3200);
}

async function checkSpell() {
    let text = document.getElementById("editor").value.trim();

    if (!text) {
        showToast("Please enter some text to analyze.");
        return;
    }

    document.getElementById("loader").classList.remove("hidden");

    try {
        const response = await fetch("/api/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        // Highlight mispelled words
        const highlightedHTML = data.original.split(" ").map(word => {
            if (data.misspelled.includes(word)) {
                return `<span style="color:#b30000;font-weight:bold;border-bottom:2px dotted #b30000;">${word}</span>`;
            }
            return word;
        }).join(" ");

        document.getElementById("correctedOutput").innerHTML = data.corrected;

        // Suggestion list
        const missList = document.getElementById("misspelledList");
        missList.innerHTML = "";
        data.misspelled.forEach(w => {
            missList.innerHTML += `<li>${w} → <span style="color:#005bbb;font-weight:700">${data.suggestions[w]}</span></li>`;
        });

        showToast("Spell Check Completed Successfully!");

    } catch (err) {
        console.error(err);
        showToast("Error processing text.");
    } finally {
        document.getElementById("loader").classList.add("hidden");
    }
}