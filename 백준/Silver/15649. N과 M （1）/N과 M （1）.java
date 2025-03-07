import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	private static int N;
	private static int M;
	static int[] result; //결과배열
	static boolean[] visited; //방문쳌

	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken()); // ex. 4
		M = Integer.parseInt(st.nextToken()); // ex. 2
		
		result = new int[M];
		visited = new boolean[N];
		
		perm(0);
		
		System.out.println(sb.toString());
	}
	
	// 순열
	static void perm(int idx) {
		if(idx == M) {
			
			for(int i=0 ; i<M;i++) {
				sb.append(result[i]).append(" ");
			}
			sb.append("\n");
			
			return;
		}
		
		// 재귀부분
		for(int i=0; i < N ; i++) {
			if(visited[i]) continue;
			result[idx] = i+1;
			visited[i] = true;
			perm(idx+1);
			visited[i] = false;// 원상복구
		}
		
		
		
		
		
		
	}
}
