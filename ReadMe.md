# 웹사이트 열기 프로젝트

이 프로젝트는 지정된 웹사이트 목록을 일정 시간 간격을 두고 지정된 브라우저로 여는 간단한 스크립트를 제공합니다. 설정은 JSON 파일을 통해 관리됩니다.

## 목차

- [기능](#기능)
- [설치](#설치)
- [설정](#설정)
- [사용법](#사용법)
- [기여](#기여)
- [라이선스](#라이선스)

## 기능

- 여러 웹사이트를 순차적으로 일정 시간 간격을 두고 엽니다.
- JSON 파일을 통해 웹사이트, 지연 시간 및 선호 브라우저를 설정할 수 있습니다.
- 디버깅 및 모니터링을 위한 활동 로그 파일 생성.

## 설치

1. 저장소를 클론합니다:
    ```sh
    git clone https://github.com/<YOUR_GITHUB_USERNAME>/<REPOSITORY_NAME>.git
    cd <REPOSITORY_NAME>
    ```

2. 시스템에 Python이 설치되어 있는지 확인합니다. 이 프로젝트는 Python 3.x가 필요합니다.

3. (선택 사항) 가상 환경을 만들고 활성화합니다:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Windows에서는 `venv\Scripts\activate` 사용
    ```

4. 필요한 경우, 필요한 의존성을 설치합니다 (이 기본 스크립트에는 특별한 의존성이 없습니다).

## 설정

1. `websites_config.json` 설정 파일은 열고자 하는 웹사이트 목록, 각 웹사이트를 여는 시간 간격 및 사용할 브라우저를 지정하는 데 사용됩니다.
   
2. 예시 `websites_config.json`:
    ```json
    {
        "websites": ["https://www.example.com"],
        "delay": 2,
        "browser": "default"
    }
    ```

3. 원하는 설정으로 설정 파일을 업데이트합니다.

## 사용법

1. 설정 파일 `websites_config.json`이 `open_websites.py`와 동일한 디렉토리에 있는지 확인합니다.

2. 스크립트를 실행합니다:
    ```sh
    python open_websites.py
    ```

3. 스크립트가 설정 파일을 읽고 지정된 브라우저에서 각 웹사이트를 지정된 시간 간격으로 엽니다.

## 기여

1. 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature-branch`).
3. 변경 사항을 커밋합니다 (`git commit -am 'Add new feature'`).
4. 브랜치에 푸시합니다 (`git push origin feature-branch`).
5. 새로운 풀 리퀘스트를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 `LICENSE` 파일을 참조하십시오.
