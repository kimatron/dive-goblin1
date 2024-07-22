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
