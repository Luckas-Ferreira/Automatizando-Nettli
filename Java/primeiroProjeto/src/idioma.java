import java.util.*;
public class idioma {
    public static void main(String[] args) {
        Locale Log = Locale.getDefault();
        System.out.print("O idioma do sistema é: " + Log.getDisplayLanguage() + "-");
        System.out.println(Log.getLanguage());
    }
}
