document.addEventListener('DOMContentLoaded', function() {
    console.log('Document ready, initializing components...');
    
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
    // Initialize toasts if jQuery and Bootstrap are available
    if (typeof $ !== 'undefined' && typeof $.fn.toast !== 'undefined') {
        $('.toast').toast({
            autohide: false
        });
        
        $('.toast').toast('show');
        
        $('.toast .close, .toast .btn-close').on('click', function() {
            $(this).closest('.toast').toast('hide');
        });
        
        $('.toast').on('hidden.bs.toast', function() {
            $(this).remove();
        });
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