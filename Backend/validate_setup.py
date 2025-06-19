#!/usr/bin/env python3
"""
Validation script for RU Carpooling Backend
Tests that all imports work and basic functionality is available
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        from app.main import app
        print("✓ FastAPI app imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import app: {e}")
        return False
    
    try:
        from app.core.config import settings
        print("✓ Settings configuration imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import settings: {e}")
        return False
    
    try:
        from app.api.routes import router
        print("✓ API routes imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import routes: {e}")
        return False
        
    return True

def test_configuration():
    """Test configuration settings"""
    print("\nTesting configuration...")
    
    try:
        from app.core.config import settings
        print(f"✓ App name: {settings.app_name}")
        print(f"✓ AWS region: {settings.aws_region}")
        print(f"✓ Log level: {settings.log_level}")
        print(f"✓ JWT algorithm: {settings.jwt_algorithm}")
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False

def test_required_dependencies():
    """Test that required dependencies are available"""
    print("\nTesting dependencies...")
    
    required_modules = [
        'fastapi',
        'pydantic', 
        'uvicorn',
        'boto3',
        'mangum',
        'python_dotenv',
        'pydantic_settings'
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✓ {module}")
        except ImportError:
            print(f"✗ {module} - not installed")
            return False
    
    return True

def main():
    """Run all validation tests"""
    print("🚀 RU Carpooling Backend Validation\n")
    
    tests = [
        test_required_dependencies,
        test_imports,
        test_configuration
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✅ All tests passed! Backend is ready for development.")
        print("\nNext steps:")
        print("1. Copy .env.example to .env and fill in your credentials")
        print("2. Run: uvicorn app.main:app --reload")
        print("3. Visit: http://localhost:8000/docs for API documentation")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
