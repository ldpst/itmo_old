import pokemons.*;
import ru.ifmo.se.pokemon.Battle;

public class PokeLab {
    public static void main(String[] args) {
        Latias latias = new Latias("Latias", 1);
        Palossand palossand = new Palossand("Palossand", 1);
        Pichu pichu = new Pichu("Pichu", 1);
        Pikachu pikachu = new Pikachu("Pikachu", 1);
        Raichu raichu = new Raichu("Raichu", 1);
        Sandygast sandygast = new Sandygast("Sandygast", 1);
        Battle battle = new Battle();
        battle.addAlly(latias);
        battle.addAlly(pichu);
        battle.addAlly(raichu);
        battle.addFoe(palossand);
        battle.addFoe(pikachu);
        battle.addFoe(sandygast);
        battle.go();
    }
}
