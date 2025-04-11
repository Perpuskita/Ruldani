import javax.swing.*;

public abstract class ATM extends javax.swing.JFrame {

    final int maxhirarki = 6;
    String[] indikator = new String[maxhirarki+1];
    int buttonNow;
    protected int loop;
    String Cancel;
    String Enter;
    String Delete;
    // Variables declaration - do not modify
    private javax.swing.JLabel BackgroundATM;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel17;
    private javax.swing.JLabel jLabel18;
    private javax.swing.JLabel jLabel19;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel20;
    private javax.swing.JLabel jLabel21;
    private javax.swing.JLabel jLabel22;
    private javax.swing.JLabel jLabel23;
    private javax.swing.JLabel jLabel24;
    private javax.swing.JLabel jLabel25;
    private javax.swing.JLabel jLabel26;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextArea1;
    // End of variables declaration

    public ATM() {

        setTitle("SIATOR ( Simple ATM Simulator ) X >");

        try {

            initComponents();

        } catch (Exception e){

            JOptionPane.showMessageDialog(new JFrame(), "gagal load", "gagal untuk load asset", JOptionPane.ERROR_MESSAGE);
            System.exit(0);
        }

        for (int i = 0; i < maxhirarki; i++ )
            indikator[i] = "0";
        code(codex());
        setVisible(true);
        setBounds(0,0,980,970);
    }

    public abstract void code( String codex );

    private void looping(String laporan) {

        int count;
        count = 0;
        do {

            loop = count;

            if (indikator[count].equals("0")){

                indikator[count] = laporan;
                count = maxhirarki;

            }

            count++;

        } while ( count < maxhirarki);

        code(codex());

    }

    // <editor-fold defaultstate="collapsed" desc="Generated Code">
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();
        jLabel17 = new javax.swing.JLabel();
        jLabel18 = new javax.swing.JLabel();
        jLabel19 = new javax.swing.JLabel();
        jLabel20 = new javax.swing.JLabel();
        jLabel21 = new javax.swing.JLabel();
        jLabel22 = new javax.swing.JLabel();
        jLabel23 = new javax.swing.JLabel();
        jLabel24 = new javax.swing.JLabel();
        jLabel25 = new javax.swing.JLabel();
        jLabel26 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        BackgroundATM = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(null);

