# Phone-Central

Django website/bot for our discord.

## Development

### Python environment

```bash
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
django-admin migrate
django-admin runserver
```

### Frontend

We use npm/webpack. See the README.md in the frontend/ folder.

```bash
cd frontend/
npm run watch
```
