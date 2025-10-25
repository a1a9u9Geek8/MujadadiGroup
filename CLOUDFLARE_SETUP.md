# Cloudflare Pages Deployment Guide

## Domain: mujadadigroup.com

## Step-by-Step Deployment

### 1. GitHub Repository
1. Create GitHub repository: `mujadadi-group-website`
2. Push all code to repository
3. Ensure these files are included:
   - `runtime.txt` - Python version
   - `Procfile` - Web server configuration
   - `build.sh` - Build script
   - `_redirects` - URL routing
   - `requirements.txt` - Dependencies

### 2. Cloudflare Pages Setup
1. Login to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Go to **Pages** → **Create a project**
3. Select **Connect to Git**
4. Choose your GitHub repository
5. Configure build settings:
   ```
   Framework preset: None
   Build command: chmod +x build.sh && ./build.sh
   Build output directory: /
   Root directory: (leave empty)
   ```

### 3. Environment Variables
In Cloudflare Pages → Settings → Environment variables, add:

**Production Variables:**
```
SECRET_KEY=django-insecure-CHANGE-THIS-IN-PRODUCTION
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

### 4. Custom Domain Configuration
1. Go to **Pages** → Your project → **Custom domains**
2. Add custom domain: `mujadadigroup.com`
3. Add www subdomain: `www.mujadadigroup.com`
4. Cloudflare will provide DNS records to configure

### 5. DNS Configuration
In Cloudflare DNS, add these records:
```
Type: CNAME
Name: mujadadigroup.com
Target: your-project.pages.dev
Proxy: Enabled (Orange cloud)

Type: CNAME  
Name: www
Target: your-project.pages.dev
Proxy: Enabled (Orange cloud)
```

### 6. SSL/TLS Configuration
1. Go to **SSL/TLS** → **Overview**
2. Set encryption mode to **Full (strict)**
3. Enable **Always Use HTTPS**
4. Enable **HTTP Strict Transport Security (HSTS)**

### 7. Post-Deployment Setup
1. Visit `https://mujadadigroup.com/admin/`
2. Login with:
   - Username: `Mujadadi`
   - Password: `MujadadiGroup2024!`
3. **IMMEDIATELY** change admin password
4. Add business unit categories
5. Upload hero images
6. Configure contact information
7. Test email functionality

## Required Business Unit Categories
Add these categories in admin with exact slugs:
- `agric` - Agriculture
- `pharmacy` - Pharmacy & Labs  
- `supply-chain` - Supply Chain
- `logistics` - Logistics
- `contractor` - Contracting
- `energy` - Energy
- `real-estate` - Real Estate

## Email Configuration
- **Display Emails**: `info@mujadadi.com`, `partnerships@mujadadi.com`
- **Backend Email**: `mujadadigroup@gmail.com`
- **SMTP**: Gmail with app password

## Security Checklist
- [ ] Change default admin password
- [ ] Generate new SECRET_KEY for production
- [ ] Verify HTTPS is working
- [ ] Test all forms send emails
- [ ] Verify file uploads work
- [ ] Check mobile responsiveness
- [ ] Test all 7 business unit pages

## Monitoring
- Cloudflare Analytics for traffic
- Email delivery monitoring
- Regular admin panel checks
- Database backups (if using external DB)

## Support
- **Website**: https://mujadadigroup.com
- **Admin**: https://mujadadigroup.com/admin/
- **Email**: info@mujadadi.com