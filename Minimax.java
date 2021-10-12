
import java.util.ArrayList;
import javax.swing.JPanel;
import java.awt.Graphics2D;
import java.awt.Graphics;
import java.awt.event.MouseListener;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JProgressBar;
import javax.swing.UIManager;

public class Minimax {

    public static class No {

        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura = 0;
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
        int valor = 0;
    }

    public static class Personagem implements Cloneable {

        public ArrayList<PlayerImagem> playerImagem;
        int vida = 2;
        JProgressBar life = new JProgressBar(0,vida);
        int ataque = 1;
        int level = 1;
        int id = 0;
        int indice;
        int time = 150;
        int tempo = 0;
        int x = 0;
        int y = 0;

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
            imagem.get(i).imagem = Minimax.flip(imagem.get(i).imagem);
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

    public static class TelaGame extends JPanel implements MouseListener {
        ArrayList<Personagem> player;
        ArrayList<Personagem> playerInimigo;
        
        ArrayList<Integer> selecao = new ArrayList();
        boolean click = true;

        No no;
        
        public void escolhe(int i){
            if(click){
                selecao.add(i);
                click = !click;
            }
            else{
                selecao.add(i);
                click = !click;
            }
            if(selecao.size() >= 2){
                playerInimigo.get(selecao.get(1)).vida -= player.get(selecao.get(0)).ataque;
                selecao = new ArrayList();
                try {
                    System.out.println("Valor: " + minimax(no, false, Integer.MIN_VALUE, Integer.MAX_VALUE));
                    System.out.println("Gerados: " + tamanho);
                    System.out.println("Tamanho: " + no.filho.size());
                    for (int k = 0; k < no.filho.size(); k++) {
                        System.out.println(k + " | " + no.filho.get(ku).valor);
                    }
                } catch (CloneNotSupportedException ex) {
                    Logger.getLogger(Minimax.class.getName()).log(Level.SEVERE, null, ex);
                }
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

        @Override
        public void paintComponent(Graphics g2) {
            Graphics2D g = (Graphics2D) g2.create();
            g.setColor(Color.BLACK);
            g.fillRect(0, 0, 600, 600);
            g.setStroke(new BasicStroke(3));
            for (int k = 0; k < player.size(); k++) {
                if (player.get(k).vida > 0) {
                    g.drawImage(player.get(k).playerImagem.get(player.get(k).indice).imagem, player.get(k).x, player.get(k).y, null);
                    player.get(k).update();
                    player.get(k).life.setBounds(80, player.get(k).y, 50, 10);
                    this.add(player.get(k).life);
                }
                else{
                    this.remove(player.get(k).life);
                }
            }
            for (int k = 0; k < playerInimigo.size(); k++) {
                if (playerInimigo.get(k).vida > 0) {
                    g.drawImage(playerInimigo.get(k).playerImagem.get(playerInimigo.get(k).indice).imagem, playerInimigo.get(k).x, playerInimigo.get(k).y, null);
                    playerInimigo.get(k).update();
                    playerInimigo.get(k).life.setBounds(450, playerInimigo.get(k).y, 50, 10);
                    this.add(playerInimigo.get(k).life);
                }
                else{
                    this.remove(playerInimigo.get(k).life);
                }
            }

            repaint();
        }

        @Override
        public void mouseClicked(MouseEvent e) {
            //System.out.println(e.getX());
            //System.out.println(e.getY());

            if (e.getX() >= 5 && e.getX() <= 80
                    && e.getY() >= 30 && e.getY() <= 200) {
                escolhe(0);
                System.out.println("Naruto");
            }
            if (e.getX() >= 5 && e.getX() <= 80
                    && e.getY() >= 210 && e.getY() <= 380) {
                escolhe(1);
                System.out.println("Sasuke");
            }
            if (e.getX() >= 5 && e.getX() <= 80
                    && e.getY() >= 390 && e.getY() <= 600) {
                escolhe(2);
                System.out.println("Kakashi");
            }

            if (e.getX() >= 500 && e.getX() <= 600
                    && e.getY() >= 30 && e.getY() <= 200) {
                escolhe(0);
                System.out.println("Nagato");
            }
            if (e.getX() >= 500 && e.getX() <= 600
                    && e.getY() >= 210 && e.getY() <= 380) {
                escolhe(1);
                System.out.println("Madara");
            }
            if (e.getX() >= 500 && e.getX() <= 600
                    && e.getY() >= 390 && e.getY() <= 600) {
                escolhe(2);
                System.out.println("Hashirama");
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
    static Integer MAX = Integer.MAX_VALUE;
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
            player.add(aux);
        }

        ArrayList<PlayerImagem> naruto = new ArrayList<PlayerImagem>();
        naruto.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Naruto\\50_Asset_90.png")), 0, 0));
        naruto.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Naruto\\60_Asset_83.png")), 0, 0));
        player.get(0).playerImagem = naruto;
        ArrayList<PlayerImagem> sasuke = new ArrayList<PlayerImagem>();
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\1_Asset_43.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\43_Asset_40.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\115_Asset_39.png")), 0, 0));
        sasuke.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Sasuke\\139_Asset_41.png")), 0, 0));
        player.get(1).playerImagem = sasuke;
        player.get(1).y = 190;
        ArrayList<PlayerImagem> kakashi = new ArrayList<PlayerImagem>();
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\86_Asset_38.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\96_Asset_33.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\101_Asset_37.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\106_Asset_35.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\111_Asset_34.png")), 0, 0));
        kakashi.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Kakashi\\115_Asset_36.png")), 0, 0));
        player.get(2).playerImagem = kakashi;
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
        nagato = Minimax.virar(nagato);
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

        madara = Minimax.virar(madara);
        playerInimigo.get(1).playerImagem = madara;
        playerInimigo.get(1).x = 470;
        playerInimigo.get(1).y = 170;

        ArrayList<PlayerImagem> hashirama = new ArrayList<PlayerImagem>();
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_20.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_21.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_22.png")), 0, 0));
        hashirama.add(new PlayerImagem((BufferedImage) ImageIO.read(new File(System.getProperty("user.dir") + "\\img\\Hashirama\\Asset_23.png")), 0, 0));
        hashirama = Minimax.virar(hashirama);
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
        UIManager.put("ProgressBar.foreground", Color.green);

        frame.addMouseListener(game);

        No no = new No();
        no.player = player;
        no.playerInimigo = playerInimigo;

        player.get(0).ataque = 3;
        //player.get(1).ataque = 2;
        player.get(0).vida = 5;
        playerInimigo.get(1).vida = 4;
        playerInimigo.get(0).vida = 2;
        playerInimigo.get(1).ataque = 4;
        
        game.no = no;
        
        for (Personagem p : player) {
            p.life.setMaximum(p.vida);
            p.life.setValue(p.vida);
        }
        for (Personagem p : playerInimigo) {
            p.life.setMaximum(p.vida);
            p.life.setValue(p.vida);
        }

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
            return -no.altura;
        }
        if (no.playerInimigo.size() == 0) {
            return no.altura;
        }
        if (jogada) {
            int best = MIN;
            for (int i = 0; i < no.player.size(); i++) {
                for (int j = 0; j < no.playerInimigo.size(); j++) {
                    No novoFilho = new No();
                    novoFilho.pai = no;
                    no.filho.add(novoFilho);
                    for (int k = 0; k < no.player.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.player.get(k).clone();
                        novoFilho.player.add(aux);
                    }
                    for (int k = 0; k < no.playerInimigo.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.playerInimigo.get(k).clone();
                        novoFilho.playerInimigo.add(aux);
                    }
                    novoFilho.altura = no.altura + 1;
                    novoFilho.playerInimigo.get(j).vida -= no.player.get(i).ataque;
                    if (novoFilho.playerInimigo.get(j).vida <= 0) {
                        novoFilho.playerInimigo.remove(j);
                    }
                    tamanho += 1;
                    novoFilho.valor = no.valor = MIN;
                    novoFilho.valor = no.valor = Math.max(no.valor, minimax(novoFilho, false, alpha, beta));
                    best = Math.max(best, novoFilho.valor);
                    alpha = Math.max(alpha, best);
                    if (beta <= alpha) {
                        break;
                    }
                }
            }
            return best;
        } else {
            int best = MAX;
            for (int i = 0; i < no.playerInimigo.size(); i++) {
                for (int j = 0; j < no.player.size(); j++) {
                    No novoFilho = new No();
                    novoFilho.pai = no;
                    no.filho.add(novoFilho);
                    for (int k = 0; k < no.player.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.player.get(k).clone();
                        novoFilho.player.add(aux);
                    }
                    for (int k = 0; k < no.playerInimigo.size(); k++) {
                        Personagem aux = new Personagem();
                        aux = no.playerInimigo.get(k).clone();
                        novoFilho.playerInimigo.add(aux);
                    }
                    novoFilho.altura = no.altura + 1;
                    novoFilho.player.get(j).vida -= no.playerInimigo.get(i).ataque;
                    if (novoFilho.player.get(j).vida <= 0) {
                        novoFilho.player.remove(j);
                    }
                    tamanho += 1;
                    novoFilho.valor = no.valor = MAX;
                    jogada = !jogada;
                    novoFilho.valor = no.valor = Math.min(no.valor, minimax(novoFilho, true, alpha, beta));
                    best = Math.min(best, novoFilho.valor);
                    beta = Math.min(beta, best);
                    if (beta <= alpha) {
                        break;
                    }
                }
            }
            return best;
        }
    }
}
