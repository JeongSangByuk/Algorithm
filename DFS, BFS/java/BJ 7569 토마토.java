import java.util.*;
import java.io.*;

public class Main {

    static int[][][] g;
    static boolean visit[][][];
    static int[] dy = {-1, 1, 0, 0, 0, 0};
    static int[] dx = {0, 0, -1, 1, 0, 0};
    static int[] dz = {0, 0, 0, 0, -1, 1};
    static int n, m, z;
    static int ans = 0;
    static Queue<Node> que;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        z = Integer.parseInt(st.nextToken());

        g = new int[z][n][m];
        visit = new boolean[z][n][m];
        que = new LinkedList<>();

        for (int i = 0; i < z; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(bf.readLine());
                for (int k = 0; k < m; k++) {
                    g[i][j][k] = Integer.parseInt(st.nextToken());

                    if (g[i][j][k] == 1) {
                        que.add(new Node(i, j, k, 0));
                        visit[i][j][k] = true;
                    }
                }
            }
        }

        bfs();

        for (int i = 0; i < z; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {

                    if (g[i][j][k] == 0) {
                        ans = -1;
                        break;
                    }

                }
            }
        }

        System.out.println(ans);
    }

    public static void bfs() {

        while (!que.isEmpty()) {

            Node node = que.remove();
            ans = Math.max(ans, node.cnt);

            for (int i = 0; i < 6; i++) {

                int nz = node.z + dz[i];
                int ny = node.y + dy[i];
                int nx = node.x + dx[i];
                int cnt = node.cnt;

                if (nz < 0 || nz >= z || ny < 0 || ny >= n || nx < 0 || nx >= m) {
                    continue;
                }

                if (g[nz][ny][nx] != 0 || visit[nz][ny][nx] == true) {
                    continue;
                }

                que.add(new Node(nz, ny, nx, cnt + 1));
                g[nz][ny][nx] = 1;
                visit[nz][ny][nx] = true;
            }
        }

    }
}

class Node {
    int z, y, x, cnt;

    public Node(int z, int y, int x, int cnt) {
        this.z = z;
        this.y = y;
        this.x = x;
        this.cnt = cnt;
    }

    @Override
    public String toString() {
        return "(" + z + " " + y + " " + x + ")";
    }
}

