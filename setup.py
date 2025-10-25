#!/usr/bin/env python3
"""
Setup script for PredictionMart
This script sets up the entire project for development
"""

import os
import sys
import subprocess
import platform

# Hello World

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_prerequisites():
    """Check if required tools are installed"""
    print("🔍 Checking prerequisites...")
    
    # Check Python
    try:
        python_version = sys.version_info
        if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
            print("❌ Python 3.8+ is required")
            return False
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    except Exception:
        print("❌ Python not found")
        return False
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True, check=True)
        node_version = result.stdout.strip()
        print(f"✅ Node.js {node_version}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js not found. Please install Node.js 16+")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True, check=True)
        npm_version = result.stdout.strip()
        print(f"✅ npm {npm_version}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ npm not found")
        return False
    
    return True

def setup_backend():
    """Set up the Flask backend"""
    print("\n🔧 Setting up backend...")
    
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    original_dir = os.getcwd()
    
    try:
        os.chdir(backend_dir)
        
        # Create virtual environment
        if not os.path.exists('venv'):
            if not run_command(f'{sys.executable} -m venv venv', 'Creating virtual environment'):
                return False
        
        # Activate virtual environment and install dependencies
        if platform.system() == 'Windows':
            activate_cmd = 'venv\\Scripts\\activate'
            pip_cmd = 'venv\\Scripts\\pip'
        else:
            activate_cmd = 'source venv/bin/activate'
            pip_cmd = 'venv/bin/pip'
        
        if not run_command(f'{pip_cmd} install -r requirements.txt', 'Installing Python dependencies'):
            return False
            
        return True
        
    finally:
        os.chdir(original_dir)

def setup_frontend():
    """Set up the Vue.js frontend"""
    print("\n🔧 Setting up frontend...")
    
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
    original_dir = os.getcwd()
    
    try:
        os.chdir(frontend_dir)
        
        if not run_command('npm install', 'Installing Node.js dependencies'):
            return False
            
        return True
        
    finally:
        os.chdir(original_dir)

def main():
    print("🌟 PredictionMart Setup Script")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites check failed. Please install required tools.")
        sys.exit(1)
    
    print("\n✅ All prerequisites met!")
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed.")
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed.")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start the full-stack application:")
    print("   python start_full_stack.py")
    print("\n2. Or start servers individually:")
    print("   python start_backend.py  (Backend at http://localhost:5000)")
    print("   python start_frontend.py (Frontend at http://localhost:3000)")
    print("\n3. Open your browser and visit:")
    print("   http://localhost:3000")

if __name__ == '__main__':
    main()
