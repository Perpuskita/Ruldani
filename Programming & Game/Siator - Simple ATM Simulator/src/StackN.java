class StackN implements Stack
{
    private final int[] arr;
    private int head;
    private final int capacity;

    StackN(int size)
    {
        arr = new int[size+1];
        capacity = size+1;
        head = -1;
    }

    public void push(int x)
    {

        if (!isFull()) {
            arr[++head] = x;
        }

        System.out.println(head);

    }

    public void pop()
    {
        if (!isEmpty()) {
            head--;
        }
    }

    public void reset(){

        head = -1;

    }

    private int info()
    {
        int total = 0;
        int hitung = 1;
        if (!isEmpty()) {

            for (int i=head; i > 0; i--){
                total = total + ( hitung * arr[i]);
                hitung = hitung * 10;

            }

        }

        return total;
    }

    public String info(boolean invisible){

        if (invisible){

            StringBuilder stringcode = new StringBuilder(" ");

            if (!isEmpty()) {

                for (int i=head; i > 0; i--){

                    if (arr[i]!=0){

                        stringcode.append("*");

                    }

                }

            }

            return stringcode.toString();

        }

        else {

            return String.valueOf(info());

        }

    }

    private Boolean isEmpty()
    {
        return head == 0;
    }

    private Boolean isFull() {
        return head == capacity - 1;
    }
}