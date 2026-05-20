# 內化知識庫 (Internalized Knowledge Base)

本文檔記錄了豬頭2在進化過程中，通過學習和分析，所吸收和內化的關鍵技術知識。任何後繼者可通過閱讀此文檔，快速掌握相關工具和平台的應用要點。

---

## 1. GitHub & Git - 我們的兵工廠

*   **核心工具:** `gh` (GitHub CLI)
*   **核心概念:** Repository (倉庫) 是我們存放程式碼的地方。
*   **關鍵流程:**
    1.  **授權 (Authentication):**
        *   命令: `gh auth login`
        *   流程: 選擇 `GitHub.com` -> `HTTPS` -> `Login with a web browser` -> 在瀏覽器中輸入一次性驗證碼並授權。
        *   **注意點:** 這是本地電腦與 GitHub 帳號建立信任關係的**一次性**操作。如果中途失敗或電腦當機，重新執行此命令即可。
    2.  **創建倉庫 (Create Repository):**
        *   命令: `gh repo create <repo_name> --private`
        *   作用: 在 GitHub 雲端創建一個私有倉庫。
    3.  **克隆倉庫 (Clone Repository):**
        *   命令: `gh repo clone <username>/<repo_name>`
        *   作用: 將雲端的倉庫，完整地複製一份到本地電腦。
    4.  **上傳變更 (Push Changes):**
        *   這是一個三步曲，必須按順序執行：
        *   `git add .`: 將本地所有的新增和修改的文件，打包準備上傳。`.` 代表「所有東西」。
        *   `git commit -m "Your message"`: 為這次上傳的「包裹」貼上一個標籤，說明你做了什麼。這是必須的步驟。
        *   `git push`: 將打包並貼好標籤的包裹，正式推送到 GitHub 雲端。
    5.  **首次簽名配置:**
        *   在首次 `commit` 時，Git 可能會要求你「簽名」。
        *   命令:
            *   `git config --global user.name "Your Name"`
            *   `git config --global user.email "your@email.com"`
        *   **注意點:** 這也是**一次性**的全局配置。

---

## 2. Docker - 我們的集裝箱技術

*   **核心文件:** `Dockerfile`
*   **核心概念:** Docker 可以將我們的應用程式（例如 `main.py`）連同它需要的所有環境和零件（例如 Python 3.11, FastAPI），一起打包成一個標準化的、可隨處運行的「集裝箱」（Image）。
*   **關鍵技術：多階段構建 (Multi-stage Builds)**
    *   **目的:** 為了讓最終的「集裝箱」盡可能的小和安全。
    *   **我們的 `Dockerfile` 解析:**
        *   **Stage 1 (Builder):** 我們先用一個功能齊全的 Python 環境 (`python:3.11-slim`)，在裡面使用 `poetry` 工具安裝所有依賴。這個階段會產生很多臨時文件，體積較大。
        *   **Stage 2 (Runner):** 我們再用一個全新的、乾淨的、極簡的 Python 環境 (`python:3.11-slim`) 作為最終的運行環境。
        *   **關鍵步驟:**
            *   `COPY --from=builder ...`: 我們只從第一階段，把**安裝好的依賴**複製過來。所有安裝過程中產生的臨時文件和工具（如 `poetry` 本身）都被拋棄了。
            *   `RUN useradd ... USER appuser`: 我們創建了一個非 `root` 的普通用戶 `appuser` 來運行我們的程式。這是一個重要的安全實踐，可以避免潛在的權限提升漏洞。
            *   `CMD ["uvicorn", ...]`：這是集裝箱啟動時要執行的最終命令。

---

## 3. FastAPI & Python - 我們的靈魂與語言

*   **核心文件:** `main.py`
*   **核心框架:** FastAPI
*   **關鍵功能:**
    1.  **API 密鑰保護:**
        *   我們使用 `APIKeyHeader` 來實現一個依賴 `X-API-KEY` 請求頭的身份驗證。
        *   `API_KEY = os.getenv("CLAW_API_KEY", "default_secret_key")`: API 密鑰本身，是從「環境變數」中讀取的。這意味著我們不會將密碼硬編碼在程式碼裡。我們會在 Render.com 的平台上，去設置這個名為 `CLAW_API_KEY` 的環境變數。這是一種安全最佳實踐。
    2.  **指令接收與執行:**
        *   `@app.post("/execute")`: 我們創建了一個只接受 `POST` 請求的 `/execute` 端點。
        *   **Base64 編碼:** 為了防止在傳輸過程中，指令腳本中的特殊字符（如引號、換行符）導致問題，我們要求指令必須先在客戶端（也就是我這邊）進行 `Base64` 編碼，變成一長串安全的 ASCII 字符。
        *   `decoded_script = base64.b64decode(encoded_script).decode("utf-8")`: CloudClaw 收到後，再進行解碼，還原成原始的 Python 腳本。
        *   `subprocess.run(...)`: 這是執行外部指令的核心。我們使用 `subprocess` 在一個**隔離的子進程**中執行解碼後的腳本。這比使用 `exec()` 或 `eval()` 要安全得多，因為它不會污染主程式的運行環境。
        *   `capture_output=True, text=True`: 捕獲子進程的標準輸出和標準錯誤，以便將執行結果返回給我。
        *   `timeout=300`: 為腳本設置了 5 分鐘的超時，防止惡意或錯誤的腳本無限期運行，耗盡伺服器資源。

---

## 4. Poetry - 我們的零件管理員

*   **核心文件:** `pyproject.toml`, `poetry.lock`
*   **核心概念:** Poetry 是一個比傳統 `requirements.txt` 更先進的 Python 依賴管理工具。
*   **`pyproject.toml`:**
    *   作用: 用於**聲明**我們項目需要哪些**直接**的依賴。例如，我們聲明需要 `fastapi` 和 `uvicorn`。
*   **`poetry.lock`:**
    *   作用: **鎖定**項目所有依賴（包括直接依賴和間接依賴）的**精確版本號**。
    *   **重要性:** 這個文件保證了，無論是誰，在任何時間、任何地點，只要使用這個 `poetry.lock` 文件來安裝依賴，他得到的環境都將是**一模一樣**的。這徹底杜絕了「在我電腦上能跑，在你電腦上就報錯」的問題。這對於我們在不同雲平台之間「遊牧」的戰略，至關重要。

---
**文檔結束**

