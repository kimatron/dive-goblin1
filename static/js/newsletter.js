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
                            
                            // Remove any existing toasts
                            $('.toast').remove();
                            
                            // Add the new toast HTML to the container
                            if (data.toast_html) {
                                $('.message-container').html(data.toast_html);
                                // Initialize and show the new toast
                                $('.toast').toast({
                                    autohide: true,
                                    delay: 5000
                                }).toast('show');
                            } else {
                                // Fallback to simple toast if no custom HTML
                                showToast(
                                    data.status === 'success' ? 'Success!' : 'Notice', 
                                    data.message, 
                                    data.status
                                );
                            }
            
                            if (data.status === 'success') {
                                this.reset();
                            }
                        } catch (error) {
                            // Show error toast
                            $('.message-container').html(`
                                <div class="custom-toast newsletter-toast error-toast">
                                    <div class="brutal-toast">
                                        <div class="toast-header">
                                            <i class="fas fa-exclamation-circle text-danger"></i>
                                            <strong class="ml-2">Oops! 🤿</strong>
                                            <button type="button" class="btn-close" data-dismiss="toast">×</button>
                                        </div>
                                        <div class="toast-body">
                                            <h4 class="mb-3">Something went wrong!</h4>
                                            <p>Please try again later.</p>
                                        </div>
                                    </div>
                                </div>
                            `);
                            $('.toast').toast('show');
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
                
                // Helper function to show toast messages (fallback)
                function showToast(title, message, type) {
                    const toastHTML = `
                        <div class="custom-toast newsletter-toast ${type}-toast">
                            <div class="brutal-toast">
                                <div class="toast-header">
                                    <i class="fas fa-${type === 'success' ? 'check' : 'info'}-circle"></i>
                                    <strong class="ml-2">${title}</strong>
                                    <button type="button" class="btn-close" data-dismiss="toast">×</button>
                                </div>
                                <div class="toast-body">
                                    <p>${message}</p>
                                </div>
                            </div>
                        </div>
                    `;
                    
                    $('.message-container').html(toastHTML);
                    $('.toast').toast({
                        autohide: true,
                        delay: 5000
                    }).toast('show');
                }
            });
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