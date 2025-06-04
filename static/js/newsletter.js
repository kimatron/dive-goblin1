document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.querySelector('#newsletter-form, .newsletter-form');
    
    if (newsletterForm) {
        console.log('EMERGENCY: Newsletter form found');
        
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('EMERGENCY: Form submitted');
            
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            // Send AJAX request
            fetch('/newsletter/signup/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                console.log('EMERGENCY: Got response:', data);
                
                // COMPLETELY BYPASS displayBrutalistToast and create toast directly
                showEmergencyToast(data.toast_html);
            })
            .catch(error => {
                console.error('EMERGENCY: Error:', error);
                alert('Network error occurred');
            });
        });
    }
});

function showEmergencyToast(htmlString) {
    console.log('EMERGENCY: Showing toast with HTML:', htmlString);
    
    // Remove any existing toasts
    const existingContainers = document.querySelectorAll('.emergency-toast-container');
    existingContainers.forEach(container => container.remove());
    
    // Create container
    const container = document.createElement('div');
    container.className = 'emergency-toast-container';
    container.style.cssText = `
        position: fixed;
        top: 50px;
        right: 50px;
        z-index: 999999;
    `;
    
    // USE THE ACTUAL HTML FROM BACKEND instead of hardcoded text
    container.innerHTML = htmlString;
    
    // Add close functionality to the new toast
    const closeButton = container.querySelector('.btn-close');
    if (closeButton) {
        closeButton.addEventListener('click', function() {
            container.remove();
        });
    }
    
    document.body.appendChild(container);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (container.parentNode) {
            container.remove();
        }
    }, 5000);
    
    console.log('EMERGENCY: Toast created and added to page');
} // ← THIS CLOSING BRACKET WAS MISSING!

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

console.log('EMERGENCY Newsletter.js loaded');