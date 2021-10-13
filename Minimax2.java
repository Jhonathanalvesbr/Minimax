
import java.util.ArrayList;
import javax.swing.JPanel;
import java.awt.Graphics2D;
import java.awt.Graphics;
import java.awt.event.MouseListener;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.sound.midi.Soundbank;
import javax.swing.JFrame;
import javax.swing.JProgressBar;
import javax.swing.UIManager;

public class Minimax2 {

    public static class No {

        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura = 0;
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
        int valor = 0;
        boolean jogada;
        ArrayList<Integer> selecao = new ArrayList();
        int heuristica = 0;
    }

    public static class Personagem implements Cloneable {

        public ArrayList<PlayerImagem> playerImagem;
        int vida = 2;
        JProgressBar life = new JProgressBar(0, vida);
        int ataque = 1;
        int level = 1;
        int id = 0;
        int indice;
        int time = 150;
        int tempo = 0;
        int x = 0;
        int y = 0;
        String nome = new String();
        boolean isPlayer = false;

        @Override
        protected Personagem clone() throws CloneNotSupportedException {
            return (Personagem) super.clone();
        }

        public void update() {
            if (tempo > time) {
                indice++;
                if (indice > playerImagem.size() - 1) {
                    indice = 0;
                }
                playerImagem.get(indice).x = x;
                playerImagem.get(indice).y = y;
                tempo = 0;
            }
            tempo++;
            life.setValue(vida);
        }
    }

    public static class PlayerImagem {

        BufferedImage imagem;
        int x;
        int y;

        public PlayerImagem(BufferedImage imagem, int x, int y) {
            this.imagem = imagem;
            this.x = x;
            this.y = y;
        }
    }

    public static ArrayList<PlayerImagem> virar(ArrayList<PlayerImagem> imagem) {
        for (int i = 0; i < imagem.size(); i++) {
            imagem.get(i).imagem = Minimax2.flip(imagem.get(i).imagem);
        }
        return imagem;
    }

    public static BufferedImage flip(BufferedImage image) {
        AffineTransform tx = tx = AffineTransform.getScaleInstance(-1, 1);
        AffineTransformOp op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
        tx.translate(-image.getWidth(null), 0);
        op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
        image = op.filter(image, null);

        return image;
    }

    public static class Img {

        Rectangle2D img;
        int id;
    }

    static int maximo = Integer.MIN_VALUE;

    public static class TelaGame extends JPanel implements MouseListener {

        ArrayList<Personagem> player;
        ArrayList<Personagem> playerInimigo;
        ArrayList<Img> img = new ArrayList<>();
        Font fontePequena = new Font("Consolas", Font.BOLD, 10);

        ArrayList<Integer> selecao = new ArrayList();
        boolean click = true;

        No no;

