import java.util.*;
import java.io.*;


public class Main {

    static int n, m;
    static HashMap<Integer, List<Node>> g;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(bf.readLine());
        m = Integer.parseInt(bf.readLine());

        g = new HashMap<>();

        for (int i = 0; i < n; i++) {
            g.put(i + 1, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {

            st = new StringTokenizer(bf.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            g.get(a).add(new Node(b, w));
        }

        st = new StringTokenizer(bf.readLine());

        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        bfs(start,end);
    }

    public static void bfs(int start, int end) {
        PriorityQueue<Node> que = new PriorityQueue<>();

        int[] visit = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            visit[i] = Integer.MAX_VALUE;
        }
        visit[start] = 0;

        que.add(new Node(start, 0));

        while (!que.isEmpty()) {

            Node node = que.poll();

            if (visit[node.to] < node.w) {
                continue;
            }

            for (int i = 0; i < g.get(node.to).size(); i++) {

                Node newNode = g.get(node.to).get(i);

                if (visit[newNode.to] > newNode.w + node.w) {
                    visit[newNode.to] = newNode.w + node.w;
                    que.add(new Node(newNode.to, newNode.w + node.w));
                }
            }
        }

        System.out.println(visit[end]);
    }
}

class Node implements Comparable<Node>{

    int to;
    int w;

    public Node(int to, int w) {
        this.to = to;
        this.w = w;
    }

    @Override
    public String toString() {
        return "(" + to + "," + w + ")";
    }

    @Override
    public int compareTo(Node o) {
        return this.w - o.w;
    }
}

