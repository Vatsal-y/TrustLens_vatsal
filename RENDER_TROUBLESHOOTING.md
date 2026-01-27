# 🔧 Render Deployment Troubleshooting

## 🚨 Common Errors & Fixes

### **Error 1: Git Clone Failed (Exit Code 128)**

**Log Message:**
```
❌ Git command error: Cmd('git') failed due to: exit code(128)
```

**Root Cause:** Git is not installed on Render

**Fix:**
1. Go to Render Dashboard → your-backend-service
2. Click "Advanced" tab
3. Find "Pre-deployment command"
4. Enter: `apt-get update && apt-get install -y git`
5. Click "Save"
6. Manual redeploy

**Verification:**
```
✅ Git is installed: git version 2.x.x
```

---

### **Error 2: AWS Credentials Not Found**

**Log Message:**
```
⚠️ AWS credentials not found - using MOCK mode
❌ Cannot upload to S3
```

**Root Cause:** Environment variables not set

**Fix:**
1. Go to Render Dashboard → your-backend-service
2. Click "Environment" tab
3. Add these variables as "Secret":
   - `AWS_ACCESS_KEY_ID` = your-access-key
   - `AWS_SECRET_ACCESS_KEY` = your-secret-key
   - `AWS_REGION` = us-east-1
   - `S3_BUCKET_NAME` = your-bucket-name
4. Click "Save"
5. Manual redeploy

**Verification:**
```
✅ S3 uploader initialized for bucket: trustlens
```

---

### **Error 3: S3 Bucket Not Found**

**Log Message:**
```
❌ Bucket 'trustlens' does not exist
```

**Root Cause:** 
- Bucket name is wrong
- Bucket doesn't exist in AWS S3
- Wrong AWS region

**Fix:**
1. Go to AWS S3 console
2. Verify bucket exists
3. Check bucket region
4. Update `AWS_REGION` and `S3_BUCKET_NAME` in Render
5. Redeploy

**Verification:**
```
✅ Bucket 'your-bucket-name' exists and is accessible
```

---

### **Error 4: Gemini API Key Invalid**

**Log Message:**
```
❌ Invalid API key provided
❌ [401] Unauthorized - API key is invalid
```

**Root Cause:** GEMINI_API_KEY is missing or incorrect

**Fix:**
1. Go to https://makersuite.google.com/app/apikey
2. Get your API key
3. Go to Render Dashboard → your-backend-service
4. Click "Environment" tab
5. Add variable as "Secret":
   - `GEMINI_API_KEY` = your-api-key
6. Click "Save"
7. Manual redeploy

**Verification:**
```
✅ Gemini API initialized successfully
```

---

### **Error 5: Frontend Cannot Reach Backend**

**Error in Browser:**
```
Error: Cannot connect to API
Failed to fetch from https://undefined/api/...
```

**Root Cause:** VITE_API_URL not set or incorrect

**Fix:**
1. Go to Render Dashboard → your-frontend-service
2. Click "Environment" tab
3. Add variable:
   - `VITE_API_URL` = https://your-backend-xxxxx.onrender.com
4. Click "Save"
5. Manual redeploy

**Verification:**
- Open frontend in browser
- Check browser console (F12)
- Should see API requests to correct URL

---

### **Error 6: Build Failing (Missing Dependencies)**

**Log Message:**
```
ModuleNotFoundError: No module named 'boto3'
ModuleNotFoundError: No module named 'flask'
```

**Root Cause:** requirements.txt not found or incomplete

**Fix:**
1. Ensure `backend/requirements.txt` exists
2. Ensure it contains:
   ```
   boto3==1.34.0
   flask==3.0.0
   GitPython==3.1.40
   google-generativeai==0.3.0
   requests==2.31.0
   gunicorn==21.2.0
   ```
3. Commit and push to GitHub
4. Redeploy from Render

**Verification:**
```
✅ Successfully built Python app
✅ Collecting boto3
✅ Installing collected packages
```

---

### **Error 7: Port Issues**

**Log Message:**
```
Address already in use
Port 10000 is not available
```

**Root Cause:** Port is bound or service already running

**Fix:**
1. Don't need to set PORT in environment (Render assigns it)
2. Check startup command is: `gunicorn run_api:app`
3. Manually redeploy

