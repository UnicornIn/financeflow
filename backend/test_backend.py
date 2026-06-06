#!/usr/bin/env python
"""Quick test to verify backend setup."""

import sys
import asyncio

# Test imports
try:
    from app.main import app
    print("✓ FastAPI app imported successfully")
except ImportError as e:
    print(f"✗ Failed to import FastAPI app: {e}")
    sys.exit(1)

# Test services
try:
    from app.services.auth_service import AuthService
    from app.services.user_service import UserService
    from app.services.streak_service import StreakService
    from app.services.chat_service import ChatService
    from app.services.game_service import GameService
    from app.services.concept_service import ConceptService
    print("✓ All services imported successfully")
except ImportError as e:
    print(f"✗ Failed to import services: {e}")
    sys.exit(1)

# Test quick flow
async def test_flow():
    try:
        # Test register
        user, token = await AuthService.register("test@example.com", "password123", "Test User")
        print(f"✓ User registered: {user.email}")
        
        # Test login
        user2, token2 = await AuthService.login("test@example.com", "password123")
        print(f"✓ User logged in: {user2.email}")
        
        # Test token verification
        verified_id = AuthService.verify_token(token)
        print(f"✓ Token verified: {verified_id}")
        
        # Test get user
        user3 = await UserService.get_user(user.id)
        print(f"✓ User retrieved: {user3.email}")
        
        # Test get concepts
        concepts = await ConceptService.list_concepts(5)
        print(f"✓ Concepts loaded: {len(concepts)} concepts")
        
        # Test get games
        scenarios = await GameService.list_scenarios(5)
        print(f"✓ Scenarios loaded: {len(scenarios)} scenarios")
        
        print("\n✓ All tests passed! Backend is ready.")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    print("Testing FinanceFlow Backend...\n")
    asyncio.run(test_flow())
