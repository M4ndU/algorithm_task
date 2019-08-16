정주행
============= 
 
 시간이 흘러 지구는 2100년이 되었고, 웹툰 소리의 마음은 10만회 이상을 연재하며 세계 기록을 매 번 갱신하고 있다. 대부분의 사람들에게 소리의 마음은 삶의 일부가 되었으며, 어린 학생들이 소리의 마음을 회차 순서에 맞게 쭉 정주행을 하는 모습을 쉽게 찾아 볼 수 있다.

 하지만 조금 특이한 성격을 가진 승철이는 여태까지 소리의 마음을 순서에 구애받지 않고 읽어왔다. 그러던 어느날 승철이는 여태까지 자신이 본 에피소드의 번호들을 정렬하면 연속적인 수열로 표현될 수 있는지 궁금해졌다. 승철이는 소리의 마음을 다음과 같은 규칙을 지키며 읽었음이 보장된다.

- 승철이는 총 N화의 에피소드를 보았다.

- 승철이는 기억력이 좋기 때문에 똑같은 에피소드를 두번 보지는 않았다.

 승철이가 여태까지 읽은 에피소드들의 번호가 차례로 주어질 때, 승철이가 본 에피소드들의 번호를 정렬하면 연속된 수열로 표현될 수 있는지 판별하는 프로그램을 작성하시오.

 - 연속적인 수열이란 항상 i번째 숫자의 값이 (i+1)번째 숫자보다 1이 작은 정수로 이루어진 수열을 의미한다.

- - -

###입력 형식

 첫 줄에는 여태까지 승철이가 본 에피소드의 수 N이 주어진다. N은 1과 10만 사이의 자연수이다.

두 번째 줄에는 승철이가 본 에피소드의 번호들이 공백으로 구분되어 주어진다. 에피소드의 번호는 모두 서로 다르며 1과 100만 사이의 자연수이다.

- - -

###출력 형식

 승철이가 본 에피소드의 번호들이 연속적인 수열로 표현될 수 있다면 YES를 출력하고, 그렇지 않다면 NO를 출력한다.

- - -

###문제 출처

구름EDU - 알고리즘 문제해결기법 입문

- - -

###입/출력 예시

⋇ 입출력 형식을 잘 지켜주세요.

␣ : 공백↵ : 줄바꿈

입력 1
<pre><code>5↵
1␣2␣5␣3␣4
</code></pre>

출력 1
<pre><code>YES
</code></pre>

입력 2
<pre><code>5↵
1␣2␣6␣3␣4
</code></pre>

출력 2
<pre><code>NO
</code></pre>