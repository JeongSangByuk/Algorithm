import java.util.*;
import java.io.*;

public class Main {

    static int[][] g;
    static boolean visit[][];
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        g = new int[n][m];
        visit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String[] line = bf.readLine().split("");

            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(line[j]);
            }
        }

        System.out.println(bfs());

    }

    private static int bfs() {
        Queue<Node> que = new LinkedList<>();

        que.add(new Node(0, 0, 0));
        visit[0][0] = true;

        while (!que.isEmpty()) {

            Node node = que.remove();

            for (int i = 0; i < 4; i++) {

                int ny = node.y + dy[i];
                int nx = node.x + dx[i];
                int cnt = node.cnt;

                if (ny < 0 || ny >= n || nx < 0 || nx >= m) {
                    continue;
                }

                if (g[ny][nx] == 0 || visit[ny][nx] == true) {
                    continue;
                }

                if (ny == n - 1 && nx == m - 1) {
                    return cnt + 2;
                }

                que.add(new Node(ny, nx, cnt + 1));
                visit[ny][nx] = true;
            }


        }

        return 0;
    }
}

class Node {
    int x;
    int y;
    int cnt;

    public Node(int y, int x, int cnt) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
    }

    @Override
    public String toString() {
        return "(" + y + " " + x + " " + cnt + ")";
    }
}