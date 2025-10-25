# Mujadadi Group - Admin Management Guide

## Admin Panel Access

### Login URL
- **Development**: `http://localhost:8000/admin/`
- **Production**: `https://yourdomain.com/admin/`

### Current Credentials
- **Username**: Mujadadi
- **Password**: [Your updated secure password]

## Admin Panel Features

### 1. Categories (Business Units)
- **Purpose**: Manage the 7 business subsidiaries
- **Required Slugs**: 
  - `agric` (Agriculture)
  - `pharmacy` (Pharmacy & Labs)
  - `supply-chain` (Supply Chain)
  - `logistics` (Logistics)
  - `contractor` (Contracting)
  - `energy` (Energy)
  - `real-estate` (Real Estate)

### 2. Services
- Add services for each business unit
- Upload service images
- Write descriptions

### 3. Gallery
- Upload project images
- Mark as "featured" for homepage display
- Organize by business unit

### 4. Hero Images
- Manage homepage carousel images
- Set display order
- Enable/disable images

### 5. Contact Information
- Update company addresses
- Manage phone numbers (separate with |)
- Update email and social media

### 6. Team Members
- Add team profiles with photos
- Categories: Executive, Management, Staff, Advisor
- Set display order

### 7. Contact Messages
- View form submissions
- Mark as read/unread
- Export data if needed

### 8. Job Applications
- Review submitted CVs
- Download application files
- Track application status

### 9. Newsletter
- Create email campaigns
- Send to subscribers
- Track delivery status

## Security Best Practices

### Password Management
```bash
# Change admin password
python manage.py changepassword admin

# Create additional admin user
python manage.py createsuperuser
```

### Access Control
- Use strong passwords (12+ characters)
- Enable 2FA if available
- Regular password updates
- Limit admin user accounts

## Content Management Workflow

### Adding New Business Unit
1. Go to Categories
2. Add new category with proper slug
3. Add services under that category
4. Upload gallery images
5. Update navigation if needed

### Managing Team
1. Go to Team Members
2. Upload high-quality photos (square format recommended)
3. Write professional bios (300 chars max)
4. Set appropriate category and order

### Updating Contact Info
1. Go to Contact Information
2. Update addresses, phones, email
3. Changes reflect site-wide immediately

## Troubleshooting

### Can't Access Admin
- Check URL is correct (/admin/)
- Verify credentials
- Ensure user has superuser status

### Images Not Displaying
- Check file permissions
- Verify MEDIA_URL settings
- Ensure images are uploaded correctly

### Email Not Working
- Check SMTP settings in .env
- Verify email credentials
- Test with simple contact form

## Backup Procedures

### Database Backup
```bash
python manage.py dumpdata > backup.json
```

### Media Files Backup
- Backup entire `/media/` folder
- Include uploaded images, CVs, documents

## Support
- Technical Issues: Check Django logs
- Content Questions: Refer to this guide
- Emergency: Contact system administrator