# Mujadadi Group Website

Africa's premier diversified conglomerate website built with Django.

## Features
- 7 Business Units: Agriculture, Pharmacy, Supply Chain, Logistics, Contracting, Energy, Real Estate
- Admin-managed content and images
- Responsive design
- SEO optimized

## Setup
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`

## Admin Access
- URL: `/admin/`
- Username: `admin`
- Password: `admin123`

## Deployment
1. Set environment variables from `.env.example`
2. Set `DEBUG=False`
3. Configure `ALLOWED_HOSTS`
4. Use production database
5. Collect static files: `python manage.py collectstatic`