**Verification:**
```
✅ Application running on 0.0.0.0:PORT
```

---

### **Error 8: CORS Issues**

**Browser Error:**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Root Cause:** CORS headers not configured

**Fix:**
- Check `backend/api/app.py` has CORS enabled:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```
- Verify it's set up correctly
- Redeploy backend

**Verification:**
- Check response headers in browser (F12 → Network)
- Should see: `Access-Control-Allow-Origin: *`

---

### **Error 9: Service Not Starting**

**Log Message:**
```
Failed to start service
Timeout: service did not start within 30 seconds
```

**Root Cause:**
- Syntax errors in code
- Missing dependencies
- Port configuration issue
- Long startup time

**Fix:**
1. Check build logs for errors
2. Verify requirements.txt is complete
3. Check `run_api.py` has no syntax errors
4. Try manual redeploy
5. Check service status in Render dashboard

**Verification:**
```
✅ Service started successfully
✅ Listening on port 10000
```

---

### **Error 10: Gunicorn Worker Crash**

**Log Message:**
```
[CRITICAL] WORKER TIMEOUT after 30 seconds
Worker exited with code 1
```

**Root Cause:**
- Long running request
- Memory limit exceeded
- Infinite loop in code

**Fix:**
1. Optimize code performance
2. Check for infinite loops
3. Optimize S3 uploads
4. Increase timeout in gunicorn config
5. Check memory usage

**Verification:**
```
✅ Workers running normally
```

---

## 🔍 Debug Checklist

### Before Reporting Issue:

- [ ] Checked Render logs for specific error message
- [ ] Verified all environment variables are set
- [ ] Verified environment variables are marked "Secret" if needed
- [ ] Manually redeployed service
- [ ] Checked GitHub has latest code pushed
- [ ] Verified pre-deployment commands are set
- [ ] Tested locally first (if possible)
- [ ] Checked all required files exist (requirements.txt, etc.)

---

## 📊 Render Dashboard Checks

### **Service Status Page**

Check:
1. Service is "Running" (green status)
2. Build logs show "✅ Build succeeded"
3. No errors in "Logs" tab
4. Recent deploy is latest

### **Environment Variables**

Verify:
- [ ] All required variables are set
- [ ] Secrets are marked as "Secret"
- [ ] No typos in variable names
- [ ] No extra spaces in values

### **Build Settings**

Verify:
- [ ] Root Directory is correct (`backend` for backend, `frontend` for frontend)
- [ ] Runtime is correct (Python 3.9 for backend, Node for frontend)
- [ ] Build Command is correct
- [ ] Start Command is correct
- [ ] Pre-deployment command is set (for backend)

---

## 🧪 Quick Test Commands

After deployment:

```bash
# Test backend health
curl https://your-backend.onrender.com/health

# Test API endpoint
curl -X POST https://your-backend.onrender.com/api/code-review \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/...", "analysis_id": "test"}'

# Check Git installed
curl https://your-backend.onrender.com/logs | grep -i git

# Check AWS connected
curl https://your-backend.onrender.com/logs | grep -i "s3\|bucket"
```

---

## 🆘 Getting Help

### **Render Support**
- Render Docs: https://render.com/docs
- Status Page: https://status.render.com
- Support: https://render.com/support

### **Common Render Commands**
```bash
# View live logs
Render Dashboard → Logs tab

# Manual redeploy
Render Dashboard → Manual Deploy

# View build logs
Render Dashboard → Build → Build logs

# Check environment variables
Render Dashboard → Environment tab
```

---

## ✅ Post-Deployment Verification

After fixing any error:

1. **Service Status:** Green (Running)
2. **Logs:** No error messages
3. **Test Endpoint:** Returns 200 OK
4. **Git:** Clone works (check logs)
5. **AWS:** S3 uploads work
6. **Gemini:** API calls work
7. **Frontend:** Loads and connects to API

---

**If still stuck after these steps, check specific error guides:**
- Git Clone: `GIT_CLONE_ERROR_FIX.md`
- Full Render Guide: `RENDER_DEPLOYMENT_GUIDE.md`
- Quick Setup: `RENDER_QUICK_SETUP.md`

**Status:** Ready to troubleshoot! 🚀
