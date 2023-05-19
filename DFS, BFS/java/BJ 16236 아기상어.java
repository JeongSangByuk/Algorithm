import java.util.*;
import java.io.*;


public class Main {


    static PriorityQueue<Node> heap;
    static Queue<Node> que;
    static boolean[][] visit;

    static int n;
    static int fishCnt = 0;
    static int sharkSize = 2;
    static int result = 0;

    static int[][] g;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        heap = new PriorityQueue<>();
        que = new LinkedList<>();

        n = Integer.parseInt(bf.readLine());
        g = new int[n][n];
        visit = new boolean[n][n];

        for (int i = 0; i < n; i++) {

            st = new StringTokenizer(bf.readLine());

            for (int j = 0; j < n; j++) {

                g[i][j] = Integer.parseInt(st.nextToken());

                if (g[i][j] == 9) {
                    que.add(new Node(i, j, 0, 2));
                    visit[i][j] = true;
                    g[i][j] = 0;
                }
            }
        }

        bfs();

        System.out.println(result);
    }

    public static void bfs() {

        while (true) {
            while (!que.isEmpty()) {
//                System.out.println(Arrays.toString(que.toArray()));

                Node node = que.poll();

                for (int i = 0; i < 4; i++) {

                    int ny = node.y + dy[i];
                    int nx = node.x + dx[i];

                    if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
                        continue;
                    }

                    if (visit[ny][nx] || node.size < g[ny][nx]) {
                        continue;
                    }

                    if (g[ny][nx] != 0 && node.size > g[ny][nx]) {
                        heap.add(new Node(ny, nx, node.time + 1, node.size));
                    } else {
                        que.add(new Node(ny, nx, node.time + 1, node.size));
                    }

                    visit[ny][nx] = true;
                }
            }

            if (heap.isEmpty()) {
                break;
            }

            Node node = heap.poll();
            heap.clear();
            g[node.y][node.x] = 0;
            fishCnt += 1;

            if (fishCnt == sharkSize) {
                sharkSize += 1;
                fishCnt = 0;
            }

            result += node.time;
            visit = new boolean[n][n];
            visit[node.y][node.x] = true;
            que.add(new Node(node.y, node.x, 0, sharkSize));
        }
    }
}

class Node implements Comparable<Node> {

    int y, x, time, size;

    public Node(int y, int x, int time, int size) {
        this.y = y;
        this.x = x;
        this.time = time;
        this.size = size;
    }

    @Override
    public int compareTo(Node o) {

        if (o.time != this.time) {
            return this.time - o.time;
        }

        if (o.y == this.y) {
            return this.x - o.x;
        }

        return this.y - o.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(y, x);
    }

    @Override
    public boolean equals(Object ob) {

        if (this == ob) {
            return true;
        }

        if (!(ob instanceof Node)) {
            return false;
        }

        Node node = (Node) ob;

        return node.y == y && node.x == x;
    }

    @Override
    public String toString() {
        return "["+this.y + "," + this.x + "," + this.time +"]";
    }
}


