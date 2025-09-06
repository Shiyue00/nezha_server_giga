# alwaysdata_login.py
import os
import sys
from playwright.sync_api import sync_playwright

# --- 修改点: 更新了读取的环境变量名称 ---
USERNAME = os.environ.get("ALWAYSADATA_USERNAME")
PASSWORD = os.environ.get("ALWAYSADATA_PASSWORD")
# -----------------------------------------

LOGIN_URL = "https://admin.alwaysdata.com/login/?next=/"

def run_login():
    """使用 Playwright 执行在 alwaysdata.com 上的登录流程"""
    # --- 修改点: 更新了错误提示信息 ---
    if not USERNAME or not PASSWORD:
        print("错误：必须在 GitHub Secrets 中设置 ALWAYSADATA_USERNAME 和 ALWAYSADATA_PASSWORD。")
        sys.exit(1)
    # ------------------------------------

    with sync_playwright() as p:
        browser = None
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            print(f"正在访问登录页面: {LOGIN_URL}")
            page.goto(LOGIN_URL)

            print("正在填写用户名...")
            page.locator("#id_login").fill(USERNAME)
            
            print("正在填写密码...")
            page.locator("#id_password").fill(PASSWORD)
            
            print("正在点击登录按钮...")
            page.get_by_role("button", name="Se connecter").click()

            print("等待页面跳转以验证登录...")
            page.wait_for_url("**/admin.alwaysdata.com/**", timeout=15000)
            
            print("登录成功！当前页面 URL:", page.url)

        except Exception as e:
            print(f"自动化登录过程中发生错误: {e}")
            sys.exit(1)
        finally:
            if browser:
                browser.close()

if __name__ == "__main__":
    run_login()
