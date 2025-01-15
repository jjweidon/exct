import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] bucket = new int[N + 1];
        for (int m = 0; m < M; m++) {
        	st = new StringTokenizer(br.readLine());
        	int i = Integer.parseInt(st.nextToken());
        	int j = Integer.parseInt(st.nextToken());
        	int k = Integer.parseInt(st.nextToken());
        	for (int index = i; index <= j; index++) {
        		bucket[index] = k;
        	}
        }
        
        for (int i = 1; i <= N; i++) {
        	bw.write(bucket[i] + " ");
        }
        
        br.close();
        bw.flush();
        bw.close();
    }
}