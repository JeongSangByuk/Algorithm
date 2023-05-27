import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int bag[][] = new int[n + 1][2];
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(bf.readLine());
            bag[i][0] = Integer.parseInt(st.nextToken());
            bag[i][1] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.deepToString(bag));

        int[][] dp = new int[n + 1][k + 1];

        //  1  2  3  4  5  6  7
        //  0  0  0  0  0 13 13
        //  0  0  0  8  8 13 13
        //  0  0  6  8  8 13 14
        //  0  0  6  8 12 13 14

        for (int i = 1; i < n + 1; i++) {

            for (int j = 1; j < k + 1; j++) {

                int w = bag[i][0];
                int v = bag[i][1];

                if (w <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j - w] + v, dp[i - 1][j]);
                } else{
                    dp[i][j] = dp[i - 1][j];
                }

            }
        }

//        System.out.println(Arrays.deepToString(dp));
        System.out.println(dp[n][k]);


    }


}
