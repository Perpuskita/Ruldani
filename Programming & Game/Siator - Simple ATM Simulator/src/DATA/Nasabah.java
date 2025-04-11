package DATA;

public class Nasabah extends MenuUtamaNasabah {

    public Nasabah(){

        super();

    }

    public boolean transfer( String NorekTujuan, int nominal){

        DataNasabah current = first;
        while(!current.Norek.equals(NorekTujuan)){
            current = current.next;
            if(current == null)
                return false;
        }

        current.Saldo = current.Saldo + nominal;
        return true;

    }

}