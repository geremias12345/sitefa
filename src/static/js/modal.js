  const deleteModal = document.getElementById('deleteModal');
  deleteModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const nombre = button.getAttribute('data-nombre');
    const url = button.getAttribute('data-url');

    const nombreLabel = deleteModal.querySelector('#modalNombre');
    const form = deleteModal.querySelector('#deleteForm');

    nombreLabel.textContent = nombre;
    form.action = url;
  });