        public void escolhe(int i) {
            if (click) {
                int k = 0;
                int e = 0;
                for (Personagem personagem : player) {
                    if (personagem.id == i) {
                        e = 1;
                        break;
                    }
                    k++;
                }
                if (e == 0) {
                    return;
                }
                selecao.add(k);
                click = !click;
            } else {
                int k = 0;
                for (Personagem personagem : playerInimigo) {
                    if (personagem.id == i) {
                        break;
                    }
                    k++;
                }
                selecao.add(k);
                click = !click;
            }
            System.out.println(selecao);
            if (selecao.size() >= 2 && playerInimigo.size() > 0 || selecao.size() >= 2 && player.size() > 0) {
                playerInimigo.get(selecao.get(1)).vida -= player.get(selecao.get(0)).ataque;
                System.out.println("Eu: " + player.get(selecao.get(0)).nome + " -> " + playerInimigo.get(selecao.get(1)).nome);
                playerInimigo.get((selecao.get(1))).update();
                

                
                No no = new No();
                no.player = player;
                no.playerInimigo = this.playerInimigo;

                if (playerInimigo.size() > 0) {
                    try {
                        maximo = Integer.MIN_VALUE;
                        System.out.println("Valor: " + minimax(no, true, MIN, MAX));
                        System.out.println("Gerados: " + tamanho);
                        tamanho = 0;
                        System.out.println("Tamanho: " + no.filho.size());
                        System.out.println("Minimo: " + maximo);
                        ArrayList<Integer> aux = new ArrayList();
                        ArrayList<Integer> valor = new ArrayList();
                        ArrayList<Integer> maior = new ArrayList();
                        valor.add(Integer.MIN_VALUE);
                        valor.add(0);
                        maior.add(Integer.MIN_VALUE);
                        maior.add(0);
                        for (int k = 0; k < no.filho.size(); k++) {
                            System.out.println(k + " | " + no.filho.get(k).valor + " : " + no.filho.get(k).selecao + " -- " + no.filho.get(k).jogada);
                            if (no.filho.get(k).valor > 0 && no.filho.get(k).valor >= valor.get(0)) {
                                //System.out.println("    : " + no.filho.get(k).playerInimigo.get(no.filho.get(k).selecao.get(0)).nome);
                                valor.remove(0);
                                valor.remove(0);
                                valor.add(no.filho.get(k).valor);
                                valor.add(k);
                            }

                            if (no.filho.get(k).valor > maior.get(0)) {
                                //System.out.println("    : " + no.filho.get(k).playerInimigo.get(no.filho.get(k).selecao.get(0)).nome);
                                maior.remove(0);
                                maior.remove(0);
                                maior.add(no.filho.get(k).valor);
                                maior.add(k);
                            }
                        }
                        System.out.println("============ " + valor.get(0));
                        if (valor.get(0) == Integer.MIN_VALUE) {
                            //System.out.println(valor.get(0));
                            valor = maior;
                        }
                        int x = 0;
                        int y = 0;
                        for (int j = 0; j < player.size(); j++) {
                            if (player.get(j).id == no.filho.get(valor.get(1)).selecao.get(0)) {
                                y = j;
                                break;
                            }
                        }
                        for (int j = 0; j < playerInimigo.size(); j++) {
                            if (playerInimigo.get(j).id == no.filho.get(valor.get(1)).selecao.get(1)) {
                                x = j;
                                break;
                            }
                        }
                        System.out.println("PLayer Morreu: " + (3 - player.size()));
                        System.out.println("Minimax: " + playerInimigo.get(x).nome + " -> " + player.get(y).nome);
                        System.out.println("Minimax: " + playerInimigo.get(x).id + " -> " + player.get(y).id);
                        player.get(y).vida -= playerInimigo.get(x).ataque;
                        player.get(y).update();
                        if(player.get(y).vida <= 0)
                            player.remove(player.get(y));


                        
                    } catch (CloneNotSupportedException ex) {
                        Logger.getLogger(Minimax.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }

                selecao = new ArrayList();
            }
        }

        public TelaGame(ArrayList<Personagem> player, ArrayList<Personagem> playerInimigo) {
            this.player = player;
            this.playerInimigo = playerInimigo;
            /*for (int k = 0; k < player.size(); k++) {
                this.add(player.get(k).life);
            }
            for (int k = 0; k < playerInimigo.size(); k++) {
                this.add(playerInimigo.get(k).life);
            }*/
        }
        int q = 0;

        @Override
        public void paintComponent(Graphics g2) {
            Graphics2D g = (Graphics2D) g2.create();
            g.setColor(Color.BLACK);
            g.fillRect(0, 0, 600, 600);
            g.setStroke(new BasicStroke(3));

            for (int k = 0; k < player.size(); k++) {
                if (player.get(k).vida > 0) {
                    if (q == 0) {
                        Img aux = new Img();
                        aux.img = new Rectangle2D.Double(player.get(k).x, player.get(k).y, player.get(k).playerImagem.get(player.get(k).indice).imagem.getWidth(), player.get(k).playerImagem.get(player.get(k).indice).imagem.getHeight());
                        aux.id = player.get(k).id;
                        img.add(aux);
                    }
                    g.setFont(fontePequena);
                    g.setColor(Color.green);
                    g.drawString(" Atk: " + player.get(k).ataque, player.get(k).x + 80, player.get(k).y + 20);
                    g.drawImage(player.get(k).playerImagem.get(player.get(k).indice).imagem, player.get(k).x, player.get(k).y, null);
                    player.get(k).life.setBounds(80, player.get(k).y, 50, 10);
                    player.get(k).update();
                    this.add(player.get(k).life);
                } else {
                    //this.remove(player.get(k).life);
                    player.remove(k);

                }
            }
            for (int k = 0; k < playerInimigo.size(); k++) {
                if (playerInimigo.get(k).vida > 0) {
                    if (q == 0) {
                        Img aux = new Img();
                        aux.img = new Rectangle2D.Double(playerInimigo.get(k).x, playerInimigo.get(k).y, playerInimigo.get(k).playerImagem.get(playerInimigo.get(k).indice).imagem.getWidth(), playerInimigo.get(k).playerImagem.get(playerInimigo.get(k).indice).imagem.getHeight());
                        aux.id = player.get(k).id;
                        img.add(aux);
                    }
                    if (playerInimigo.get(k).nome == "Nagato") {
                        g.setFont(fontePequena);
                        g.setColor(Color.red);
                        g.drawString(" Atk: " + playerInimigo.get(k).ataque, playerInimigo.get(k).x - 45, playerInimigo.get(k).y + 20);

                    } else {
                        g.setFont(fontePequena);
                        g.setColor(Color.red);
                        g.drawString(" Atk: " + playerInimigo.get(k).ataque, playerInimigo.get(k).x - 15, playerInimigo.get(k).y + 20);

                    }
                    g.drawImage(playerInimigo.get(k).playerImagem.get(playerInimigo.get(k).indice).imagem, playerInimigo.get(k).x, playerInimigo.get(k).y, null);
                    playerInimigo.get(k).life.setBounds(450, playerInimigo.get(k).y, 50, 10);
                    this.add(playerInimigo.get(k).life);
                    playerInimigo.get(k).update();
                } else {
                    //this.remove(playerInimigo.get(k).life);
                    playerInimigo.remove(k);
                }
            }
            q++;
            repaint();
        }

        @Override
        public void mouseClicked(MouseEvent e) {
            Point p = e.getPoint();

            for (int i = 0; i < img.size(); i++) {
                if (img.get(i).img.contains(p)) {
                    escolhe(img.get(i).id);
                    break;
                }
            }

        }

        @Override
        public void mousePressed(MouseEvent e) {
            //System.out.println(e.getX());
        }

        @Override
        public void mouseReleased(MouseEvent e) {
            //System.out.println(e.getX());
        }

        @Override
        public void mouseEntered(MouseEvent e) {
            //System.out.println(e.getX());
        }

        @Override
        public void mouseExited(MouseEvent e) {
            //System.out.println(e.getX());
        }

    }

    static int tamanho = 0;
    static int MAX = Integer.MAX_VALUE;
    static int MIN = Integer.MIN_VALUE;

    public static void main(String[] args) throws CloneNotSupportedException, IOException {
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            Personagem aux = new Personagem();
            aux.id = i;
            aux.life.setBackground(Color.red);
            aux.life.setForeground(Color.green);
            aux.life.setValue(aux.vida);
            aux.life.setVisible(true);
            playerInimigo.add(aux);
        }

        for (int i = 0; i < 3; i++) {
            Personagem aux = new Personagem();
            aux.id = i;
            aux.life.setBackground(Color.red);
            aux.life.setForeground(Color.green);
            aux.life.setValue(aux.vida);
            aux.life.setVisible(true);
            aux.isPlayer = true;
            player.add(aux);
        }

        ArrayList<PlayerImagem> naruto = new ArrayList<PlayerImagem>();
        naruto.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Naruto\\50_Asset_90.png")), 0, 0));
        naruto.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Naruto\\60_Asset_83.png")), 0, 0));
        player.get(0).playerImagem = naruto;
        player.get(0).nome = "Naruto";
        ArrayList<PlayerImagem> sasuke = new ArrayList<PlayerImagem>();
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\1_Asset_43.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\43_Asset_40.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\115_Asset_39.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\139_Asset_41.png")), 0, 0));
        player.get(1).playerImagem = sasuke;
        player.get(1).nome = "Sasuke";
        player.get(1).y = 190;
        ArrayList<PlayerImagem> kakashi = new ArrayList<PlayerImagem>();
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\86_Asset_38.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\96_Asset_33.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\101_Asset_37.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\106_Asset_35.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\111_Asset_34.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\115_Asset_36.png")), 0, 0));
        player.get(2).playerImagem = kakashi;
        player.get(2).nome = "Kakashi";
        player.get(2).y = 380;

        ArrayList<PlayerImagem> nagato = new ArrayList<PlayerImagem>();
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\4_Asset_34.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\5_Asset_35.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\21_Asset_41.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\43_Asset_36.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\65_Asset_38.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\75_Asset_40.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\95_Asset_146.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\126_Asset_37.png")), 0, 0));
        nagato.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Nagato\\146_Asset_39.png")), 0, 0));
        nagato = Minimax2.virar(nagato);
        playerInimigo.get(0).nome = "Nagato";
        playerInimigo.get(0).playerImagem = nagato;
        playerInimigo.get(0).x = 500;

        ArrayList<PlayerImagem> madara = new ArrayList<PlayerImagem>();
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_61.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_60.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_59.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_58.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_57.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_58.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_59.png")), 0, 0));
        madara.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Madara\\Asset_60.png")), 0, 0));
        playerInimigo.get(1).nome = "Madara";
        madara = Minimax2.virar(madara);
        playerInimigo.get(1).playerImagem = madara;
        playerInimigo.get(1).x = 470;
        playerInimigo.get(1).y = 170;

        ArrayList<PlayerImagem> hashirama = new ArrayList<PlayerImagem>();
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_20.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_21.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_22.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_23.png")), 0, 0));
        hashirama = Minimax2.virar(hashirama);
        playerInimigo.get(2).nome = "Hashirama";
        playerInimigo.get(2).playerImagem = hashirama;
        playerInimigo.get(2).x = 470;
        playerInimigo.get(2).y = 380;

        JFrame frame = new JFrame("RPG");
        frame.setSize(600, 600);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        TelaGame game = new TelaGame(player, playerInimigo);
        game.setVisible(true);
        game.player = player;
        frame.add(game);


        frame.addMouseListener(game);

        player.get(1).ataque = 10;
        player.get(0).vida = 1;
        player.get(1).vida = 2;
        player.get(2).vida = 3;
        playerInimigo.get(0).ataque = 11;

        for (Personagem p : player) {
            p.life.setMaximum(p.vida);
            p.life.setValue(p.vida);
        }
        for (Personagem p : playerInimigo) {
            p.life.setMaximum(p.vida);
            p.life.setValue(p.vida);
        }

        /*
        No no = new No();
        no.player = player;
        no.playerInimigo = playerInimigo;

       

        game.no = no;

        

        player.get(1).ataque = 1;

        /*System.out.println("Valor: " + minimax(no, true, MIN, MAX));

        System.out.println("Gerados: " + tamanho);
        System.out.println("Tamanho: " + no.filho.size());
        for (int i = 0; i < no.filho.size(); i++) {
            System.out.println(i + " | " + no.filho.get(i).valor);
        }*/
    }

