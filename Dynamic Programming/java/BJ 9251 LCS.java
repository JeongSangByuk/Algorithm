import java.util.*;
import java.io.*;

public class Main {

    // https://st-lab.tistory.com/285

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        char[] a = bf.readLine().toCharArray();
        char[] b = bf.readLine().toCharArray();

        int[] dp = new int[b.length];

        for (int i = 0; i < a.length; i++) {

            int cnt = 0;

            for (int j = 0; j < b.length; j++) {

                if (cnt < dp[j]) {
                    cnt = dp[j];
                } else if (a[i] == b[j]) {
                    dp[j] = cnt + 1;
                }

            }
        }

        int result = Arrays.stream(dp).max().getAsInt();

        System.out.println(result);

    }


}
