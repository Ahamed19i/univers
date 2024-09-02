


function showReclamationForm(noteId) {
    document.getElementById('note_id').value = noteId;
    document.getElementById('reclamationForm').style.display = 'block';
}

function hideReclamationForm() {
    document.getElementById('reclamationForm').style.display = 'none';
}

function showNoteForm() {
    document.getElementById('noteForm').style.display = 'block';
}

function hideNoteForm() {
    document.getElementById('noteForm').style.display = 'none';
}
