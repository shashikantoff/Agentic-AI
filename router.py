import re

def detect_tool(user_input):
    text = user_input.lower()

    # Image
    if "image" in text or "picture" in text or "photo" in text:
        query = text
        for word in ["image", "picture", "photo", "of", "send me", "give me", "show me", "download"]:
            query = query.replace(word, "")
        query = query.strip()
        return "image", {"query": query if query else user_input}

    # Calculator
    if re.search(r"\d+\s*[\+\-\*/]\s*\d+", text):
        return "calculator", {"expression": user_input}

    # Time
    if "time" in text or "date" in text:
        return "time", {}

    # Weather
    if any(keyword in text for keyword in ["weather", "temperature", "temprature", "temp", "forecast", "climate"]):
        city = None

        # explicit city after in/of/at
        match = re.search(r"(?:weather|temperature|temprature|temp|forecast|climate).*?(?:in|of|at)\s+(.+)", text)
        if match:
            city = match.group(1).strip()
        else:
            match = re.search(r"(?:in|of|at)\s+(.+)", text)
            if match:
                city = match.group(1).strip()

        if not city:
            city = re.sub(r"\b(weather|temperature|temprature|temp|forecast|climate|tell me|what is|what's|show me|give me|please|the|current|today|now|currently|right now|of|in|at)\b", "", text)
            city = re.sub(r"\s+", " ", city).strip()

        # Drop trailing words that aren't part of the city
        city = re.sub(r"\b(now|today|currently|please|right now)\b$", "", city).strip()

        return "weather", {"city": city}

    # News
    if "news" in text:
        topic = text.replace("news", "").replace("about", "").strip()
        return "news", {"topic": topic}

    # Dictionary
    if "meaning of" in text:
        word = text.replace("meaning of", "").strip()
        return "dictionary", {"word": word}

    return None, None