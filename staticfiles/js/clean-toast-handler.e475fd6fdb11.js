// Single, clean toast handler for Dive Goblin
class BrutalistToastManager {
    constructor() {
        this.container = null;
        this.init();
    }

    init() {
        // Create or find message container
        this.container = document.querySelector('.message-container');
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.className = 'message-container';
            this.container.setAttribute('aria-live', 'polite');
            this.container.setAttribute('aria-atomic', 'true');
            document.body.appendChild(this.container);
        }

        // Initialize any existing toasts
        this.initializeExistingToasts();
    }

    initializeExistingToasts() {
        const existingToasts = document.querySelectorAll('.toast, .brutal-toast');
        existingToasts.forEach(toast => this.activateToast(toast));
    }

    showToast(html) {
        // Clear existing toasts
        this.container.innerHTML = '';
        
        // Add new toast
        this.container.innerHTML = html;
        
        // Activate the new toast
        const toast = this.container.querySelector('.toast, .brutal-toast');
        if (toast) {
            this.activateToast(toast);
        }
    }

    activateToast(toast) {
        // Make sure it's visible
        toast.classList.add('show');
        
        // Setup close button
        const closeButtons = toast.querySelectorAll('.btn-close, .close');
        closeButtons.forEach(button => {
            button.addEventListener('click', () => this.hideToast(toast));
        });
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            if (toast && toast.parentNode) {
                this.hideToast(toast);
            }
        }, 5000);
    }

    hideToast(toast) {
        if (toast) {
            toast.classList.remove('show');
            toast.style.opacity = '0';
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing Brutalist Toast Manager...');
    window.toastManager = new BrutalistToastManager();
});