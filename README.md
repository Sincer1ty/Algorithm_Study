# 스터디원

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/PersonableD">
        <img src="https://github.com/PersonableD.png" width="100px;" alt="PersonableD"/><br />
        <sub><b>PersonableD</b></sub><br/>
        <sub><b>김슬아</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Sincer1ty">
        <img src="https://github.com/Sincer1ty.png" width="100px;" alt="Sincer1ty"/><br />
        <sub><b>Sincer1ty</b></sub><br/>
        <sub><b>김성희</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jsonsvalue">
        <img src="https://github.com/jsonsvalue.png" width="100px;" alt="jsonsvalue"/><br />
        <sub><b>jsonsvalue</b></sub><br/>
        <sub><b>이재석</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lazyArtisan">
        <img src="https://github.com/lazyArtisan.png" width="100px;" alt="lazyArtisan"/><br />
        <sub><b>lazyArtisan</b></sub><br/>
        <sub><b>고태환</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jeongyuje0ngyujeong">
        <img src="https://github.com/jeongyuje0ngyujeong.png" width="100px;" alt="jeongyuje0ngyujeong"/><br />
        <sub><b>jeongyuje0ngyujeong</b></sub><br/>
        <sub><b>정유정</b></sub>
      </a>
    </td>
  </tr>
</table>


<br>

# 진행 방법

```python
import time

N = int(input())
member = [input() for _ in range(N)]
level = ['hasu' for _ in range(N)]
solved = [False]*N
homework = None
all_gosu = False

while not all_gosu:
    print("숙제 풀기")

    if (time.localtime().tm_hour == 13) and (time.localtime().tm_min == 30):
        print("풀이 발표 시간")
        solved = [False]*N
        homework = input("다음 문제는: ")

    if 'hasu' not in level:
        all_gosu = True
```

<br>

# 진행 상황
<details>
  <summary>8월</summary>

<table>
  <tr>
    <th>Date</th>
    <th>Problem</th>
  </tr>
  <tr>
    <td>8.12</td>
    <td><a href="https://www.acmicpc.net/problem/2468">2468 안전영역</a></td>
  </tr>
  <tr>
    <td>8.13</td>
    <td><a href="https://www.acmicpc.net/problem/2504">2504 괄호의 값</a></td>
  </tr>
  <tr>
    <td>8.14</td>
    <td><a href="https://www.acmicpc.net/problem/1655">1655 가운데를 말해요</a></td>
  </tr>
  <tr>
    <td>8.15</td>
    <td><a href="https://www.acmicpc.net/problem/13334">13334 철로</a></td>
  </tr>
  <tr>
    <td>8.16</td>
    <td><a href="https://www.acmicpc.net/problem/17298">17298 오큰수</a></td>
  </tr>
  <tr>
    <td>8.17</td>
    <td>Review session</td>
  </tr>
  <tr>
    <td>8.19</td>
    <td><a href="https://www.acmicpc.net/problem/2805">2805 나무 자르기</a></td>
  </tr>
  <tr>
    <td>8.20</td>
    <td><a href="https://www.acmicpc.net/problem/3190">3190 뱀</a></td>
  </tr>
  <tr>
    <td>8.21</td>
    <td><a href="https://www.acmicpc.net/problem/2110">2110 공유기 설치</a></td>
  </tr>
  <tr>
    <td>8.22</td>
    <td><a href="https://www.acmicpc.net/problem/2812">2812 크게 만들기</a></td>
  </tr>
  <tr>
    <td>8.23</td>
    <td><a href="https://www.acmicpc.net/problem/2869">2869 달팽이는 올라가고 싶다</a></td>
  </tr>
  <tr>
    <td>8.24</td>
    <td>Review session</td>
  </tr>
  <tr>
    <td>8.26</td>
    <td><a href="https://www.acmicpc.net/problem/1707">1707 이분 그래프</a></td>
  </tr>
  <tr>
    <td>8.28</td>
    <td><a href="https://www.acmicpc.net/problem/14888">14888 연산자 끼워넣기</a></td>
  </tr>
  <tr>
    <td>8.30</td>
    <td><a href="https://www.acmicpc.net/problem/3055">3055 탈출</a></td>
    <td></td>
  </tr>
  <tr>
    <td>8.31</td>
    <td>Review session</td>
  </tr> 
</table>
</details>

<details>
  <summary>9월</summary>
<table>
  <tr>
    <th>Date</th>
    <th>Problem</th>
  </tr>
  <tr>
    <td>9.4</td>
    <td><a href="https://www.acmicpc.net/problem/7569">7569 토마토</a></td>
  </tr>
  <tr>
    <td>9.6</td>
    <td><a href="https://www.acmicpc.net/problem/10026">10026 적록색약</a></td>
  </tr>
  <tr>
    <td>9.23<br>추석 특별 숙제<br>(9.13 - 9.22)</td>
    <td><a href="https://www.acmicpc.net/problem/21606">21606 아침 산책</a><br>
      <a href="https://www.acmicpc.net/problem/1948">1948 임계경로</a><br>
      <a href="https://www.acmicpc.net/problem/2637">2637 장난감 조립</a><br>
      <a href="https://www.acmicpc.net/problem/2573">2573 빙산</a><br>
      <a href="https://www.acmicpc.net/problem/2667">2667 단지번호 붙이기</a><br>
      <a href="https://www.acmicpc.net/problem/31575">31575 도시와 비트코인</a><br>
  </tr>
  <tr>
    <td>9.26</td>
    <td><a href="https://www.acmicpc.net/problem/1912">1912 연속합</a></td>
  </tr>
  <tr>
    <td>9.28</td>
    <td><a href="https://www.acmicpc.net/problem/11049">11049 행렬 곱셈 순서</a></td>
  </tr>
  <tr>
    <td>9.30</td>
    <td><a href="https://www.acmicpc.net/problem/1463">1463 1로 만들기</a></td>
  </tr>
</table>
</details>

<details>
  <summary>10월</summary>
<table>
  <tr>
    <th>Date</th>
    <th>Problem</th>
  </tr>
  <tr>
    <td>10.</td>
    <td><a href="https://www.acmicpc.net/problem/7569">7569 토마토</a></td>
  </tr>
</table>
</details>

<br>

# 주제별 분류

<details>
  <summary>정글 compass 1주차 주제</summary>
  <br>
  <ul>
    <li>1. 단순 구현</li>
    <li>2. 재귀함수</li>
    <li>3. 정렬</li>
    <li>4. 완전 탐색, 이분 탐색</li>
    <li>5. 분할 정복</li>
    <li>6. 스택, 큐</li>
    <li>7. 우선순위 큐</li>
  </ul>
</details>

<details>
  <summary>정글 compass 2주차 주제</summary>
  <br>
  <ul>
    <li>1. DFS, BFS</li>
    <li>2. 위상 정렬</li>
    <li>3. 최소 신장 트리</li>
    <li>4. 다익스트라, 플로이드 와샬</li>
    <li>5. Trie</li>
  </ul>
</details>

<details>
  <summary>정글 compass 3주차 주제</summary>
  <br>
  <ul>
    <li>1. 다이나믹 프로그래밍</li>
    <li>2. 그리디 알고리즘</li>
    <li>3. LCS (Longest Common Subsequence)</li>
    <li>4. 배낭 문제 (Knapsack Problem)</li>
  </ul>
</details>

