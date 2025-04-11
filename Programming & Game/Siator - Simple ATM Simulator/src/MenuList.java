import DATA.Nasabah;

public class MenuList extends ATM{

    private final Nasabah NasabahN;
    StackN pin = new StackN(6);
    StackN cair = new StackN(8);
    private int withdraw;
    private boolean activate, cukup;

    MenuList ( Nasabah NasabahN  ){

        super();
        this.NasabahN = NasabahN;

    }

    public void code( String codex ) {

        if (activate){

            switch(codex){

                case "000000" -> {

                    print("\nsilahkan pilih jumlah penarikan \n atau menu lain \n\n\n\n 300.000                                        500.000  \n\n 1.000.000                                   2.500.000  \n\n informasi rekening      Penarikan jumlah lain  \n\n keluar                                      menu lain  \n ");
                    resetButtonFunction("4","0","0");

                }
                // statment giro tabungan

                case "100000", "200000", "500000", "600000", "700000" -> print("\n\n\n\n\n\n                                      --> Rekening giro \n\n                             --> Rekening Tabungan \n\n\n\nKembali <-- ");

                case "140000", "240000", "540000", "640000", "740000"-> reset();

                case "150000", "250000", "550000", "650000", "750000" -> print("maintance klik 8 untuk kembali");

                case "158000", "258000", "558000", "658000", "758000" -> reset(2);

                // end of statment giro tabungan

                // withdraw 3000.000

                case "160000" -> withdraw(300000);

                case "164000" -> reset();

                case "165000" -> {

                    cukup = true;
                    withdraw(50000,300000);

                }

                case "166000" -> {

                    cukup = true;
                    withdraw(100000,300000);

                }

                // end of withdraw 300.000

                // withdraw statment 1.000.000

                case "260000" -> withdraw(1000000);

                case "264000" -> reset();

                case "265000" -> {

                    cukup = true;
                    withdraw(50000,1000000);

                }

                case "266000" -> {

                    cukup = true;
                    withdraw(100000,1000000);

                }

                // end of withdraw statment 1.000.000

                //link again statment

                case "165800" -> {

                    if (!cukup){

                        print("\n\n   ingin melakukan transaksi lagi ? \n\n\n\n\n\n\n\n                                                    -- > y \n\n                                                    -- > n");

                    }

                    else {
                        refresh(2);
                    }

                }

                case "165870" -> reset();

                case "165880" -> print("\n\n\n\n\n\n Terimakasih Telah Menggunakan Bank Kami\n          Silahkan ambil kartu ATM anda");

                case "16588atmcard" -> {

                    activate=false;
                    quit();
                }

                //end of link again statment

                // print statment

                case "300000" -> print("Nomor Rekening"+NasabahN.GetCurrNorek()+"\nSaldo"+NasabahN.getSaldoNasabah()+"\n\n 7.cetak info \n8. kembali");

                case "370000" -> print("maintance klik 8 untuk kembali");

                case "378000" -> reset(2);

                case "380000" -> reset();

                // end of print statment

                // quit

                case "400000" -> {
                    quit();
                    activate = false;
                }

                // end of quit statment

                // withdraw statment 500.000

                case "560000" -> withdraw(500000);

                case "564000" -> reset();

                case "565000" -> {

                    cukup = true;
                    withdraw(50000,500000);

                }

                case "566000" -> {

                    cukup = true;
                    withdraw(100000,500000);

                }

                // end of withdraw statment 500.000

                // withdraw statment 2.500.000

                case "660000" -> withdraw(2500000);

                case "664000" -> reset();

                case "665000" -> {

                    cukup = true;
                    withdraw(50000,2500000);

                }

                case "666000" -> {

                    cukup = true;
                    withdraw(100000,2500000);

                }

                // end of withdraw statment 2.500.000

                // withdraw nominal

                case "760000" -> {

                    resetButtonFunction("8", "9", "7");
                    push(cair);
                    print("Masukan Nominal\n " + cair.info(false) + " \n\n 7. Next \n 8. kembali ");

                }

                case "767000" -> {

                    withdraw(Integer.parseInt(cair.info(false)));
                    cair.reset();
                    linktoagain();
                }

                case "768000" -> {
                    cair.reset();
                    reset(3);
                    code(codex());
                }

                // end of withdraw nominal

                // menu ganti pin

                case "800000" -> print("menu 2\n\n 1. ganti pin");

                case "810000" -> {

                    pin.push(buttonNow);

                    if (Integer.parseInt(pin.info(false))!=0){

                        print("Masukan pin baru " + pin.info(false) + "\n\nklik 7 untuk oke, 8 kembali menu utama");

                    } else {

                        print("Masukan pin baru \n\nklik 7 untuk oke, 8 kembali menu utama");

                    }

                }

                case "818000" -> reset();

                case "817000" -> {

                    print("pin telah diganti klik 7 untuk melanjutkan");
                    NasabahN.SetPIN(pin.info(false));

                }

                case "817700" -> {

                    linktoagain();
                    pin.reset();

                }

                case "840000" -> reset();

                default -> refresh(loop);

            }

        } else {

            switch(codex){

                case "000000" -> {

                    print("\n\n\n\n\n\n              Masukan Kartu ATM Anda");
                    buttonNow=0;
                    refresh(0);
                    resetButtonFunction();

                }

                case "atmcard00000" ->{

                    String info = "";


                    resetButtonFunction("8", "9","7");
                    NasabahN.SetCurrNorek("1234");

                    if (buttonNow!=11){

                        push(pin);

                    }

                    print("\n                      Masukan PIN\n\n"+pin.info(true)+"\n\n\n\n\n\n\n                                                lanjut -- >\n\n                                               keluar -- >");
                    refresh(1);

                }

                case "atmcard70000" ->{

                    if (pin.info(false).equals(NasabahN.GetPIN())){

                        activate = true;
                        reset();

                    } else {

                        print("PIN SALAH tekan 7 untuk kembali login \n 8 untuk keluar");

                    }

                    pin.reset();

                }

                case "atmcard90000" -> {

                    pop(pin);
                    reset(2);

                }

                case "atmcard77000" -> reset(2);

                case "atmcard78000", "atmcard80000" ->{

                    pin.reset();
                    print("Silahkan ambil kartu ATM anda");

                }

                case "atmcard78atmcard00","atmcard8atmcard000" -> reset();

                default -> refresh(loop);

            }

        }

    }

