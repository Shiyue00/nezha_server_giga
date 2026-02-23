import asyncio
import aiohttp
import os
import time

# 留好位置：优先从环境变量读取（为了安全），如果没有则使用后方的默认字符串
API_URL = os.getenv("API_URL", "https://generativelanguage.googleapis.com/v1beta/models")
API_KEY = os.getenv("API_KEY", "YOUR_API_KEY_HERE")
MODEL = os.getenv("MODEL", "gemini-1.5-flash")

# 拼接完整的 Gemini 请求 URL
# 如果你使用的是第三方代理，URL 格式不同，请直接把代理的全路径写在这里
FULL_URL = f"{API_URL}/{MODEL}:generateContent?key={API_KEY}"

async def fetch(session, index):
    # Gemini 标准的请求体，提示词为“你好”
    payload = {
        "contents": [{"parts": [{"text": "你好"}]}]
    }
    headers = {"Content-Type": "application/json"}
    
    print(f"[{time.strftime('%H:%M:%S')}] 🚀 正在发起第 {index} 次调用...")
    try:
        # 发起 POST 请求，不处理回复的具体内容，只获取状态码
        async with session.post(FULL_URL, json=payload, headers=headers) as response:
            print(f"[{time.strftime('%H:%M:%S')}] ✅ 第 {index} 次调用结束，状态码: {response.status}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ 第 {index} 次调用失败: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 11): # 总共循环 10 次
            # 创建异步任务，立即执行
            task = asyncio.create_task(fetch(session, i))
            tasks.append(task)
            
            # 严格等待 2 秒后再触发下一次循环（最后一次后不需要等）
            if i < 10:
                await asyncio.sleep(2)
        
        # 等待所有发出去的请求都收到响应（或超时）后再彻底结束脚本
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
