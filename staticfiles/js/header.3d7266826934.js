document.addEventListener('DOMContentLoaded', function() {
    // Mega Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const menuContent = document.querySelector('.menu-content');

    if (menuToggle && menuContent) {
        menuToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            this.classList.toggle('active');
            menuContent.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.mega-menu')) {
                menuToggle.classList.remove('active');
                menuContent.classList.remove('active');
            }
        });

        // Prevent menu from closing when clicking inside
        menuContent.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }

    // Mobile Menu Accordion
    function initMobileMenu() {
        const menuColumns = document.querySelectorAll('.menu-column');
        
        menuColumns.forEach(column => {
            const heading = column.querySelector('h3');
            const list = column.querySelector('ul');
            
            if (heading && window.innerWidth <= 768) {
                heading.style.cursor = 'pointer';
                list.style.display = 'none';
                
                heading.addEventListener('click', () => {
                    const isOpen = list.style.display === 'block';
                    
                    // Close all lists
                    menuColumns.forEach(col => {
                        col.querySelector('ul').style.display = 'none';
                    });
                    
                    // Open clicked list if it was closed
                    if (!isOpen) {
                        list.style.display = 'block';
                    }
                });
            }
        });
    }

    // Initialize mobile menu
    initMobileMenu();
    
    // Reinitialize on resize
    window.addEventListener('resize', initMobileMenu);
});