# 🤗 Problem Solving With Python 🤗
> 알고리즘 문제를 풀어보자!! 차근차근!!<br/>
> 언젠가 코테를 뿌실 때 까지!!

<br/>

### 📚 PS CATEGORY
- DFS/BFS
- Greedy
- Dynamic Programming
- Brute Force
- Binary Search
- Data Structure
- Sorting

</br>

### 📚 PS SITE
- <a href="https://www.acmicpc.net/user/jsb100800"/>Baekjoon</a>
- Programmers

</br>

### 📚 PS GOALS
- '백준 알고리즘 분류' 위의 7개 카테고리 1페이지 상위 20문제 다뿌시기ㅎㅎ.
- ~~프로그래머스 고득점 kit 뿌시기. **[2022-02-15 달성]**~~

</br>

### 📚 PS MEMO
> 공부하다가 까먹지 말고, 다시 한번 생각해 볼 만한 점들을 메모합니다!

<br/>

<details>
<summary>메모리 사용량 : 사전 > 리스트</summary>
  
</br>

```
✔️ 메모리 초과 날 경우, 사전으로 구현한 그래프를 리스트로 바꿔보기.(visit 사전 등)
✔️ 백준 1967 트리의 지름 문제
```

</details>

<details>
<summary>deque를 사용할 때 메모리가 초과가 날 경우</summary>
  
</br>

```
✔️ deque에는 중복된 값들이 들어갈 수도 있기 때문에, 같은 동작을 반복할 우려가 있다!
✔️ 이 경우 set을 이용해서 반복된 로직을 없앨 수 있다.
✔️ 집합에서 pop은 임의의 수를 꺼낸다 -> 어차피 bfs 돌리면 큐 안에 있는 모든 지점에서 돌아가기 때문에 상관이 없어짐.
✔️ 백준 1987 알파벳 문제
```

</details>

<details>
<summary>파이썬 string에 index로 접근할때</summary>

</br>
  
``` python
✔️ 아래 코드처럼 string 그대로 접근하는 것이 아닌, list화 해서 인덱스로 접근하는것이 시간 측면에서 빠르다.
✔️ 백준 1987 알파벳 문제
```
  
``` python
  str = "abcd"
  str_lst = list(str)

  print(str[1])
  print(str_list[1])
```

</details>

<details>
<summary>최단경로를 구할 때, visit 배열</summary>

</br>
  
``` python
✔️ bfs 탐색할 때 visit 배열을 계속 생성하는 것이 아닌, 한개만 생성하고 사용해도 된다.
✔️ 최단 경로이기 때문에! 한번 방문 한 곳에 다시 방문하는 것은 최단 경로가 될 수 없다.
✔️ 최단경로와 도달 가능 경우의 수를 구하는 것의 차이.
```

</details>


