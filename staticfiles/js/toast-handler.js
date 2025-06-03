// Toast initialization and handling
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing brutalist toasts...');
    
    // Initialize Bootstrap toasts if Bootstrap is available
    if (typeof bootstrap !== 'undefined') {
        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
        var toastList = toastElList.map(function(toastEl) {
            return new bootstrap.Toast(toastEl, {
                autohide: true,
                delay: 5000
            });
        });
        
        toastList.forEach(toast => toast.show());
    }
    // Or use jQuery if available
    else if (typeof $ !== 'undefined' && typeof $.fn.toast !== 'undefined') {
        $('.toast').toast({
            autohide: true,
            delay: 5000
        });
        
        $('.toast').toast('show');
    }
    // Fallback to vanilla JS
    else {
        console.log('Using vanilla JS for toasts');
        var toasts = document.querySelectorAll('.toast, .brutal-toast');
        
        toasts.forEach(function(toast) {
            // Show the toast
            toast.classList.add('show');
            
            // Setup close buttons
            var closeButtons = toast.querySelectorAll('.btn-close, .close');
            closeButtons.forEach(function(button) {
                button.addEventListener('click', function() {
                    toast.classList.remove('show');
                    setTimeout(function() {
                        if (toast.parentNode) {
                            toast.parentNode.removeChild(toast);
                        }
                    }, 300);
                });
            });
            
            // Auto-hide after 5 seconds
            setTimeout(function() {
                toast.classList.remove('show');
                setTimeout(function() {
                    if (toast.parentNode) {
                        toast.parentNode.removeChild(toast);
                    }
                }, 300);
            }, 5000);
        });
    }
});