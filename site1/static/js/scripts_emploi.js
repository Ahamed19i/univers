

// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function () {
    const filterSelect = document.getElementById('filterSelect');
    const scheduleTable = document.querySelector('.schedule-table tbody');

    filterSelect.addEventListener('change', function () {
        const filterValue = this.value.toLowerCase();
        const rows = scheduleTable.querySelectorAll('tr');

        rows.forEach(row => {
            const jour = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
            const professeur = row.querySelector('td:nth-child(3)').textContent.toLowerCase();

            if (filterValue === 'all' || jour.includes(filterValue) || professeur.includes(filterValue)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });

    // Function to sort table columns
    document.querySelectorAll('.sortable').forEach(header => {
        header.addEventListener('click', () => {
            const table = header.closest('table');
            const index = Array.from(header.parentNode.children).indexOf(header);
            const ascending = header.classList.toggle('ascending');
            
            Array.from(table.querySelectorAll('tbody tr'))
                .sort((rowA, rowB) => {
                    const cellA = rowA.children[index].textContent;
                    const cellB = rowB.children[index].textContent;
                    return cellA.localeCompare(cellB, undefined, { numeric: true }) * (ascending ? 1 : -1);
                })
                .forEach(row => table.querySelector('tbody').appendChild(row));
        });
    });
});
