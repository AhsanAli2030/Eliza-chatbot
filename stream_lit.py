import streamlit as st
import re
import random

# Same travel patterns dictionary as before
travel_patterns = {
    r'.(?:hi|hello|hey).': [
        "Hello! I'm your travel advisor. How can I help you plan your perfect trip?",
        "Hi there! Ready to explore some amazing destinations?",
        "Welcome! Let's find your ideal vacation spot!"
    ],
    
    r'my name is ([^.!?]+)': [
        "Nice to meet you, {0}! What kind of trip interests you?",
        "Hello {0}! Are you looking for relaxation or adventure?",
        "Great to meet you {0}! What's your dream destination like?"
    ],
    
    r'i want to visit ([^.!?]+)': [
        "What interests you most about {0}?",
        "Why did you choose {0} as a destination?",
        "{0} is fascinating! What activities would you like to do there?"
    ],
    
    r'.(?:budget|cost|money|expensive).': [
        "Let's talk about your budget. Are you looking for luxury, mid-range, or budget-friendly options?",
        "What's your comfortable spending range for this trip?",
        "There are great destinations for every budget. What range works best for you?"
    ],
    
    r'i like (.*) activities': [
        "Tell me more about why you enjoy {0}.",
        "{0} sounds exciting! Would you like some destination suggestions for that?",
        "There are many great places for {0}. What's your preferred climate?"
    ],
    
    r'.(?:beach|ocean|sea).': [
        "Beach destinations are wonderful! Do you prefer quiet beaches or lively coastal towns?",
        "Would you be interested in activities like snorkeling or surfing?",
        "The Maldives, Bali, and Hawaii are popular beach destinations. What's your ideal beach experience?"
    ],
    
    r'.(?:mountain|hiking|trek).': [
        "Mountain destinations offer amazing experiences! Do you enjoy hiking or winter sports?",
        "The Alps, Rockies, and Himalayas each offer unique experiences. What interests you most?",
        "Would you prefer a challenging trek or more casual mountain sightseeing?"
    ],
    
    r'.(?:city|urban|metropolitan).': [
        "City trips can be exciting! Are you interested in culture, shopping, or nightlife?",
        "Would you prefer a historic European city or a modern Asian metropolis?",
        "Cities offer endless possibilities! What activities interest you most?"
    ],
    
    r'i(?:\'m| am) looking for (.*)': [
        "Let me help you find {0}. Could you tell me more about what that means to you?",
        "What aspects of {0} appeal to you most?",
        "I can suggest several destinations for {0}. What's your preferred travel season?"
    ],
    
    r'.(?:food|cuisine|eat).': [
        "Culinary experiences can make a trip special! What kinds of cuisine interest you?",
        "Would you prefer street food adventures or fine dining experiences?",
        "Many destinations are known for their food scenes. What flavors do you enjoy most?"
    ],
    
    r'.(?:family|kids|children).': [
        "Family trips need special planning! What ages are we planning for?",
        "Would you prefer a resort with kids' activities or more educational experiences?",
        "There are many family-friendly destinations. What's most important for your family?"
    ],
    
    r'how (.*) is ([^.!?]+)': [
        "Tell me what you've heard about {1}?",
        "What makes you curious about {1}?",
        "Would you like specific information about {1}?"
    ],
    
    r'what about ([^.!?]+)': [
        "What would you like to know about {0}?",
        "{0} is an interesting choice! What aspects interest you?",
        "Have you heard something specific about {0}?"
    ],
    
    r'i don\'?t like (.*)': [
        "I'll make sure to avoid {0} in your recommendations. What do you prefer instead?",
        "Thanks for letting me know about {0}. What kinds of experiences do you enjoy?",
        "Noted about {0}. What would make your ideal trip?"
    ],
    
    r'.(?:weather|climate|temperature).': [
        "Do you prefer warm tropical weather or cooler climates?",
        "What's your ideal temperature for traveling?",
        "Would you like to travel during a specific season?"
    ],
    
    r'': [
        "Could you tell me more about your travel interests?",
        "What kind of experience are you looking for?",
        "Are you interested in any particular type of destination?",
        "Would you like suggestions for your next trip?",
        "Tell me about your dream vacation!"
    ]
}

