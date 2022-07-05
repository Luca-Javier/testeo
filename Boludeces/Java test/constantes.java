public class constantes {
  /* por que el main no agarra esta variable?? */
  public final int num = 10;

  public static void main(String[] args) {
    final int num = 10;
    int num2 = 10;
    while (num == 10) {
      System.out.println("num vale " + num);
      /* num = num + 1; */ /*
                            * Lo comento y pongo el break porque sino me
                            * ejecuta este archivo
                            */

      break;
      /* No se puede */

    }
  }

}