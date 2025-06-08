// Profile page functionality
// Initialize the profile page when DOM is loaded
function initializeProfilePage() {
    setupModalEventListeners();
    setupFormValidation();
}

// Modal Functions
function showEditForm() {
    document.getElementById('editModal').style.display = 'flex';
}

function hideEditForm() {
    document.getElementById('editModal').style.display = 'none';
}

function showDeleteForm() {
    document.getElementById('deleteModal').style.display = 'flex';
}

function hideDeleteForm() {
    document.getElementById('deleteModal').style.display = 'none';
}

// Event Listeners
function setupModalEventListeners() {
    // Close modals when clicking outside
    const editModal = document.getElementById('editModal');
    const deleteModal = document.getElementById('deleteModal');
    
    if (editModal) {
        editModal.addEventListener('click', function(e) {
            if (e.target === this) {
                hideEditForm();
            }
        });
    }
    
    if (deleteModal) {
        deleteModal.addEventListener('click', function(e) {
            if (e.target === this) {
                hideDeleteForm();
            }
        });
    }
    
    // ESC key to close modals
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            hideEditForm();
            hideDeleteForm();
        }
    });
}

// Form Validation
function setupFormValidation() {
    // Edit account form validation
    const editForm = document.querySelector('#editModal form');
    if (editForm) {
        editForm.addEventListener('submit', function(e) {
            const newPassword = document.getElementById('newPass').value;
            const confirmPassword = document.getElementById('confirmPass').value;
            
            if (newPassword && newPassword !== confirmPassword) {
                e.preventDefault();
                alert('New passwords do not match.');
                return false;
            }
            
            // Additional validation
            if (newPassword && newPassword.length < 8) {
                e.preventDefault();
                alert('New password must be at least 8 characters long.');
                return false;
            }
        });
    }
    
    // Delete account form validation
    const deleteForm = document.querySelector('#deleteModal form');
    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            const checkbox = document.getElementById('confirmCheck');
            const passwordField = document.querySelector('#deleteModal input[name="password"]');
            
            // Check if checkbox is checked
            if (!checkbox.checked) {
                e.preventDefault();
                alert('Please confirm account deletion by checking the box.');
                return false;
            }
            
            // Check if password is entered
            if (!passwordField.value.trim()) {
                e.preventDefault();
                alert('Please enter your password to confirm deletion.');
                return false;
            }
            
            // Final confirmation
            const confirmed = confirm('Are you ABSOLUTELY sure you want to delete your account? This action cannot be undone!');
            if (!confirmed) {
                e.preventDefault();
                return false;
            }
        });
    }
}

// Utility Functions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePassword(password) {
    // At least 8 characters, at least one letter and one number
    const re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/;
    return re.test(password);
}

// Form Enhancement Functions
function enhanceForms() {
    // Add real-time validation feedback
    const inputs = document.querySelectorAll('.form-input, .form-select, .form-textarea');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    
    // Remove any existing error styling
    clearFieldError(field);
    
    // Email validation
    if (fieldName === 'email' && value && !validateEmail(value)) {
        showFieldError(field, 'Please enter a valid email address');
        return false;
    }
    
    // Password validation for new password
    if (fieldName === 'new_password' && value && !validatePassword(value)) {
        showFieldError(field, 'Password must be at least 8 characters with letters and numbers');
        return false;
    }
    
    return true;
}

function showFieldError(field, message) {
    field.style.borderColor = '#ff3333';
    field.style.backgroundColor = '#ffebee';
    
    // Create or update error message
    let errorDiv = field.parentNode.querySelector('.field-error');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'field-error';
        errorDiv.style.color = '#ff3333';
        errorDiv.style.fontSize = '12px';
        errorDiv.style.marginTop = '5px';
        errorDiv.style.fontWeight = '700';
        field.parentNode.appendChild(errorDiv);
    }
    errorDiv.textContent = message;
}

function clearFieldError(field) {
    field.style.borderColor = '#000';
    field.style.backgroundColor = '#fff';
    
    const errorDiv = field.parentNode.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Profile Stats Animation
function animateStats() {
    const statValues = document.querySelectorAll('.stat-value');
    
    statValues.forEach(stat => {
        const finalValue = parseInt(stat.textContent) || 0;
        let currentValue = 0;
        const increment = Math.ceil(finalValue / 20);
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                stat.textContent = finalValue;
                clearInterval(timer);
            } else {
                stat.textContent = currentValue;
            }
        }, 50);
    });
}

// Profile Card Hover Effects
function setupCardEffects() {
    const profileCard = document.querySelector('.profile-card');
    const infoCards = document.querySelectorAll('.info-card');
    
    // Add subtle animations
    if (profileCard) {
        profileCard.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        profileCard.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    }
    
    // Info card effects
    infoCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translate(-2px, -2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translate(0, 0)';
        });
    });
}

// Bio Character Counter
function setupBioCounter() {
    const bioTextarea = document.querySelector('textarea[name="bio"]');
    if (bioTextarea) {
        const maxLength = 500;
        
        // Create counter element
        const counter = document.createElement('div');
        counter.className = 'bio-counter';
        counter.style.textAlign = 'right';
        counter.style.fontSize = '12px';
        counter.style.color = '#666';
        counter.style.marginTop = '5px';
        
        bioTextarea.parentNode.appendChild(counter);
        
        function updateCounter() {
            const remaining = maxLength - bioTextarea.value.length;
            counter.textContent = `${remaining} characters remaining`;
            
            if (remaining < 50) {
                counter.style.color = '#ff3333';
            } else {
                counter.style.color = '#666';
            }
        }
        
        bioTextarea.addEventListener('input', updateCounter);
        updateCounter(); // Initial count
    }
}

// Initialize all enhancements
function initializeEnhancements() {
    enhanceForms();
    setupCardEffects();
    setupBioCounter();
    
    // Animate stats on page load
    setTimeout(animateStats, 500);
}

// Call initialization after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeProfilePage();
    initializeEnhancements();
});