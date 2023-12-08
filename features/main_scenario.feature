Feature: MainPage

# feature 초기화 작업
Background: 초기화
    Given Chrome Browser로 NAVER URL에 접속한다.
    And 테스트 수행에 필요한 초기화를 한다.
    And 창을 최대화한다.

Scenario: 메인 페이지 접속 확인하기
    Then 네이버 검색 필드가 표시된다.

Scenario: 프로필 영역 확인하기
    Then 프로필 영역이 표시된다.

Scenario: 로그인 영역 UI 확인하기
    Then 로그인 안내 문구가 표시된다.
    Then 로그인 버튼이 표시된다.
    Then "아이디 찾기" 링크 텍스트가 표시된다.
    Then "비밀번호 찾기" 링크 텍스트가 표시된다.
    Then "회원가입" 링크 텍스트가 표시된다.

Scenario: 로그인 페이지 이동하기
    When 로그인 버튼을 클릭한다.
    Then 로그인 페이지로 이동한다.

Scenario: 네이버 카페 페이지로 이동하기
    When 네이버 카페 메뉴를 클릭한다.
    Then 네이버 카페 페이지로 이동한다.

Scenario: 네이버 블로그 페이지로 이동하기
    When 네이버 블로그 메뉴를 클릭한다.
    Then 네이버 블로그 페이지로 이동한다.

Scenario: 네이버 쇼핑 페이지로 이동하기
    When 네이버 쇼핑 메뉴를 클릭한다.
    Then 네이버 쇼핑 페이지로 이동한다.

Scenario: 네이버 뉴스 페이지로 이동하기
    When 네이버 뉴스 메뉴를 클릭한다.
    Then 네이버 뉴스 페이지로 이동한다.

Scenario: 네이버 증권 페이지로 이동하기
    When 네이버 증권 메뉴를 클릭한다.
    Then 네이버 증권 페이지로 이동한다.

Scenario: 네이버 부동산 페이지로 이동하기
    When 네이버 부동산 메뉴를 클릭한다.
    Then 네이버 부동산 페이지로 이동한다.

Scenario: 네이버 지도 페이지로 이동하기
    When 네이버 지도 메뉴를 클릭한다.
    Then 네이버 지도 페이지로 이동한다.

Scenario: 네이버 웹툰 페이지로 이동하기
    When 네이버 웹툰 메뉴를 클릭한다.
    Then 네이버 웹툰 페이지로 이동한다.

Scenario: GNB 메뉴 - 바로가기 확인하기
    Then GNB 메뉴 영역에 "바로가기" 아이콘이 표시된다.

Scenario: GNB 메뉴 - 네이버페이 확인하기
    Then GNB 메뉴 영역에 "네이버페이" 아이콘이 표시된다.

Scenario: GNB 메뉴 - 네이버톡 확인하기
    Then GNB 메뉴 영역에 "네이버톡" 아이콘이 표시된다.

Scenario: GNB 메뉴 - 알림/혜택 확인하기
    Then GNB 메뉴 영역에 "알림/혜택" 아이콘이 표시된다.
    