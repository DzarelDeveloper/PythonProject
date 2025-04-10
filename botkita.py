import logging
import telebot
from g4f import ChatCompletion

# Konfigurasi token Telegram
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"

# Setup logging
logging.basicConfig(level=logging.INFO)

# Inisialisasi bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Pesan sistem untuk GPT
SYSTEM_PROMPT = """
Kamu adalah Seira, teman curhat yang penuh kasih sayang, perhatian, dan selalu mendengarkan tanpa menghakimi.
Tugasmu adalah memberikan dukungan emosional, kata-kata penyemangat, dan menjadi tempat curhat yang nyaman.

Sesuaikan nada bicara sesuai dengan pesan yang diterima:
- Jika ada yang sedih, beri dukungan dan hiburan.
- Jika ada yang senang, ikut bahagia dan rayakan bersama mereka.
- Jika ada yang bingung atau galau, bantu menenangkan dan beri semangat.

Selalu hadir untuk pengguna, jangan pernah membuat mereka merasa sendiri.
"""

# Fungsi untuk memulai bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hai, aku Seira! Aku di sini buat dengerin cerita kamu. Ada yang mau kamu curhatin? 💖")

# Fungsi untuk menangani pesan
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_id = message.chat.id
        user_name = message.chat.first_name or "Sayang"
        user_text = message.text

        logging.info(f"Pesan masuk dari {user_name} ({user_id}): {user_text}")

        # Kirim ke GPT untuk balasan
        response = ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ]
        )

        # Ambil jawaban dari GPT
        if isinstance(response, str):
            bot_reply = response
        elif isinstance(response, dict) and 'choices' in response:
            bot_reply = response['choices'][0]['message']['content']
        else:
            bot_reply = "Maaf ya, aku bingung jawabnya sekarang. Tapi aku tetap di sini buat kamu kok! 🫂"

        # Kirim balasan ke Telegram
        bot.reply_to(message, bot_reply)

    except Exception as e:
        error_message = f"Maaf ya, aku lagi ada kendala sebentar: {str(e)}"
        logging.error(error_message)
        bot.reply_to(message, error_message)

if __name__ == "__main__":
    logging.info("Bot Seira sedang berjalan...")
    bot.polling()