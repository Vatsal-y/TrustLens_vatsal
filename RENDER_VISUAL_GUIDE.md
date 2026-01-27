# 🎨 Render Deployment - Visual Guide

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        RENDER PLATFORM                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────┐      ┌──────────────────────┐  │
│  │  BACKEND SERVICE     │      │  FRONTEND SERVICE    │  │
│  │  trustlens-backend   │      │ trustlens-frontend   │  │
│  ├──────────────────────┤      ├──────────────────────┤  │
│  │ Runtime: Python 3.9  │      │ Runtime: Node        │  │
│  │ Start: gunicorn      │      │ Build: npm build     │  │
│  │ Port: 10000          │      │ Publish: dist/       │  │
│  └──────────────────────┘      └──────────────────────┘  │
│         │                                │                  │
│         │ Environment Variables          │                  │
│         ├─ GEMINI_API_KEY (Secret)      │                  │
│         ├─ AWS_ACCESS_KEY_ID (Secret)   │                  │
│         ├─ AWS_SECRET_ACCESS_KEY (Sec)  │                  │
│         ├─ AWS_REGION                   │                  │
│         ├─ S3_BUCKET_NAME               │                  │
│         │                               │ VITE_API_URL     │
│         │                               │ (Backend URL)    │
│         └───────────────────────────────┘                  │
│         │                                                   │
│         └─→ Pre-deployment Command                         │
│            apt-get install -y git                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │                                    │
         ▼                                    ▼
    ┌─────────────┐                  ┌──────────────┐
    │   AWS S3    │                  │   Browser    │
    │  (Snippets) │                  │  (Users)     │
    └─────────────┘                  └──────────────┘
         │
         │
    ┌─────────────┐
    │  Gemini API │
    │  (Analysis) │
    └─────────────┘
```

---

## Setup Flow

```
START
  │
  ▼
┌────────────────────────────────────────────────┐
│ 1. Gather AWS & Gemini Credentials (5 min)    │
│    - AWS Access Key ID                        │
│    - AWS Secret Access Key                    │
│    - S3 Bucket Name                           │
│    - Gemini API Key                           │
└────────────────────────────────────────────────┘
  │
  ▼
┌────────────────────────────────────────────────┐
│ 2. Configure Backend (5 min)                  │
│    - Add 6 environment variables               │
│    - Mark 3 as "Secret"                       │
│    - Add pre-deploy: apt-get install git      │
└────────────────────────────────────────────────┘
  │
  ▼
┌────────────────────────────────────────────────┐
│ 3. Configure Frontend (2 min)                 │
│    - Add VITE_API_URL                         │
│    - Point to backend URL                     │
└────────────────────────────────────────────────┘
  │
  ▼
┌────────────────────────────────────────────────┐
│ 4. Deploy Both Services (5 min)              │
│    - Backend: Manual Deploy                   │
│    - Frontend: Manual Deploy                  │
│    - Wait for GREEN status                    │
└────────────────────────────────────────────────┘
  │
  ▼
┌────────────────────────────────────────────────┐
│ 5. Test & Verify (10 min)                    │
│    - Health endpoint ✓                        │
│    - Frontend loads ✓                         │
│    - API test ✓                               │
│    - Full workflow ✓                          │
└────────────────────────────────────────────────┘
  │
  ▼
 🎉 LIVE!
```

---

## Environment Variables Tree

```
RENDER ENVIRONMENT VARIABLES
│
├─ BACKEND (trustlens-backend)
│  │
│  ├─ 🔒 SECRETS (Mark as Secret!)
│  │  ├─ AWS_ACCESS_KEY_ID
│  │  ├─ AWS_SECRET_ACCESS_KEY
│  │  └─ GEMINI_API_KEY
│  │
│  └─ 📝 CONFIG (Regular)
│     ├─ AWS_REGION = us-east-1
│     ├─ S3_BUCKET_NAME = [name]
│     ├─ PORT = 10000
│     └─ PYTHON_VERSION = 3.9.18
│
└─ FRONTEND (trustlens-frontend)
   └─ 📝 CONFIG
      └─ VITE_API_URL = https://backend-url
