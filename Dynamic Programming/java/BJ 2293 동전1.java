import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int g[] = new int[n + 1];
        g[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            g[i] = Integer.parseInt(bf.readLine());
        }

        int[] dp = new int[k + 1];
        dp[0] = 1;

        for (int i = 1; i < n + 1; i++) {

            for (int j = g[i]; j < k + 1; j++) {
                dp[j] += dp[j - g[i]];
            }
        }

        System.out.println(dp[k]);


    }

}
