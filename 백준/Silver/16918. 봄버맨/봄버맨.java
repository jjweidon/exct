import java.io.*;
import java.util.*;

public class Main {
    private static int R, C, N;
    private static int[][] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        grid = new int[R][C];
        
        for (int j = 0; j < R; j++) {
            String s = br.readLine();
            for (int i = 0; i < C; i++) {
                if (s.charAt(i) == 'O') {
                    grid[j][i] = 2;
                } else {
                    grid[j][i] = 0;
                }
            }
        }

        for (int n = 1; n < N; n++) {
            decreaseTimer();
            if (n % 2 == 1) {
                makeBomb();
            } else {
                boooooom();
            }
        }
        drawGrid();

        br.close(); 
        bw.close();
    }

    public static void drawGrid() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int j = 0; j < R; j++) {
            for (int i = 0; i < C; i++) {
                if (grid[j][i] > 0) {
                    bw.write("O");
                } else {
                    bw.write(".");
                }
            }
            bw.write("\n");
        }
        bw.flush();
    }

    public static void decreaseTimer() {
        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                grid[y][x]--;
            }
        }
    }

    public static void makeBomb() {
        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                if (grid[y][x] <= 0) {
                    grid[y][x] = 3;
                }
            }
        }
    }

    public static void boooooom() {
        int[] dy = { 0, 0, 1, -1 };
        int[] dx = { 1, -1, 0, 0 };
        List<int[]> coordinates = new ArrayList<>();

        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                if (grid[y][x] <= 0) {
                    coordinates.add(new int[]{ y, x });
                }
            }
        }

        for (int[] coordinate : coordinates) {
            for (int k = 0; k < 4; k++) {
                int ny = coordinate[0] + dy[k];
                int nx = coordinate[1] + dx[k];
                if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;
                grid[ny][nx] = 0;
            }
        }
    }
}