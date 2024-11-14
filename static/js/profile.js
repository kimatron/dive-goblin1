document.addEventListener('DOMContentLoaded', function() {
    // Update Account Form Validation
    const updateForm = document.querySelector('.update-account-form');
    if (updateForm) {
        updateForm.addEventListener('submit', function(e) {
            const newPassword = document.querySelector('input[name="new_password"]').value;
            const confirmPassword = document.querySelector('input[name="confirm_password"]').value;

            if (newPassword && newPassword !== confirmPassword) {
                e.preventDefault();
                alert('New passwords do not match.');
            }
        });
    }

    // Delete Account Form Validation
    const deleteForm = document.querySelector('.delete-account-form');
    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            const confirmCheckbox = document.querySelector('#confirm_delete');
            if (!confirmCheckbox.checked) {
                e.preventDefault();
                alert('Please confirm account deletion by checking the box.');
            }
        });
    }
});