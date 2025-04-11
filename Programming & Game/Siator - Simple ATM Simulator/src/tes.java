import DATA.Nasabah;

public class tes {

    public static void main(String[] args) {

        Nasabah BNI = new Nasabah();
        MenuList bank = new MenuList(BNI);

        BNI.setNoRek("1234","123444");
        BNI.setNoRek("7890","789000");
        BNI.SetCurrNorek("1234");
        BNI.setSaldoNasabah(1000000);

    }

}
