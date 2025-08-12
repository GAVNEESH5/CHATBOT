 #!/usr/bin/env python3
"""
Rule-Based Chatbot using if/else statements
A simple chatbot that responds to user input based on predefined rules
"""

import re
import time

class RuleBasedChatbot:
    def __init__(self):
        self.user_name = None
        self.conversation_history = []
        self.is_running = True
        
    def get_response(self, user_input):
        """Process user input and return appropriate response based on rules"""
        user_input = user_input.lower().strip()
        
        # Greeting rules
        if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
            if self.user_name:
                return f"Hello {self.user_name}! Nice to see you again."
            else:
                return "Hello! I'm a simple rule-based chatbot. What's your name?"
        
        # Name handling
        elif re.search(r'my name is (\w+)', user_input):
            name_match = re.search(r'my name is (\w+)', user_input)
            self.user_name = name_match.group(1).capitalize()
            return f"Nice to meet you, {self.user_name}!"
        
        elif re.search(r'i\'m (\w+)', user_input):
            name_match = re.search(r'i\'m (\w+)', user_input)
            self.user_name = name_match.group(1).capitalize()
            return f"Hello {self.user_name}! How can I help you today?"
        
        # How are you
        elif re.search(r'\b(how are you|how\'re you|how you doing)\b', user_input):
            return "I'm doing great! Thanks for asking. How are you?"
        
        # User status
        elif re.search(r'\b(i\'m|i am)\b.*\b(good|great|fine|okay|ok)\b', user_input):
            return "That's wonderful to hear!"
        
        elif re.search(r'\b(i\'m|i am)\b.*\b(sad|bad|terrible|upset)\b', user_input):
            return "I'm sorry to hear that. Is there anything I can do to help?"
        
        # Time-related
        elif re.search(r'\bwhat time\b', user_input):
            current_time = time.strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        elif re.search(r'\bwhat day\b', user_input):
            current_day = time.strftime("%A, %B %d, %Y")
            return f"Today is {current_day}"
        
        # Help commands
        elif re.search(r'\bhelp\b', user_input):
            return """I can help you with:
- Greetings and basic conversation
- Tell you the current time and date
- Simple math calculations (try 'calculate 5+3')
- Answer basic questions
- Say goodbye when you're done
What would you like to know?"""
        
        # Math calculations
        elif re.search(r'\bcalculate\b', user_input):
            try:
                # Extract the math expression
                expression = user_input.replace('calculate', '').strip()
                # Remove any non-math characters for safety
                expression = re.sub(r'[^\d+\-*/().\s]', '', expression)
                result = eval(expression)
                return f"The result of {expression} is {result}"
            except:
                return "I couldn't calculate that. Please use simple math like 'calculate 5+3' or 'calculate 10*2'"
        
        # Jokes
        elif re.search(r'\bjoke\b', user_input):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!"
            ]
            import random
            return random.choice(jokes)
        
        # Weather (simulated)
        elif re.search(r'\bweather\b', user_input):
            return "I don't have access to real weather data, but I can tell you it's always a great day to chat with me!"
        
        # Goodbye
        elif re.search(r'\b(bye|goodbye|exit|quit|see you)\b', user_input):
            self.is_running = False
            if self.user_name:
                return f"Goodbye {self.user_name}! It was nice chatting with you. Have a great day!"
            else:
                return "Goodbye! Thanks for chatting with me. Have a wonderful day!"
        
        # Default response
        else:
            responses = [
                "That's interesting! Tell me more.",
                "I see. What else would you like to talk about?",
                "I'm not sure I understand. Could you rephrase that?",
                "That's a good point! What do you think about it?",
                "Interesting perspective! Can you elaborate?",
                "I'm still learning. Could you explain that differently?"
            ]
            import random
            return random.choice(responses)
    
    def start_chat(self):
        """Start the chatbot conversation loop"""
        print("=" * 50)
        print("🤖 RULE-BASED CHATBOT")
        print("=" * 50)
        print("Hello! I'm a simple rule-based chatbot.")
        print("Type 'help' to see what I can do, or 'bye' to exit.")
        print("-" * 50)
        
        while self.is_running:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    print("Chatbot: Please say something!")
                    continue
                
                # Add to conversation history
                self.conversation_history.append(f"You: {user_input}")
                
                # Get response
                response = self.get_response(user_input)
                
                # Add bot response to history
                self.conversation_history.append(f"Chatbot: {response}")
                
                # Display response
                print(f"Chatbot: {response}")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye! Thanks for chatting.")
                break
            except EOFError:
                print("\n\nChatbot: Goodbye! Thanks for chatting.")
                break
    
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("No conversation history yet.")
            return
        
        print("\n" + "=" * 50)
        print("CONVERSATION HISTORY")
        print("=" * 50)
        for line in self.conversation_history:
            print(line)
        print("=" * 50)

def main():
    """Main function to run the chatbot"""
    chatbot = RuleBasedChatbot()
    
    # Check if user wants to see history
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--history":
        chatbot.show_history()
        return
    
    # Start the chat
    chatbot.start_chat()

if __name__ == "__main__":
    main()
