import java.util.Scanner;
/*
public class Exemplo {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        byte quantidade;
        String condicao;
        System.out.print("Quantas pernas tem? ");
        quantidade = teclado.nextByte();
        
        if (quantidade == 1) {
            condicao = "Saci";
        }
        else if (quantidade == 2) {
            condicao = "bípede";
        }
        else if (quantidade == 4) {
            condicao = "quadrúpede";
        }
        else if (quantidade == 6 || quantidade == 8) {
            condicao = "aranha";
        }
        else {
            condicao = "ET";
        }
        System.out.format("Isto claramente é um %s", condicao);
        teclado.close();
    }
}
*/

public class Exemplo{
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        byte pernas;
        String tipo;
        System.out.print("Quantas pernas tem? ");
        pernas = teclado.nextByte();
        switch (pernas) {
            case 1:
                tipo = "Saci";
                break;
            case 2:
                tipo = "bípede";
                break;
            case 4:
                tipo = "quadrúpede";
                break;
            case 6:
                tipo = "aranha";
                break;
            default:
                tipo = "ET";
        }
        System.out.printf("Isto claramente é um %s", tipo);
        teclado.close();
    }
}