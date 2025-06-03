document.addEventListener('DOMContentLoaded', function() {
    console.log('=== DOM CONTENT LOADED ===');
    console.log('Document ready, initializing components...');
    
    // Rest of your existing code...
    
    // Initialize desktop mega menu
    initializeMegaMenu();
    
    // Initialize mobile menu
    initializeMobileMenu();
    
    // Initialize external links
    makeExternalLinksOpenInNewTab();
    
    // Initialize toasts
    initializeToasts();
    
    // Initialize quantity controls (if needed)
    initializeQuantityControls();
    
    // Initialize product image modal
    initializeProductModal();
});

function initializeMegaMenu() {
    console.log('Initializing mega menu...');
    const menuToggle = document.querySelector('.menu-toggle');
    const menuContent = document.querySelector('.menu-content');

    if (!menuToggle || !menuContent) {
        console.log('Mega menu elements not found');
        return;
    }

    // Menu Toggle Click Handler
    menuToggle.addEventListener('click', function(e) {
        e.stopPropagation();
        this.classList.toggle('active');
        menuContent.classList.toggle('active');
        console.log('Mega menu toggled');
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.mega-menu')) {
            menuToggle.classList.remove('active');
            menuContent.classList.remove('active');
        }
    });

    // Prevent closing when clicking inside menu
    menuContent.addEventListener('click', function(e) {
        e.stopPropagation();
    });
}

function initializeMobileMenu() {
    console.log('Initializing mobile menu...');
    // Mobile menu toggle
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuToggle && mobileMenu) {
        console.log('Mobile menu elements found');
        mobileMenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('Mobile menu toggle clicked');
            mobileMenu.classList.toggle('active');
            
            // Toggle icon between bars and times
            const icon = this.querySelector('i');
            if (icon) {
                if (icon.classList.contains('fa-bars')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    } else {
        console.log('Mobile menu elements not found:', { mobileMenuToggle, mobileMenu });
    }
    
    // Mobile category accordions
    const categoryHeaders = document.querySelectorAll('.mobile-category-header');
    console.log('Category headers found:', categoryHeaders.length);
    
    categoryHeaders.forEach(header => {
        header.addEventListener('click', function() {
            // Get the target ID from data attribute
            const targetId = this.getAttribute('data-target');
            const content = document.querySelector(targetId);
            console.log('Category clicked:', targetId);
            
            // Toggle active class on content
            if (content) {
                content.classList.toggle('active');
                
                // Toggle the chevron icon
                const icon = this.querySelector('i');
                if (icon.classList.contains('fa-chevron-down')) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                } else {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            }
        });
    });
}

function makeExternalLinksOpenInNewTab() {
    // Make external links open in new tab with proper rel attributes
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.host + '"])');
    
    externalLinks.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
}

function initializeToasts() {
    console.log('Initializing toasts...');
    
    // Initialize toasts if jQuery and Bootstrap are available
    if (typeof $ !== 'undefined' && typeof $.fn.toast !== 'undefined') {
        // Initialize all toasts with both auto and manual dismiss
        $('.toast').toast({
            autohide: true,
            delay: 5000  // Auto dismiss after 5 seconds
        });
        
        // Show all toasts
        $('.toast').toast('show');
        
        // Ensure close buttons work properly
        $('.toast .close, .toast .btn-close').off('click').on('click', function() {
            console.log('Toast close button clicked');
            $(this).closest('.toast').toast('hide');
        });
        
        // Clean up toasts when hidden
        $('.toast').on('hidden.bs.toast', function() {
            $(this).remove();
        });
    } else {
        console.log('jQuery or Bootstrap toast not available');
        
        // Fallback for vanilla JS
        document.querySelectorAll('.toast .close, .toast .btn-close').forEach(button => {
            button.addEventListener('click', function() {
                const toast = this.closest('.toast');
                if (toast) {
                    toast.style.opacity = '0';
                    setTimeout(() => {
                        toast.remove();
                    }, 300);
                }
            });
        });
        
        // Auto hide toasts after 5 seconds
        setTimeout(() => {
            document.querySelectorAll('.toast').forEach(toast => {
                toast.style.opacity = '0';
                setTimeout(() => {
                    toast.remove();
                }, 300);
            });
        }, 5000);
    }
}

function initializeQuantityControls() {
    // Quantity Controls
    const quantityControls = document.querySelectorAll('.quantity-control, .brutal-quantity-controls');
    
    quantityControls.forEach(control => {
        const input = control.querySelector('.quantity-input, .brutal-qty-input');
        const minusBtn = control.querySelector('.minus, .brutal-qty-btn.minus');
        const plusBtn = control.querySelector('.plus, .brutal-qty-btn.plus');
        
        if (!input || !minusBtn || !plusBtn) return;

        minusBtn.addEventListener('click', () => {
            const currentValue = parseInt(input.value) || 1;
            if (currentValue > 1) {
                input.value = currentValue - 1;
                input.dispatchEvent(new Event('change'));
            }
        });

        plusBtn.addEventListener('click', () => {
            const currentValue = parseInt(input.value) || 1;
            if (currentValue < 99) {
                input.value = currentValue + 1;
                input.dispatchEvent(new Event('change'));
            }
        });
    });
}

function initializeProductModal() {
    console.log('=== initializeProductModal CALLED ===');
    
    // Check what exists on the page
    console.log('Modal element:', document.getElementById('imageModal'));
    console.log('Image box element:', document.querySelector('.brutal-image-box'));
    console.log('Image element:', document.querySelector('.brutal-product__main-image'));
    
    // Only run on pages that have a modal
    const modal = document.getElementById('imageModal');
    if (!modal) {
        console.log('No modal found on this page - skipping modal initialization');
        return;
    }

    console.log('Modal found, initializing...');

    // Remove any existing onclick handlers to prevent conflicts
    const imageBox = document.querySelector('.brutal-image-box');
    if (imageBox) {
        imageBox.removeAttribute('onclick');
        
        // Add our clean click handler
        imageBox.addEventListener('click', function(e) {
            console.log('Image clicked, opening modal');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }

    // Clean close functionality
    const closeBtn = document.getElementById('modalClose');
    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            console.log('Close button clicked');
            e.stopPropagation();
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        });
    }

    // Click outside to close
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            console.log('Clicked outside modal');
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });

    // Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            console.log('Escape pressed');
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
}