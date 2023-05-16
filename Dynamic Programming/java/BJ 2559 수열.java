import java.util.*;
import java.io.*;

public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int[] g = new int[n];
        for (int i = 0; i < n; i++) {
            g[i] = Integer.parseInt(st.nextToken());
        }

        int max = Arrays.stream(g, 0, k).sum();
        int tmp = max;

        for (int i = k; i < n; i++) {
            tmp += (g[i] - g[i - k]);
            max = Math.max(max, tmp);
        }

        System.out.println(max);
    }
}



