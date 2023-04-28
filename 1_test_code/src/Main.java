import java.util.*;
import java.io.*;

public class Main {

    static HashMap<Integer, List<Integer>> g;
    static int n, m;

    static HashSet<Integer> visit = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        g = new HashMap<>();

        st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            g.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
            g.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
        }

        for (int i = 0; i < n; i++) {

            visit.add(i);
            dfs(i, 0);
            visit.remove(i);
        }

        System.out.println(0);
    }

    public static void dfs(int now, int cnt) {

        if (cnt == 4) {
            System.out.println(1);
            System.exit(0);
            return;
        }

        for (Integer i : g.getOrDefault(now, new ArrayList<>())) {

            if (visit.contains(i)) {
                continue;
            }

            visit.add(i);
            dfs(i, cnt + 1);
            visit.remove(i);
        }
    }

}


