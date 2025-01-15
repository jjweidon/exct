import java.io.*;
import java.util.*;

public class Main {
    private static int[][] bat;
    private static int N, M;
    private static boolean[][] visited;
    private static int[] dy = new int[]{ 0, 0, 1, -1 };
    private static int[] dx = new int[]{ 1, -1, 0, 0 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            bat = new int[N][M];
            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                bat[y][x] = 1;
            }

            visited = new boolean[N][M];
            int cnt = 0;
            for (int y = 0; y < N; y++) {
                for (int x = 0; x < M; x++) {
                    if (bat[y][x] == 1 && !visited[y][x]) {
                        cnt += bfs(y, x);
                    }
                }
            }
            bw.write(cnt + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }

    private static int bfs(int y, int x) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{ y, x });
        
        while (!q.isEmpty()) {
            int[] point = q.poll();
            int ey = point[0];
            int ex = point[1];
            for (int k = 0; k < 4; k++) {
                int ny = ey + dy[k];
                int nx = ex + dx[k];
                if (ny < 0 || ny >= N || nx < 0 || nx >= M || visited[ny][nx]) {
                    continue;
                }
                if (bat[ny][nx] == 1) {
                    q.add(new int[]{ ny, nx });
                    visited[ny][nx] = true;
                }
            }
        }

        return 1;
    }
}