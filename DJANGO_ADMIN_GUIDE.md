# Django Admin Guide for Construction Website

This documentation describes what you can do in the Django Admin for your Construction Website project.

## Accessing Django Admin

1. Go to `/admin` in your browser (e.g., http://127.0.0.1:8000/admin/).
2. Log in with your superuser credentials.

## What You Can Manage in Django Admin

### 1. Blog
- **Posts:** Add, edit, or delete blog posts.
- **Categories/Tags:** (If implemented) Manage categories or tags for blog posts.

### 2. Calendar App
- **Events:** Add, edit, or delete project deadlines, milestones, or other calendar events.

### 3. Contact
- **Contact Messages:** View messages submitted via the contact form.
- **Contact Info:** (If implemented) Edit company contact details shown on the website.

### 4. Core
- **Company Info:** Edit company name, tagline, about us, and other core information.
- **Gallery:** Add, edit, or delete images in the gallery.
- **Services:** Add, edit, or delete services offered by the company.
- **Testimonials:** Add, edit, or delete client testimonials shown on the homepage.

### 5. Users
- **User Accounts:** Add, edit, or delete admin users and staff.
- **Permissions:** Assign permissions and groups to control access.

## Typical Admin Actions
- **Add:** Click "Add" next to a model to create a new entry.
- **Edit:** Click an item in the list to edit it.
- **Delete:** Select items and use the "Delete selected" action.
- **Search/Filter:** Use the search bar and filters to find specific entries.

## Customization
- The admin interface can be customized for better usability (e.g., list display, filters, search fields).
- Some models may have inline editing for related objects.

## Notes
- Only users with staff or superuser status can access the admin.
- Be careful when deleting items, as this may affect what is shown on the public site.

---
For more details, see the Django documentation: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
