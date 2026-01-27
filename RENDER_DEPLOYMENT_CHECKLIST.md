# ✅ Render Deployment Checklist

## 🎯 Phase 1: Environment Variables (Backend)

Go to: **Render Dashboard → trustlens-backend → Environment**

### AWS Credentials
- [ ] `AWS_ACCESS_KEY_ID` = [your-key] **[Mark as SECRET]**
- [ ] `AWS_SECRET_ACCESS_KEY` = [your-secret] **[Mark as SECRET]**
- [ ] `AWS_REGION` = us-east-1
- [ ] `S3_BUCKET_NAME` = [your-bucket-name]

### API Keys
- [ ] `GEMINI_API_KEY` = [your-api-key] **[Mark as SECRET]**

### Configuration
- [ ] `PORT` = 10000
- [ ] `PYTHON_VERSION` = 3.9.18

### Click: "Save Environment Variables"

---

## 🎯 Phase 2: Pre-Deployment Command (Backend)

Go to: **Render Dashboard → trustlens-backend → Advanced**

Find: **Pre-deployment command**

Paste:
```
apt-get update && apt-get install -y git
```

### Click: "Save"

---

## 🎯 Phase 3: Build & Start Commands (Backend)

Verify these are already set:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn run_api:app
```

✅ Should already be correct in `render.yaml`

---

## 🎯 Phase 4: Environment Variables (Frontend)

Go to: **Render Dashboard → trustlens-frontend → Environment**

Add:
- [ ] `VITE_API_URL` = https://your-backend-xxxxx.onrender.com

(Replace `xxxxx` with your actual backend service name)

### Click: "Save Environment Variables"

---

## 🎯 Phase 5: Build & Publish (Frontend)

Verify these are already set:

**Build Command:**
```
npm install && npm run build
```

**Publish Directory:**
```
dist
```

✅ Should already be correct in `render.yaml`

---

## 🎯 Phase 6: Deploy

### For Backend:
1. Go to **Render Dashboard → trustlens-backend**
2. Click **"Manual Deploy"** button
3. Wait for build to complete (green status)

### For Frontend:
1. Go to **Render Dashboard → trustlens-frontend**
2. Click **"Manual Deploy"** button
3. Wait for build to complete (green status)

---

## 🧪 Testing Phase

### Test 1: Check Services Are Running
- [ ] Backend status is **GREEN** (Running)
- [ ] Frontend status is **GREEN** (Running)

### Test 2: Check Build Logs
- [ ] Backend: Click "Logs" → check for errors
- [ ] Frontend: Click "Logs" → check for errors

### Test 3: Test Backend Health
Run in terminal:
```bash
curl https://your-backend-xxxxx.onrender.com/health
```
Expected: `200 OK` or success message

- [ ] Backend responds to health check

### Test 4: Test Frontend
1. Open browser
2. Go to: `https://your-frontend-xxxxx.onrender.com`
3. Open browser console (F12 → Console tab)

- [ ] Frontend loads without errors
- [ ] No red errors in console
- [ ] Can see page content

### Test 5: Test API Connection
In browser console (F12 → Console):
```javascript
fetch('https://your-backend-xxxxx.onrender.com/health')
  .then(r => r.json())
  .then(d => console.log('Success!', d))
  .catch(e => console.log('Error:', e))
```

- [ ] API responds successfully

### Test 6: Full API Test
Run in terminal:
```bash
curl -X POST https://your-backend-xxxxx.onrender.com/api/code-review \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/kavyacp123/trend-pulse-spark.git",
    "analysis_id": "test-'$(date +%s)'"
  }'
```

- [ ] API accepts request
- [ ] API processes repository
- [ ] Returns analysis results

---

## 🔍 Verification Phase

### Backend Service Checks
- [ ] ✅ No error in logs
- [ ] ✅ Git is installed (check logs)
- [ ] ✅ AWS credentials set
- [ ] ✅ S3 connection works
- [ ] ✅ Gemini API works
- [ ] ✅ Health endpoint responds

### Frontend Service Checks
- [ ] ✅ No error in logs
- [ ] ✅ Loads in browser
- [ ] ✅ API URL is correct
- [ ] ✅ Can connect to backend
- [ ] ✅ No CORS errors

### Integration Checks
- [ ] ✅ Frontend calls backend
- [ ] ✅ Backend can clone repos
- [ ] ✅ Backend can upload to S3
- [ ] ✅ Backend can call Gemini API
- [ ] ✅ Analysis completes successfully

---

## 🆘 Troubleshooting

If any test fails, check:

| Error | Guide |
|-------|-------|
| `exit code(128)` | Add pre-deployment command |
| AWS credentials | Set environment variables |
| S3 bucket not found | Check bucket exists |
| API unreachable | Set VITE_API_URL |
| Build failed | Check logs tab |
| Any other error | See `RENDER_TROUBLESHOOTING.md` |

---

## 📋 Final Checklist

### Before Declaring Success:

- [ ] ✅ All environment variables set
- [ ] ✅ Pre-deployment command added
- [ ] ✅ Both services showing GREEN
- [ ] ✅ No errors in build logs
- [ ] ✅ No errors in runtime logs
- [ ] ✅ Health endpoint responds
- [ ] ✅ Frontend loads in browser
- [ ] ✅ API tests pass
- [ ] ✅ Full integration works

---

## 🎉 Success!

When all checkmarks above are green, your TrustLens is live on Render! 🚀

Your project is now:
- ✅ Deployed on Render
- ✅ Running in production
- ✅ Connected to AWS S3
- ✅ Using Gemini API
- ✅ Cloning repositories
- ✅ Analyzing code
- ✅ Extracting snippets (in parallel, 60-70% faster!)

---

## 📞 Need Help?

**Guides available:**
- `RENDER_QUICK_SETUP.md` - Fast setup
- `RENDER_DEPLOYMENT_GUIDE.md` - Full guide
- `RENDER_TROUBLESHOOTING.md` - Fix errors
- `GIT_CLONE_ERROR_FIX.md` - Git issues

**Time estimate:**
- Setup: 5-10 minutes
- Testing: 10-15 minutes
- Troubleshooting: 15-30 minutes (if needed)

---

**Status: Ready to deploy! 🚀**