    public static int minimax(No no, boolean jogada, int alpha, int beta) throws CloneNotSupportedException {
        if (no.player.size() == 0) {
            if (maximo < -no.altura) {
                maximo = -no.altura;
            }
            //System.out.println(no.altura);
            return no.altura + no.heuristica;
        }
        if (no.playerInimigo.size() == 0) {
            //System.out.println(no.altura);
            return -no.altura + no.heuristica;
        }
        tamanho++;
        if (jogada) {


            for (int i = 0; i < no.playerInimigo.size(); i++) {
                for (int j = 0; j < no.player.size(); j++) {
                    No novoFilho = new No();
                    novoFilho.pai = no;
                    novoFilho.jogada = jogada;
                    no.filho.add(novoFilho);
                    novoFilho.altura = no.altura + 1;
                    novoFilho.selecao.add(no.playerInimigo.get(i).id);
                    novoFilho.selecao.add(no.player.get(j).id);
                    novoFilho.heuristica = no.heuristica;

                    for (int k = 0; k < no.player.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.player.get(k).clone();
                        //novoFilho.heuristica += aux.ataque;
                        //novoFilho.heuristica += aux.vida;
                        novoFilho.player.add(aux);
                    }
                    for (int k = 0; k < no.playerInimigo.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.playerInimigo.get(k).clone();
                        //novoFilho.heuristica += aux.ataque;
                        //novoFilho.heuristica += aux.vida;
                        novoFilho.playerInimigo.add(aux);
                    }
                    //novoFilho.heuristica += novoFilho.playerInimigo.get(i).ataque;
                    //novoFilho.heuristica += novoFilho.playerInimigo.size();
                    novoFilho.player.get(j).vida -= no.playerInimigo.get(i).ataque;
                    if (novoFilho.player.get(j).vida <= 0) {
                        //novoFilho.heuristica -= novoFilho.playerInimigo.get(i).ataque;
                        //novoFilho.heuristica -= novoFilho.playerInimigo.get(j).vida;
                        novoFilho.player.remove(j);

                    }
                    //novoFilho.heuristica = no.player.size();
                    //novoFilho.heuristica += novoFilho.playerInimigo.size();
                    novoFilho.valor = minimax(novoFilho, false, alpha, beta);
                    alpha = Math.max(alpha, novoFilho.valor);

                    // Alpha Beta Pruning
                    if (alpha >= beta) {
                        return alpha;
                    }
                }

            }

            return alpha;
        } else {


            for (int i = 0; i < no.player.size(); i++) {
                for (int j = 0; j < no.playerInimigo.size(); j++) {
                    No novoFilho = new No();
                    novoFilho.pai = no;
                    novoFilho.jogada = jogada;
                    no.filho.add(novoFilho);
                    novoFilho.altura = no.altura + 1;
                    novoFilho.selecao.add(no.player.get(i).id);
                    novoFilho.selecao.add(no.playerInimigo.get(j).id);
                    novoFilho.heuristica = no.heuristica;
                    for (int k = 0; k < no.player.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.player.get(k).clone();
                        //novoFilho.heuristica += aux.ataque;
                        //novoFilho.heuristica += aux.vida;
                        novoFilho.player.add(aux);
                    }
                    for (int k = 0; k < no.playerInimigo.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.playerInimigo.get(k).clone();
                        //novoFilho.heuristica += aux.ataque;
                        //novoFilho.heuristica += aux.vida;
                        novoFilho.playerInimigo.add(aux);
                    }
                   
                    //novoFilho.heuristica += novoFilho.player.get(i).ataque;
                    novoFilho.playerInimigo.get(j).vida -= no.player.get(i).ataque;
                    if (novoFilho.playerInimigo.get(j).vida <= 0) {
                        //novoFilho.heuristica -= novoFilho.player.get(i).ataque;
                        //novoFilho.heuristica -= novoFilho.player.get(j).vida;
                        novoFilho.playerInimigo.remove(j);
                    }
                    //novoFilho.heuristica = no.playerInimigo.size();
                    //novoFilho.heuristica += novoFilho.player.size();
                    //System.out.println(2);
                    novoFilho.valor = minimax(novoFilho, true, alpha, beta);

                    beta = Math.min(beta, novoFilho.valor);

                    if (alpha >= beta) {
                        return beta;
                    }

                }
            }
            return beta;
        }
    }
}
