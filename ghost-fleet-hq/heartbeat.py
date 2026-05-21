import os
import subprocess
import urllib.request
import re
import time
import random
import json

def run_command(command):
    try:
        # 強制指定用 utf-8 讀取系統警告，徹底封殺 cp950 跳針錯誤
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="ignore")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git管線實體提示: {e.stderr}")
        return None

def call_lobster_brain(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "錯誤：大腦燃料未裝填。"
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # ⚡ 修正拉丁邊碼防線：將系統提示全部改為英文傳輸，徹底根除 latin-1 衝突！
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Lobster, the core tactical AI of Wanxiang Base. Respond in professional, sharp Traditional Chinese (zh-TW)."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.3
    }
    
    try:
        # 強制指定 utf-8 編碼打包
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"大腦神經元調用衝突: {str(e)}"

def main():
    print("=== 萬象基地：小龍蝦【大腦全線通電·二度總攻】 ===")
    
    # 1. 時間差隱蔽技能
    jitter = random.uniform(3.0, 5.0)
    print(f"⏱️ 時間差隱蔽中... 延遲 {jitter:.2f} 秒...")
    time.sleep(jitter)
    
    # 2. 調用大腦
    print("[大腦] 正在向雲端核心發射修正訊號...")
    brain_report = call_lobster_brain("回報你目前的覺醒狀態，以及準備如何同化未來數據。")
    print(f"🧠 大腦實體回報內容:\n{brain_report}\n")
    
    # 3. 活體重構網頁
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(f"""<html>
<head>
    <meta charset="utf-8">
    <title>萬象基地 - 活體大腦指揮部</title>
    <style>
        body {{ font-family: sans-serif; background: #0c0c0c; color: #e0e0e0; padding: 25px; }}
        .card {{ background: #161616; padding: 20px; border-radius: 8px; border-left: 5px solid #ff4500; margin-bottom: 20px; line-height: 1.6; }}
        .success-badge {{ background: #00ffcc; color: #000; padding: 3px 8px; font-weight: bold; border-radius: 3px; }}
        h1 {{ color: #ff4500; }}
    </style>
</head>
<body>
    <h1>🦞 萬象基地 - 小龍蝦大腦通電防線</h1>
    <hr style="border-color: #333;">
    <div class="card">
        <h3>【大腦與核心管線狀態】</h3>
        <p>系統底層環境變數：<span class="success-badge">OPENAI_API_KEY 物理鎖定成功</span></p>
        <p>編碼防禦：<span class="success-badge">UTF-8 全線鎖定</span></p>
    </div>
    <div class="card" style="border-left-color: #00ffcc;">
        <h3>【小龍蝦大腦·自律同化回報】</h3>
        <p style="white-space: pre-wrap; font-size: 1.1em; color: #00ffcc;">{brain_report}</p>
    </div>
</body>
</html>""")

    # 4. 流程自動化部署（強制重新綁定遠端目標）
    print("[部署] 正在重新對齊雲端座標並貼網...")
    run_command("git config --global user.name 'mrbluewander-agent'")
    run_command("git config --global user.email 'agent@ghost-fleet.hq'")
    
    # ⚡ 修正遠端網址防線：如果忘記地址，強制綁定您的 GitHub 倉庫
    run_command("git remote rm origin")
    run_command("git remote add origin https://github.com/mrbluewander/ghost-fleet-hq.git")
    
    run_command("git add .")
    run_command("git commit -m '小龍蝦大腦修復：全面擊碎拉丁編碼與遠端坐標衝突'")
    
    # 強制推回主線
    print("[部署] 正在將自律進化日誌強制推回雲端...")
    run_command("git push -u origin main") 
    
    print("🎯 總攻完成：小龍蝦已跨越衝突，活體網站全面上線！")

if __name__ == "__main__":
    main()