# 🚀 Render Deployment - Quick Setup

## 📋 Environment Variables (Copy-Paste)

Add these to **Render Dashboard → Environment Variables**:

### Backend Service
```
GEMINI_API_KEY = [your-api-key] ← MARK AS SECRET
AWS_ACCESS_KEY_ID = [your-access-key] ← MARK AS SECRET
AWS_SECRET_ACCESS_KEY = [your-secret-key] ← MARK AS SECRET
AWS_REGION = us-east-1
S3_BUCKET_NAME = [your-bucket-name]
PORT = 10000
PYTHON_VERSION = 3.9.18
```

### Frontend Service
```
VITE_API_URL = https://trustlens-backend-xxxxx.onrender.com
```

---

## ⚙️ Critical: Pre-Deployment Command

**This fixes Git Clone Error!**

**In Backend Service → Advanced → Pre-deployment command:**
```bash
apt-get update && apt-get install -y git
```

---

## 🔧 Build & Start Commands

### Backend
```
Build:  pip install -r requirements.txt
Start:  gunicorn run_api:app
```

### Frontend
```
Build:   npm install && npm run build
Publish: dist
```

---

## ✅ Environment Variables Checklist

**Backend (trustlens-backend):**
- [ ] GEMINI_API_KEY (Secret)
- [ ] AWS_ACCESS_KEY_ID (Secret)
- [ ] AWS_SECRET_ACCESS_KEY (Secret)
- [ ] AWS_REGION
- [ ] S3_BUCKET_NAME
- [ ] Pre-deployment command: `apt-get update && apt-get install -y git`

**Frontend (trustlens-frontend):**
- [ ] VITE_API_URL

---

## 🧪 Test After Deployment

```bash
# Test backend health
curl https://your-backend.onrender.com/health

# Test API
curl -X POST https://your-backend.onrender.com/api/code-review \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/...", "analysis_id": "test"}'

# Test frontend
Open in browser: https://your-frontend.onrender.com
```

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| Git clone error (128) | Add pre-deployment: `apt-get update && apt-get install -y git` |
| AWS credentials not found | Set AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY as Secrets |
| S3 bucket not found | Check bucket name matches S3_BUCKET_NAME |
| Frontend can't reach API | Set VITE_API_URL to your backend URL |
| Gemini API fails | Verify GEMINI_API_KEY is correct |

---

## 📞 Get Your URLs

After deployment:
```
Backend:  https://trustlens-backend-xxxxx.onrender.com
Frontend: https://trustlens-frontend-xxxxx.onrender.com
```

Replace `xxxxx` with your actual Render-generated names.

---

## 🎯 Full Deployment Guide
See: `RENDER_DEPLOYMENT_GUIDE.md` (comprehensive guide)

**Status:** Ready to deploy! 🚀
