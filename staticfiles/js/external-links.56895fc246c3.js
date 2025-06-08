// Add rel attributes to external links
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing external links handler...');
    
    // Select all links that point to external domains
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    
    // Add target and rel attributes
    externalLinks.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
});