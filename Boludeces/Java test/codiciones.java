class condiciones {
  public static void main(String[] args) {
    int num = 0;
    /* anda */
    while (num++ != 10) {
      System.out.println(num);
    }
    /* AHHH, viste que no tiene sentido. Pero en JS si se puede por EJ */
    /*
     * if (num = 10) {
     * System.out.println(num);
     * }
     */
    String palabras[] = { "hola", "hoy", "pepe", "esta", "en", "casa" };
    String escritor;
    num = 0;
    /* Lo mismo. En JS si. Me di cuenta de que esto es un foreach */
    /*
     * while (escritor = palabras[num]) {
     * 
     * }
     */
    for (String h : palabras) {
      System.out.println(h);
      num++;
    }
    System.out.println("FIN");
  }
}