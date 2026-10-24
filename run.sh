#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
cd ~/abdi-web
while true; do
  python3 bot.py >> bot.log 2>&1
  sleep 5
done
