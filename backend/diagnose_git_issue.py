#!/usr/bin/env python3
"""
Diagnostic Tool for Git Clone Issues
Helps identify and resolve Git setup problems
"""

import subprocess
import sys
import platform
import os
from pathlib import Path

def print_section(title):
    """Print formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def run_command(cmd, description):
    """Run command and return result"""
    print(f"\n🔍 {description}...")
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=5, shell=True)
        output = result.stdout.decode().strip()
        error = result.stderr.decode().strip()
        returncode = result.returncode
        
        if returncode == 0:
            print(f"✅ SUCCESS: {output if output else description}")
            return True, output
        else:
            print(f"❌ FAILED: {error if error else 'Unknown error'}")
            return False, error
    except subprocess.TimeoutExpired:
        print(f"❌ TIMEOUT: Command took too long")
        return False, "Timeout"
    except FileNotFoundError as e:
        print(f"❌ NOT FOUND: {e}")
        return False, str(e)
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False, str(e)

def diagnose_git():
    """Diagnose Git installation and setup"""
    print_section("GIT DIAGNOSTIC REPORT")
    
    issues = []
    solutions = []
    
    # 1. Check OS
    print(f"\n📊 System Information:")
    print(f"   OS: {platform.system()} {platform.release()}")
    print(f"   Python: {sys.version}")
    print(f"   Working Dir: {os.getcwd()}")
    
    # 2. Check Git installation
    print_section("1. Git Installation Check")
    success, output = run_command("git --version", "Checking Git version")
    
    if not success:
        issues.append("Git is NOT installed")
        if platform.system() == "Linux":
            solutions.append("Ubuntu/Debian: apt-get update && apt-get install -y git")
            solutions.append("CentOS/RHEL: yum install -y git")
            solutions.append("Alpine: apk add git")
        elif platform.system() == "Windows":
            solutions.append("Download from: https://git-scm.com/download/win")
            solutions.append("Or use: choco install git (if using Chocolatey)")
        elif platform.system() == "Darwin":
            solutions.append("macOS: brew install git")
    
    # 3. Check Git config
    print_section("2. Git Configuration Check")
    run_command("git config --list", "Checking Git configuration")
    
    # 4. Check network connectivity
    print_section("3. Network Connectivity Check")
    success, _ = run_command("ping -c 1 github.com" if platform.system() != "Windows" else "ping -n 1 github.com", 
                             "Testing GitHub connectivity")
    if not success:
        issues.append("Cannot reach GitHub (network issue)")
        solutions.append("Check internet connection")
        solutions.append("Check firewall settings")
    
    # 5. Check temp directory
    print_section("4. Temporary Directory Check")
    import tempfile
    temp_dir = tempfile.gettempdir()
    print(f"📁 Temp Directory: {temp_dir}")
    
    if os.path.exists(temp_dir) and os.access(temp_dir, os.W_OK):
        print(f"✅ Temp directory exists and is writable")
    else:
        issues.append("Temp directory is not writable")
        solutions.append(f"Check permissions on {temp_dir}")
    
    # 6. Check SSH key setup (if using SSH)
    print_section("5. SSH Configuration Check (optional)")
    success, output = run_command("ssh -T git@github.com", "Testing GitHub SSH key")
    
    if not success and "You've successfully authenticated" not in output:
        print("⚠️  SSH key not configured (use HTTPS URLs instead)")
        print("   To set up SSH, follow: https://docs.github.com/en/authentication/connecting-to-github-with-ssh")
    else:
        print("✅ SSH key is configured")
    
    # 7. Test Git clone
    print_section("6. Test Git Clone")
    test_dir = os.path.join(tempfile.gettempdir(), "test-git-clone")
    os.makedirs(test_dir, exist_ok=True)
    
    success, _ = run_command(
        f"cd {test_dir} && git clone --depth 1 https://github.com/torvalds/linux.git test-repo",
        "Testing Git clone with small repository"
    )
    
    if success:
        print("✅ Git clone works!")
        # Cleanup
        import shutil
        try:
            shutil.rmtree(os.path.join(test_dir, "test-repo"))
        except:
            pass
    else:
        issues.append("Git clone failed - see error above")
        solutions.append("Check all diagnostics above")
    
    # 7. Check GitPython
    print_section("7. Python GitPython Package Check")
    try:
        import git
        print(f"✅ GitPython is installed: {git.__version__}")
    except ImportError:
        issues.append("GitPython Python package is NOT installed")
        solutions.append("Install with: pip install GitPython")
    
    # Summary
    print_section("DIAGNOSTIC SUMMARY")
    
    if not issues:
        print("✅ All diagnostics PASSED! Git is properly configured.")
        print("\n🎉 Your Git setup is ready to use!")
    else:
        print(f"❌ Found {len(issues)} issue(s):\n")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
        
        print(f"\n💡 Suggested Solutions:\n")
        for i, solution in enumerate(solutions, 1):
            print(f"   {i}. {solution}")
    
    print("\n" + "="*60 + "\n")
    
    return len(issues) == 0

def show_quick_fix():
    """Show quick fix based on OS"""
    print_section("QUICK FIX FOR YOUR SYSTEM")
    
    system = platform.system()
    
    if system == "Linux":
        print("\n📦 Install Git on Linux:")
        print("\n   Ubuntu/Debian:")
        print("   $ sudo apt-get update")
        print("   $ sudo apt-get install -y git")
        print("\n   CentOS/RHEL:")
        print("   $ sudo yum install -y git")
        print("\n   Alpine:")
        print("   $ apk add git")
    
    elif system == "Windows":
        print("\n📦 Install Git on Windows:")
        print("\n   Option 1 - Download installer:")
        print("   1. Go to https://git-scm.com/download/win")
        print("   2. Download and run the installer")
        print("   3. Follow the installation steps")
        print("\n   Option 2 - Using Chocolatey:")
        print("   $ choco install git")
        print("\n   Option 3 - Using Windows Package Manager:")
        print("   $ winget install Git.Git")
    
    elif system == "Darwin":
        print("\n📦 Install Git on macOS:")
        print("\n   Using Homebrew:")
        print("   $ brew install git")
        print("\n   Using Xcode Command Line Tools:")
        print("   $ xcode-select --install")
    
    print("\n   Then verify:")
    print("   $ git --version")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════╗
║         Git Clone Error Diagnostic Tool                    ║
║                                                            ║
║  Exit Code 128 = Git command failed                        ║
║  This usually means Git is not installed                   ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Run diagnostics
    all_ok = diagnose_git()
    
    # Show quick fix if issues found
    if not all_ok:
        show_quick_fix()
    
    sys.exit(0 if all_ok else 1)