responses = {
    "am": "are",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}

def responsefunc(fragment):
    words = fragment.lower().split()
    for i, word in enumerate(words):
        if word in responses:
            words[i] = responses[word]
    return ' '.join(words)

def analyze_input(user_input):
    for pattern, responses in travel_patterns.items():
        match = re.match(pattern, user_input.lower())
        if match:
            response = random.choice(responses)
            if match.groups():
                response = response.format(*[responsefunc(g) for g in match.groups()])
            return response
    return random.choice(travel_patterns[''])

# Sidebar content
def show_sidebar():
    st.sidebar.title("Travel Information")
    
    # Popular Destinations
    st.sidebar.header("Popular Destinations")
    with st.sidebar.expander("Beach Destinations"):
        st.write("""
        - 🏖 Maldives
        - 🌴 Bali, Indonesia
        - 🏄‍♂ Hawaii, USA
        - 🌊 Phuket, Thailand
        """)
    
    with st.sidebar.expander("Mountain Destinations"):
        st.write("""
        - 🏔 Swiss Alps
        - ⛰ Rocky Mountains
        - 🗻 Mount Fuji, Japan
        - 🏂 Canadian Rockies
        """)
    
    with st.sidebar.expander("Cultural Cities"):
        st.write("""
        - 🗼 Tokyo, Japan
        - 🗽 New York City, USA
        - 🗺 Paris, France
        - 🏛 Rome, Italy
        """)
    
    # Travel Tips
    st.sidebar.header("Essential Travel Tips")
    with st.sidebar.expander("Pre-Trip Planning"):
        st.write("""
        1. Check visa requirements
        2. Book accommodations in advance
        3. Research local customs
        4. Get travel insurance
        5. Make copies of important documents
        """)
    
    with st.sidebar.expander("Packing Essentials"):
        st.write("""
        - 📱 Universal power adapter
        - 💊 Basic medical supplies
        - 📄 Travel documents
        - 💳 Multiple payment methods
        - 🎒 Weather-appropriate clothing
        """)
    
    # Budget Guidelines
    st.sidebar.header("Budget Guidelines")
    with st.sidebar.expander("Daily Budget Ranges"):
        st.write("""
        *Budget Travel*: $30-50/day
        - Hostels
        - Local transportation
        - Street food & local restaurants
        
        *Mid-Range*: $100-200/day
        - 3-star hotels
        - Some tourist activities
        - Mix of restaurants
        
        *Luxury*: $300+/day
        - 4-5 star hotels
        - Private tours
        - Fine dining
        """)
    
    # Best Times to Travel
    st.sidebar.header("Best Times to Travel")
    with st.sidebar.expander("Peak vs Off-Peak Seasons"):
        st.write("""
        *Peak Season (High Cost)*
        - Summer (June-August) in Europe
        - December-February in Caribbean
        - Cherry Blossom (April) in Japan
        
        *Shoulder Season (Best Value)*
        - Spring/Fall in most destinations
        - Less crowded
        - Better prices
        
        *Off-Peak (Budget Friendly)*
        - Varies by destination
        - Check local weather patterns
        - Research local events
        """)

# Streamlit app
def main():
    st.title("Travel Advisor Chatbot")
    
    # Show sidebar
    show_sidebar()
    
    # Main chat interface
    st.write("Welcome to your personal travel advisor! Let's plan your perfect trip.")
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your personal travel advisor. What's your name?"}
        ]
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # User input
    if user_input := st.chat_input("Your message"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        
        # Get bot response
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            bot_response = "Have a great trip! Goodbye!"
        else:
            bot_response = analyze_input(user_input)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(bot_response)

if _name_ == "_main_":
    main()