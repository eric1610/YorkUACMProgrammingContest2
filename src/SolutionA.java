import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SolutionA {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		String [] temp;
		List<String> words = new ArrayList<String>();
		while (sc.hasNextLine()) {
			temp = sc.nextLine().split(" ");
			int counter = 0;
			for (String a: temp) {
				a = a.toLowerCase();
				counter ++;
				if (words.contains(a)) {
					System.out.print(".");
				} else {
					words.add(a);
					System.out.print(a);
				}
				if (counter < temp.length) {
					System.out.print(" ");
				}
			}
			System.out.println("");
		}
	}
}
