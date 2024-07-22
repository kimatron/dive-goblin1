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

Dive Goblin operates on a B2C (Business to Consumer) e-commerce business model, focusing on providing a wide range of high-quality dive gear, watersports apparel, and related travel products directly to consumers. The business model is designed to offer a seamless shopping experience, from browsing products to making purchases and receiving orders.

### Key Components of Our Business Model

1. **Product Offering**: 
    - **Diving Gear**: A comprehensive range of equipment for recreational and professional diving.
    - **Watersports Apparel**: Clothing and accessories suitable for various watersports activities.
    - **Travel Products**: Items specifically curated for dive and watersports travel needs.

2. **Revenue Streams**:
    - **Direct Sales**: Revenue generated from the sale of products through the Dive Goblin website.
    - **Membership and Subscription**: Potential future streams from exclusive member benefits, early access to new products, and periodic subscription boxes.
    - **Affiliate Partnerships**: Revenue from partnerships with related travel and adventure companies.

### Marketing Strategies

1. **Search Engine Optimization (SEO)**:
    - **Keyword Optimization**: Implementing high-ranking keywords related to diving and watersports throughout the website content.
    - **Meta Tags and Descriptions**: Crafting precise meta tags and descriptions to enhance search engine visibility.
    - **Content Marketing**: Regularly updating the blog with articles, tips, and guides related to diving and watersports to attract organic traffic.

2. **Social Media Marketing**:
    - **Platform Presence**: Active engagement on major social media platforms such as Facebook, Instagram, and Twitter to build a community.
    - **Content Strategy**: Posting high-quality images, videos, and user-generated content to promote products and engage with the audience.
    - **Influencer Collaborations**: Partnering with influencers and industry experts to expand reach and credibility.

3. **Email Marketing**:
    - **Newsletter Campaigns**: Regular newsletters featuring product updates, special promotions, and industry news to keep customers informed and engaged.
    - **Personalized Emails**: Utilizing customer data to send personalized product recommendations and offers.

4. **Paid Advertising**:
    - **PPC Campaigns**: Running pay-per-click advertising campaigns on platforms like Google Ads and Facebook Ads to drive targeted traffic.
    - **Retargeting Ads**: Using retargeting strategies to convert visitors who have shown interest in our products but haven't made a purchase.

5. **Content Marketing**:
    - **Blog**: Maintaining a blog with informative articles about diving tips, gear reviews, travel destinations, and safety guidelines.
    - **Video Content**: Creating and sharing engaging videos showcasing product demonstrations, adventure stories, and customer testimonials.

6. **Customer Engagement**:
    - **Customer Reviews and Testimonials**: Encouraging customers to leave reviews and share their experiences to build trust and credibility.
    - **Loyalty Programs**: Developing loyalty programs to reward repeat customers with discounts, exclusive offers, and early access to new products.

### Future Plans

Dive Goblin aims to continuously evolve and expand by:
- **Expanding Product Range**: Introducing new product categories and exclusive items.
- **Global Reach**: Enhancing international shipping capabilities to reach a broader audience.
- **Community Building**: Organizing events, workshops, and webinars to foster a community of dive and watersports enthusiasts.

By leveraging these strategies, Dive Goblin aims to establish itself as a leading e-commerce platform in the dive and watersports industry, delivering exceptional value and experiences to its customers.


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
