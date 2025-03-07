

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		Map<String, Integer> map = new HashMap<>();
	
		for(int i=0; i<N;i++) {
			String word = br.readLine();
			if(word.length() >= M) {
				map.put(word, map.getOrDefault(word, 0)+1);
				
			}
		}
	
		
		System.out.println(solution(map, N,M).toString());
		
	}

	public static StringBuilder solution(Map<String, Integer> map, int n, int m) {
		StringBuilder sb = new StringBuilder();
		
		List<Map.Entry<String,Integer>> list = new ArrayList<>(map.entrySet()); 
		list.sort((entry1, entry2) -> {
			int valueCompare = entry2.getValue() - entry1.getValue();
			if (valueCompare != 0) {
				
				return valueCompare; 
			}
			
			int lengthCompare = entry2.getKey().length() - entry1.getKey().length();
			if (lengthCompare != 0) {
				return lengthCompare; 
			}
			
			return entry1.getKey().compareTo(entry2.getKey());
		});

        for (Map.Entry<String, Integer> entry : list) {
            sb.append(entry.getKey()+"\n");
        }
		
		return sb;
	}
}
