#!/usr/bin/env python3
"""Test script to validate create_agent functionality"""

import sys
import asyncio
import json

# Add src to path
sys.path.insert(0, 'src')

async def test_create_agent():
    """Test the create_agent function directly"""
    
    # Import the enhanced agent manager directly
    from tools.enhanced_agent_manager import EnhancedAgentManager
    
    # Create instance
    agent_manager = EnhancedAgentManager()
    
    print("🧪 Testing create_agent functionality...")
    print("📝 Creating mail tracker agent...")
    
    # Test create_agent
    result = await agent_manager.create_agent(
        name="Mail Tracker & Responder",
        description="Agent do monitorowania skrzynki pocztowej, wykrywania nowych wiadomości i automatycznego odpowiadania na nie.",
        domain="email",
        complexity="medium"
    )
    
    print("\n✅ Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Check if it was successful
    if result.get("success"):
        print(f"\n🎉 SUCCESS! Agent '{result['agent']['name']}' created successfully!")
        print(f"📊 Agent ID: {result['agent_id']}")
        print(f"🔧 Components: {len(result['agent']['components'])}")
        print(f"⚡ Ready to use: {result.get('ready_to_use', False)}")
    else:
        print(f"\n❌ FAILED: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    try:
        asyncio.run(test_create_agent())
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()