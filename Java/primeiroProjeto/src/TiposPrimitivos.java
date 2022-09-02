import java.util.Scanner;
public class TiposPrimitivos {
    public static void main(String[] args) {
        System.out.println("Os tipos primitivos são: ");
        
        Scanner teclado = new Scanner(System.in);
        System.out.print("Nome do aluno: ");
        String nome = teclado.nextLine();
        System.out.print("Nota do aluno: ");
        float nota = teclado.nextFloat();

        System.out.printf("A nota de %s foi: %.1f pontos", nome, nota);
        teclado.close();
    }
}
