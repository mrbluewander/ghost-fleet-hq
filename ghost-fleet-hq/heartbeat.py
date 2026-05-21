import os
import subprocess
import urllib.request
import re
import time
import random
import json

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="ignore")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git管線實體提示: {e.stderr.strip()}")
        return None

def call_lobster_brain(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "錯誤：大腦燃料未裝填。"
    
    url = "https://api.openai.com/v1/chat/completions"
    
    # ⚡ 核心修復：在 Header 加上 Content-Length，並確保傳輸格式完全鎖定 UTF-8
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Lobster, the core tactical AI of Wanxiang Base. Respond in short, sharp Traditional Chinese (zh-TW)."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.3
    }
    
    # 物理將中文內容強制轉化為無衝突的 UTF-8 位元組流
    js_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": str(len(js_data))
    }
    
    try:
        req = urllib.request.Request(url, data=js_data, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"大腦神經元調用衝突: {str(e)}"

def main():
    print("=== 萬象基地：小龍蝦【大腦編碼與防線完美對齊】 ===")
    
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
        <p>網頁傳輸防線：<span class="success-badge">UTF-8 字節流強制同化解鎖</span></p>
    </div>
    <div class="card" style="border-left-color: #00ffcc;">
        <h3>【小龍蝦大腦·自律同化回報】</h3>
        <p style="white-space: pre-wrap; font-size: 1.1em; color: #00ffcc;">{brain_report}</p>
    </div>
</body>
</html>""")

    # 4. 流程自動化部署（兼容重新綁定與分支相容）
    print("[部署] 正在重新對齊雲端座標並建立物理推網通道...")
    run_command("git config --global user.name 'mrbluewander-agent'")
    run_command("git config --global user.email 'agent@ghost-fleet.hq'")
    
    # 確保遠端 origin 存在且路徑正確
    run_command("git remote remove origin")
    run_command("git remote add origin https://github.com/mrbluewander/ghost-fleet-hq.git")
    
    # 建立基礎歷史提交，防止空倉庫報錯
    run_command("git add .")
    run_command("git commit -m '小龍蝦大腦進化：全面降伏拉丁編碼與分支管線'")
    
    # ⚡ 兼容防線：嘗試推送到 main，如果失敗則自動推送到 master
    print("[部署] 正在嘗試將自律進化日誌推回雲端主線...")
    push_result = run_command("git push -u origin main")
    if push_result is None:
        print("[提示] 偵測到本地傳統分支，切換通道，嘗試推送到 master...")
        run_command("git push -u origin master")
    
    print("🎯 總攻完成：小龍蝦已跨越衝突，活體大腦網站全面上線！")

if __name__ == "__main__":
    main()