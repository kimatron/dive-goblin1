# Dive Goblin - Testing Documentation

## Table of Contents
1. [Validation Testing](#validation-testing)
2. [User Story Testing](#user-story-testing)
3. [Functionality Testing](#functionality-testing)
4. [Navigation Testing](#navigation-testing)
5. [CRUD Testing](#crud-testing)
6. [Authentication Testing](#authentication-testing)
7. [Payment Testing](#payment-testing)
8. [Newsletter Testing](#newsletter-testing)
9. [Form Testing](#form-testing)
10. [Responsiveness Testing](#responsiveness-testing)
11. [Browser Compatibility](#browser-compatibility)
12. [Accessibility Testing](#accessibility-testing)
13. [Performance Testing](#performance-testing)
14. [Known Bugs](#known-bugs)
15. [Bugs Fixed](#bugs-fixed)
16. [Future Testing](#future-testing)

---

## Validation Testing

### HTML Validation
| Page | Result | Evidence |
|------|---------|-----------|
| Home | Pass | [Screenshot](link-to-image) |
| Products | Pass | [Screenshot](link-to-image) |
| Product Detail | Pass | [Screenshot](link-to-image) |
| Bag | Pass | [Screenshot](link-to-image) |
| Checkout | Pass | [Screenshot](link-to-image) |
| Profile | Pass | [Screenshot](link-to-image) |

### CSS Validation
| File | Result | Evidence |
|------|---------|-----------|
| base.css | Pass | [Screenshot](link-to-image) |
| checkout.css | Pass | [Screenshot](link-to-image) |

### JavaScript Validation (JSHint)
| File | Result | Evidence |
|------|---------|-----------|
| stripe_elements.js | Pass | [Screenshot](link-to-image) |
| countryfield.js | Pass | [Screenshot](link-to-image) |

### Python Validation (PEP8)
| File | Result | Evidence |
|------|---------|-----------|
| settings.py | Pass | [Screenshot](link-to-image) |
| urls.py | Pass | [Screenshot](link-to-image) |
| models.py | Pass | [Screenshot](link-to-image) |

---

## User Story Testing

### User Story: Account Registration
| User Story ID | Feature | Test Description | Expected Result | Actual Result | Evidence |
|--------------|---------|------------------|-----------------|---------------|-----------|
| US01 | Registration | User can create account | Account created | As expected | [GIF](link-to-gif) |
| US02 | Login | User can login | Successfully logged in | As expected | [GIF](link-to-gif) |

### User Story: Shopping Experience
| User Story ID | Feature | Test Description | Expected Result | Actual Result | Evidence |
|--------------|---------|------------------|-----------------|---------------|-----------|
| US03 | Product Browsing | User can view products | Products displayed | As expected | [GIF](link-to-gif) |
| US04 | Add to Cart | User can add items | Item added to cart | As expected | [GIF](link-to-gif) |

---

## Functionality Testing

### Navigation Elements
| Element | Action | Expected Result | Actual Result | Pass/Fail |
|---------|--------|-----------------|---------------|-----------|
| Logo | Click | Redirect to home | As expected | ✅ |
| Shop Nav Link | Click | Open shop menu | As expected | ✅ |
| Cart Icon | Click | Open cart modal | As expected | ✅ |

### Product Functions
| Function | Action | Expected Result | Actual Result | Pass/Fail |
|----------|--------|-----------------|---------------|-----------|
| Sort Products | Select option | Products reorder | As expected | ✅ |
| Filter Products | Apply filter | Products filtered | As expected | ✅ |
| Product Search | Enter text | Relevant results | As expected | ✅ |

### Shopping Cart Functions
| Function | Action | Expected Result | Actual Result | Pass/Fail |
|----------|--------|-----------------|---------------|-----------|
| Add Item | Click add | Item added | As expected | ✅ |
| Update Quantity | Change number | Quantity updated | As expected | ✅ |
| Remove Item | Click remove | Item removed | As expected | ✅ |

---

## CRUD Testing

### Products
| Operation | Test Description | Expected Result | Actual Result | Evidence |
|-----------|------------------|-----------------|---------------|-----------|
| Create | Add new product | Product created | As expected | [Screenshot](link) |
| Read | View product | Product displayed | As expected | [Screenshot](link) |
| Update | Edit product | Product updated | As expected | [Screenshot](link) |
| Delete | Remove product | Product deleted | As expected | [Screenshot](link) |

---

## Authentication Testing

| Test Case | Description | Steps | Expected Result | Actual Result |
|-----------|-------------|-------|-----------------|---------------|
| Register | New user registration | 1. Click register<br>2. Fill form<br>3. Submit | Account created | Pass |
| Login | User login | 1. Enter credentials<br>2. Submit | Logged in | Pass |
| Password Reset | Reset password | 1. Click forgot<br>2. Enter email | Email sent | Pass |

---

## Payment Testing

### Stripe Integration
| Test Case | Card Number | Expected Result | Actual Result | Evidence |
|-----------|-------------|-----------------|---------------|-----------|
| Valid Payment | 4242424242424242 | Payment success | As expected | [GIF](link) |
| Invalid Card | 4000000000000002 | Payment failed | As expected | [GIF](link) |

---

## Newsletter Testing

| Test Case | Description | Expected Result | Actual Result | Evidence |
|-----------|-------------|-----------------|---------------|-----------|
| Subscribe | Valid email | Subscription successful | As expected | [Screenshot](link) |
| Invalid Email | Wrong format | Error message | As expected | [Screenshot](link) |

---

## Form Testing

### Contact Form
| Field | Test Case | Expected Result | Actual Result |
|-------|-----------|-----------------|---------------|
| Name | Empty field | Error message | Pass |
| Email | Invalid format | Error message | Pass |
| Message | < 10 chars | Error message | Pass |

### Checkout Form
| Field | Test Case | Expected Result | Actual Result |
|-------|-----------|-----------------|---------------|
| Phone | Invalid format | Error message | Pass |
| Address | Empty field | Error message | Pass |
| Post Code | Invalid format | Error message | Pass |

---

## Responsiveness Testing

### Device Testing Matrix
| Device | Screen Size | Browser | Result | Evidence |
|--------|-------------|---------|---------|-----------|
| iPhone 12 | 390x844 | Safari | Pass | [Screenshot](link) |
| iPad | 768x1024 | Chrome | Pass | [Screenshot](link) |
| Desktop | 1920x1080 | Firefox | Pass | [Screenshot](link) |

### Breakpoint Testing
| Breakpoint | Elements Tested | Expected Behavior | Result |
|------------|----------------|-------------------|--------|
| 320px | Nav menu | Collapses to burger | Pass |
| 768px | Product grid | 2 columns | Pass |
| 1024px | Footer | 4 columns | Pass |

---

## Browser Compatibility

| Browser | Version | Result | Evidence |
|---------|---------|--------|-----------|
| Chrome | 121.0 | Pass | [Screenshot](link) |
| Firefox | 123.0 | Pass | [Screenshot](link) |
| Safari | 17.0 | Pass | [Screenshot](link) |
| Edge | 121.0 | Pass | [Screenshot](link) |

---

## Accessibility Testing

### WAVE Testing Results
| Page | Errors | Warnings | Evidence |
|------|---------|----------|-----------|
| Home | 0 | 2 | [Screenshot](link) |
| Products | 0 | 1 | [Screenshot](link) |
| Checkout | 0 | 0 | [Screenshot](link) |

### Keyboard Navigation
| Function | Expected Behavior | Result |
|----------|------------------|--------|
| Tab Navigation | Sequential focus | Pass |
| Skip Links | Skip to content | Pass |
| Modal Escape | Close with ESC | Pass |

---

## Performance Testing

### Lighthouse Scores
| Page | Performance | Accessibility | Best Practices | SEO | Evidence |
|------|-------------|---------------|----------------|-----|-----------|
| Home | 95 | 100 | 92 | 100 | [Screenshot](link) |
| Products | 92 | 98 | 94 | 100 | [Screenshot](link) |
| Checkout | 90 | 100 | 95 | 98 | [Screenshot](link) |

### Load Time Testing
| Page | First Load | Cached Load | Evidence |
|------|------------|-------------|-----------|
| Home | 1.2s | 0.4s | [Report](link) |
| Products | 1.5s | 0.5s | [Report](link) |

---

## Known Bugs

| Bug ID | Description | Impact | Status |
|--------|-------------|--------|--------|
| BUG-001 | Newsletter form double submission | Low | Open |
| BUG-002 | Cart total delay update | Low | In Progress |

---

## Bugs Fixed

| Bug ID | Description | Solution | Evidence |
|--------|-------------|----------|-----------|
| BUG-001 | Mobile menu overlap | Adjusted z-index | [Before/After](link) |
| BUG-002 | Payment form timeout | Updated Stripe timeout | [Commit](link) |
| BUG-003 | Quantity increasing in odd numbers | Javascript was entered twice in .js file and .html, removed duplicated script in html | [Commit](link) |

Example Bug Fix:
```css
/* Before */
.mobile-menu {
    z-index: 100;
}

/* After */
.mobile-menu {
    z-index: 1001;
}
```

---

## Future Testing

### Planned Improvements
- Automated testing implementation
- API endpoint testing
- Load testing for high traffic
- Security penetration testing

### Future Test Cases
1. Multiple item discount calculations
2. Bulk order processing
3. International shipping calculations
4. Regional tax compliance

---




# Dive Goblin Testing Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Test Environment Setup](#test-environment-setup)
3. [Unit Testing](#unit-testing)
4. [Integration Testing](#integration-testing)
5. [End-to-End Testing](#end-to-end-testing)
6. [Manual Testing](#manual-testing)
7. [Test Cases](#test-cases)
8. [Test Results](#test-results)
9. [Conclusion](#conclusion)

## Introduction
This document provides a comprehensive overview of the testing strategy and results for the Dive Goblin e-commerce project. It includes details on unit, integration, end-to-end, and manual testing.

## Test Environment Setup
1. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
2. Install testing dependencies:
    ```bash
    pip install -r requirements-test.txt
    ```

## Unit Testing
Unit tests are written using the `unittest` framework to verify the functionality of individual components.

### Example Unit Test
```python
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Dive Mask", price=29.99)
        self.assertEqual(product.name, "Dive Mask")
        self.assertEqual(product.price, 29.99)


