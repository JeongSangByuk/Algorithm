import java.util.*;
import java.io.*;

public class Main {

    // https://st-lab.tistory.com/285

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(bf.readLine());
        int[] g = new int[n];

        st = new StringTokenizer(bf.readLine());

        for (int i = 0; i < n; i++) {
            g[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> dp = new ArrayList<>();
        dp.add(0);

        for (int i = 0; i < g.length; i++) {

            if (dp.get(dp.size() - 1) < g[i]) {
                dp.add(g[i]);
                continue;
            }

            int lo = 0;
            int hi = dp.size();

            while (lo + 1 < hi) {
                int mid = (int) ((lo + hi) / 2);

                if (dp.get(mid) < g[i]) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }

            dp.set(hi, g[i]);

        }

        System.out.println(dp.size() - 1);

    }


}
