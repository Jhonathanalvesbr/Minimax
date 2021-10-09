import java.util.ArrayList;


public class Minimax {
    
    
    public static class No{
        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura = 0;
        ArrayList<Personagem> playerInimigo = new ArrayList<>();
        ArrayList<Personagem> player = new ArrayList<>();
    }
    public static class Personagem implements Cloneable {
        int vida = 3;
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
            aux = new Personagem();
            player.add(aux);
        }
        
        No no = new No();
        no.player = player;
        no.playerInimigo = playerInimigo;
        
        Minimax a = new Minimax();
        
        
        minimax(no,a);
        
        
        System.out.println("Gerados: " +  a.tamanho);
        System.out.println("Tamanho: " +  no.filho.size());
       
        
    }
    
    public static void minimax(No no, Minimax a) throws CloneNotSupportedException{
        if(no.player.size() == 0){
            return;
        }
        if(no.playerInimigo.size() == 0){
            return;
        }
        if(no.altura == 4){
            return;
        }
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
                    novoFilho.playerInimigo.get(j).vida -= 1;
                    a.tamanho += 1;
                    minimax(novoFilho,a);
            }
        }
    }
}
