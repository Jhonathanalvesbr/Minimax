
import java.util.ArrayList;
import static java.lang.Math.*;

public class Minimax {

    public static class No {

        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura = 0;
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
        int v = 0;
    }

    public static class Personagem implements Cloneable {

        int vida = 1;
        int ataque = 1;
        int level = 1;
        int id = 0;

        @Override
        protected Personagem clone() throws CloneNotSupportedException {
            return (Personagem) super.clone();
        }
    }

    static int tamanho = 0;
    static int MAX = 1000;
    static int MIN = -1000;

    public static void main(String[] args) throws CloneNotSupportedException {
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            Personagem aux = new Personagem();
            aux.id = i;
            playerInimigo.add(aux);
        }

        for (int i = 0; i < 2; i++) {
            Personagem aux = new Personagem();
            aux.id = i;
            player.add(aux);
        }


        No no = new No();
        no.player = player;
        no.playerInimigo = playerInimigo;

        player.get(0).ataque = 3;
        player.get(1).ataque = 1;
        player.get(0).vida = 5;
        playerInimigo.get(1).vida = 4;
        playerInimigo.get(0).ataque = 4;

        //player.get(1).ataque = 1;
        System.out.println("Valor: " + minimax(no, true, MIN, MAX));

        System.out.println("Gerados: " + tamanho);
        System.out.println("Tamanho: " + no.filho.size());
        for (int i = 0; i < no.filho.size(); i++) {
            System.out.println(i + " | " + no.filho.get(i).v);
        }
        /*for (int i = 0; i < no.playerInimigo.size(); i++) {
            System.out.println(i + " <|> " + no.playerInimigo.get(i).id);
        }*/

    }

    public static boolean tamanho(ArrayList<Personagem> player) {
        int e = 0;
        for (int k = 0; k < player.size(); k++) {
            if (player.get(k).vida == 0) {
                e += 1;
            }
        }
        if (e == player.size()) {
            return true;
        }
        return false;
    }

    public static int minimax(No no, boolean jogada, int alpha, int beta) throws CloneNotSupportedException {
        if (no.player.size() == 0) {
            //System.out.println("PlayerInimigo win: " + no.altura);
            return -no.altura;
        }
        if (no.playerInimigo.size() == 0) {
            //System.out.println("Player win: " + no.altura);
            return no.altura;
        }

        if (jogada) {
            int best = Integer.MIN_VALUE;
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
                    novoFilho.v = no.v = Integer.MIN_VALUE;
                    //System.out.println(1);
                    novoFilho.v = no.v = Math.max(no.v, minimax(novoFilho, false, alpha, beta));
                    //System.out.println(no.beta);
                    best = Math.max(no.v, best);
                    beta = Math.min(beta, best);
                    if (beta <= alpha) {
                        //System.out.println(novoFilho.v);
                        break;
                    }
                }
            }
            return best;
        } else {
            int best = Integer.MAX_VALUE;
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
                    novoFilho.v = no.v = Integer.MAX_VALUE;
                    jogada = !jogada;

                    novoFilho.v = no.v = Math.min(no.v, minimax(novoFilho, true, alpha, beta));
                    best = Math.min(no.v, best);
                    //System.out.println(no.alpha);
                    beta = Math.min(beta, best);
                    alpha = Math.max(alpha, best);
                    if (beta <= alpha) {
                        //System.out.println(novoFilho.v);
                        break;
                    }
                }
            }
            return best;
        }

    }
}