    private void push (StackN target){

        if (buttonNow!=11) {

            target.push(buttonNow);
        }

    }

    private void pop(StackN target)
    {

        target.pop();
        buttonNow=11;

    }

    private void withdraw (int tipe, int jumlah){

        if (cukup){

            dompet(tipe, jumlah);
            NasabahN.getSaldoNasabah(withdraw);

        }

        cukup = false;
        linktoagain();

    }

    private void withdraw(int withdraw){

        this.withdraw = withdraw;
        if (NasabahN.getSaldoNasabah()>=withdraw){

            print("\n Saldo anda sekarang : "+ NasabahN.getSaldoNasabah()+"\n Saldo setelah dikurangi : " + (NasabahN.getSaldoNasabah()-withdraw) +"\n\n\n\n                          uang pecahan 50.000 -->\n\n                        uang pecahan 100.000 -->\n\n\n\nkembali");


        } else {

            cukup = false;
            print("saldo anda tidak mencukupi");

        }

    }

    private void dompet(int tipe, int jumlah){

        System.out.println("uang yang ditambahkan ke dompet " + tipe + " sebanyak " + jumlah/tipe);

    }

    void reset(){

        for (int i=0; i < maxhirarki; i++){

            indikator[i]="0";

        }

        code(codex());

    }

    void resetButtonFunction(){

        Cancel="0";
        Delete="0";
        Enter="0";

    }


    void resetButtonFunction( String C, String D, String E){

        Cancel=C;
        Delete=D;
        Enter=E;

    }

    void reset(int index){

        indikator[index]="0";
        indikator[index-1]="0";
        code(codex());

    }

    public void quit (){

        indikator[0] = "1";
        indikator[1] = "6";
        indikator[2] = "5";
        indikator[3] = "8";
        reset();

    }

    void refresh(int index){

        indikator[index]="0";

    }

    void linktoagain(){

        reset();
        indikator[0] = "1";
        indikator[1] = "6";
        indikator[2] = "5";
        indikator[3] = "8";

        code(codex());

    }

}
