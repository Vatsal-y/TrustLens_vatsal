# 🚀 TrustLens on Render - Deployment Guide

## ✅ Your render.yaml is Configured

Your project has a `render.yaml` file that defines:
- ✅ **Backend Service** (Python/Gunicorn)
- ✅ **Frontend Service** (Node/Vite)

---

## 📋 Environment Variables Setup on Render

You need to configure these in Render Dashboard for your services:

### **Backend Service (trustlens-backend)**

#### 1. **Critical: Git Installation** ⚠️
Since the backend clones repositories, you MUST add a build script.

**In Render Dashboard:**
1. Go to your service settings
2. Click "Advanced" 
3. Find "Pre-deployment command"
4. Add this command:
```bash
apt-get update && apt-get install -y git
```

This ensures Git is installed before your code runs.

#### 2. **AWS S3 Credentials** (Required for uploads)
```
Key: AWS_ACCESS_KEY_ID
Value: your-access-key-id
Mark as: Secret
```

```
Key: AWS_SECRET_ACCESS_KEY
Value: your-secret-access-key
Mark as: Secret
```

```
Key: AWS_REGION
Value: us-east-1  (or your region)
```

```
Key: S3_BUCKET_NAME
Value: your-bucket-name
```

#### 3. **Google Gemini API Key** (For LLM analysis)
```
Key: GEMINI_API_KEY
Value: your-gemini-api-key
Mark as: Secret
```

#### 4. **API Configuration**
```
Key: PORT
Value: 10000  (default for Render)
```

```
Key: FLASK_ENV
Value: production
```

```
Key: PYTHON_VERSION
Value: 3.9.18
```

#### 5. **Optional: S3 Configuration**
```
Key: AWS_AUTO_CREATE_BUCKET
Value: false  (should already exist)
```

```
Key: S3_PREFIX
Value: trustlens/  (or your prefix)
```

---

### **Frontend Service (trustlens-frontend)**

#### **API Connection**
```
Key: VITE_API_URL
Value: https://your-trustlens-backend.onrender.com
```

This is automatically populated if using `fromService` in render.yaml.

---

## 🔧 Complete Setup Checklist

### **Step 1: Set Backend Environment Variables**
In Render Dashboard → trustlens-backend → Environment:

```
✓ GEMINI_API_KEY = [your-key] (Secret)
✓ AWS_ACCESS_KEY_ID = [your-key] (Secret)
✓ AWS_SECRET_ACCESS_KEY = [your-key] (Secret)
✓ AWS_REGION = us-east-1
✓ S3_BUCKET_NAME = [your-bucket]
✓ PORT = 10000
✓ PYTHON_VERSION = 3.9.18
```

### **Step 2: Add Git Installation (CRITICAL)**
In Render Dashboard → trustlens-backend → Advanced → Pre-deployment command:
```bash
apt-get update && apt-get install -y git
```

### **Step 3: Set Frontend Environment Variables**
In Render Dashboard → trustlens-frontend → Environment:

```
✓ VITE_API_URL = https://trustlens-backend-xxxxx.onrender.com
```

### **Step 4: Verify Build Commands**
Backend:
```bash
pip install -r requirements.txt
```

Frontend:
```bash
npm install && npm run build
```

### **Step 5: Verify Start Commands**
Backend:
```bash
gunicorn run_api:app
```

---

## 🔐 Security Best Practices

### **Secrets Management**
- ✅ Mark AWS credentials as "Secret"
- ✅ Mark GEMINI_API_KEY as "Secret"  
- ✅ Never commit .env files to git
- ✅ Rotate keys periodically

### **S3 Access**
- ✅ Use IAM user with limited permissions
- ✅ Don't use root AWS credentials
- ✅ Enable S3 bucket versioning
- ✅ Enable S3 bucket encryption

### **API Security**
- ✅ Use HTTPS only (Render provides this)
- ✅ Set CORS headers properly
- ✅ Rate limit API endpoints
- ✅ Validate input on backend

---

## 🐛 Troubleshooting Common Issues

### **Issue 1: Git Clone Error (Exit Code 128)**
✅ **Fix**: Add pre-deployment command:
```bash
apt-get update && apt-get install -y git
```

### **Issue 2: AWS Credentials Not Found**
❌ Problem:
```
⚠️ AWS credentials not found - using MOCK mode
```

✅ Fix:
- Set `AWS_ACCESS_KEY_ID` in environment
- Set `AWS_SECRET_ACCESS_KEY` in environment
- Mark both as "Secret"
- Redeploy after saving

### **Issue 3: S3 Bucket Not Found**
❌ Problem:
```
❌ Bucket 'trustlens' does not exist
```

✅ Fix:
- Verify bucket exists in AWS S3
- Check bucket name matches `S3_BUCKET_NAME`
- Verify AWS credentials have access
- Check bucket region matches `AWS_REGION`

### **Issue 4: Gemini API Key Invalid**
❌ Problem:
```
❌ Invalid Gemini API key
```

