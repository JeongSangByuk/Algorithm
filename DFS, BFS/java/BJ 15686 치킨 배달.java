import java.util.*;
import java.io.*;

public class Main {

    static int[][] g;
    static int n, m;

    static List<Node> chicken = new ArrayList();
    static List<Node> home = new ArrayList();
    static HashSet<Integer> visit = new HashSet<>();
    static int chickSize;
    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        g = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());

                if (g[i][j] == 1) {
                    home.add(new Node(i, j));
                } else if (g[i][j] == 2) {
                    chicken.add(new Node(i, j));
                }
            }
        }

        chickSize = chicken.size();

        for (int i = 0; i < chickSize; i++) {

            visit.add(i);
            dfs(i, 1);
            visit.remove(i);
        }

        System.out.println(result);

    }

    public static int calculate() {

        int result = 0;

        for (Node node : home) {

            int min = Integer.MAX_VALUE;

            for (Integer i : visit) {
                int tmp = Math.abs(node.y - chicken.get(i).y) + Math.abs(node.x - chicken.get(i).x);
                min = Math.min(min, tmp);
            }

            result += min;
        }

        return result;
    }

    public static void dfs(int oriIndex, int cnt) {

        if (cnt == m) {

            result = Math.min(result, calculate());
            return;
        }

        for (int i = oriIndex + 1; i < chickSize; i++) {

            visit.add(i);
            dfs(i, cnt + 1);
            visit.remove(i);
        }

    }


}

class Node {

    int y, x;

    public Node(int y, int x) {
        this.y = y;
        this.x = x;
    }

    @Override
    public int hashCode() {
        return Objects.hash(y, x);
    }

    @Override
    public boolean equals(Object obj) {

        if (this == obj)
            return true;

        if (!(obj instanceof Node)) {
            return false;
        }

        Node node = (Node) obj;
        return y == node.y && x == node.x;
    }
}

