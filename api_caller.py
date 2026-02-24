import asyncio
import aiohttp
import os
import time

# 从环境变量读取配置
API_URL = os.getenv("API_URL", "https://generativelanguage.googleapis.com/v1beta/models")
API_KEY = os.getenv("API_KEY", "YOUR_API_KEY_HERE")
MODEL = os.getenv("MODEL", "gemini-1.5-flash")

# URL 去掉了 ?key=... 的拼接
FULL_URL = f"{API_URL}/v1beta/models/{MODEL}:generateContent"

async def fetch(session, index):
    payload = {
        "contents": [{"parts": [{"text": "一只猫"}]}]
    }
    
    # 核心改动：把 API Key 放进请求头里
    # 如果你用的是兼容 OpenAI 格式的代理网关，这里可能需要改成 "Authorization": f"Bearer {API_KEY}"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }
    
    print(f"[{time.strftime('%H:%M:%S')}] 🚀 正在发起第 {index} 次调用...")
    try:
        async with session.post(FULL_URL, json=payload, headers=headers) as response:
            print(f"[{time.strftime('%H:%M:%S')}] ✅ 第 {index} 次调用结束，状态码: {response.status}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ 第 {index} 次调用失败: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 11):
            task = asyncio.create_task(fetch(session, i))
            tasks.append(task)
            
            if i < 10:
                await asyncio.sleep(2)
        
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
