
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add current directory to path so we can import our modules
sys.path.append(os.getcwd())

from storage.git_handler import GitHandler
from utils.logger import Logger

def test_git_workflow():
    # Attempt to load .env if it exists
    load_dotenv()
    
    logger = Logger("TestWorkflow")
    handler = GitHandler()
    
    # The specific URL requested by the user
    repo_url = "https://github.com/kavyacp123/test-demo.git"
    
    logger.info("=" * 60)
    logger.info(f"STARTING LOCAL TEST FOR: {repo_url}")
    logger.info("=" * 60)
    
    # Check if GITHUB_TOKEN is available
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        logger.info(f"✅ GITHUB_TOKEN found: {token[:4]}...{token[-4:]}")
    else:
        logger.warning("⚠️  GITHUB_TOKEN NOT FOUND in environment. (Will attempt public clone)")
    
    # Run the clone
    result = handler.clone_repository(
        repo_url=repo_url, 
        branch="main", 
        depth=1
    )
    
    if result["success"]:
        logger.info("=" * 60)
        logger.info("🎉 SUCCESS! GIT WORKFLOW IS WORKING!")
        logger.info(f"📁 Local Path: {result['local_path']}")
        logger.info(f"📊 Branch: {result['branch']}")
        logger.info("=" * 60)
        
        # Keep the files for the user to see, but offer cleanup code
        logger.info(f"Note: Files are in {result['local_path']}. You can delete them manually or run cleanup.")
        # handler.cleanup_repository(result["repo_name"])
    else:
        logger.error("=" * 60)
        logger.error("❌ CLONE FAILED")
        logger.error(f"Reason: {result['error']}")
        if "details" in result:
             logger.error(f"Details: {result['details']}")
        logger.error("=" * 60)

if __name__ == "__main__":
    test_git_workflow()
