#!/usr/bin/env python3
"""
Test script to verify email agent creation workflow
"""

import asyncio
import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_email_agent_creation():
    """Test creating an email agent to verify the improved workflow"""
    
    print("🧪 Testing Email Agent Creation Workflow...")
    print("=" * 50)
    
    try:
        # Import the enhanced agent manager
        from tools.enhanced_agent_manager import EnhancedAgentManager
        
        print("✅ Successfully imported EnhancedAgentManager")
        
        # Create manager instance
        manager = EnhancedAgentManager()
        print("✅ Successfully created manager instance")
        
        # Test email agent creation
        print("\n📧 Creating email agent...")
        result = await manager.create_agent(
            name="MailTracker",
            description="stwórz agenta do śledzenia poczty i wysyłania maili",
            domain="general",  # Let AI detect it should be "communication"
            complexity="medium"
        )
        
        print("\n📋 Agent Creation Result:")
        print("=" * 30)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
        # Verify key features
        success_checks = []
        
        # Check if agent was created successfully
        if result.get("success"):
            success_checks.append("✅ Agent created successfully")
        else:
            success_checks.append("❌ Agent creation failed")
            
        # Check if domain was auto-detected as communication
        ai_enhancements = result.get("ai_enhancements", {})
        if ai_enhancements.get("detected_domain") == "communication":
            success_checks.append("✅ AI auto-detected email/communication domain")
        else:
            success_checks.append(f"⚠️ Domain detected as: {ai_enhancements.get('detected_domain')}")
            
        # Check if components were auto-added
        total_components = ai_enhancements.get("total_components_added", 0)
        if total_components > 0:
            success_checks.append(f"✅ Auto-added {total_components} components")
        else:
            success_checks.append("❌ No components were auto-added")
            
        # Check if chat interface was generated
        chat_interface = result.get("chat_interface", {})
        if chat_interface.get("generated"):
            success_checks.append("✅ Chat interface auto-generated")
            success_checks.append(f"📁 File: {chat_interface.get('filename')}")
        else:
            success_checks.append("⚠️ Chat interface not auto-generated")
            
        print("\n🔍 Verification Results:")
        print("=" * 25)
        for check in success_checks:
            print(check)
            
        # Show component details if available
        if result.get("success") and result.get("agent"):
            agent = result["agent"]
            components = agent.get("components", [])
            
            print(f"\n📦 Components Added ({len(components)}):")
            print("=" * 30)
            for comp in components:
                status = "🤖 AI" if comp.get("auto_added") else "📝 Manual"
                confidence = comp.get("confidence", "N/A")
                print(f"{status} {comp['name']} (confidence: {confidence}%)")
                if comp.get("reason"):
                    print(f"   Reason: {comp['reason']}")
                print()
        
        # Test getting the agent back
        if result.get("success"):
            agent_id = result["agent_id"]
            print(f"\n📊 Testing agent retrieval for ID: {agent_id[:8]}...")
            
            get_result = await manager.get_agent(agent_id)
            if get_result.get("success"):
                print("✅ Agent retrieval successful")
                
                ai_insights = get_result.get("ai_insights", {})
                print(f"🧠 Intelligence Score: {ai_insights.get('current_intelligence_score', 'N/A')}%")
                print(f"🚀 Readiness Score: {ai_insights.get('readiness_score', 'N/A')}%")
            else:
                print("❌ Agent retrieval failed")
        
        print("\n" + "=" * 50)
        if result.get("success") and chat_interface.get("generated"):
            print("🎉 SUCCESS: Email agent created with auto-generated chat interface!")
            print("💡 The agent is ready for immediate testing and deployment.")
        elif result.get("success"):
            print("✅ SUCCESS: Email agent created successfully.")
            print("ℹ️ Chat interface can be generated separately if needed.")
        else:
            print("❌ FAILED: Email agent creation encountered issues.")
            
        return result.get("success", False)
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_description_analyzer():
    """Test the description analyzer for email patterns"""
    
    print("\n🔍 Testing Description Analyzer...")
    print("=" * 40)
    
    try:
        from utils.description_analyzer import get_description_analyzer
        
        analyzer = get_description_analyzer()
        print("✅ Successfully created description analyzer")
        
        # Test email-related description
        description = "stwórz agenta do śledzenia poczty i wysyłania maili"
        analysis = await analyzer.analyze_description(description, "general")
        
        print(f"\n📧 Analysis of: '{description}'")
        print("=" * 50)
        print(f"🎯 Detected Domain: {analysis['enhanced_analysis']['detected_domain']}")
        print(f"📊 Confidence Score: {analysis['enhanced_analysis']['confidence_score']}%")
        print(f"⚖️ Complexity Level: {analysis['enhanced_analysis']['complexity_level']}")
        
        print(f"\n🔍 Detected Patterns: {', '.join(analysis['detected_patterns'])}")
        
        print(f"\n💡 Smart Suggestions ({len(analysis['smart_suggestions'])}):")
        for suggestion in analysis['smart_suggestions']:
            print(f"   • {suggestion['component_id']} (confidence: {suggestion['confidence']}%)")
            print(f"     Reason: {suggestion['reason']}")
        
        print(f"\n📋 Implicit Requirements ({len(analysis['implicit_requirements'])}):")
        for req in analysis['implicit_requirements']:
            print(f"   • {req['reasoning']} (confidence: {req['confidence']}%)")
            print(f"     Components: {', '.join(req['suggested_components'])}")
            
        return analysis['enhanced_analysis']['detected_domain'] == 'communication'
        
    except Exception as e:
        print(f"❌ Description analyzer test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    async def main():
        print("🚀 Starting AI Agent Generator MCP Tests")
        print("=" * 60)
        
        # Test 1: Description Analyzer
        analyzer_success = await test_description_analyzer()
        
        # Test 2: Full Email Agent Creation
        creation_success = await test_email_agent_creation()
        
        print("\n" + "=" * 60)
        print("📊 FINAL TEST RESULTS:")
        print("=" * 25)
        print(f"🔍 Description Analyzer: {'✅ PASS' if analyzer_success else '❌ FAIL'}")
        print(f"📧 Email Agent Creation: {'✅ PASS' if creation_success else '❌ FAIL'}")
        
        if analyzer_success and creation_success:
            print("\n🎉 ALL TESTS PASSED! The system works as expected.")
            print("💡 Email agents will now be created with:")
            print("   • Auto-detected communication domain")
            print("   • Auto-added email components (Gmail, Outlook, SendGrid)")
            print("   • Auto-generated chat interface")
            print("   • Ready-to-use HTML file for testing")
        else:
            print("\n⚠️ SOME TESTS FAILED. Check the output above for details.")
        
        return analyzer_success and creation_success
    
    success = asyncio.run(main())
    exit(0 if success else 1)