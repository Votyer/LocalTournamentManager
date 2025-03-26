🧹 LocalTournamentManager

LocalTournamentManager è un'applicazione open-source per la gestione di tornei di carte collezionabili (come Pokémon TCG) in contesti locali (negozi, community, eventi).

⚠️ Progetto in fase di sviluppo. Struttura modulare e facilmente estendibile.

✨ Funzionalità

✅ Creazione e gestione di tornei locali

✅ Inserimento dei risultati da parte dei giocatori

✅ Interfaccia desktop moderna grazie a Tauri

✅ Frontend in Vue 3 + Tailwind CSS + TypeScript

✅ Comunicazione con backend FastAPI

✅ Tabella dinamica per visualizzare tornei attivi

✅ Routing interno con Vue Router

🧱 Tecnologie

Area

Stack

Backend

Python + FastAPI

Frontend

Vue 3 + Vite + Tailwind CSS + TS

Desktop

Tauri (con WebView + Rust)

Storage

In-memory per ora (file/DB in futuro)

🚀 Avvio rapido

📆 Backend (FastAPI)

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Server disponibile su http://localhost:8000

💻 Frontend (Tauri + Vue)

cd desktop/local-tournament-manager-app
npm install
npm run tauri

Se usi Wayland su Linux (es. Fedora), potresti dover avviare con:

GDK_BACKEND=x11 WEBKIT_DISABLE_COMPOSITING_MODE=1 npm run tauri

💠 Funzionalità recenti

🌐 [x] Endpoint /tournaments in FastAPI che restituisce l'elenco dei tornei in JSON

📊 [x] Componente PlayerTable.vue con tabella responsive usando Tailwind

📁 [x] Routing Vue: Home, Submit, Admin, Result

📲 [x] Navbar AppMenu.vue con router-link attivi

💾 [ ] Persistenza in SQLite (in arrivo)

🤝 Contribuire

Forka il repository

Crea una branch (git checkout -b feature/xyz)

Fai le modifiche

Invia una pull request

📄 Licenza

Distribuito sotto licenza MIT.

👨‍💻 Autore

FedericoProgetto nato per supportare i tornei Pokémon TCG nei negozi e nelle community locali.

