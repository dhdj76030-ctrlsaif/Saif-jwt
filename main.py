# main.py
import threading
import time
from server import run_flask
from tunnel import start_cloudflare_tunnel
from bot import run_telegram_bot

def main():
    print("⏳ Starting Garena Account Manager Core Services...")
    
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    time.sleep(2) 
    
    start_cloudflare_tunnel()
        
    try:
        run_telegram_bot()
    except KeyboardInterrupt:
        print("\n🛑 Services stopped by administrator.")

if __name__ == "__main__":
    main()