# 🧩 LocalTournamentManager

**LocalTournamentManager** is an open-source application for managing trading card game tournaments (such as Pokémon TCG) in local settings (shops, communities, events).

> ⚠️ Project under development. Modular structure and easily extendable.

---

## 🧱 Technologies

| Area     | Stack                            |
| -------- | -------------------------------- |
| Backend  | Python + FastAPI                 |
| Frontend | Vue 3 + Vite + Tailwind CSS + TS |
| Desktop  | Tauri (WebView + Rust)           |
| Storage  | In-memory (file/DB coming soon)  |

---

## 🚀 Quick Start

### 📦 Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Server available at `http://localhost:8000`

---

### 💻 Frontend (Tauri + Vue)

```bash
cd desktop/local-tournament-manager-app
npm install
npm run tauri
```

> If you are using Wayland on Linux (e.g., Fedora), you may need to start with:
>
> ```bash
> GDK_BACKEND=x11 WEBKIT_DISABLE_COMPOSITING_MODE=1 npm run tauri
> ```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature/xyz`)
3. Make your changes
4. Submit a pull request

---

## 📄 License

Distributed under the **MIT** license.

---

## 👨‍💻 Author

**Federico**\
Project created to support Pokémon TCG tournaments in local shops and communities.

