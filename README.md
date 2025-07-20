# Marvin's Blog

A simple Django-powered blog application with user authentication, post management, and a modern Bootstrap interface.

## Live Demo

Visit the live site: [https://marvinblog.com](https://marvinblog.com)

## Features

- User registration, login, and logout
- Create, edit, and delete blog posts (only by the author)
- Posts ordered by latest first
- Responsive design using Bootstrap 5
- Friendly navigation bar and footer with contact/social links
- Only authenticated users can create posts

## Tech Stack

- Python 3
- Django 5
- Bootstrap 5
- SQLite (default)

## Getting Started

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd blog_project
   ```

2. **Install dependencies**
   ```sh
   pip install django
   ```

3. **Apply migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

6. **Access the app**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Folder Structure

- `blog/` - Blog app (models, views, templates)
- `accounts/` - User registration app
- `templates/` - All HTML templates (Bootstrap styled)
- `blog_project/` - Project settings and URLs

## Customization

- Update contact info and social links in `templates/base.html` footer.
- Change blog name in the navbar in `base.html`.

## License

This project is for learning and demonstration purposes.