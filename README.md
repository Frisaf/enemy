# Inventory
Relevant files:
- app.py
    - The GUI for the inventory program, made with Tkinter.
- inventory.py
    - File with all the classes and functions used in app.py.

The file program.py was a previous assignment and is not relevant for the inventory assignment.

I'm going to write in Swedish from now on for no apparent reason.

## Vad har jag gjort?
Jag har gjort ett program som hanterar ett inventory för en spelare. Spelaren har HP och "äger" ett inventory samt en hotbar (som egentligen bara är ett mindre inventory) med ett equipped item.

!!!. De två olika typerna av items är Weapons och Consumables, varav båda ärver egenskaper från Itemklassen.

Sedan flyttade jag över programmet till Tkinter för att få ett grafiskt gränssnitt att jobba med.

Tyvärr hann jag inte lägga till så man kan lägga till items i hotbar i Tkinterprogrammet, men det finns funktionalitet för det i inventory.py.

## Vad behöver jag tänka på?
Att skapa ett snyggare gränssnitt hade varit trevligt, men då hade jag behövt mer tid. Klasser har varit mycket intressant att fördjupa sig i, men jag tror jag behöver mycket mer övning innan jag har bemästrat det. Jag tror dock att jag har fattat grundidén samt grundläggande användning av dem.

Jag tror även att det hade varit användbart med att ha hotbar content i sin egen låda, men det hade jag inte tid att fixa. Jag skulle behöva använda grid för det, vilket jag inte hade tid att sätta mig in i.