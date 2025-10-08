#!/usr/bin/env python3
"""
Start script for PredictionMart Vue.js frontend
Run this script to start the frontend development server
"""

import os
import sys
import subprocess

def main():
    # Change to frontend directory
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
    os.chdir(frontend_dir)
    
    print("🚀 Starting PredictionMart Frontend Server...")
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Check if node_modules exists
    node_modules_path = os.path.join(frontend_dir, 'node_modules')
    if not os.path.exists(node_modules_path):
        print("⚠️  Node modules not found. Installing dependencies...")
        subprocess.run(['npm', 'install'], check=True)
        print("✅ Dependencies installed")
    
    # Start Vite development server
    print("🌐 Starting Vite development server...")
    print("📍 Frontend will be available at: http://localhost:3000")
    print("🔄 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run(['npm', 'run', 'dev'], check=True, shell=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
