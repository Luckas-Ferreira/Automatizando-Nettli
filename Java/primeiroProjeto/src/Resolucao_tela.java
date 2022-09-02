import java.awt.Dimension;
import java.awt.Toolkit;

public class Resolucao_tela {
    public static void main(String[] args) {
        Dimension tela = Toolkit.getDefaultToolkit().getScreenSize();
        int alt = (int) tela.getHeight();
        int lar = (int) tela.getWidth();
        System.out.println("Sua tela tem resolução: " + alt + "X" + lar);
    }
}
