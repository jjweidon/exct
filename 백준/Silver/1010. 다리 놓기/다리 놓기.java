import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[] dp = new int[N+1];
            dp[1] = M - N + 1;

            for (int i = 2; i <= N; i++) {
                dp[i] = dp[i-1] * (M - N + i) / i;
            }

            bw.write(dp[N] + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}