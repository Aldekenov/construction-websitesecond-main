# Django Admin Guide: Concrete Actions by App

This guide details exactly what you can do in the Django Admin for each app in your Construction Website project.

---

## Calendar App (`calendar_app`)

### ProjectDeadline
- **Add/Edit/Delete project deadlines** (e.g., for jobs, deliverables, or phases)
- Set:
  - Title, description, client name, project location
  - Deadline date, priority (low/medium/high/urgent), status (pending/in progress/completed/delayed)
  - Assign to a user (staff)
  - Estimated cost, completion notes
- **Inline manage milestones** for each deadline (add/edit/delete milestones directly from the deadline admin page)
- **List view:**
  - See deadlines with title, client, date, status, priority, assigned user, and overdue status (color-coded)
  - Filter by status, priority, assigned user, and date
  - Search by title, client, location, or description
  - Edit status, priority, and assigned user directly in the list

### ProjectMilestone
- **Add/Edit/Delete milestones** (linked to a project deadline)
- Set:
  - Title, description, target date, completed status, completion date, notes
- **List view:**
  - See milestones with project, title, target date, completed status
  - Filter by completed status and date
  - Search by title, project, or client
  - Edit completed status directly in the list

---

## Blog App (`blog`)

### BlogPost
- **Add/Edit/Delete blog posts**
- Set:
  - Title, slug, author, content (rich text), excerpt, featured image
  - Published and featured status
- **List view:**
  - See posts with title, author, published/featured status, date, and image preview
  - Filter by published/featured status, author, date
  - Search by title, content, excerpt
  - Edit published/featured status directly in the list

### BlogCategory
- **Add/Edit/Delete categories**
- Set name, slug, description

### BlogPostCategory
- **Link posts to categories**
- Filter by category

---

## Core App (`core`)

### CompanyInfo
- **Edit main company info** (only one allowed)
  - Name, tagline, about us, mission, years experience, projects completed, happy clients, logo, hero image
  - Cannot delete or add more than one

### Service
- **Add/Edit/Delete services**
- Set name, description, icon, image, active status, order
- Edit active/order directly in the list

### Testimonial
- **Add/Edit/Delete testimonials**
- Set client name, position, company, testimonial text, rating (1-5), client image, featured status
- Edit featured status directly in the list

### ProjectGallery
- **Add/Edit/Delete gallery images**
- Set title, description, image, category, completion date, featured status, order
- Edit featured/order directly in the list

---

## Contact App (`contact`)

### ContactForm
- **View contact form submissions** (cannot add manually)
- See name, email, type, subject, message, date, read/responded status
- Filter by type, read/responded status, date
- Edit read/responded status directly in the list

### ContactInfo
- **Edit company contact info** (only one allowed)
  - Name, address, phone, email, business hours, emergency phone
  - Cannot delete or add more than one

---

## Users
- **Add/Edit/Delete users and staff**
- Assign permissions and groups

---

For more, see the Django docs: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
