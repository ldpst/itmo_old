package moves.special;

import ru.ifmo.se.pokemon.*;

public class Thunder extends SpecialMove {
    public Thunder() {
        super(Type.ELECTRIC, 110, 70);
    }

    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        def.setCondition(new Effect().chance(0.3).condition(Status.PARALYZE));
        def.setMod(Stat.HP, (int) damage);

    }
}
