document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.getElementById('newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const email = this.querySelector('input[name="email"]').value;
            const submitBtn = this.querySelector('.newsletter-submit');
            const originalBtnText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<span class="submit-text">SUBSCRIBING...</span>';
            submitBtn.disabled = true;
            
            try {
                const response = await fetch('/newsletter/signup/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ email })
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    // Show success message
                    showToast('Success!', data.message, 'success');
                    this.reset();
                } else {
                    // Show error message
                    showToast('Error', data.message, 'error');
                }
            } catch (error) {
                showToast('Error', 'Something went wrong. Please try again.', 'error');
            } finally {
                // Restore button state
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            }
        });
    }
    
    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Helper function to show toast messages
    function showToast(title, message, type) {
        // Use your existing toast system or create a new one
        // This assumes you have a toast system in place
        if (window.showToast) {
            window.showToast(title, message, type);
        } else {
            alert(`${title}: ${message}`);
        }
    }
});