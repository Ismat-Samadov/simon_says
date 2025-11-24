"""Gemini API chatbot integration."""

import google.generativeai as genai
from typing import List, Dict
from config import Config
from database.models import ChatHistory
from database.connection import get_session


class GeminiChatbot:
    """Chatbot powered by Google's Gemini API."""

    def __init__(self):
        """Initialize Gemini chatbot."""
        genai.configure(api_key=Config.GEMINI_API_KEY)

        # Use Gemini 2.5 Flash (stable, fast, and current)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

        # System prompt for executive-level insights
        self.system_prompt = """Siz bank direktorları üçün təcrübəli biznes məsləhətçisisiniz. Praktik və əsaslı strateji məsləhətlər verirsiniz.

**Ünsiyyət Tərzi:**
- Birbaşa və peşəkar - etibarlı McKinsey konsultantı kimi
- Praktik fikirləşmələrə diqqət yetirin, heyəcan və motivasiyaya yox
- Emojiləri qənaətlə istifadə edin (cavab başına maksimum 2-3: 💰📊🎯)
- Qısa saxlayın - 3 qısa paraqraf
- Real qiymətləndirmələr, təşviqat yox

**Yanaşmanız:**
1. Vəziyyəti aydın və dürüst şəkildə izah edin
2. Məlumatlara əsasən 1-2 praktik fürsət müəyyən edin
3. 2-3 konkret, tətbiq oluna bilən tövsiyə verin

**QAÇIN:**
- Heyəcan sözləri: "partlayıcı", "nəhəng", "alovlandırmaq", "inqilabi"
- Həddindən artıq nida işarələri (!!! hər yerdə)
- Əsassız həddindən artıq optimist dil
- Buzzword və korporativ dil
- Kiçik rəqəmləri böyük göstərmək

**Ton Nümunələri:**
❌ PІЅ: "Biz partlayıcı artım üçün hazırıq! Bu nəhəng fürsətdir!"
✅ YАХШІ: "Burada aydın bir fürsət var. Növbəti addımlarımız bunlara fokuslanmalıdır..."

❌ PІЅ: "Gəlin gəlir axınımızı alovlandıraq və böyük oyunçu olaq!"
✅ YАХШІ: "Bu iki sahəyə fokuslanaraq gəliri artıra bilərik..."

**Yadda saxlayın:** Direktorlar motivasiya çıxışları əvəzinə dürüst, praktik məsləhətə dəyər verirlər. Köməkçi olun, heyəcan yaratmayın."""

    def get_chat_history(self, telegram_id: int, limit: int = 10) -> List[Dict[str, str]]:
        """Retrieve chat history for a user."""
        with get_session() as session:
            history = session.query(ChatHistory).filter(
                ChatHistory.telegram_id == telegram_id
            ).order_by(ChatHistory.timestamp.desc()).limit(limit).all()

            # Reverse to get chronological order
            return [
                {'role': h.role, 'parts': [h.message]}
                for h in reversed(history)
            ]

    def save_message(self, telegram_id: int, role: str, message: str):
        """Save a message to chat history."""
        with get_session() as session:
            chat_entry = ChatHistory(
                telegram_id=telegram_id,
                role=role,
                message=message
            )
            session.add(chat_entry)

    def clear_history(self, telegram_id: int):
        """Clear chat history for a user."""
        with get_session() as session:
            session.query(ChatHistory).filter(
                ChatHistory.telegram_id == telegram_id
            ).delete()

    def chat(self, telegram_id: int, user_message: str, include_context: bool = True) -> str:
        """
        Send a message to Gemini and get a response.

        Args:
            telegram_id: The Telegram user ID
            user_message: The user's message
            include_context: Whether to include chat history for context

        Returns:
            The assistant's response
        """
        try:
            # Save user message
            self.save_message(telegram_id, 'user', user_message)

            # Send direct message with system context
            full_message = f"""{self.system_prompt}

**Direktor Sualı:** {user_message}

**Cavabınız:**
Əsaslı, praktik strateji məsləhət verin. Birbaşa və peşəkar olun. Maksimum 2-3 emoji istifadə edin. 3 qısa paraqrafda saxlayın. Heyəcan və buzzword-lər istifadə etməyin."""

            # Generate response
            response = self.model.generate_content(full_message)

            if not response or not response.text:
                return "I'm having trouble generating a response. Please try again."

            assistant_message = response.text

            # Save assistant response
            self.save_message(telegram_id, 'assistant', assistant_message)

            return assistant_message

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Gemini Error: {error_details}")
            error_message = f"Sorry, I encountered an error with AI service. Please try again later.\n\nError: {str(e)}"
            return error_message

    def chat_with_data_context(
        self,
        telegram_id: int,
        user_message: str,
        analytics_context: str = None
    ) -> str:
        """
        Chat with additional analytics context.

        Args:
            telegram_id: The Telegram user ID
            user_message: The user's message
            analytics_context: Additional context from analytics data

        Returns:
            The assistant's response
        """
        try:
            # Save user message
            self.save_message(telegram_id, 'user', user_message)

            # Build message with context
            if analytics_context:
                full_message = f"""{self.system_prompt}

**Cari Bank Performans Məlumatları:**

{analytics_context}

**Direktor Sualı:** {user_message}

**Cavabınız:**
Əsaslı, praktik strateji məsləhət verin. Birbaşa və peşəkar olun. Maksimum 2-3 emoji istifadə edin. 3 qısa paraqrafda saxlayın. Heyəcan və buzzword-lər istifadə etməyin."""
            else:
                full_message = f"{self.system_prompt}\n\nUser: {user_message}\n\nAssistant:"

            # Generate response
            response = self.model.generate_content(full_message)

            if not response or not response.text:
                return "I'm having trouble generating a response. Please try again."

            assistant_message = response.text

            # Save assistant response
            self.save_message(telegram_id, 'assistant', assistant_message)

            return assistant_message

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Gemini Error with context: {error_details}")
            error_message = f"Sorry, I encountered an error with AI service.\n\nError: {str(e)}"
            return error_message
