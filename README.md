Sample Django project which acts as a service provider for SSO testing. It uses mocksaml.com as mock IdP server for authentication.

URL: http://localhost:800

### Setup with Docker
Build container and start the server
```
docker compose build --no-cache 
docker compose up
```

Rebuilding container after any code change
```
docker compose build --no-cache 
docker compose up
```
