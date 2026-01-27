# 🔴 Git Clone Error - Quick Fix

## Problem
```
Exit Code 128: Cmd('git') failed
Error: git clone https://github.com/kavyacp123/trend-pulse-spark.git /tmp/repo-...
```

## Root Cause
**Git is NOT installed or not in system PATH**

---

## ✅ Immediate Fix (Choose your OS)

### **Linux/Ubuntu/WSL**
```bash
sudo apt-get update
sudo apt-get install -y git
git --version
```

### **CentOS/RHEL**
```bash
sudo yum install -y git
git --version
```

### **Windows (if using WSL)**
Inside WSL terminal:
```bash
sudo apt-get update
sudo apt-get install -y git
```

### **Docker**
Add to Dockerfile:
```dockerfile
RUN apt-get update && apt-get install -y git
```

---

## 🧪 Verify Fix

```bash
# Check Git is installed
git --version

# Run TrustLens diagnostic
cd backend
python diagnose_git_issue.py

# Test clone manually
git clone --depth 1 https://github.com/torvalds/linux.git /tmp/test-repo
```

---

## 🎯 What was improved

**Code Changes in `git_handler.py`:**

1. ✅ **Auto Git detection** - Checks if Git is installed on startup
2. ✅ **Better error messages** - Tells you exactly what's wrong:
   - `Exit code 128` → Git not installed
   - Network error → Connection issue
   - `401/403` → Authentication failed
3. ✅ **Helpful diagnostics** - Suggests exact fixes for your OS

**New Tool:**
- 📊 `diagnose_git_issue.py` - Complete diagnostic report

**New Guide:**
- 📖 `GIT_CLONE_ERROR_FIX.md` - Detailed troubleshooting guide

---

## 📋 After Installing Git

System will automatically:
- ✅ Detect Git installation
- ✅ Log Git version
- ✅ Provide better error messages
- ✅ Retry clone with diagnostics

Expected log output:
```
✅ Git is installed: git version 2.34.1
🔄 Starting clone: https://github.com/...
✅ Successfully cloned: trend-pulse-spark
```

---

## 🚀 Next Steps

1. **Install Git** using command above for your OS
2. **Verify:** `git --version`
3. **Test:** `python diagnose_git_issue.py`
4. **Retry:** Try the clone again through TrustLens API

That's it! Git clone should work after installation. 🎉
