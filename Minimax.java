import java.util.ArrayList;
import static java.lang.Math.*;


public class Minimax {
    
    
    public static class No{
        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura = 0;
        Integer alpha = Integer.MIN_VALUE;
        Integer beta = Integer.MAX_VALUE;
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
        int v = 0;
    }
    public static class Personagem implements Cloneable {
        int vida = 1;
        int ataque = 1;
        int level = 1;
        
        @Override
        protected Personagem clone() throws CloneNotSupportedException {
            return (Personagem) super.clone();
        }
    }
    
    
    int tamanho = 0;
    
    public static void main(String[] args) throws CloneNotSupportedException {
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
        
        for (int i = 0; i < 3; i++) {
            Personagem aux = new Personagem();
            playerInimigo.add(aux);
            
        }
        Personagem aux = new Personagem();
            player.add(aux);

        No no = new No();
        no.player = player;
        no.playerInimigo = playerInimigo;

        player.get(0).ataque = 2;
        player.get(0).vida = 4;
        playerInimigo.get(1).vida = 2;
        playerInimigo.get(2).ataque = 3;
        //player.get(1).ataque = 1;
        
        Minimax a = new Minimax();
        
        
        System.out.println("Valor: " + minimax(no, a, true));
        
        
        System.out.println("Gerados: " +  a.tamanho);
        System.out.println("Tamanho: " +  no.filho.size());
        System.out.println("Beta: " +  no.beta);
        System.out.println("Alpha: " +  no.alpha);
        for(int i = 0; i < no.filho.size(); i++){
            System.out.println(i + "  " + no.filho.get(i).v);
        }
        
    }
    
    public static boolean tamanho(ArrayList<Personagem> player){
        int e = 0;
        for(int k = 0; k < player.size(); k++){
            if(player.get(k).vida == 0){
                e += 1;
            }
        }
        if(e == player.size()){
            return true;
        }
        return false;
    }

    public static int minimax(No no, Minimax a, boolean jogada) throws CloneNotSupportedException{
        if(no.player.size() == 0){
            //System.out.println("PlayerInimigo win: " + no.altura);
            return -no.altura;
        }
        if(no.playerInimigo.size() == 0){
            //System.out.println("Player win: " + no.altura);
            return no.altura;
        }
            
        if(jogada){
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
                        novoFilho.altura = no.altura + 1 ;
                        novoFilho.playerInimigo.get(j).vida -= no.player.get(i).ataque;
                        if(novoFilho.playerInimigo.get(j).vida <= 0){
                            novoFilho.playerInimigo.remove(j);
                        }
                        a.tamanho += 1;
                        no.v = Integer.MIN_VALUE;
                        //System.out.println(1);
                        no.v = Math.max(no.v, minimax(novoFilho, a, false));
                        //System.out.println(no.beta);
                            
                        if(no.v >= no.beta){
                            System.out.println("ssssss");
                            return no.v;
                        }
                        no.alpha = Math.max(no.alpha, no.v);
                        
                }
            }
            return no.v;
        }
        else{
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
                            novoFilho.altura = no.altura + 1 ;
                            novoFilho.player.get(j).vida -= no.playerInimigo.get(i).ataque;
                            if(novoFilho.player.get(j).vida <= 0){
                                novoFilho.player.remove(j);
                            }
                            a.tamanho += 1;
                            no.v = Integer.MAX_VALUE;
                            jogada = !jogada;
                            
                            no.v = Math.min(no.v, minimax(novoFilho, a, true));
                            //System.out.println(no.alpha);
                            if(no.v <= no.alpha){
                                System.out.println("ssssss");
                                return no.v;
                            }
                            no.beta = Math.min(no.beta, no.v);
                }
            }
            return no.v;
        }
        
    }
}
