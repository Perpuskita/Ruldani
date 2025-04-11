package DATA;

public class DataNasabah extends DataWajibNasabah {

    int Saldo;
    DataNasabah next;
    DataNasabah prev;

    public DataNasabah(String Norek) {
        this.Norek = Norek;
    }
    public void tampil(){

        super.tampil();
        System.out.print(Saldo + "\n");

    }

}
