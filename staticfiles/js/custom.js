// Document Ready Handler
document.addEventListener('DOMContentLoaded', function() {
    initExternal();
    initToasts();
});

// Toggle categories menu
function toggleCategories() {
    const menu = document.getElementById('categoryMenu');
    const toggle = document.querySelector('.category-toggle');
    
    if (menu.classList.contains('active')) {
        menu.classList.remove('active');
        toggle.classList.remove('active');
    } else {
        menu.classList.add('active');
        toggle.classList.add('active');
    }
}

// Add proper rel attributes to external links
function initExternal() {
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.host + '"])');
    
    externalLinks.forEach(function(link) {
        // Add target="_blank" if not already present
        if (!link.hasAttribute('target')) {
            link.setAttribute('target', '_blank');
        }
        
        // Add proper rel attributes for SEO and security
        const rel = link.getAttribute('rel');
        const attrs = ['noopener', 'noreferrer'];
        
        if (link.href.includes('facebook.com') || 
            link.href.includes('twitter.com') || 
            link.href.includes('instagram.com') || 
            link.href.includes('linkedin.com')) {
            attrs.push('external');
        }
        
        if (rel) {
            const currentAttrs = rel.split(' ');
            attrs.forEach(attr => {
                if (!currentAttrs.includes(attr)) {
                    currentAttrs.push(attr);
                }
            });
            link.setAttribute('rel', currentAttrs.join(' '));
        } else {
            link.setAttribute('rel', attrs.join(' '));
        }
    });
}

// Initialize toasts
function initToasts() {
    if (typeof $ !== 'undefined' && typeof $.fn.toast !== 'undefined') {
        $('.toast').toast({
            autohide: true,
            delay: 5000
        });
        
        $('.toast').toast('show');
        
        $('.toast .close, .toast .btn-close').on('click', function() {
            $(this).closest('.toast').toast('hide');
        });
    }
}