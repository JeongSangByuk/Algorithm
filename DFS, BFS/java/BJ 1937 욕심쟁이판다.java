import java.util.*;
import java.io.*;

public class Main {

    static int[][] g;
    static int[][] dp;
    static int n;
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());

        g = new int[n][n];
        dp= new int[n][n];

        for (int i = 0; i < n; i++) {

            st = new StringTokenizer(bf.readLine());

            for (int j = 0; j < n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, dfs(new Node(i, j)));
            }
        }

        System.out.println(ans);
    }

    public static int dfs(Node node) {

        if (dp[node.y][node.x] != 0)
            return dp[node.y][node.x];

        dp[node.y][node.x] = 1;

        for (int i = 0; i < 4; i++) {

            int ny = node.y + dy[i];
            int nx = node.x + dx[i];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
                continue;
            }

            if (g[node.y][node.x] >= g[ny][nx]) {
                continue;
            }

            dp[node.y][node.x] = Math.max(dp[node.y][node.x], dfs(new Node(ny, nx)) + 1);
        }

        return dp[node.y][node.x];

    }
}

class Node {
    int y, x;

    public Node(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

