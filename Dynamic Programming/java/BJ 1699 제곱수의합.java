import java.security.KeyStore.TrustedCertificateEntry;
import java.util.*;
import java.io.*;

public class Main {

    // https://maivve.tistory.com/199

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(bf.readLine());

        int[] dp = new int[n + 1];

        int t = 1;

        for (int i = 0; i < dp.length; i++) {
            dp[i] = i;
        }

        while (t * t <= n) {
            dp[t * t] = 1;
            t += 1;
        }

        for (int i = 1; i < n + 1; i++) {

            for (int j = 1; j * j < i + 1; j++) {
                // 최소가 되려면 무조건 제곱수를 하나 포함해야한다. -> 약간 그리디스럽다.
                dp[i] = Math.min(dp[i], dp[i - (j * j)] + 1);
            }
        }

        System.out.println(dp[n]);
//        System.out.println(Arrays.toString(dp));
    }


}
