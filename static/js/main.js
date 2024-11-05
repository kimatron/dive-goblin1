document.addEventListener('DOMContentLoaded', function() {
    initializeMegaMenu();
    initializeQuantityControls();
    initializeModal();
});

function initializeMegaMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const menuContent = document.querySelector('.menu-content');

    if (!menuToggle || !menuContent) return;

    // Menu Toggle Click Handler
    menuToggle.addEventListener('click', function(e) {
        e.stopPropagation();
        menuToggle.classList.toggle('active');
        menuContent.classList.toggle('active');
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

    // Mobile Menu Accordion
    function initializeMobileMenu() {
        const menuColumns = document.querySelectorAll('.menu-column');
        
        menuColumns.forEach(column => {
            const heading = column.querySelector('h3');
            const list = column.querySelector('ul');
            
            if (heading && list && window.innerWidth <= 768) {
                heading.style.cursor = 'pointer';
                
                heading.addEventListener('click', () => {
                    menuColumns.forEach(col => {
                        const colList = col.querySelector('ul');
                        const isCurrentColumn = col === column;
                        
                        if (colList) {
                            colList.style.display = isCurrentColumn && 
                                                  colList.style.display !== 'block' ? 'block' : 'none';
                        }
                    });
                });
            }
        });
    }

    initializeMobileMenu();
    window.addEventListener('resize', initializeMobileMenu);
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

function initializeModal() {
    const modalClose = document.querySelector('.brutal-modal__close');
    const imageModal = document.getElementById('imageModal');
    const modalContent = document.querySelector('.brutal-modal__content');

    if (modalClose && imageModal) {
        // Close button click
        modalClose.addEventListener('click', () => {
            imageModal.classList.remove('active');
        });

        // Click outside modal
        imageModal.addEventListener('click', (e) => {
            if (e.target === imageModal) {
                imageModal.classList.remove('active');
            }
        });

        // Prevent closing when clicking modal content
        if (modalContent) {
            modalContent.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        }
    }
}

// Initialize toasts if they exist
if (document.querySelector('.toast')) {
    $('.toast').toast({
        autohide: true,
        delay: 5000,
        animation: true
    });
    
    $('.toast').toast('show');
    
    $('.btn-close').on('click', function() {
        $(this).closest('.toast').toast('hide');
    });
    
    $('.toast').on('hidden.bs.toast', function() {
        $(this).remove();
    });
}

// For Option 3: Sliding Drawer
function initializeSlidingBanner() {
    const banner = document.querySelector('.delivery-banner');
    const trigger = document.createElement('button');
    trigger.className = 'banner-trigger';
    trigger.innerHTML = 'Delivery Info <i class="fas fa-truck"></i>';
    
    let isVisible = false;
    
    trigger.addEventListener('click', () => {
        isVisible = !isVisible;
        banner.classList.toggle('visible', isVisible);
    });
    
    document.body.appendChild(trigger);
}


document.addEventListener('DOMContentLoaded', function() {
 
    // initializeCollapsibleBanner();
     initializeFloatingBanner();
    // initializeSlidingBanner();
});

document.addEventListener('DOMContentLoaded', function() {
    const logoutForm = document.querySelector('.logout-form');
    const submitBtn = logoutForm.querySelector('button[type="submit"]');

    logoutForm.addEventListener('submit', function(e) {
        submitBtn.classList.add('loading');
        submitBtn.textContent = 'Signing Out...';
    });
});