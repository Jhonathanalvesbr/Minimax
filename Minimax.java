import java.util.ArrayList;


public class Minimax {

    public static class No{
        ArrayList<No> filho = new ArrayList<>();
        No pai = null;
        int altura;
        ArrayList<Personagem> playerInimigo;
        ArrayList<Personagem> player;
    }
    public static class Personagem{
        int vida = 3;
        int ataque = 1;
        int level = 1;
    }
    
    public static void main(String[] args) {
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
        
        minimax(no);
        
        System.out.println("Tamanho: " + no.filho.get(0).filho.get(0).filho.get(0).filho.get(0).playerInimigo.size());
       
        
    }
    public static void minimax(No no){
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
                if(no.playerInimigo.get(j).vida == 0){
                    no.playerInimigo.remove(j);
                    j--;
                }
                else{
                    No novoFilho = new No();
                    novoFilho.pai = no;
                    no.filho.add(novoFilho);
                    ArrayList<Personagem> auxPlayerInimigo = new ArrayList<>();
                    for (int k = 0; k < no.player.size(); k++) {
                        Personagem aux = new Personagem();
                        aux.level = 1;
                        aux.ataque = no.player.get(k).ataque * 1;
                        aux.vida = no.player.get(k).vida * 1 ;
                        auxPlayerInimigo.add(aux);
                    }
                    novoFilho.player = auxPlayerInimigo;
                    auxPlayerInimigo = new ArrayList<>();
                    for (int k = 0; k < no.playerInimigo.size(); k++) {
                        Personagem aux = new Personagem();
                        aux.ataque = no.playerInimigo.get(k).ataque * 1;
                        aux.vida = no.playerInimigo.get(k).vida * 1 ;
                        auxPlayerInimigo.add(aux);
                    }
                    novoFilho.playerInimigo = auxPlayerInimigo;
                    
                    novoFilho.altura = (no.altura+1)*1;
                    novoFilho.playerInimigo.get(j).vida -= 1;
                    
                    
                    minimax(novoFilho);
                    
                    j++;
                }
            }
        }
    }
}
