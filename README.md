# 🛡️ AI-Powered Security Log Analyzer

A production-ready **Security Operations Center (SOC)** style web application that automatically analyzes uploaded security log files, detects suspicious activities, classifies threats using machine learning, visualizes insights, and generates professional PDF/Excel security reports.

Built as a Final Year Engineering Project — looks and feels like a commercial cybersecurity product.

---

## ✨ Features

### 🔐 Authentication
- User registration & login with JWT
- Password hashing (bcrypt)
- Role-based access control (Admin / User)
- First registered user is automatically promoted to admin

### 📊 Dashboard
- Total uploaded logs / entries / threats
- Critical, High, Medium, Low alert counters
- Security score (0-100)
- Interactive charts: Pie (severity), Line (failed-login trend), Bar (threat categories)
- Recent activities audit feed
- Top suspicious source IPs table

### 📤 Log Upload
- Drag-and-drop upload
- Supported formats: `.log`, `.txt`, `.csv` (max 50 MB)

### 🔍 Automatic Log Parsing
Extracts: timestamp, username, source IP, destination IP, event type, message, status.

### 🚨 Threat Detection (Rule-Based)
- Failed Login
- Brute Force Attack (≥5 failures from same IP)
- Unknown IP Login
- Account Lockout
- SQL Injection
- Cross Site Scripting (XSS)
- Directory Traversal
- Port Scan
- Privilege Escalation
- Malware Detection
- Firewall Block

Each threat gets a severity: **Critical / High / Medium / Low**.

### 🤖 Machine Learning
- Random Forest classifier with TF-IDF features
- Trained on curated security-log corpus
- Predicts: **Normal / Suspicious / Critical**
- Displays confidence percentage per detection
- Model auto-trains on first launch

### 📈 Analytics
- Attack Distribution (Pie)
- Failed Login Trend (Line, last 7 days)
- Threat Categories (Bar)
- Most Active Source IPs (Table)

### 🔎 Advanced Search
Search entries by username, IP, date range, event type, severity.

### 📄 Reports
- **PDF** reports with executive summary, metrics, charts, threat detail tables, and recommendations
- **Excel** workbooks with multi-sheet structure (Summary, Threats, Top IPs, Recommendations)

### 🛡️ Security
- JWT authentication
- Bcrypt password hashing
- Input validation via Pydantic
- SQL injection protection via SQLAlchemy ORM
- CORS restricted to configured origins
- Full audit logging

---

## 🗂️ Project Structure

```
security-log-analyzer/
├── backend/
│   ├── app/
│   │   ├── api/            # Route handlers (auth, logs, threats, dashboard, reports, admin)
│   │   ├── core/           # Config + security helpers (JWT, hashing)
│   │   ├── db/             # SQLAlchemy setup
│   │   ├── models/         # ORM models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # log_parser, threat_detector, report_generator
│   │   ├── ml/             # ML classifier
│   │   └── main.py         # FastAPI entry point
│   ├── tests/              # pytest test suite
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/     # Layout, sidebar, shared UI
│   │   ├── contexts/       # AuthContext
│   │   ├── pages/          # Login, Register, Dashboard, Upload, Logs, Threats, Search, Reports
│   │   ├── services/       # Axios client
│   │   ├── types/          # TypeScript types
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── sample_logs/            # Ready-to-upload demo logs
│   ├── auth.log
│   ├── webserver.log
│   └── events.csv
├── dataset/                # ML training corpus (also embedded in classifier.py)
├── docs/                   # Installation guide
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12
- Node.js 18+ (with npm)

### 1. Backend

```bash
cd security-log-analyzer/backend
python -m venv venv
source venv/bin/activate       # macOS/Linux
# venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will start at **http://localhost:8000** — Swagger docs at **http://localhost:8000/docs**.

### 2. Frontend

Open a new terminal:

```bash
cd security-log-analyzer/frontend
npm install
npm run dev
```

Frontend will start at **http://localhost:5173**.

### 3. Try It

1. Open **http://localhost:5173** in your browser.
2. Register a new account — the very first account is automatically admin.
3. Log in.
4. Go to **Upload Logs** and drop a file from `sample_logs/` (e.g. `auth.log`).
5. Watch the dashboard, threats table, and search page populate.
6. Generate a PDF or Excel report from **Reports**.

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

Covers: authentication flow, log parsing, threat detection, ML classification.

---

## 🧠 Machine Learning Details

- **Algorithm**: `RandomForestClassifier` (scikit-learn) with `class_weight="balanced"`, 100 estimators.
- **Features**: TF-IDF vectors (unigrams + bigrams), IP-address & number normalization.
- **Classes**: Normal / Suspicious / Critical.
- **Training corpus**: 60+ hand-curated security-log samples (see `backend/app/ml/classifier.py` and `dataset/threat_training_data.csv`).
- **Persistence**: Trained model saved to `backend/ml_models/threat_classifier.joblib`.
- **Auto-training**: On first launch, the model trains itself if the persisted file is missing.

---

## 🔌 API Reference (summary)

All endpoints are prefixed with `/api/v1`. All non-auth endpoints require `Authorization: Bearer <token>`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Get JWT |
| POST | `/auth/logout` | Log out |
| GET  | `/auth/me` | Current user |
| POST | `/logs/upload` | Upload & analyze log |
| GET  | `/logs` | List log files |
| GET  | `/logs/{id}` | Log file details |
| GET  | `/logs/{id}/entries` | Paginated entries |
| DELETE | `/logs/{id}` | Delete log file |
| GET  | `/logs/search/entries` | Search with filters |
| GET  | `/threats` | List detected threats |
| GET  | `/dashboard/stats` | Aggregate stats |
| POST | `/reports/generate` | Create PDF/Excel report |
| GET  | `/reports` | List reports |
| GET  | `/reports/{id}/download` | Download report file |
| GET  | `/admin/users` | (admin) List users |
| GET  | `/admin/audit-logs` | (admin) Audit trail |

Full OpenAPI schema available at `/docs` when the backend is running.

---

## 📸 Screens

- **Login / Register** — cybersecurity-themed dark UI
- **Dashboard** — stat cards, charts, top IPs, recent activity feed
- **Upload** — drag-and-drop area with per-file result summary
- **Log Files** — list + inline paginated entry viewer
- **Threats** — filterable severity table with ML classification + confidence
- **Search** — multi-filter form (user / IP / event / date range)
- **Reports** — one-click PDF/Excel generation and download

---

## 🛡️ Security Notes

- Change `SECRET_KEY` in `backend/app/core/config.py` (or via `.env`) before deploying.
- SQLite is fine for development / demo; swap to any SQLAlchemy-supported RDBMS in `DATABASE_URL`.
- CORS whitelist is restricted to `localhost:5173` / `localhost:3000` — update for production hosts.

---

## 📄 License

Provided for educational purposes as a Final Year Engineering Project template.
