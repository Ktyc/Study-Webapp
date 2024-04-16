document.addEventListener('DOMContentLoaded', function () {
    const journalForm = document.getElementById('journalForm');
    const entriesContainer = document.getElementById('entries');

    journalForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const title = this.title.value;
        const date = this.date.value;
        const entry = this.entry.value;

        const entryItem = document.createElement('div');
        entryItem.classList.add('entry-item');
        entryItem.innerHTML = `
            <h2>${title}</h2>
            <p><strong>Date:</strong> ${date}</p>
            <p>${entry}</p>
        `;

        entriesContainer.appendChild(entryItem);

        // Clear form fields after submission
        this.reset();
    });
});