        jLabel1.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel1MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel1);
        jLabel1.setBounds(90, 450, 50, 40);

        jLabel2.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel2MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel2);
        jLabel2.setBounds(90, 500, 50, 40);

        jLabel3.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel3MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel3);
        jLabel3.setBounds(90, 550, 50, 40);

        jLabel4.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel4MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel4);
        jLabel4.setBounds(90, 600, 50, 40);

        jLabel5.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel5MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel5);
        jLabel5.setBounds(600, 450, 50, 40);

        jLabel6.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel6MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel6);
        jLabel6.setBounds(600, 500, 50, 40);

        jLabel7.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel7MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel7);
        jLabel7.setBounds(600, 550, 50, 40);

        jLabel8.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel8MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel8);
        jLabel8.setBounds(600, 600, 50, 40);

        jLabel9.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel9MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel9);
        jLabel9.setBounds(715, 340, 105, 120);

        jLabel10.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel10MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel10);
        jLabel10.setBounds(560, 790, 310, 110);

        jLabel11.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel11MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel11);
        jLabel11.setBounds(230, 794, 50, 20);

        jLabel12.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel12MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel12);
        jLabel12.setBounds(290, 794, 40, 20);

        jLabel13.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel13MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel13);
        jLabel13.setBounds(340, 794, 40, 20);

        jLabel14.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel14MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel14);
        jLabel14.setBounds(230, 820, 50, 20);

        jLabel15.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel15MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel15);
        jLabel15.setBounds(290, 820, 40, 20);

        jLabel16.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel16MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel16);
        jLabel16.setBounds(340, 820, 40, 20);

        jLabel17.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel17MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel17);
        jLabel17.setBounds(230, 850, 50, 20);

        jLabel18.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel18MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel18);
        jLabel18.setBounds(290, 850, 40, 20);

        jLabel19.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel19MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel19);
        jLabel19.setBounds(340, 850, 40, 20);
        getContentPane().add(jLabel20);
        jLabel20.setBounds(230, 880, 0, 0);

        jLabel21.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel21MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel21);
        jLabel21.setBounds(290, 876, 40, 20);
        getContentPane().add(jLabel22);
        jLabel22.setBounds(340, 880, 0, 0);

        jLabel23.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel23MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel23);
        jLabel23.setBounds(410, 794, 70, 20);

        jLabel24.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel24MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel24);
        jLabel24.setBounds(410, 820, 70, 20);
        getContentPane().add(jLabel25);
        jLabel25.setBounds(410, 850, 70, 20);

        jLabel26.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jLabel26MouseClicked(evt);
            }
        });
        getContentPane().add(jLabel26);
        jLabel26.setBounds(410, 874, 70, 20);

        jTextArea1.setEditable(false);
        jTextArea1.setBackground(new java.awt.Color(0, 0, 255));
        jTextArea1.setColumns(20);
        jTextArea1.setForeground(new java.awt.Color(255, 255, 255));
        jTextArea1.setRows(5);
        jTextArea1.setToolTipText("");
        jTextArea1.setBorder(null);
        jTextArea1.setName(""); // NOI18N
        jTextArea1.setPreferredSize(new java.awt.Dimension(190, 75));
        jTextArea1.setVerifyInputWhenFocusTarget(false);
        jScrollPane1.setViewportView(jTextArea1);

        jTextArea1.setFont(new java.awt.Font("Tahoma", 0, 21));

        getContentPane().add(jScrollPane1);
        jScrollPane1.setBounds(150, 300, 435, 357);

        BackgroundATM.setIcon(new javax.swing.ImageIcon(getClass().getResource("/ATM.png"))); // NOI18N
        getContentPane().add(BackgroundATM);
        BackgroundATM.setBounds(0, 0, 970, 940);

        pack();
    }// </editor-fold>


    private void jLabel1MouseClicked(java.awt.event.MouseEvent evt) {
        looping("1");
    }

    private void jLabel2MouseClicked(java.awt.event.MouseEvent evt) {
        looping("2");
    }

    private void jLabel3MouseClicked(java.awt.event.MouseEvent evt) {
        looping("3");
    }

    private void jLabel4MouseClicked(java.awt.event.MouseEvent evt) {
        looping("4");
    }

    private void jLabel5MouseClicked(java.awt.event.MouseEvent evt) {
        looping("5");
    }

    private void jLabel6MouseClicked(java.awt.event.MouseEvent evt) {
        looping("6");
    }

    private void jLabel7MouseClicked(java.awt.event.MouseEvent evt) {
        looping("7");
    }

    private void jLabel8MouseClicked(java.awt.event.MouseEvent evt) {
        looping("8");
    }

    private void jLabel9MouseClicked(java.awt.event.MouseEvent evt) {
        looping("atmcard");
    }

    private void jLabel10MouseClicked(java.awt.event.MouseEvent evt) {
        looping("money");
    }

    private void jLabel11MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 1;
        code(codex());
    }

    private void jLabel12MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 2;
        code(codex());
    }

    private void jLabel13MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 3;
        code(codex());
    }

    private void jLabel14MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 4;
        code(codex());
    }

    private void jLabel15MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 5;
        code(codex());
    }

    private void jLabel16MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 6;
        code(codex());
    }

    private void jLabel17MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 7;
        code(codex());
    }

    private void jLabel18MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 8;
        code(codex());
    }

    private void jLabel19MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 9;
        code(codex());
    }

    private void jLabel21MouseClicked(java.awt.event.MouseEvent evt) {
        buttonNow = 0;
        code(codex());
    }

    private void jLabel23MouseClicked(java.awt.event.MouseEvent evt) {
        looping(Cancel);
    }

    private void jLabel24MouseClicked(java.awt.event.MouseEvent evt) {
        looping(Delete);
    }

    private void jLabel26MouseClicked(java.awt.event.MouseEvent evt) {
        looping(Enter);
    }

    public void print(String print){

        jTextArea1.setText(print);

    }

    public String codex(){

        StringBuilder code = new StringBuilder(indikator[0]);

        for (int i=1; i<maxhirarki;i++){

            code.append(indikator[i]);

        }

        System.out.println(code);
        return code.toString();

    }

}
