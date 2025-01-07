import java.io.*;
import java.util.*;

public class p1936 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        if (A == 1 && B == 2 || A == 2 && B == 3 || A == 1 && B == 3) {
            bw.write("B" + "\n");
        } else {
            bw.write("A" + "\n");
        }
        bw.flush();
        bw.close();
    }
}