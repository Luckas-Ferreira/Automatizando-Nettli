import java.util.Arrays;
public class ExercidioVetores {
    public static void main(String[] args) {
        System.out.println("EXEMPLO 1");
        String mes[] = {"jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "des"};
        byte   dia[] = {31, 28, 31, 31, 31, 30, 31, 31, 30, 31, 30, 31};
        for (byte c = 0; c < mes.length; c++) {
            System.out.printf("O mês de %s tem %d dias ao todo \n",mes[c], dia[c]);
        }
        System.out.println("EXEMPLO 2");
        int   num[] = {2, 5, 1, 7, 9};
        for (int valor: num) {
            System.out.print(valor + " ");
        }
        System.out.println("\n ORDENADOS");
        Arrays.sort(num);
        System.out.printf(" " + num);

        System.out.println("\n BUSCA BINARIA");          
        
        
    }
}
