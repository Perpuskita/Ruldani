package DATA;

import DATA.DataNasabah;

public class MenuUtamaNasabah {

    protected DataNasabah first;
    protected DataNasabah last;
    protected String Norek;

    MenuUtamaNasabah(){

        first = null;
        last = null;

    }

    public void setBlokir(boolean TrueOrFalse){

        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
            if(current == null) break;
        }

        if (current != null) current.Blokir = TrueOrFalse;

    }

    public void SetCurrNorek(String Norek){

        this.Norek = Norek;

    }

    public String GetCurrNorek(){

        return Norek;

    }

    public boolean isEmpty(){
        return (first==null);
    }

    public DataNasabah deleteKey( String Norek){

        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
            if(current == null)
                return null;
        }

        if(current==first)
            first = current.next;
        else
            current.prev.next = current.next;
        if(current==last)
            last = current.prev;
        else
            current.next.prev = current.prev;
        return current;

    }

    public void setSaldoNasabah(int masuk) {

        System.out.println(Norek);
        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
        }
        current.Saldo = current.Saldo + masuk;

    }

    public int getSaldoNasabah( int masuk) {

        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
        }
        current.Saldo = current.Saldo-masuk ;
        return current.Saldo;
    }

    public int getSaldoNasabah() {

        DataNasabah current = first;

        while(!current.Norek.equals(Norek)){
            current = current.next;
        }

        return current.Saldo;

    }


    public void setNoRek( String Norek, String Pin) {
        DataNasabah DataN = new DataNasabah(Norek);
        if( isEmpty() )
            first = DataN;
        else{
            last.next = DataN;
            DataN.prev = last;
        }
        last = DataN;
        DataN.Norek = Norek;
        this.Norek = Norek;
        SetPIN(Pin);

    }

    public void SetPIN( String Pin) {

        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
        }

        current.PIN = Pin;

    }

    public String GetPIN() {

        DataNasabah current = first;
        while(!current.Norek.equals(Norek)){
            current = current.next;
        }
        return current.PIN;
    }

    public void displayForward(){
        System.out.print("List (first-->last): \n");
        DataNasabah current = first;
        while(current != null){
            current.tampil();
            current = current.next;
        }
        System.out.println("");
    }

}
