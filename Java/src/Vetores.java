public class Vetores {
    public static void main(String[] args) {
        int n[] = {2, 5, 7, 9};
        System.out.println(" USANDO FOR");
        for (int c = 0; c < n.length; c++) {
            System.out.printf("Na posição %d está o numero %d \n", c, n[c]);
        }
        System.out.println("\n USANDO WHILE");
        int c = 0;
        while (c <= 3) {
            System.out.printf("Na posição %d está o numero %d \n", c, n[c]);
            c++;
        }
        System.out.println("\n USANDO DO");
        
    }
}
