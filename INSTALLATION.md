# Installation Guide

## 1. Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.12+ |
| Node.js | 18+ |
| npm | 9+ |

Verify:
```bash
python --version
node --version
npm --version
```

## 2. Clone / Copy the Project

Place the entire `security-log-analyzer/` folder somewhere on your machine.

## 3. Backend Setup

```bash
cd security-log-analyzer/backend
python -m venv venv
# Activate the venv:
#   Linux / macOS:  source venv/bin/activate
#   Windows CMD:    venv\Scripts\activate
#   Windows PS:     venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### (Optional) Configure environment
Copy `.env.example` to `.env` and edit `SECRET_KEY`, etc.

### Run the API server
```bash
uvicorn app.main:app --reload
```

Verify:
- Health check: <http://localhost:8000/api/v1/health>
- Swagger:     <http://localhost:8000/docs>

The first launch will:
- Create `security_analyzer.db` (SQLite) with all tables
- Train and cache the ML model at `ml_models/threat_classifier.joblib`

## 4. Frontend Setup

Open a **new terminal**:

```bash
cd security-log-analyzer/frontend
npm install
npm run dev
```

Vite will print a URL like:
```
➜  Local: http://localhost:5173/
```

Open that URL in your browser.

## 5. First-Time Use

1. **Register** — the first user becomes admin automatically.
2. **Log in**.
3. Go to **Upload Logs** and drop one of the files from `sample_logs/`:
   - `auth.log`       — SSH/auth log style
   - `webserver.log`  — web server style
   - `events.csv`     — structured CSV
4. Explore Dashboard, Threats, Search, and Reports.

## 6. Running Tests

```bash
cd backend
pytest tests/ -v
```

## 7. Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError` | Activate the venv, run `pip install -r requirements.txt` again |
| `Port 8000 in use` | `uvicorn app.main:app --reload --port 8001` (also update `vite.config.ts` proxy) |
| `Port 5173 in use` | `npm run dev -- --port 5174` |
| CORS errors | Add your frontend URL to `CORS_ORIGINS` in `backend/app/core/config.py` |
| bcrypt errors on Python 3.13 | Use Python 3.12 (as recommended) |
| Model not classifying well | Delete `backend/ml_models/threat_classifier.joblib` and restart — it retrains |

## 8. Production Notes

- Set a strong `SECRET_KEY`
- Switch to a production ASGI server: `gunicorn -k uvicorn.workers.UvicornWorker app.main:app`
- Serve the built frontend (`npm run build`) via a reverse proxy (nginx)
- Consider swapping SQLite for a production RDBMS by updating `DATABASE_URL`
