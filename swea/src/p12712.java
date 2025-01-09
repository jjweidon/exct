import java.io.*;
import java.util.StringTokenizer;

public class p12712 {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(bf.readLine());
        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int max = calculateMax(N, M, arr);
            bw.write("#" + t + " " + max + "\n");
        }
        bw.flush();
        bw.close();
    }

    private static int calculateMax(int N, int M, int[][] arr) {
        int max = 0;

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                int crossSum = calculateCrossSum(N, M, arr, y, x);
                int diagonalSum = calculateDiagonalSum(N, M, arr, y, x);

                max = Math.max(max, Math.max(crossSum, diagonalSum));
            }
        }
        return max;
    }

    private static int calculateCrossSum(int N, int M, int[][] arr, int y, int x) {
        int temp = 0;
        for (int j = y - M + 1; j < y + M; j++) {
            if (j >= 0 && j < N) {
                temp += arr[j][x];
            }
        }
        for (int i = x - M + 1; i < x + M; i++) {
            if (i >= 0 && i < N) {
                temp += arr[y][i];
            }
        }
        temp -= arr[y][x];
        return temp;
    }

    private static int calculateDiagonalSum(int N, int M, int[][] arr, int y, int x) {
        int temp = 0;
        for (int k = -M + 1; k < M; k++) {
            if (y + k >= 0 && y + k < N && x + k >= 0 && x + k < N) {
                temp += arr[y + k][x + k];
            }
            if (y - k >= 0 && y - k < N && x + k >= 0 && x + k < N) {
                temp += arr[y - k][x + k];
            }
        }
        temp -= arr[y][x];
        return temp;
    }
}