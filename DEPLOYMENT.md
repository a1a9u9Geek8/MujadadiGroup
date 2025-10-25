# Mujadadi Group - Cloudflare Pages Deployment

## Domain: mujadadigroup.com

## Pre-Deployment Requirements

### 1. Environment Configuration
- [ ] Set environment variables in Cloudflare Pages dashboard
- [ ] Set `DEBUG=False` in production
- [ ] Domain configured: `mujadadigroup.com` and `www.mujadadigroup.com`
- [ ] Generate new `SECRET_KEY` for production
- [ ] Email settings already configured with Gmail SMTP

### 2. Database Setup
- [ ] Run `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] **IMPORTANT**: Use strong credentials for production admin
- [ ] Load initial data via admin panel

### 3. Static Files
- [ ] Run `python manage.py collectstatic`
- [ ] Configure web server to serve static files

### 4. Security
- [ ] Ensure HTTPS is configured
- [ ] Security headers are enabled (already in settings.py)
- [ ] File upload limits are set (5MB max)

## Cloudflare Pages Deployment Steps

### 1. Repository Setup
1. Push code to GitHub repository
2. Ensure all files are committed:
   - `runtime.txt` (Python version)
   - `Procfile` (Web server config)
   - `build.sh` (Build script)
   - `_redirects` (URL routing)
   - Updated `requirements.txt`

### 2. Cloudflare Pages Configuration
1. Login to Cloudflare Dashboard
2. Go to Pages → Create a project
3. Connect GitHub repository
4. Set build settings:
   - **Build command**: `chmod +x build.sh && ./build.sh`
   - **Build output directory**: `/`
   - **Root directory**: `/`

### 3. Environment Variables
Set in Cloudflare Pages → Settings → Environment variables:
```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=mujadadigroup.com,www.mujadadigroup.com,*.pages.dev
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=mujadadigroup@gmail.com
EMAIL_HOST_PASSWORD=ljjpzjoqqfqduurw
DEFAULT_FROM_EMAIL=mujadadigroup@gmail.com
DISPLAY_EMAIL=info@mujadadi.com
```

### 4. Custom Domain Setup
1. Go to Pages → Custom domains
2. Add `mujadadigroup.com`
3. Add `www.mujadadigroup.com`
4. Configure DNS records in Cloudflare DNS
5. Enable SSL/TLS (Full mode)

## Post-Deployment Verification

### Test All Features:
- [ ] Homepage loads at `https://mujadadigroup.com`
- [ ] All 7 business unit pages work
- [ ] Contact form sends emails to `mujadadigroup@gmail.com`
- [ ] Job application form accepts CV uploads
- [ ] Admin panel accessible at `/admin/`
- [ ] Static files loading (CSS, images)
- [ ] Mobile responsiveness
- [ ] SSL certificate working (Cloudflare SSL)
- [ ] Both `mujadadigroup.com` and `www.mujadadigroup.com` work
- [ ] Email display shows `info@mujadadi.com` and `partnerships@mujadadi.com`

### Admin Panel Setup:
1. Login to `/admin/` with your credentials
2. Add Categories for all 7 business units
3. Upload hero images
4. Add team members
5. Configure contact information
6. Test email functionality

## Admin Access & Management

### Accessing Admin Panel:
- **URL**: `https://mujadadigroup.com/admin/`
- **Username**: Mujadadi
- **Password**: MujadadiGroup2024! (change after first login)

### Admin Features Available:
- **Categories**: Manage 7 business units
- **Services**: Add/edit services for each unit
- **Gallery**: Upload project images
- **Hero Images**: Manage homepage carousel
- **Contact Info**: Update company contact details
- **Team Members**: Add/edit team profiles
- **Contact Messages**: View form submissions
- **Job Applications**: Review CVs and applications
- **Newsletter**: Send bulk emails to subscribers

### Creating Additional Admin Users:
```bash
python manage.py createsuperuser
```

### Changing Admin Password:
```bash
python manage.py changepassword Mujadadi
```

## Monitoring & Maintenance
- [ ] Set up error logging
- [ ] Monitor email delivery
- [ ] Regular database backups
- [ ] Monitor file uploads storage
- [ ] Regular admin password updates

## Support
- Email: info@mujadadi.com
- Admin Panel: /admin/ (secure credentials required)