mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#f9b36b'
backgroundColor='#f3e9ce'
secondaryBackgroundColor='#f9b36b'
textColor='#000000'
[server]
headless = true
port = $PORT
enableCORS = false
"> ~/.streamlit/config.toml