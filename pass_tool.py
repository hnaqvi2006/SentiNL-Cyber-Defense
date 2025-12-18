from zxcvbn import zxcvbn
import os
from google import genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

try:
    client = genai.Client(api_key=GOOGLE_API_KEY)
    AI_AVAILABLE = True
except Exception as e:
    AI_AVAILABLE = False

assert GOOGLE_API_KEY is not None

def test_password_strength(password):
    """
    Uses zxcvbn for hard math AND Gemini for helpful advice/roasts.
    """
    if not password:
        return None

    # --- 1. MATHEMATICAL ANALYSIS (zxcvbn) ---
    results = zxcvbn(password)
    
    score = results['score'] # 0 to 4
    crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']
    zxcvbn_feedback = results['feedback']['suggestions']
    
    # --- 2. RANK SYSTEM LOGIC ---
    rank = "Civilian"
    badge = "⬜"

    if score == 0:
        rank = 'Noob'
        badge = "👶"
    elif score == 1:
        rank = 'Amateur'
        badge = "🟦"
    elif score == 2:
        rank = 'Mediocre'
        badge = "🟨"
    elif score == 3:
        rank = 'Advanced'
        badge = "🟩"
    elif score == 4:
        rank = 'Master'
        badge = "🤖"

    # --- 3. AI ANALYSIS (Gemini) ---
    ai_advice = "AI analysis unavailable."
    
    if AI_AVAILABLE:
        try:
            # The Prompt: Brutal honesty + Technical tip
            prompt = (
                f"I am testing the password '{password}'. "
                "1. Give it a brutally honest, funny, 1-sentence roast about why it is weak or strong. "
                "2. Give 1 specific technical tip to make it stronger (e.g., 'Add a symbol'). "
                "Keep the total response under 50 words."
            )
            
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt
            )
            ai_advice = response.text.strip()
            
        except Exception as e:
            print(f"AI Error: {e}")
            ai_advice = "Neural link offline. Relying on math scores."

    # --- 4. RETURN AGGREGATED DATA ---
    return {
        "score": score,
        "crack_time": crack_time,
        "feedback": zxcvbn_feedback, 
        "rank": rank,               
        "badge": badge,             
        "ai_analysis": ai_advice    

    }
