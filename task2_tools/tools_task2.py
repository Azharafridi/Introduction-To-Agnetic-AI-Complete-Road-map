import os
import base64
from typing import Optional, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


_last_description = None


@tool
def describe_image(image_path: str) -> str:
    """
    Generate a detailed text description of an image using GPT-4o mini Vision.
    
    This tool MUST be used FIRST before list_objects can be called.
    
    Args:
        image_path: Path to the image file (e.g., '/path/to/image.jpg')
        
    Returns:
        Detailed description of the image including objects, people, actions, and setting
    """
    global _last_description
    
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found in environment variables"
        
        if not os.path.exists(image_path):
            return f"Error: Image file not found at path: {image_path}"
        
        vision_llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=api_key,
            temperature=0.7
        )
        
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        image_format = image_path.lower().split('.')[-1]
        if image_format == 'jpg':
            image_format = 'jpeg'
        
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "Please provide a detailed description of this image. Include information about objects, people, actions, setting, colors, and any other notable details."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{image_format};base64,{base64_image}"
                    }
                }
            ]
        )
        
        response = vision_llm.invoke([message])
        description = response.content
        
        _last_description = description
        
        return f"Image Description:\n{description}"
        
    except FileNotFoundError:
        return f"Error: Image file not found at path: {image_path}"
    except Exception as e:
        return f"Error describing image: {str(e)}"


@tool
def list_objects(description_input: str) -> str:
    """
    Extract and list all objects from an image description.
    
    This tool should ONLY be used AFTER describe_image has been called.
    
    Args:
        description_input: Either 'last' to use the previous description, or a custom text description
        
    Returns:
        Bullet-point list of all objects, people, and items found in the description
    """
    global _last_description
    
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found in environment variables"
        
        if description_input.lower().strip() == "last":
            if not _last_description:
                return "Error: No previous image description available. Please use describe_image tool first."
            description = _last_description
        else:
            description = description_input
        
        extraction_llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=api_key,
            temperature=0.7
        )
        
        message = HumanMessage(
            content=f"""Based on the following image description, extract and list all objects, items, and entities mentioned.
Present them as a clear bullet-point list.

Description:
{description}

Please provide a comprehensive list of all objects, people, animals, and items mentioned."""
        )
        
        response = extraction_llm.invoke([message])
        object_list = response.content
        
        return f"Objects Found:\n{object_list}"
        
    except Exception as e:
        return f"Error extracting objects: {str(e)}"


class SimpleVisionAgent:

    def __init__(self, api_key: Optional[str] = None, verbose: bool = True):
        """
        Initialize the Vision Agent
        
        Args:
            api_key: OpenAI API key (if None, reads from OPENAI_API_KEY env var)
            verbose: Whether to print progress messages
            
        Raises:
            ValueError: If no API key is provided or found in environment
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set in OPENAI_API_KEY environment variable")
        
        os.environ["OPENAI_API_KEY"] = self.api_key
        
        self.verbose = verbose
        self.tools = [describe_image, list_objects]
    
    def analyze_image(self, image_path: str) -> str:
        """
        Analyze an image by describing it and extracting objects
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Analysis results including description and object list
        """
        if self.verbose:
            print("\n🔧 Tool 1: describe_image")
            print(f"   Input: {image_path}")
        
        description_result = describe_image.invoke({"image_path": image_path})
        
        if self.verbose:
            print(f"   Output: {description_result[:100]}...")
        
        if description_result.startswith("Error:"):
            return description_result
        
        if self.verbose:
            print("\n🔧 Tool 2: list_objects")
            print("   Input: last")
        
        objects_result = list_objects.invoke({"description_input": "last"})
        
        if self.verbose:
            print(f"   Output: {objects_result[:100]}...")
        
        final_result = f"""
{description_result}

{objects_result}
"""
        return final_result.strip()
    
    def run(self, query: str) -> str:
        """
        Run a custom query through the agent
        
        This method tries to extract image path from the query and analyze it.
        
        Args:
            query: User query/instruction
            
        Returns:
            Agent response
        """

        words = query.split()
        image_path = None
        
        for word in words:
            if '/' in word or '\\' in word or word.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')):
                image_path = word.strip('"\' ')
                break
        
        if not image_path:
            return "Error: Could not find image path in query. Please provide a valid image path."
        
        return self.analyze_image(image_path)


def create_sample_image(image_path: str) -> bool:
    """
    Create a sample test image with basic shapes
    
    Args:
        image_path: Path where the image should be saved
        
    Returns:
        True if successful, False otherwise
    """
    try:
        from PIL import Image, ImageDraw
        
        img = Image.new('RGB', (800, 600), color='lightblue')
        draw = ImageDraw.Draw(img)

        draw.rectangle([100, 100, 300, 300], fill='red', outline='black', width=3)
        draw.ellipse([400, 150, 600, 350], fill='yellow', outline='black', width=3)
        draw.polygon([(700, 500), (650, 400), (750, 400)], fill='green', outline='black')

        draw.text((250, 50), "Test Image: Shapes", fill='black')

        img.save(image_path)
        return True
    except ImportError:
        print("⚠ PIL/Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"⚠ Error creating sample image: {e}")
        return False


def main():
    """Example usage of the Simple Vision Agent"""
    
    print("=" * 80)
    print("Simple Vision Agent (No Complex LangChain Dependencies)")
    print("=" * 80)
    
    try:

        agent = SimpleVisionAgent(verbose=True)
        print("✓ Agent initialized successfully")
        print(f"✓ Tools loaded: {[tool.name for tool in agent.tools]}")
        print()
        
        image_path = input("Enter your image path (or press Enter for default 'test_image.jpg'): ").strip()
        if not image_path:
            image_path = "test_image.jpg"
        
        if not os.path.exists(image_path):
            print(f"\n⚠ Image not found at: {image_path}")
            print("Creating sample image for testing...")
            
            if create_sample_image(image_path):
                print(f"✓ Sample image created at: {image_path}\n")
            else:
                print("❌ Could not create sample image. Please provide your own image.")
                return
        
        print(f"\nAnalyzing image: {image_path}")
        print("-" * 80)
        
        result = agent.analyze_image(image_path)

        print("\n" + "=" * 80)
        print("FINAL RESULT:")
        print("=" * 80)
        print(result)
        
        print("\n" + "=" * 80)
        print("Tool Information:")
        print("=" * 80)
        print(f"Tool 1: {describe_image.name}")
        print(f"  Description: {describe_image.description[:100]}...")
        print(f"\nTool 2: {list_objects.name}")
        print(f"  Description: {list_objects.description[:100]}...")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nTo use this agent, you need to set your OpenAI API key:")
        print("  1. Set environment variable:")
        print("     export OPENAI_API_KEY='your-api-key-here'")
        print("  2. Or pass it directly:")
        print("     agent = SimpleVisionAgent(api_key='your-api-key-here')")
    except KeyboardInterrupt:
        print("\n\n⚠ Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()