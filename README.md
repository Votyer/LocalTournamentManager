# 🧩 LocalTournamentManager

**LocalTournamentManager** è un'applicazione open-source progettata per facilitare la gestione dei tornei di carte collezionabili (come Pokémon TCG) in negozi locali, associazioni ludiche o community.

> ⚠️ Progetto in fase iniziale. Le funzionalità sono in sviluppo attivo.

---

## ✨ Funzionalità

- ✅ Creazione e gestione di tornei locali
- ✅ Inserimento dei risultati da parte dei giocatori tramite interfaccia web
- ✅ Backend in FastAPI, veloce e leggero
- ✅ Frontend in Vue.js + Tailwind CSS
- ✅ Nessuna dipendenza da database: i dati vengono mantenuti in memoria

---

## 🧱 Tecnologie

| Area       | Stack                      |
|------------|----------------------------|
| Backend    | Python + FastAPI           |
| Frontend   | Vue.js 3 + Vite + Tailwind |
| Build      | PyInstaller (per .exe)     |
| Storage    | In-memory (per ora)        |

---

## 🚀 Avvio rapido

### Prerequisiti

- Python 3.10+
- Node.js + npm
- (Consigliato) Ambiente virtuale

### 📦 Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
