


// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function () {
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