```

---

## Service Configuration

### Backend Service
```
┌─ Service Settings
│  ├─ Name: trustlens-backend
│  ├─ Type: Web Service
│  ├─ Runtime: Python 3.9.18
│  ├─ Root Directory: backend
│  │
│  ├─ Build
│  │  └─ Command: pip install -r requirements.txt
│  │
│  ├─ Start
│  │  └─ Command: gunicorn run_api:app
│  │
│  ├─ Advanced
│  │  └─ Pre-deployment: apt-get update && apt-get install -y git
│  │
│  └─ Environment (7 variables)
│     ├─ GEMINI_API_KEY (Secret)
│     ├─ AWS_ACCESS_KEY_ID (Secret)
│     ├─ AWS_SECRET_ACCESS_KEY (Secret)
│     ├─ AWS_REGION
│     ├─ S3_BUCKET_NAME
│     ├─ PORT
│     └─ PYTHON_VERSION
```

### Frontend Service
```
┌─ Service Settings
│  ├─ Name: trustlens-frontend
│  ├─ Type: Static Site
│  ├─ Runtime: Node
│  ├─ Root Directory: frontend
│  │
│  ├─ Build
│  │  └─ Command: npm install && npm run build
│  │
│  ├─ Publish
│  │  └─ Directory: dist
│  │
│  └─ Environment (1 variable)
│     └─ VITE_API_URL
```

---

## Deployment Phases

```
Phase 1: Configuration (12 minutes)
┌──────────────────────────────────────────────┐
│ ⏱️  5 min  │ Gather credentials              │
│ ⏱️  5 min  │ Configure backend env vars      │
│ ⏱️  2 min  │ Configure frontend env vars     │
└──────────────────────────────────────────────┘

Phase 2: Deployment (10 minutes)
┌──────────────────────────────────────────────┐
│ ⏱️  5 min  │ Deploy backend (wait for green) │
│ ⏱️  5 min  │ Deploy frontend (wait for green)│
└──────────────────────────────────────────────┘

Phase 3: Testing (13 minutes)
┌──────────────────────────────────────────────┐
│ ⏱️  3 min  │ Health check                    │
│ ⏱️  5 min  │ API test                        │
│ ⏱️  5 min  │ Full workflow test              │
└──────────────────────────────────────────────┘

TOTAL: ~35 minutes
```

---

## Verification Flowchart

```
After Deployment
│
├─→ Check Service Status
│   ├─ GREEN ✓ → Next
│   └─ RED ✗ → Check logs
│
├─→ Check Build Logs
│   ├─ No errors ✓ → Next
│   └─ Errors ✗ → See TROUBLESHOOTING.md
│
├─→ Test Health Endpoint
│   ├─ curl backend/health
│   ├─ 200 OK ✓ → Next
│   └─ Error ✗ → See TROUBLESHOOTING.md
│
├─→ Test Frontend Load
│   ├─ Open in browser
│   ├─ Loads ✓ → Next
│   └─ Error ✗ → Check API URL
│
├─→ Test API Integration
│   ├─ curl -X POST /api/code-review
│   ├─ Success ✓ → Next
│   └─ Error ✗ → See TROUBLESHOOTING.md
│
└─→ Test Full Workflow
    ├─ Clone, analyze, upload
    ├─ Success ✓ → 🎉 LIVE!
    └─ Error ✗ → See TROUBLESHOOTING.md
```

---

## Dashboard Navigation

```
RENDER DASHBOARD
│
├─ Services
│  ├─ trustlens-backend
│  │  ├─ Overview (Check GREEN status)
│  │  ├─ Environment (Set variables)
│  │  ├─ Advanced (Add pre-deployment)
│  │  ├─ Logs (Check for errors)
│  │  └─ Deployments (Manual Deploy button)
│  │
│  └─ trustlens-frontend
│     ├─ Overview (Check GREEN status)
│     ├─ Environment (Set VITE_API_URL)
│     ├─ Logs (Check for errors)
│     └─ Deployments (Manual Deploy button)
│
└─ Account
   ├─ API Keys (If needed)
   └─ Settings (Config)
