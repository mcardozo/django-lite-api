# Django Lite API

A minimal Django project with Docker support. This project serves as a basic REST API template and includes a simple HTML homepage.

## Features

- 🐍 Django (Python 3.12)
- 🐳 Dockerized with a custom `Dockerfile`
- 🔌 REST API endpoint example
- 🎨 Static files and HTML template support
- 📁 Ready for deployment or further development

## Getting Started

### Requirements

- Docker
- Docker Compose (optional)

### Run the project

1. **Build the image**  
   ```bash
   docker build -t django-lite-api .
   ```

2. **Run the container**  
   ```bash
   docker run -p 8000:8000 django-lite-api
   ```

3. Visit `http://localhost:8000` to see the homepage.

## File structure

```
.
├── django_lite_api/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   └── ...
├── manage.py
├── Dockerfile
└── requirements.txt
```

## License

This project is licensed under the MIT License.
