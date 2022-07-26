class temi {

    public static void main(String[] args) {

        String name = "Temie";
        String x = Greet(name);
        System.out.println(x);

    }

    public static String Greet(String name) {

        System.out.println("Hello " + name);
        return name + " Dani";

    }
}