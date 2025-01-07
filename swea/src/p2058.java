import java.io.*;

public class p2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int sum = 0;
        while (N > 0) {
            sum += N % 10;
            N /= 10;
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sum+"\n");
        bw.flush();
        bw.close();
    }
}