✅ Fix:
- Get key from: https://makersuite.google.com/app/apikey
- Set `GEMINI_API_KEY` environment variable
- Mark as "Secret"
- Redeploy

### **Issue 5: Frontend Cannot Reach Backend**
❌ Problem:
```
Error: Cannot connect to API
```

✅ Fix:
- Set `VITE_API_URL` to your backend URL
- Example: `https://trustlens-backend-xxxxx.onrender.com`
- Rebuild frontend after changing
- Check backend is running (no errors in logs)

---

## 📊 Environment Variables Summary

| Variable | Required | Secret | Example |
|----------|----------|--------|---------|
| `GEMINI_API_KEY` | Yes | Yes | `AIzaSy...` |
| `AWS_ACCESS_KEY_ID` | Yes | Yes | `AKIA...` |
| `AWS_SECRET_ACCESS_KEY` | Yes | Yes | `wJal...` |
| `AWS_REGION` | Yes | No | `us-east-1` |
| `S3_BUCKET_NAME` | Yes | No | `trustlens-snippets` |
| `PORT` | No | No | `10000` |
| `VITE_API_URL` | Yes (Frontend) | No | `https://...onrender.com` |

---

## 🚀 Deployment Steps

### **First Time Deployment**

1. **Connect GitHub to Render**
   - Go to Render.com → New → Web Service
   - Connect your GitHub account
   - Select TrustLens repository
   - Select branch (main)

2. **Configure Backend Service**
   - Root Directory: `backend`
   - Runtime: Python 3.9
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run_api:app`
   - Add environment variables (see table above)
   - **Add pre-deployment command**: `apt-get update && apt-get install -y git`

3. **Configure Frontend Service**
   - Root Directory: `frontend`
   - Runtime: Node
   - Build Command: `npm install && npm run build`
   - Publish Directory: `dist`
   - Add environment variables

4. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete
   - Check logs for any errors

### **Subsequent Deployments**

- Push changes to GitHub
- Render automatically redeploys
- Check deployment logs for errors

---

## 🔍 Testing After Deployment

### **Test Backend**

```bash
# Test API health
curl https://your-backend.onrender.com/health

# Test with GitHub URL
curl -X POST https://your-backend.onrender.com/api/code-review \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/kavyacp123/trend-pulse-spark.git",
    "analysis_id": "test-123"
  }'
```

### **Test Frontend**

```bash
# Open in browser
https://your-frontend.onrender.com

# Check browser console for errors
# Should see API calls to backend
```

---

## 📝 render.yaml Reference

Your file already includes:

```yaml
services:
  # Backend
  - type: web                        # Web service
    name: trustlens-backend          # Service name
    runtime: python                  # Python runtime
    rootDir: backend                 # Source directory
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn run_api:app
    envVars:                         # Environment variables
      - key: PYTHON_VERSION
        value: 3.9.18

  # Frontend  
  - type: static                     # Static site
    name: trustlens-frontend         # Service name
    runtime: node                    # Node runtime
    rootDir: frontend                # Source directory
    buildCommand: npm install && npm run build
    publishDir: dist                 # Output directory
    routes:                          # Routing rules
      - type: rewrite
        source: /*
        destination: /index.html     # SPA routing
```

---

## 🎯 Expected URLs After Deployment

```
Backend:  https://trustlens-backend-xxxxx.onrender.com
Frontend: https://trustlens-frontend-xxxxx.onrender.com
          (or custom domain if configured)
```

Example API call:
```bash
curl https://trustlens-backend-xxxxx.onrender.com/api/code-review
```

---

## 📚 Important Files

Make sure these files are in your repository:

- ✅ `backend/requirements.txt` - Python dependencies
- ✅ `backend/run_api.py` - Flask app entry point
- ✅ `frontend/package.json` - Node dependencies
- ✅ `render.yaml` - Render configuration
- ✅ `.gitignore` - Don't commit secrets!

---

## 🆘 Getting Help

### **Check Render Logs**
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Check for errors

### **Common Log Errors**

```
❌ ModuleNotFoundError: No module named 'boto3'
→ Fix: Make sure boto3 is in requirements.txt

❌ FileNotFoundError: git
→ Fix: Add pre-deployment command to install git

❌ AWS credentials not found
→ Fix: Set AWS environment variables

❌ Cannot connect to S3
→ Fix: Check bucket name and AWS credentials
```

---

## ✅ Deployment Verification Checklist

After deployment, verify:

- [ ] Backend service is running (green status)
- [ ] Frontend service is running (green status)
- [ ] No build errors in logs
- [ ] Backend health endpoint responds: `curl https://backend-url/health`
- [ ] Frontend loads in browser
- [ ] API calls from frontend reach backend
- [ ] Git clone works (check logs for success message)
- [ ] S3 uploads work (check for success message)
- [ ] Gemini API calls work (check analysis results)

---

## 🚀 Next Steps

1. **Set all environment variables** in Render Dashboard
2. **Add Git pre-deployment command**
3. **Deploy** and check logs
4. **Test** API endpoints
5. **Monitor** error logs

---

**Your project is ready for Render deployment! 🎉**
