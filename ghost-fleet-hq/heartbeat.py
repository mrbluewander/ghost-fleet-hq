import os
import subprocess
import urllib.request
import re

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"執行失敗: {e.stderr}")
        return None

def scout_network():
    print("[2/4] 偵察雙眼啟動：正在前往目標網路實體抓取數據...")
    # 範例測試目標：抓取世界時間與基礎網路節點狀態，確保偵察管線通暢
    try:
        url = "https://worldtimeapi.org/api/timezone/Asia/Taipei"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            # 物理提取時間實體數據
            match = re.search(r'"datetime":"([^"]+)"', html)
            if match:
                return f"實體偵察回報成功！目標當前時間：{match.group(1)}"
            return "偵察成功，但數據格式需要進一步解析。"
    except Exception as e:
        return f"偵察受阻，網路防火牆攔截或目標斷線: {str(e)}"

def main():
    print("=== 小龍蝦雲端核心：第二階段【偵察防線】啟動 ===")
    
    # 1. 自我修復診斷
    print("[1/4] 正在執行系統實體診斷...")
    if not os.path.exists("index.html"):
        with open("index.html", "w", encoding="utf-8") as f:
            f.write("<html><body><h1>萬象基地 - 哨兵在線</h1></body></html>")
    
    # 2. 執行實體數據搜尋任務
    scout_report = scout_network()
    print(f"🎯 偵察兵帶回實體報告: {scout_report}")
    
    # 3. 物理寫入網站檔案
    print("[3/4] 正在將偵察到的資料實體寫入網頁...")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(f"""<html>
<head><meta charset="utf-8"><title>萬象基地指揮部</title></head>
<body>
    <h1>萬象基地 - 小龍蝦自主任務日誌</h1>
    <hr>
    <h3>【最新出任務回報】</h3>
    <p>{scout_report}</p>
    <p>系統狀態：有手有腳，成功自主搜尋並貼回。</p>
</body>
</html>""")

    # 4. 觸發第一步的雲端雙手，強制推回倉庫
    print("[4/4] 啟動自主防禦覆蓋 (Git Push)...")
    run_command("git config --global user.name 'mrbluewander-agent'")
    run_command("git config --global user.email 'agent@ghost-fleet.hq'")
    
    status = run_command("git status --porcelain")
    if status and status.strip():
        run_command("git add .")
        run_command("git commit -m '小龍蝦第二階段：自主搜尋並更新實體網頁'")
        run_command("git push")
        print("🎯 實體結果：小龍蝦已成功出任務、抓到資料、並自動 Push 貼回網站！")
    else:
        print("🎯 實體結果：網頁內容無變更，防線閉鎖安全。")

if __name__ == "__main__":
    main()