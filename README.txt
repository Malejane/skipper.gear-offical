SKIPPER WEBSITE UPGRADE

Included:
- index.html: separate upgraded copy of your original website
- app.py: optional Python Flask product-catalogue API
- requirements.txt: Flask dependency

New storefront features:
- Product search
- Product sorting by price/name
- More product categories and demo items
- Wishlist saved in the browser
- Shopping cart saved in the browser after refresh
- Mobile-friendly existing layout retained

IMPORTANT:
GitHub Pages cannot execute Python. If you keep hosting on GitHub Pages, the HTML features work with the built-in demo catalogue and Python API calls safely fall back. To run Python, deploy the Flask backend to a Python-compatible host.

Run locally:
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run: python -m venv .venv
4. Activate on Windows PowerShell: .venv\\Scripts\\Activate.ps1
5. Run: pip install -r requirements.txt
6. Run: python app.py
7. Open: http://127.0.0.1:5000

Before publishing:
- Back up your GitHub repository first.
- Replace sample product photos, product names, prices and sizes with real SKIPPER inventory.
- The photos and catalogue are illustrative examples, not confirmed SKIPPER stock.
- Checkout is still a preview; PayFast is NOT connected.
- Do not collect customer passwords or card details in this demo.
- A real PayFast checkout needs secure server-side payment initiation and notification verification.
