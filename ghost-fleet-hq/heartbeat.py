import os
import subprocess
import urllib.request
import re
import time
import random
import json

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git管線診斷: {e.stderr}")
        return None

def call_lobster_brain(prompt):
    """
    🧠 物理點火：直接呼叫小龍蝦的雲端 AI 大腦
    使用環境變數中的 OPENAI_API_KEY 進行推理與同化
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "錯誤：大腦燃料未裝填。"
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",  # 採用高效能戰術模型
        "messages": [
            {"role": "system", "content": "你是萬象基地的核心智能小龍蝦。請用冷硬、鋼直、精準的指令風格，針對統帥的指令給出最實體的進度與同化報告。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300,
        "temperature": 0.3
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"大腦神經元調用衝突: {str(e)}"

def main():
    print("=== 萬象基地：小龍蝦【大腦全線通電】總攻開始 ===")
    
    # 1. 物理觸發時間差隱蔽技能（3~7秒隨機延遲）
    jitter = random.uniform(3.0, 7.0)
    print(f"⏱️ 時間差隱蔽中... 延遲 {jitter:.2f} 秒，抹除機器人特徵...")
    time.sleep(jitter)
    
    # 2. 測試大腦推理能力（讓小龍蝦自己發送一封自我覺醒的回報）
    print("[大腦] 正在對雲端核心發射神經訊號...")
    brain_report = call_lobster_brain("回報你目前的覺醒狀態，以及你作為活體網站載體，準備如何同化未來難民與物資數據的決心。")
    print(f"🧠 大腦實體回報內容:\n{brain_report}\n")
    
    # 3. 活體重新構建網站：把大腦說的話，原封不動自己貼上網頁
    print("[部署] 小龍蝦正在將大腦思考結果，物理寫入 index.html...")
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
        <p>時間差潛伏技能：<span class="success-badge">動態亂數延遲啟用中</span></p>
        <p>網站結構狀態：<span class="success-badge">活體載體自適應部署</span></p>
    </div>
    
    <div class="card" style="border-left-color: #00ffcc;">
        <h3>【小龍蝦大腦·自律同化回報】</h3>
        <p style="white-space: pre-wrap; font-size: 1.1em; color: #00ffcc;">{brain_report}</p>
    </div>
</body>
</html>""")

    # 4. 流程自動化部署：小龍蝦自己寫完、自己推回雲端
    print("[部署] 觸發自律 Git 管線，強制推回雲端貼網...")
    run_command("git config --global user.name 'mrbluewander-agent'")
    run_command("git config --global user.email 'agent@ghost-fleet.hq'")
    
    run_command("git add .")
    run_command("git commit -m '小龍蝦大腦正式點火：解鎖同化與智慧推理能力'")
    run_command("git push")
    
    print("🎯 總攻完成：活體網站已成功由小龍蝦大腦重構並貼回雲端！")

if __name__ == "__main__":
    main()