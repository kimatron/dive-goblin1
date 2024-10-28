
document.addEventListener('DOMContentLoaded', function() {
    // Mega Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const menuContent = document.querySelector('.menu-content');

    menuToggle.addEventListener('click', function() {
        menuContent.style.display = menuContent.style.display === 'block' ? 'none' : 'block';
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.mega-menu')) {
            menuContent.style.display = 'none';
        }
    });

    // Prevent menu from closing when clicking inside
    menuContent.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Quantity controls
    document.querySelectorAll('.quantity-control').forEach(control => {
        const input = control.querySelector('.quantity-input');
        const minusBtn = control.querySelector('.minus');
        const plusBtn = control.querySelector('.plus');

        minusBtn.addEventListener('click', () => {
            const currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
            }
        });

        plusBtn.addEventListener('click', () => {
            const currentValue = parseInt(input.value);
            if (currentValue < 99) {
                input.value = currentValue + 1;
            }
        });
    });
});

// Add to your main.js or in a script tag in your template
document.addEventListener('DOMContentLoaded', function() {
    // Quantity buttons
    const minusButtons = document.querySelectorAll('.brutal-qty-btn.minus');
    const plusButtons = document.querySelectorAll('.brutal-qty-btn.plus');
    
    minusButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const itemId = this.getAttribute('data-item_id');
            const input = document.querySelector(`#id_qty_${itemId}`);
            const currentValue = parseInt(input.value);
            if (currentValue > 1) {
                input.value = currentValue - 1;
            }
        });
    });
    
    plusButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const itemId = this.getAttribute('data-item_id');
            const input = document.querySelector(`#id_qty_${itemId}`);
            const currentValue = parseInt(input.value);
            if (currentValue < 99) {
                input.value = currentValue + 1;
            }
        });
    });
});

// Add to static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Mega Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const menuContent = document.querySelector('.menu-content');

    menuToggle.addEventListener('click', function() {
        menuToggle.classList.toggle('active');
        menuContent.classList.toggle('active');
    });

    // Mobile Menu Accordion
    if (window.innerWidth <= 991) {
        const menuColumns = document.querySelectorAll('.menu-column');
        
        menuColumns.forEach(column => {
            const heading = column.querySelector('h3');
            heading.addEventListener('click', () => {
                // Close other columns
                menuColumns.forEach(otherColumn => {
                    if (otherColumn !== column) {
                        otherColumn.classList.remove('active');
                    }
                });
                // Toggle current column
                column.classList.toggle('active');
            });
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.mega-menu')) {
            menuToggle.classList.remove('active');
            menuContent.classList.remove('active');
        }
    });

    // Stop propagation for menu content clicks
    menuContent.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});


document.querySelector('.brutal-modal__close').addEventListener('click', function() {
    document.getElementById('imageModal').classList.remove('active');
});

// Close modal when clicking outside the image
document.getElementById('imageModal').addEventListener('click', function(e) {
    if (e.target === this) {
        this.classList.remove('active');
    }
});

// Prevent closing when clicking the image itself
document.querySelector('.brutal-modal__content').addEventListener('click', function(e) {
    e.stopPropagation();
});