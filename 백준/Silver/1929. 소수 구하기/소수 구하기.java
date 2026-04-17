import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int m = scanner.nextInt();
		int n = scanner.nextInt();
		boolean[] b = new boolean[n + 1];
		b[0] = b[1] = true;
		for (int i = 2; i < n + 1; i++) 
			for (int j = 2; i * j < n + 1; j++)
				b[i * j] = true;
		for (int i = m; i < n + 1; i++)
			if (b[i] == false)
				System.out.println(i);
		scanner.close();
	}
}