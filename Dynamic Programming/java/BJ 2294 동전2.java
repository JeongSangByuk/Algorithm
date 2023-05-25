import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int g[] = new int[n];
        for (int i = 0; i < n; i++) {
            g[i] = Integer.parseInt(bf.readLine());
        }

        int[] dp = new int[k + 1];

        for (int i = 0; i < k + 1; i++) {
            dp[i] = -1;
        }

        for (int i : g) {

            if (i > k) {
                continue;
            }
            dp[i] = 1;
        }

        for (int i = 1; i < k + 1; i++) {

            if (dp[i] == 1) {
                continue;
            }

            ArrayList<Integer> t = new ArrayList<>();

            for (int j = 0; j < g.length; j++) {

                if (i - g[j] <= 0 || g[j] > k || dp[i - g[j]] == -1) {
                    continue;
                }

                t.add(dp[i - g[j]]);
            }

            if (t.size() == 0) {
                continue;
            }

            dp[i] = Collections.min(t) + 1;
        }


        System.out.println(dp[k]);


    }

}