```

---

## Data Flow

```
User's Browser
  │
  │ HTTPS
  ▼
Frontend (https://frontend-xxxxx.onrender.com)
  │ VITE_API_URL
  │
  ▼
Backend (https://backend-xxxxx.onrender.com)
  │
  ├─→ Clone GitHub Repo
  │   └─→ GitHandler
  │
  ├─→ Extract Code Snippets (PARALLEL! 3 threads)
  │   ├─→ Security Thread
  │   ├─→ Logic Thread
  │   └─→ Quality Thread
  │
  ├─→ Call Gemini API
  │   └─→ AI Analysis
  │
  ├─→ Upload to S3
  │   └─→ AWS S3
  │
  └─→ Return Results
      └─→ Frontend
          └─→ User's Browser
```

---

## What Gets Deployed

```
GitHub Repository
│
├─ backend/
│  ├─ requirements.txt (Dependencies)
│  ├─ run_api.py (Flask app)
│  ├─ storage/
│  │  ├─ git_handler.py
│  │  ├─ s3_uploader.py
│  │  ├─ snippet_extractor.py (PARALLEL!)
│  │  └─ ...more files...
│  └─ ...more code...
│
├─ frontend/
│  ├─ package.json (Dependencies)
│  ├─ src/
│  │  ├─ ...components...
│  │  └─ ...pages...
│  ├─ vite.config.js
│  └─ ...more files...
│
└─ render.yaml (Configuration)
    └─ Already configured!
```

---

## Performance Features

```
PARALLEL CODE EXTRACTION
┌─────────────────────────────────┐
│ Input: Repository               │
└──────────────┬──────────────────┘
               │
         ┌─────▼─────────────┐
         │ Parse All Files   │ (Shared)
         └─────┬─────────────┘
               │
        ┌──────┴──────┬──────────┐
        │             │          │
    ┌───▼───┐    ┌────▼────┐  ┌─▼──────┐
    │Thread1│    │ Thread2 │  │Thread3 │
    │Security   │ Logic   │  │Quality │
    └───┬───┘    └────┬────┘  └─┬──────┘
        │             │         │
        └──────┬──────┴────┬────┘
               │
        ┌──────▼──────────┐
        │ Collect Results │
        └──────┬──────────┘
               │
         ┌─────▼──────┐
         │ Output     │ (3 categories)
         └────────────┘

⏱️  60-70% FASTER than sequential!
```

---

## Success Indicators

```
✅ Service Status
   Backend: 🟢 RUNNING
   Frontend: 🟢 RUNNING

✅ Logs
   No ❌ errors
   Git installed ✓
   AWS connected ✓

✅ Endpoints
   Health: 200 OK
   API: Responds
   Frontend: Loads

✅ Features
   Git clone works ✓
   S3 upload works ✓
   Gemini API works ✓
   Full workflow ✓

🎉 LIVE AND WORKING!
```

---

## Quick Links

📚 **Read First:**
- [START_RENDER_DEPLOYMENT.md](START_RENDER_DEPLOYMENT.md)

⚡ **Quick References:**
- [RENDER_QUICK_REFERENCE.md](RENDER_QUICK_REFERENCE.md)
- [RENDER_QUICK_SETUP.md](RENDER_QUICK_SETUP.md)

📋 **Detailed:**
- [RENDER_DEPLOYMENT_CHECKLIST.md](RENDER_DEPLOYMENT_CHECKLIST.md)
- [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)

🔧 **Troubleshooting:**
- [RENDER_TROUBLESHOOTING.md](RENDER_TROUBLESHOOTING.md)
- [GIT_CLONE_ERROR_FIX.md](GIT_CLONE_ERROR_FIX.md)

---

**You're ready to deploy! 🚀**
