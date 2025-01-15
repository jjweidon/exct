import java.io.*;
import java.util.*;

public class Main {
    private static StringBuilder sb = new StringBuilder();
    private static int[][] graph;
    private static boolean[] visited;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        graph = new int[N+1][N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = graph[b][a] = 1;
        }

        visited = new boolean[N+1];
        dfs(V);
        sb.append("\n");
        visited = new boolean[N+1];
        bfs(V);
        sb.append("\n");
        bw.write(sb.toString());

        bw.flush();
        br.close();
        bw.close();
    }

    private static void dfs(int node) {
        sb.append(node + " ");
        visited[node] = true;
        for (int next = 1; next <= N; next++) {
            if (graph[node][next] == 1 && !visited[next]) {
                dfs(next);
            }
        }
    }

    private static void bfs(int node) {
        Queue<Integer> q = new LinkedList<>();
        q.add(node);
        visited[node] = true;

        while(!q.isEmpty()) {
            int cur = q.poll();
            sb.append(cur + " ");
            for (int next = 1; next <= N; next++) {
                if (graph[cur][next] == 1 && !visited[next]) {
                    q.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}