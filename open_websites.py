import webbrowser
import time
import json
import logging
from pathlib import Path

# 설정 파일 경로
CONFIG_FILE = Path("websites_config.json")
LOG_FILE = "websites_log.txt"

# 로깅 설정
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# 기본 설정
DEFAULT_CONFIG = {
    "websites": [],
    "delay": 2,
    "browser": "default"
}

# 설정 불러오기
def load_config():
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            logging.error(f"설정 파일 읽기 오류: {e}")
            return DEFAULT_CONFIG
    else:
        # 설정 파일이 없을 경우 기본 설정 파일 생성
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

# 설정 저장
def save_config(config):
    try:
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        logging.info("설정 파일 저장됨")
    except IOError as e:
        logging.error(f"설정 파일 저장 실패: {e}")

# 웹사이트 열기
def open_websites():
    websites = config.get("websites", [])
    delay = config.get("delay", 0)
    browser = config.get("browser", "default")

    for website in websites:
        try:
            if browser == "default":
                webbrowser.open(website, new=2)
            else:
                webbrowser.get(browser).open(website, new=2)
            logging.info(f"웹사이트 열림: {website}")
        except Exception as e:
            logging.error(f"웹사이트 열기 실패: {website} - {e}")

        time.sleep(delay)

    print("모든 웹사이트가 성공적으로 열렸습니다!")

# 웹사이트 추가
def add_website(website):
    if website and website not in config["websites"]:
        config["websites"].append(website)
        save_config(config)

# 웹사이트 제거
def remove_website(website):
    if website in config["websites"]:
        config["websites"].remove(website)
        save_config(config)

# 지연 시간 업데이트
def update_delay(delay):
    config["delay"] = delay
    save_config(config)

# 브라우저 업데이트
def update_browser(browser):
    config["browser"] = browser
    save_config(config)

if __name__ == "__main__":
    # 설정 초기화
    config = load_config()

    # 설정에 따라 웹사이트 열기
    open_websites()

    # 예제 사용법 (설정 변경을 위해 주석 해제)
    # add_website("https://example.com")
    # remove_website("https://example.com")
    # update_delay(5)
    # update_browser("chrome")
