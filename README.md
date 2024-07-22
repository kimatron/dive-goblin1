# Dive Goblin E-Commerce Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Custom Models](#custom-models)
4. [Forms and UI Elements](#forms-and-ui-elements)
5. [Agile Methodologies](#agile-methodologies)
6. [SEO and Marketing](#seo-and-marketing)
7. [Digital Marketing](#digital-marketing)
8. [E-Commerce Business Model](#e-commerce-business-model)
9. [Technical Setup](#technical-setup)
10. [Testing](#testing)
11. [Development and Deployment](#development-and-deployment)

## Project Overview
Dive Goblin is an e-commerce platform specializing in dive gear, watersports apparel, and travel-related products. Our goal is to provide enthusiasts with high-quality products and exceptional user experience.

## Features
- User registration, login, and logout functionality
- E-commerce functionality to browse, search, and purchase products
- Custom admin and user interfaces for managing products and orders
- Newsletter signup form for marketing purposes
- Custom 404 error page
- SEO optimized with robots.txt, sitemap.xml, and meta tags

## Custom Models
1. **Product**: Manages the details of dive gear and watersports apparel, including categories, prices, descriptions, and stock levels.
2. **Order**: Handles customer orders, including order status, payment information, and shipping details.
3. **CustomerProfile**: Stores additional information about customers, such as address, order history, and preferences.

## Forms and UI Elements
- **CRUD Form**: A front-end form allowing users to add, edit, and delete products without accessing the admin panel.
- **Delete UI Element**: A front-end interface that allows users to delete records (e.g., products, orders) directly from the UI.

## Agile Methodologies
The development of Dive Goblin followed Agile methodologies, with detailed evidence available in our GitHub repository. This includes:
- User stories and acceptance criteria
- Sprint planning and retrospectives
- Continuous integration and delivery

## SEO and Marketing
- **robots.txt**: Configured to manage web crawler access.
- **sitemap.xml**: Generated to improve search engine indexing.
- **Meta Tags**: Descriptive meta tags included in HTML for better SEO.
- **External Link**: Included a link to an external resource with a `rel` attribute for improved SEO.

## Digital Marketing
- **Facebook Business Page**: A real/mockup Facebook business page for Dive Goblin.
- **Newsletter Signup Form**: Integrated to capture user emails for marketing campaigns.

## E-Commerce Business Model
Dive Goblin operates on a B2C (Business to Consumer) model, focusing on providing high-quality dive gear and watersports apparel to individual customers. Our marketing strategies include:
- **SEO Optimization**: Improving search engine visibility through meta tags, sitemaps, and quality content.
- **Social Media Marketing**: Leveraging platforms like Facebook to engage with our community and promote products.
- **Email Marketing**: Using the newsletter signup form to send targeted promotions and updates to subscribers.

## Technical Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/kimatron/dive-goblin1.git
    ```
2. Navigate to the project directory:
    ```bash
    cd dive-goblin
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Testing
Detailed testing documentation can be found in the [TESTING.md](TESTING.md) file.

## Development and Deployment
- **DEBUG Mode**: Ensure `DEBUG = False` in the settings file before deployment.
- **Deployment**: Instructions for deploying the project to a production environment are provided in the deployment section of this documentation.
