# Incursion Reader

A tool that analyzes screenshots from Path of Exile and reads the Incursion menu, which has a temple (made up of 13 rooms). These rooms may or may not be connected. There is also a room that is selected for the specific Incursion event, and the player may change that room to one of two options.

## Tool Showcase
![](https://i.imgur.com/NiOwCgp.jpg)
The features that need to be recognized from this image are from the "Temple of Atzoatl" (Incursion) menu in the center of the screen:
  1) What rooms are in the temple? Where are they? (Ex: Pits is the third layer up, second from the right)
  2) What rooms are connected? What rooms are "Opened" (have a path to the Entrance)? (Ex: Workshop is not "opened")
  3) How many Incursions are remaining (1 in this image)
  4) What are the two options for the selected room (Pits is the selected room, it can turn into either Lightning Workshop or Jeweller's Workshop)

These features are stored in a Temple object, which is printed below:
```
             (APX)
             /   \
         (CR2) — ($$2)
         /   \   /   \
     (PS2) —*(hh0)*— (UP3)
     /           \   /   \
 (MM1)   [LF1]   (MN1) — (PP2)
     \               \   /
     (GM1)   (ENT) — (TM2)
    1 Incursions Remaining
      LN1 <-- hh0 --> IR1
```
Rooms use an abbreviation based on their "Theme" (Currency, Weapons, Armour, etc) and their tier (0 to 3). For example, Treasury is the Tier 2 Currency room, so it is displayed as `$$2`. Opened rooms are displayed with `()`, while obstructed rooms use `[]`. The chosen room for the Incursion is highlighted with `* *`. In this image that room is Pits (abbreviated as `hh0`). The rooms it can swap to are shown at the very bottom (going left in the Incursion will swap to a Lightning Workshop (`LN1`)).

## Future Work
The goal is to eventually create a tool to help players optimally build their temples across the 12 Incursions. It also needs more testing on other resolutions.

## Acknowledgements
This uses OpenCV with Pytesseract to perform OCR on image masks.
