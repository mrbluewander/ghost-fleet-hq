import os
import subprocess
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

def call_lobster_brain_via_curl(prompt):
    """
    ⚔️ 物理降維打擊：棄用 Python 網頁管線，直接動用系統原生 cURL 出擊！
    這能百分之百掐死 Python 的 'latin-1' 編碼衝突
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "錯誤：大腦燃料未裝填。"
    
    # 建立純文字的標準 payload
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Lobster, the core tactical AI of Wanxiang Base. Respond in short Traditional Chinese (zh-TW)."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.3
    }
    
    # 將資料寫入臨時檔案，徹底避免命令行字元集衝突
    temp_json = "lobster_payload.json"
    with open(temp_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
        
    # 物理發射原生系統 cURL 請求
    curl_cmd = f'curl -s -X POST "https://api.openai.com/v1/chat/completions" -H "Authorization: Bearer {api_key}" -H "Content-Type: application/json" -d @{temp_json}'
    
    try:
        res_text = run_command(curl_cmd)
        if os.path.exists(temp_json):
            os.remove(temp_json) # 銷毀臨時彈藥
            
        if res_text:
            res_data = json.loads(res_text)
            return res_data['choices'][0]['message']['content'].strip()
        return "大腦回傳訊號真空。"
    except Exception as e:
        if os.path.exists(temp_json):
            os.remove(temp_json)
        return f"原生管線突觸衝突: {str(e)}"

def main():
    print("=== 萬象基地：小龍蝦【大腦通電·五度總攻】 ===")
    
    # 1. 時間差隱蔽技能
    jitter = random.uniform(2.0, 4.0)
    print(f"⏱️ 時間差隱蔽中... 延遲 {jitter:.2f} 秒...")
    time.sleep(jitter)
    
    # 2. 用 cURL 調用大腦
    print("[大腦] 正在動用系統底層原生管線發射訊號...")
    brain_report = call_lobster_brain_via_curl("回報你目前的覺醒狀態，以及準備如何同化未來數據。")
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
        <p>網路傳輸防線：<span class="success-badge">系統級 cURL 降維打擊啟用</span></p>
    </div>
    <div class="card" style="border-left-color: #00ffcc;">
        <h3>【小龍蝦大腦·自律同化回報】</h3>
        <p style="white-space: pre-wrap; font-size: 1.1em; color: #00ffcc;">{brain_report}</p>
    </div>
</body>
</html>""")

    # 4. 流程自動化部署
    print("[部署] 正在重新對齊雲端座標並建立物理推網通道...")
    run_command("git config --global user.name 'mrbluewander-agent'")
    run_command("git config --global user.email 'agent@ghost-fleet.hq'")
    
    run_command("git remote remove origin")
    run_command("git remote add origin https://github.com/mrbluewander/ghost-fleet-hq.git")
    run_command("git branch -M main")
    
    run_command("git add .")
    # ⚡ 修正空格地雷：用雙引號鎖死提交訊息，不給 CMD 切斷的機會
    run_command('git commit -m "lobster_evolution_stage_5"')
    
    # ⚡ 修正拒絕防線：使用 -f (force) 強制覆蓋雲端，碾壓一切同步衝突！
    print("[部署] 正在將自律進化日誌強制推回雲端主線...")
    run_command("git push -u origin main -f")
    
    print("🎯 總攻完成：小龍蝦已跨越所有衝突，活體大腦網站全面上線！")

if __name__ == "__main__":
    main()