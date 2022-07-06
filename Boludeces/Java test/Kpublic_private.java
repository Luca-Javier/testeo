public class Kpublic_private {
  public static void main(String[] args) {
    Animal tobi = new Animal();
    tobi.ladrar();
    int h = tobi.edad();
    System.out.println(h);
    tobi.tengo();
  }

  static class Animal {
    int age;

    Animal() {
      age = edad();
    }

    public void ladrar() {
      System.out.println("wow wow");
    }

    void tengo() {
      System.out.println("Tengo " + age + " años");
    }

    private int edad() {
      /* no entendi esto */
      int test = (int) (Math.random() * (10 - 1)) + 1;
      return test;
    }
  }
}
