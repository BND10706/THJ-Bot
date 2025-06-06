# Changelog

## Entry 1210783101270102156
**Author:** Catapultam
**Date:** 2024-02-24T02:59:46.605000+00:00

```
- Hello!
- Fixed the No-XP bug
- Fixed base mana regen
- Fixed crash on interacting with GM
```

---

## Entry 1210879145433628741
**Author:** Catapultam
**Date:** 2024-02-24T09:21:25.318000+00:00

```
- Disabled corpses for now to work around a crash bug
```

---

## Entry 1211454275004141629
**Author:** Catapultam
**Date:** 2024-02-25T23:26:46.893000+00:00

```
- Re-enabled corpses
- Disabled quests from checking corpses for items (lag fix)
- You can now zone out of the Bazaar using a means other than the zone line
   - Expected behavior here is that zone lines take you to the source of your portal. If you don't have one somehow, you'll go to the nexus if you have luclin unlocked or your bind point otherwise.
   - Leaving the zone by any means other than a zone line will clear your saved portal source location
- Corrected zoning into Highpass (New version for now, will work on legacy version again later)
- Implemented Faded Writ quest
- Removed all Fabled mobs from spawn lists
```

---

## Entry 1211944847376777226
**Author:** Catapultam
**Date:** 2024-02-27T07:56:08.461000+00:00

```
- Disciplines should now no longer cause crash on zone
- Implied targeting should be much improved (corpses, procs)
- Pet buffs & heals no longer force change target to pet
```

---

## Entry 1212296544359817266
**Author:** Catapultam
**Date:** 2024-02-28T07:13:39.556000+00:00

```
- Fixed Lavastorm (repatch needed)
- Fixed Patcher weirdness
- Abysmal Sea is accessible
- Added LoY, DoN, OoW, GoD zones to progression lockouts
- Any tag (Latent, Potent, or Awakened) can be used for quest turn-ins
- All AA are instant-cast.
- Fading Memories now uses mana
- Added Phinigel Autropos to Kunark unlock targets
- Attempting to zone to a disallowed zone will drop you in the nexus.
- Fixed Several bugs
- Fixed Neriak waypoint in the wrong location. Cleared all waypoints.
- Fixed pet buffs suspension after zoning
- Fixed detrimental spells suspending
```

---

## Entry 1212457069127401575
**Author:** Catapultam
**Date:** 2024-02-28T17:51:31.643000+00:00

* Pending Reboot
```
- Added 
RULE_INT(Spells, DOTsScaleWithSpellDmgPerTickPercent, 0, "Allow SpellDmg stat to affect DoT spells but by a per tick")
RULE_INT(Spells, HOTsScaleWithHealAmtPerTickPercent, 0, "Allow HealAmt stat to affect HoT spells but by a per tick")
RULE_INT(Spells, PetsScaleWithOwnerPercent, 0, "Allow Pet spells to use the owners stats when casting spells by a percent")
```

---

## Entry 1212500743593001070
**Author:** Catapultam
**Date:** 2024-02-28T20:45:04.447000+00:00

```
(Patch Required)
- Merchantlist filter now properly accounts for your classes
- Levels displayed on spell scrolls is no longer wonky for shared spells
```

---

## Entry 1212579951899836436
**Author:** Catapultam
**Date:** 2024-02-29T01:59:49.179000+00:00

```
- Switching base class should no longer be required for any class combinations
- Please report any problems with spellcasting as high-priority bugs
- Humans and Iksar with Monk in their composition will look like Monks
```

---

## Entry 1212822578775855125
**Author:** Catapultam
**Date:** 2024-02-29T18:03:55.934000+00:00

```
- reverted 'humans look like monk thing' for now
- restored original UI
- custom UI can be loaded with /loadskin thj_ui
```

---

## Entry 1212842973805420665
**Author:** Catapultam
**Date:** 2024-02-29T19:24:58.488000+00:00

```
- Soulbinders will also offer gates to bazaar and bind
```

---

## Entry 1212880650231750686
**Author:** Catapultam
**Date:** 2024-02-29T21:54:41.248000+00:00

```
- Improved merchant filtering (patch needed)
- All activated are now instant-cast (patch + reboot)
- Augments no longer require distillers to remove (reboot)
```

---

## Entry 1212887837637091349
**Author:** Catapultam
**Date:** 2024-02-29T22:23:14.859000+00:00

```
- Added MIT and AVG stats to inventory; These show ACTUAL mitigation and avoidance AC after softcap are taken into account
```

---

## Entry 1212901460459659356
**Author:** Catapultam
**Date:** 2024-02-29T23:17:22.793000+00:00

```
- Tradeskills will always return (Awakened) items.
` Removed (Latent) tag from normal-quality gear. Henceforth 'untagged' tier.
- Renamed (Potent) tag to (Latent)
```

---

## Entry 1212927236416475156
**Author:** Catapultam
**Date:** 2024-03-01T00:59:48.260000+00:00

```
- Added a large number of waypoints in Classic
- Added a large number of waypoints in Kunark
- Adjusted respawn frequency of all mobs
```

---

## Entry 1213018140976357377
**Author:** Catapultam
**Date:** 2024-03-01T07:01:01.596000+00:00

```
- Characters in the Bazaar are exempt from IP box limits
```

---

## Entry 1213344196212031572
**Author:** Catapultam
**Date:** 2024-03-02T04:36:39.222000+00:00

```
- Tradeskills can now be done with any mix of untagged\latent\awakened components```

---

## Entry 1213692673970675772
**Author:** Catapultam
**Date:** 2024-03-03T03:41:22.794000+00:00

```
- Increased the rate at which upgraded versions of items will drop
```

---

## Entry 1213776104800653393
**Author:** Catapultam
**Date:** 2024-03-03T09:12:54.254000+00:00

```
- Augments are now All\All
```

---

## Entry 1213799949716819978
**Author:** Catapultam
**Date:** 2024-03-03T10:47:39.325000+00:00

```
- Added Latent\Awakened bags (next reboot)

- SolB instances are now available.
- Permafrost instances are now available.
- Kedge instances are now available

- Instancing on The Heroes' Journey:
  - Seek out 'A Servant of the Journey' outside, near, or inside raid zones.
  - You will be offered up to two types of instances; Challenge or Opportunity
  - All instances are limited to 6 characters and last 24hours.
  - Challenge instances are available to anyone who have either
     1) Not completed the progression flag associated with this zone
     2) Not exceeded the recommended maximum level for this zone
  - Challenge instances are non-respawning, objective-based tasks, and will reward both 'Accolades of Heroism' and progression flags.
  - If an ineligible person joins a Challenge instance, it will immediately fail.
  - Challenge instances lock immediately upon starting, and have a 20 hour lockout upon completion.
  - Accolades of Heroism will be used to buy equipment in the Bazaar, and will be fully tradable.
  - Opportunity instances have a 20 hour lockout upon request.
  - Opportunity instances are direct copies of the relevant zone, with full repops, etc.
  - Opportunity instances are available to anyone who both meets the level minimum for the instance and has completed the Challenge mode on any character.
```

---

## Entry 1214087621375168573
**Author:** Carolus Rex
**Date:** 2024-03-04T05:50:45.593000+00:00

You should probably change this channel so that not everyone can post here

---

## Entry 1214387592389328927
**Author:** Catapultam
**Date:** 2024-03-05T01:42:44.256000+00:00

```
- Mixed Latent\Awakened\Untagged quest turn ins now REALLY work
- You can no longer zone into DoN or OoW zones
```

---

## Entry 1214760643895238697
**Author:** Catapultam
**Date:** 2024-03-06T02:25:06.666000+00:00

```
- Added /mapfilter to map (Thanks, @Voidless)
- Added click-to-target on map for mobs who you can detect

- Updated patcher to recognize LAA eqgame.exe (may ned to manually download new patcher at https://github.com/The-Heroes-Journey-EQEMU/eqemupatcher/releases/download/1.0.6.49/heroesjourneyeq.exe)
```

---

## Entry 1215002506032320612
**Author:** Catapultam
**Date:** 2024-03-06T18:26:11.093000+00:00

```
- Non-Weapon Instruments that can be equipped in Primary or Secondary can now be equipped in range and ammo slots (Ammo currently does nothing).
```

---

## Entry 1215020038755713165
**Author:** Catapultam
**Date:** 2024-03-06T19:35:51.220000+00:00

```
- Added Pet Discipline to starting AA for Mages, Necromancers, Beastlord, Enchanter, Shaman
- Added Advanced Pet Discipline to starting AA for Mages & Necromancers
- Starting AA are now properly reapplied on zone if you are missing any
```

---

## Entry 1215085856986103918
**Author:** Catapultam
**Date:** 2024-03-06T23:57:23.509000+00:00

```
- Progression flags can be acquired from any version of Naggy\Vox\Phinny```

---

## Entry 1215744114260443226
**Author:** Catapultam
**Date:** 2024-03-08T19:33:04.273000+00:00

```
- Slightly increased base XP rate
- Greatly increased AAXP rate
- Increased modifiers for Red\Yellow
- Decreased modifiers for Blue\LBlue\Green
```

---

## Entry 1215744343210459296
**Author:** Catapultam
**Date:** 2024-03-08T19:33:58.859000+00:00

``` - Deleted this door.```

---

## Entry 1215753990982078604
**Author:** Unbrella
**Date:** 2024-03-08T20:12:19.067000+00:00

This was my favorite door

---

## Entry 1215754000574582916
**Author:** Unbrella
**Date:** 2024-03-08T20:12:21.354000+00:00

RIP

---

## Entry 1216073319342673990
**Author:** Catapultam
**Date:** 2024-03-09T17:21:12.881000+00:00

```
- Delay on debuffs on target applied removed
- Pet spell messages should be working now
- Added pet resist and DoT messages
- Applying a charm spell no longer strips your debuffs
```

---

## Entry 1218026683962101780
**Author:** Catapultam
**Date:** 2024-03-15T02:43:11.298000+00:00

```
- Content DB is now more closely aligned with Retribution
```

---

## Entry 1218033525576433674
**Author:** Catapultam
**Date:** 2024-03-15T03:10:22.466000+00:00

```
- AA cast time is 0 again
- Adventurer's pack increased to 18 slots (will go back to 12 on next server wipe)
```

---

## Entry 1218097434379419658
**Author:** Catapultam
**Date:** 2024-03-15T07:24:19.512000+00:00

```
- Fixed Lavastorm zone lines - you will need to delete lavastorm.eqg from your game directory manually.
```

---

## Entry 1218331890960826460
**Author:** Catapultam
**Date:** 2024-03-15T22:55:58.317000+00:00

```
- Focus Effects should now work
- Monks should be able to DW empty-handed
- Monk epic should now affect base stats of empty hand h2h attacks
- Group Buffs should work on charmed pets
```

---

## Entry 1220215612547141632
**Author:** Catapultam
**Date:** 2024-03-21T03:41:12.541000+00:00

```
- Sympathetic Procs no longer trigger for anything except spell casts (from Gems)
- Sympathetic Procs no longer trigger for bard songs
```

---

## Entry 1222749347314405427
**Author:** Aporia
**Date:** 2024-03-28T03:29:21.984000+00:00

```
Pending reboot

- Emperor SSRA is now a Unique Spawn
- Monk FoS AA is now H2H only
- Bard song cap to correctly mimic Ret
```

---

## Entry 1223294443701014601
**Author:** Catapultam
**Date:** 2024-03-29T15:35:23.090000+00:00

```
- Corrected /who formatting
- Out-of-Range mobs no longer show up as 'Mob' on map.
  - This is to correct the memory leak in the client during long play sessions
- Cast time is now displayed on spell inspect window
```

---

## Entry 1223341400129540257
**Author:** Catapultam
**Date:** 2024-03-29T18:41:58.375000+00:00

* Pending Reboot
```
- Focus effects now work
- Spell Damage\Heal Amount is limited so that it will no more than double the base effect of a spell
- Sympathetic procs are now scaled based off of the cast time and mana cost of the spell which triggered them.
```

---

## Entry 1223653123919184135
**Author:** Catapultam
**Date:** 2024-03-30T15:20:39.118000+00:00

* Forgot to add earlier
```
- Faction checks now use the best modifier amongst your unlocked classes
```

---

## Entry 1223671331258892388
**Author:** Catapultam
**Date:** 2024-03-30T16:33:00.086000+00:00

Pending Reboot\Luck in getting a fresh zs
```
- Buff stacking adjusted
  - Short Buffs (Songs) and Long Buffs no longer have stacking conflicts between categories.
  - Detrimental and Beneficial spells no longer have stacking conflicts between categories.
  - The EFFECTS of the buffs may not stack (mostly between Detrimental and Beneficial), but the buff icons themselves won't block or overwrite. This mostly applies to certain effects like haste\slow.
- Casting skills can only increase from spells cast from spellgems
- Bard Songs will no longer fade just because they ran out of Rune capacity
- Re-introduced Extended Pet Affinity.
  - Now applies to instant-duration (ie heals, cures) as well. Pets need a little bit of love in terms of survivability.
- Instrument modifiers no longer scale effects inappropriately.
```

---

## Entry 1229610384810577930
**Author:** Catapultam
**Date:** 2024-04-16T01:52:40.795000+00:00

```
- THJ is now officially running entirely off of Retribution's database.
- More iteration to come in terms of scripts and content!
```

---

## Entry 1232223984561553438
**Author:** Catapultam
**Date:** 2024-04-23T06:58:11.534000+00:00

PENDING REBOOT

```
Bugfixes:
- Fixed Saryrn and Quarm (GoD and Fabled Naggy) flags
- Ancient Cragbeast Matriarch in Txevu no longer causes client disconnects
- Several misc bugfixes
- Pet bag no longer endlessly upgrades items
- AA are instant-cast again
- All versions of Intricate Wooden Figurine which you are eligible will be awarded.

New Features:
- Bazaar Portal will now return you to the place where you last used it if you use it while inside the Bazaar
- Items may now be Parceled
- Apocrypha in the Bazaar now offers an option to enhance the upgrade rate of all drops in the world for 4 hours. While in effect, this buff will cause any mob you kill to have an additional chance to upgrade each of its drops from normal to Rose Colored or from Rose Colored to Apocryphal.
```

---

## Entry 1232318545015345263
**Author:** Retribution EQ #change-log
**Date:** 2024-04-23T13:13:56.503000+00:00

```
Bugfixes:
- Fixed Saryrn and Quarm (GoD and Fabled Naggy) flags
- Ancient Cragbeast Matriarch in Txevu no longer causes client disconnects
- Several misc bugfixes
- Muzzle of Mardu is no longer usable by players

New Features:
- Bazaar Portal will now return you to the place where you last used it if you use it while inside the Bazaar
- Items may now be Parceled
- Apocrypha in the Bazaar now offers an option to enhance the upgrade rate of all drops in the world for 4 hours. While in effect, this buff will cause any mob you kill to have an additional chance to upgrade each of its drops from normal to Rose Colored or from Rose Colored to Apocryphal. (This is a world-wide buff which affects all players while it is in effect).
```

---

## Entry 1232891641598050344
**Author:** Retribution EQ #change-log
**Date:** 2024-04-25T03:11:13.376000+00:00

```
- AoR for Yxxta has been moved.
- Enchanter pets over level 55 have had their damage increased.
- Necromancer AA Death Bloom is now available at 51... be careful.
- Classic Rogue poisons *actually* have 50 charges now.
- Rathe Council banishes now instance aware.
- Backstab Damage has been completely removed from weapons. This means that backstab will now use weapon damage as backstab damage. (This is a BUFF to backstab damage).
- Monks starting AA changed from Stonewall to Rk I of Techniques of Master Wu
- All pet classes now start with Pet Discipline
- Tendrils of Fire now hits for 450 and has a -450 resist mod
- Vrabbit Xloren is now instance aware when he ports you
- Ranger AA Trickshot Rk I now starts at 5% up from 2% and continues to increase by 2% per rank
- ALL RC and Apoc weapons now have the correct +10% and +20% proc mods they were meant to
- There is now only one Vacto
```

---

## Entry 1234282565913804800
**Author:** Retribution EQ #change-log
**Date:** 2024-04-28T23:18:15.575000+00:00

```
Bazaar NPC overhaul.

Bazaar NPCs have been moved to give the Bazaar a more natural feel.

Check the back stalls for GMs, Spell Vendors, and Tomes.
```

---

## Entry 1234957730041823334
**Author:** Catapultam
**Date:** 2024-04-30T20:01:07.247000+00:00

Deploying beta branch for testing. Have fun. Partial changelog below.

```
* Renamed Latent to 'Enchanted'
* Renamed Awakened to 'Legendary'
* Implemented Dynamic Items;
  - Framework for creating persistent runtime-created items. The ID of these items is not predictable, as they are assigned JIT.  
  - Notable limitations:
    - Dynamic Items may not be sold to NPC vendors (forced to 0-value)
    - Dynamic Items may not be traded to NPCs
    - Dynamic Items may not dropped on the ground
* Implemented Artifacts;
  - Artifacts have a chance to be generated when a player recieves a Legendary item through Loot, Tradeskill, or Quests
  - Artifacts are Dynamic Items.
  - Artifacts are named after the player who found them, and can be discovered once per Season (Non-Season is Season 0)
* Implemented 'Leveling' items in Power Source slot
  - Items placed in Power Source slot block player from gaining XP normally
  - They accumulate XP until they reach a sufficient amount based on their stats, and then upgrade to the next tier (ie Normal->Tier1->Tier2)
```

---

## Entry 1235060114998956103
**Author:** Catapultam
**Date:** 2024-05-01T02:47:57.723000+00:00

```
* Leveling up an item will now produce a Discovery event
* Leveling up an item to Legendary can now produce an Artifact
* Fixed some logic around discoveries and artifacts
```

---

## Entry 1235081630373122109
**Author:** Catapultam
**Date:** 2024-05-01T04:13:27.388000+00:00

```
* Auto-looting items will no longer place items in the Power Source slot. /autoinventory or use of the auto-inventory area of your inventory screen will continue to do so (for now!)
* Added feedback for how much item XP you are gaining.
```

---

## Entry 1235639942298861588
**Author:** Catapultam
**Date:** 2024-05-02T17:11:59.324000+00:00

```
* Fixed feedback for item XP gain
* Adjusted item XP rate
* Combat effects on items can trigger on spell casts
* Spell Damage and Heal Amount is limited to doubling the initial value of a spell
* Fixed discovery message spam
* Reduced spellproc rate for bard songs
* Artifacts should be explicitly droppable
* Fixed artifact discovery from itemxp
* Fixed LoS on combat abilities (@Maze)
* Ranged attacks can proc bows (@Maze)
```

---

## Entry 1235853048107241472
**Author:** Catapultam
**Date:** 2024-05-03T07:18:47.708000+00:00

```
* Re-wrote implied targeting again
* fixed expanded pet affinity killing some pets
* combat procs only trigger on damage or healing spells
```

---

## Entry 1238741761338118144
**Author:** Catapultam
**Date:** 2024-05-11T06:37:30.612000+00:00

```
- Maybe fixed sleeping ogre!
```

---

## Entry 1239283962421968940
**Author:** Retribution EQ #change-log
**Date:** 2024-05-12T18:32:01.424000+00:00

```
- Fixed Gram Dunnar giving Intricate Wooden Figurine
- You should no longer be able to complete the Tome of New Beginnings quest multiple times
- Fixed several Paladin class checks in quests
- Fixed many Monk class checks across quest scripts
- Quarm awards GoD flag if you don't have it already somehow
```

---

## Entry 1239319403347181588
**Author:** Catapultam
**Date:** 2024-05-12T20:52:51.199000+00:00

```
- Artifacts no longer become no-drop if you zone with them equipped
- Augments can no longer be dynamic items (Artifacts)
- Discovery tag on Artifacts now refers to the person who discovered the Legendary variant
- Artifacts of items with charged activated abilities now have unlimited charges, must be equipped to use, and have a cast time of either 5 seconds or the cast time of the actual spell, whichever is greater
```

---

## Entry 1239895622669172778
**Author:** Community Updates
**Date:** 2024-05-14T11:02:32.591000+00:00

##
👀  What's that tag?

Hey Admins and Mods! Starting May 15, it's possible you might notice something new next to some of your members' usernames: ✨ **Guild Tags **✨

See a cute little tag next to a member's username or profile? That's a **Guild Tag**, which indicates someone's membership to a chosen Guild. You can click on this tag to see the Guild profile, and even apply for membership there as well. What this means for you, beloved Admins and Mods, is that if your server's AutoMod is on, it will also check for Guild Tags ☑️ 

**What's a Guild?** It's a small, exclusive server that members can apply to join. These servers are tight-knit communities where members can relish in shared identities, hobbies, play styles, and more! 
> Please note that Guilds are only available to a small number of servers at this time, so not every server has access to this experiment. Additionally, our support team cannot manually add servers to this experiment.

Much love,
The Discord Team

---

## Entry 1241537691439333516
**Author:** Retribution EQ #change-log
**Date:** 2024-05-18T23:47:32.294000+00:00

```
Pending Patch:

Enchanter AA Illusions of Grandeur now gives 200% Crit DoT damage up from 110%
Enchanter AA Illusions of Grandeur now gives 200% Crit Nuke damage down from 250%
Enchanter AA Doppelganger has had it's Rk I and II pets adjusted to match the changes made to Rk III that were somehow reverted.
Enchanter AA Eldritch Rune is now castable on others.
Enchanter Spell Cajoling Whispers can now be found on Illusionist Jerup in the Bazaar

All Disciplines that DO NOT have a hastened AA have had their Cooldowns reduced to 15 minutes.
All AA that DO NOT have a hastened AA have had their Cooldowns reduced to 15 minutes.

Warrior AA Infused by Rage is now an active AA that applies a permanent buff that can be clicked off by the player.

Tearel's Waypoint list is now sorted properly.

```

We are also bringing live Retribution's Wiki ahead of seasonal launch!

A huge thank you to @ashrem2159 and @Shin Noir (Xackery) 

Check out https://retributioneq.com/ for the link!

Please let us know if you think anything should be added/edited.

---

## Entry 1246995837700018248
**Author:** Retribution EQ #change-log
**Date:** 2024-06-03T01:16:15.770000+00:00

```
Pending Patch:

A number of small but effective changes have been made to allow for a more diverse spread in the three man set up for early progression.

Calliav Line available to MAG, NEC, and BST- Mana cost halved. Casting time halved. Cooldown halved.
Magician Sol Ro pet items (Pet Power 5) now effect level 29-49 pets in a more noticeable way.
Magician Planar pet items (Pet Power 10) now effect level 49-60 pets in a more noticeable way.
Necromancer Epic and Encyclopedia Necrotheurgia added Minion of Hate effect now has a more noticeable effect on Emissary of Thule and Invoke Death

ALL MAGE PETS from level 29+ can benefit from Pet Power in a similar way of the custom epic pet does.
Earth pets will have the same HP and AC as the epic pet while the fire pet will match the epic pets damage (matches at each pet power rank while using the appropriate pet). Water and Air will be between both but keep their unique procs/abilities/casts.

This reduces the necessity of completing the mage epic and compensates for pet power draughts.

Velious drop Essence of Nature (Tunare) now has the Summoner's Boon focus (Pet Power 15). This change serves to fill the gap in pet power between Kunark and Luclin for Necromancers and Magicians as both can now be effected by Pet Power 15.

BST Pet Spirit of Omakin has been put on Vocarate Water drop table. 
BST Pet Spirit of Zehkes put on Greater Vocaration Water drop table.
BST Pet Spirit of Khurenz put on Klandicar, Zlandicar, Wuoshi, Velketor, Kelorek, Sontalak, Master of the Guard, Tormax, and Dain 
BST Pet Spirit of Khati Sha stays in Luclin

All of these four pets have had stats adjusted based on Mage/Necro pet power updates.

BST AA Bite of the Asp RK1 now does 25 damage per tick base, but scales 1 damage per level.
BST AA Chameleon Strike RK1 now does 25 base damage, but now has RK2 available at 51 for an increased base damage.

MNK AA Imitate Death now has a base 12minute CD with each rank of Hastened Death removing 2 minutes from the CD, max rank resulting in no CD. It now costs 50 Endurance.

Chloroblast level requirement changed for RNG/BST to 59.

Stacking issues with Warrior AA Infused by Rage fixed.
Blood of Ssra is now a unique spawn and should no longer double spawn sometimes.
Items no longer delete from your cursor when zoning
Urthron's Ultimate Unattuner now works again.

Minotaurs in Steamfont no longer hoard gems.

```

---

## Entry 1247442094872858644
**Author:** Catapultam
**Date:** 2024-06-04T06:49:31.771000+00:00

```
* experimental fix for Artifacts not having persistent ItemIDs
```

---

## Entry 1253065709374930956
**Author:** Retribution EQ #change-log
**Date:** 2024-06-19T19:15:45.950000+00:00

Pending reboot/patch etc.

```
LGuk DZ fixed
Ghoulbane now drops from Shin Lord again
Infused by rage display error fixed (maybe)
Note for Janam quest has been fixed in E/W Freeport
Incorrect item IDs fixed on drop tables for 6th Necro Skullcap quest
Remaining LoY noob quest NPCs removed.
Skyshrine key no longer required to go to CS
Duplicate Chardok agents removed, remaining one fixed.
Zlandicar becomes a dragon again
Chardok, Great Divide, Fungus Grove, and Tenebrous now have Waypoints
Donation Vendor Added (Will accept EoM for goods soon)
Improved Damage I and II are now working again on 20+ broken items.
Enchanter Doppelganger AA works once again, has adjusted stats, and casts a DD according to its level/rank.
Enchanter AA Deep Sleep now has a 20/40/60/80/100% chance to proc based on rank.
Druid spells with AC debuffs now scale with level again

Necromancer and Mage Pet Buff lines have been normalized so that benefits scale throughout all levels and not one big chunk at the end. (Focus Death and Burnout Lines). Melee mitigation, Accuracy, STR, Haste, ATK, AC, Strikethrough now incrementally increase with each rank of the spell- addressing many performance questions at different level brackets.

Mistmoore, LGuk, Unrest, and CoM now have DZs available.
The shared bank will not longer accept plat.

Dire Charm now works on any light blue mobs that CAN be charmed and is no longer hard capped by level.

Veksar now unlocks with Luclin

Necro AA Cascade of Decay can now be up the same time as sympathetic strike buffs.

Fabled Nagafen can now only be reached by hailing the Sage of Anachronism in the Bazaar

```

---

## Entry 1254163331300986880
**Author:** Retribution EQ #change-log
**Date:** 2024-06-22T19:57:19.410000+00:00

Welcome to Season 1!

With all the hype, I forgot to actually post this!

```**Seasonal Characters**

 - New characters created during a Season will be flagged as 'Seasonal'
 - You may opt-out of seasonal play by using the command #disable_seasonal confirm
     - YOU MAY NOT GO BACK TO BEING SEASONAL AFTER OPTING OUT. NO EXCEPTIONS.

 - Seasonal Characters receive the following bonuses:
   - (Season 1 Specific) Start with 'First Orb of Retribution', an augment which will grow in power as you participate in the Season
   - (Season 1 Specific) Start with 'Portable Hole', an upgradable 20-slot bag which you will be able to upgrade as you progress
   - Greatly increased chance to recieve Apocryphal and Rose-Colored drops
   - Certain other rewards for defeating progression challenges!

 - Seasonal Characters may NOT...
   - Group with non-Seasonal characters
   - Trade with non-Seasonal characters
   - Buy from non-Seasonal traders
   - Buy ANYTHING from NPC vendors which was sold by players
   - Pick up items off the ground that were placed by players
   - Cast spells on non-Seasonal characters.
   - Be cast upon by non-Seasonal characters
   - Loot kills that they did not receive XP for
   - Enter DZs with non-Seasonal characters
   - Use the Bazaar Buff-bot for standard buffs
   - May not have more than 6 players in a DZ

* General Changes
 - Everything previously mentioned in the changelog that didn't actually go live due to technical issues.
 - NPCs, except for player Pets, no longer keep items handed by players, they are immediately destroyed.
 - Charmed Pets will hand the item back, while also equipping a copy. The equipped copy is destroyed when the charm breaks.
 - Agents of Retribution renamed to Echo of the Past and will now offer two types of instances; Respawning and non-Respawning
  - Each instance type is on a different replay timer
 - Dire Charm now works on any mob up to light blue to the caster.

* Bug Fixes
 - The Polymorphist now works correctly again!
 - The Purveyor of Glamour now works correctly again!

* Donation Rewards (Echo of Memory)
 - Merchant added in the Bazaar which sells items for Echo of Memory alt currency.
  - This alt currency is awarded to players as a 'Thank You' for donations to server costs
 - 20, 30, 40 slot, No Drop bags now available on this merchant in 10 different colors
 - Unattuners added to this merchant
 - No stat Illusion clickies added to this merchant
 - Anything purchased from this merchant may be sold back to them for a small loss```

---

## Entry 1254511871969726614
**Author:** Retribution EQ #change-log
**Date:** 2024-06-23T19:02:17.981000+00:00

```
6-23-24

Vah Shir, Iksar, Beastlords and Berserkers are now available for ALL players regardless of expansion unlock.
Progress with who you want!

Rogue Epic no longer completable in Classic. Congratulations on the feat and thank you for being so agreeable Pointz the Assassin! His Epic will be returned to him as soon as Kunark launches.

SK 51 AA was pointing to the wrong spell file. It was doing too much up front mana regen and was missing its recourse. Fixed on next patch.
```

---

## Entry 1255012117665550440
**Author:** Catapultam
**Date:** 2024-06-25T04:10:05.849000+00:00

```
- Implemented Implied Targeting for pet attack command
```

---

## Entry 1255515686550114346
**Author:** Retribution EQ #change-log
**Date:** 2024-06-26T13:31:06.027000+00:00

`
- BST Now correctly get Feral Swipe before Frenzied Swipes as their seasonal AA
- Pending reboot, Drelzna now has a chance to drop Jboots
- Najena getting DZ to accommodate JBoot fanbois
`

---

## Entry 1255917133528039464
**Author:** Retribution EQ #change-log
**Date:** 2024-06-27T16:06:18.445000+00:00

Pending Reboot:
`
- Hate 2.0 items are being scaled down to ensure future content isn't completely negated. Most will still be/be close to BiS for Classic. Thank you for your understanding.
- Manastone now has a 1 second cast time but has 10x the effectiveness. Please update your scripts accordingly.
- Consumable requirement removed from Enchanter runes. Casting times have been reduced.
- King-me channel caught up
- Misc quest and bug fixes (see bug/suggestion forum for details)
- Daily DZ/Lockout timers reduced to allow people with a static play schedule to have access at the beginning of their play session each day.
- SHM/BST healing spell, Spirit Salve, now available in bazaar.
- RNG spell, Falcon Eye, now available in bazaar.
`

---

## Entry 1257195892344225883
**Author:** Retribution EQ #change-log
**Date:** 2024-07-01T04:47:38.305000+00:00

Upcoming Changes Pending Patch/Reboot:

```
- Apoc Six Note Blade now WAI
- Cazic 2.0 loot brought into line with Classic expectations.
- Marsinger's Gem quest items brought into line with Classic expectations (this is a large change as it was late Luclin quality).
- Dyllin Starsine's quest drops increased.
- All Bard Instruments can now be equipped in the Range slot.
- Monk Sky Weapon Requisite, Brass Knuckles, now drop from Noble and Hand
- BST AA Frenzied Swipes now correctly lowers the CD of Feral Swipe to 3 seconds for 30 seconds.
- Disarm now moves the enemies equipment directly into inventory
- Luclin and PoP Necromancer pet power combinations have been updated based on enhanced classic stats
- Echo added INSIDE fear next to glyph circle.
- Nedaria's Landing should not be accessible until GoD.
- Rune spell cost brought in line to heal cost.
- Bards can once again use clickies while moving
- Fear, Mez, Charm, Silence, and Root will now check a players resist EVERY tick as intended
- Progression NPCs (Faded Memories) now look correct.
- Tykar Renlin works correctly again.

```
Quick note:

When something is found that is out of era that directly impacts player power, please report it. Assume any OoE item will be brought into line with expectations for availability in whatever expansion it becomes available here. We appreciate your support and understanding as we continue to make Retribution the best it can be.

Thank you!

---

## Entry 1258140468093517824
**Author:** Retribution EQ #change-log
**Date:** 2024-07-03T19:21:02.713000+00:00

Pending Patch/Reboot

```
- Spirit Salve no longer requires line of sight to cast.
- WP added to Everfrost near Permafrost.
- Bixie Sword Blade now correctly drops from Bazzt Zzzt
- PoSky quest "Test of Body" now rewards the correct item
- Stein of Moggok changed back to it's original form. Apoc version maintains its sympathetic proc
- Eejag no longer spawns within invisible walls
- Rogue AA Mrylokar's Rigor now procs 25% of the time, up from 2.5%
- Echo of the Past removed from Feerrott. The Echo inside Fear by the WP now works correctly.
- Verina Tomb respawn timer lowered to 4 hours with a 30 minute variance
- Vessel Drozlin respawn timer lowered to 4 hours with a 30 minute variance
- The Tangrin, and Oracle of K`arnon respawn timer lowered to 4 hours with a 30 minute variance
- Keeper of Souls no longer double spawns
- Increased Enchanter AA Phantasmic Reflexes chance to proc (may be adjusted again)
- WP Added to TD
- Echo of the Past added to TD
- Echo of the Past added to FM
- WP Added to FM
- Beastlords can now purchase Group Shrink AA
```

---

## Entry 1258612926680531044
**Author:** Catapultam
**Date:** 2024-07-05T02:38:25.618000+00:00

```
- Removed 'Expanded Pet Affinity' (for now, might do something with this concept later)
```

---

## Entry 1259187477865037886
**Author:** Retribution EQ #change-log
**Date:** 2024-07-06T16:41:29.295000+00:00

Rebooting to bring live pending changes as well as:
```
- Enchanters gain access to Bite of Tashani AA
- Sky weapon efreeti standard is now magic
- Summon Companion AA now available to Druids
- Sky quest rewards that were later swapped for better versions have now been swapped for their better versions.
- Inny no longer depops.
- Berserker AA Untamed Rage now correctly adds haste instead of subtracts.
- Several misc bugs/suggestions/king-mes completed.
- Magician Fire/Stone/Ice/Vapor Core AA cooldown reduced to 15min
- Charges on Staff of Forbidden Rites have been normalized and no longer scale with quality (Each version now has 50).
- Charm crashing zones *should* be fixed.
```
Thank you all for being here! Server buffs going out for unexpected reboots.

---

## Entry 1259987424134565927
**Author:** Retribution EQ #change-log
**Date:** 2024-07-08T21:40:11.348000+00:00

[Original Message Deleted]

---

## Entry 1260042653442117735
**Author:** Retribution EQ #change-log
**Date:** 2024-07-09T01:19:39.041000+00:00

On next patch:
```
- Echo of the Past added to The Howling Stones
- Zerker AA Decap has had its damage reduced
- Echo of the Past added to ChardokB
- Echo of the Past added to Veksar
- VP 2.0, ChardokB, and Veksar have had their items scaled down in anticipation of Kunark launch. VP 2.0 was done with the intent that end game Velious gear (NToV) outpaces it in most scenarios.
```
For those of you new to the server,  balance changes are ongoing, both buffs and nerfs will happen to outliers. I try to lean toward buffs for others instead of nerfs for the one- but outliers have to be handled.

---

## Entry 1260056954194366534
**Author:** Retribution EQ #change-log
**Date:** 2024-07-09T02:16:28.606000+00:00

```
- You will now recieve a notification when Echo of Luck or Seasonal status upgrades a quest reward.
- You will now recieve an upgrade when Seasonal status upgrades a loot reward.
- Really fixed Staff of Forbidden Rites charges.
```

---

## Entry 1260793044303613973
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T03:01:26.164000+00:00

```
- Pet taunt will now enable them to peel off of players.
- Pets will now taunt any mob attacking their owner during their taunt cycle, even if that is not the mob they are currently attacking.
```

---

## Entry 1260793093314183179
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T03:01:37.849000+00:00

```
- Sage of Anachronism can now expand your hole(s)
- Sage of Anachronism will replace lost First Orb of Retribution
```

---

## Entry 1260793098468986932
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T03:01:39.078000+00:00

```
- 'Unlocking' (Even if still time-locked) Velious now allows bypass of key requirement for Veeshan's Peak.
- 'Unlocking' (Even if still time-locked) Planes of Power now allows bypass of key requirement for Vex Thal.
```

---

## Entry 1260840422658277490
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T06:09:42.044000+00:00

```
- Temporary pet combat messages should now be visible.
- Pet names for temporary pets, familiars, etc are a bit more descriptive
```

---

## Entry 1260963856692285571
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T14:20:11.011000+00:00

```
- Mobs will no longer respawn at 22hr in Non-Respawning instances (to coincide with increased dz lifetimes)
```

---

## Entry 1260981600993284190
**Author:** Retribution EQ #change-log
**Date:** 2024-07-11T15:30:41.582000+00:00

Pending Patch/Reboot:

```
Beacon of Loathing now correctly has an RC and Apoc counterpart.
Ranger AA Ranged Finesse no longer displays incorrectly.
Cleric AA Celestial Regeneration now stacks with their regular HoT lines.
Zerker AA Cascading Rage no longer slows you and correctly gives haste instead.
Echo of Luck and Echo of Focus can no longer be dispelled.
Rogue AA Seized Opportunity is now auto-granted at level 1 with maximum effectiveness.
Rogue AA Virulent Venom has had its first and second-rank costs reduced.
Rogues can now purchase an upgraded version of the Strikethrough AA.
Rogue AA Massive Strike base damage increased from 30 to 35.
Rogue AA Massive Strike Rk II is now available.
Monks now start with RK I of Killing Spree like all other pure melee.
Ranger AA Precision of the Pathfinder now affects Archery accuracy but at a reduced rate.
Gift of Mana now correctly shows its effect from level 30-70 spells.

```

**Kunark Launch time changed to 7PM EST, 6PM CST,  due to RL conflicts.** Spread the word.

---

## Entry 1261218240906919977
**Author:** Retribution EQ #change-log
**Date:** 2024-07-12T07:11:00.934000+00:00

Extra stuff for Kunark
```
- Replaced the level 51 Mage Seasonal AA.
- Replaced Companion of Necessity with Dimensional Armory. Summons a 10-slot, Lore, No-Drop, (Not Temporary) 100% WR container. Any items placed inside this container will be automatically equipped by your summoned pets.
- Pets will now properly proc augments and display ornaments.
- (Summoned) Pet base damage is now influenced by the weapons they are wielding.

- Some auto-granted AA had their costs removed. This may cause your total AA spend count to go down. Expect to see more of this in the future.
```

---

## Entry 1261435868669808662
**Author:** Retribution EQ #change-log
**Date:** 2024-07-12T21:35:47.436000+00:00

```
- Removed the cost of most starting AA
- Added Group Shrink to Beastlord auto-grant AA
- All classes with pets now get auto-grant Summon Companion
- All classes with pets or charm now get auto-grant Pet Affinity
- Mage 'Companion's Fury' auto-grant replaced with 'Elemental Fury'
- Lay on Hands is now auto-granted as it becomes available through level 50
- Harm Touch is now auto-granted as it becomes available through level 50
- Archery Mastery is now auto-granted as it becomes available through level 50
```

---

## Entry 1261703391629938810
**Author:** Retribution EQ #change-log
**Date:** 2024-07-13T15:18:49.880000+00:00

Pending Reboot:
```
All Beastlord's now have their own racial pets again. Pets added:

Human - Puma
Froglok - Fungusman
Dark Elf - Black Widow
Gnome - Junkbeast
Dwarf - Green Goblin
Halfling - Bixie
High Elf - Fairy
Erudite - Kobold
Half Elf - Giant Bat
Wood Elf - Wasp

Worlace now offers key Poison Making ingredients and has been joined by his cohorts Chryssa and Dolley. Rogues- yes you shoud be making poisons.

Many Misc Bug Fixes
```

---

## Entry 1262158250791534674
**Author:** Retribution EQ #change-log
**Date:** 2024-07-14T21:26:16.755000+00:00

Pending Patch/Reboot

```
Mage Epic pet now summons at lvl 58, up from 52.
Mage Water/Fire/Air/Earth pet (lvl 60 cast) with PP 10 now summons at level 58, down from 60.
Veksar ZEM increased to 2.0
All splitpaw respawn times have been corrected down to 10.5 minute spawns.
King-me cleaned up
Misc Upstream Bug fixes from upgrading to new binaries
MANY random crash fixes

/bazaar now functions! (Parceling does not yet work).
```

---

## Entry 1262263403842633804
**Author:** Retribution EQ #change-log
**Date:** 2024-07-15T04:24:07.196000+00:00

```
* GlobalLoad updated (requires client patch)
* New Beastlord Warders
 * Human - Puma
 * Erudite - Kobold
 * Wood Elf - Green Drake
 * High Elf - Blue Drake
 * Dark Elf - Black Drake
 * Half Elf - Red Drake
 * Dwarf - Goblin
 * Halfling - Snake
 * Gnome - Junk Beast
 * Froglok - Sporali
 * Drakkin - Gold Drake
* Disabled mob summoning players who are already in melee range
```

---

## Entry 1262519984828055644
**Author:** Retribution EQ #change-log
**Date:** 2024-07-15T21:23:40.870000+00:00

Working through these right now, post in the related suggestion thread if you have any in particular you want to get hit. (https://discord.com/channels/1019251428637814874/1242512903136083968)
```
* The following spells have separated illusion and benefit components.
- Elemental Form: Air
- Elemental Form: Water
- Elemental Form: Fire
- Elemental Form: Earth
- Form of the Bear
- Form of the Great Bear
- Boon of the Garou
- Trickster's Augmentation
- Wolf Form
- Greater Wolf Form
- Share Wolf Form
- Form of the Great Wolf
- Share Form of the Great Wolf
- Form of the Howler
- Form of the Hunter
- Feral Form
- Spirit of the Black Wolf
- Spirit of the White Wolf
- Visage of the Dark Arachnid

* Added Vial of Prismatic Dye to possible rewards from 'A Mischievous Halfling'.
* Tradeskilled Poisons now stack to 100
* Tradeskilled Poisons with more than one 'hit charge' now have unlimited 'hit charges'
* Frenzied Burnout rank 2->6 are now available at level 51
```

---

## Entry 1262638983905804308
**Author:** Retribution EQ #change-log
**Date:** 2024-07-16T05:16:32.461000+00:00

```
Pending Patch:
Rage of Rallos Zek AA - Endurance Cost Reduced by 1/4

Key requirements in Seb have been removed
```

---

## Entry 1262772314844565504
**Author:** Retribution EQ #change-log
**Date:** 2024-07-16T14:06:21.034000+00:00

(Next Reboot)
```
- Heroic Charisma is now applied as a direct resist adjustment to spells. (ie; 67 HCha is -67 additional resist check to all spells)
- Improved mob pathfinding
```

---

## Entry 1262828889718390885
**Author:** Retribution EQ #change-log
**Date:** 2024-07-16T17:51:09.535000+00:00

Immediate Effect:
```
- Parcels are now available.
- Various merchants associated with the League of Antonican Bards can send\recieve Parcels
- Mysterious Mailman added to Bazaar
- Bazaar purchases via Parcel are now enabled
```

---

## Entry 1262942533567250433
**Author:** Retribution EQ #change-log
**Date:** 2024-07-17T01:22:44.340000+00:00

[Original Message Deleted]

---

## Entry 1263204566200221839
**Author:** Retribution EQ #change-log
**Date:** 2024-07-17T18:43:57.788000+00:00

```
Pending Reboot:

- Help Baelin quest fixed.
- Battle Master Ska`tu loot tables fixed.
- Shaman Cudgel quest 6 fixed.
- Howling Stone final key fixed.
- Silver Wand and silvered guard fixed.
- Eejag now spawns where that impudent sprite is.
- Rage of Zomm and Dyzil's Deafening Decoy work once again.
- SK Viscious Bite of Chaos recourse now stacks with Lich instead of overwrites.
- Priest of Najena now correctly always drops Tarnished Bronze Key
- The Undertake Lord once again has a name.
- The Skeletal Sepulcher once again has a name.
- Spell: Invigor has been removed from all merchants.
- Ragebringer proc has had it's radius reduced.
- Robe of Living Fungus now has HP Regen again.
- The following rogue abilities may now be used in combat:

Rogue Abilities Sneak Attack (20)
Thief's Vengeance (52)
Assassin's Strike (63)
Kyv Strike (65)
Ancient Chaos Strike (65)
Daggerfall (69) 
Razorarc (70)

```

---

## Entry 1263233303608164353
**Author:** Retribution EQ #change-log
**Date:** 2024-07-17T20:38:09.320000+00:00

Still pending reboot:
```- 'Must Equip' items can be cast from inventory if they are attuned

- Sympathetic Strike of Flames replaced with Sympathetic Strike
- All Sympathetic 'Strike-like' abilities replaced with Sympathetic Strike
  - Prismatic Resist (average resist of target)
  - Partial resists enabled
  - 16h duration, undispellable
  - Triggers on EVERY cast (same as healing), stacks with all similar abilities, such as the Pyromancy AA from wizards

- Sympathetic Healing Burst replaced with Sympathetic Healing
 - 16h duration, undispellable


- Ground spawns are now present in non-respawning DZ
- Swarm pets will aggro everything that has their owner on its hate list
- Certain quests which check for the presence of an item in your inventory will work correctly with RC\Apoc items```

---

## Entry 1263354038532182178
**Author:** Retribution EQ #change-log
**Date:** 2024-07-18T04:37:54.769000+00:00

```
AA Exp Scaling has been enabled for the first 300AA.

This means there is a 200% AA exp bonus for your first AA that scales down as you approach 300. At 300 AA, this bonus goes away.

This change is meant to aid: players catching up, alts, and classes that take higher AA investments to come into their own.

This bonus stacks with the server wide EXP bonus.
```
Edit: Temporarily Reverted.

Necromancer AA Soul Seeker CD reduction reduced to 2 minutes per rank. Leaving max rank LB at 5 minutes. Please do not pretend you though LB was supposed to have no CD. Thanks.

---

## Entry 1263523992602546348
**Author:** Retribution EQ #change-log
**Date:** 2024-07-18T15:53:14.977000+00:00

Pending Reboot:
```
* Fixed and re-enabled AAXP Scaling based on total earned AA
* Symp proc durations reduced to 16h from Permanent
```

---

## Entry 1263595829432946698
**Author:** Retribution EQ #change-log
**Date:** 2024-07-18T20:38:42.212000+00:00

[Original Message Deleted]

---

## Entry 1263652317794930688
**Author:** Retribution EQ #change-log
**Date:** 2024-07-19T00:23:10.087000+00:00

Consolidated Changelog:

```
- Help Baelin quest fixed.
- Battle Master Ska`tu loot tables fixed.
- Shaman Cudgel quest 6 fixed.
- Howling Stone final key fixed.
- Silver Wand and silvered guard fixed.
- Eejag now spawns where that impudent sprite is.
- Rage of Zomm and Dyzil's Deafening Decoy work once again.
- SK Viscious Bite of Chaos recourse now stacks with Lich instead of overwrites.
- Priest of Najena now correctly always drops Tarnished Bronze Key
- The Undertake Lord once again has a name.
- The Skeletal Sepulcher once again has a name.
- Spell: Invigor has been removed from all merchants.
- Ragebringer proc has had it's radius reduced.
- Robe of Living Fungus now has HP Regen again.
- The following rogue abilities may now be used in combat:
    Rogue Abilities Sneak Attack (20)
    Thief's Vengeance (52)
    Assassin's Strike (63)
    Kyv Strike (65)
    Ancient Chaos Strike (65)
    Daggerfall (69) 
    Razorarc (70)

- 'Must Equip' items can be cast from inventory if they are attuned

- Sympathetic Strike of Flames replaced with Sympathetic Strike
- All Sympathetic 'Strike-like' abilities replaced with Sympathetic Strike
  - Prismatic Resist (average resist of target)
  - Partial resists enabled
  - 16h duration, undispellable
  - Triggers on EVERY cast (same as healing), stacks with all similar abilities, such as the Pyromancy AA from wizards

- Sympathetic Healing Burst replaced with Sympathetic Healing
 - 16h duration, undispellable

- Ground spawns are now present in non-respawning DZ
- Swarm pets will aggro everything that has their owner on its hate list
- Certain quests which check for the presence of an item in your inventory will work correctly with RC\Apoc items

- Inventory data is now sent in the seconds following a zone transition, instead of during the zone. This is intended to mitigate crash-on-zone issues.
IF YOU ENTER A ZONE AND HAVE AN EMPTY INVENTORY, ZONE BACK OUT IMMEDIATELY AND REPORT IT AS A BUG BY TAGGING A GM. Your items are safe as long as you don't manipulate your inventory while it is empty.


AA Exp Scaling has been enabled for the first 300AA.
This means there is a 200% AA exp bonus for your first AA that scales down as you approach 300. At 300 AA, this bonus goes away.
This change is meant to aid: players catching up, alts, and classes that take higher AA investments to come into their own.
This bonus stacks with the server wide EXP bonus.
```

---

## Entry 1263752537756930080
**Author:** Retribution EQ #change-log
**Date:** 2024-07-19T07:01:24.388000+00:00

Pending Next Reboot\Patch
```
- Echo of Luck now guarantees Apocryphal rewards for quests
- Sympathetic Proc buffs now actually 16hr duration
- Sympathetic Procs can trigger even if the spell cannot apply to a mob (ie, Symp Heal can proc even if the buff was blocked)
- ST_SummonedPet handled correctly be implied targeting.
- Bards are no longer compelled to sing forever.
```

---

## Entry 1263912204261134387
**Author:** Retribution EQ #change-log
**Date:** 2024-07-19T17:35:51.849000+00:00

Immediate Effect:
```
- Low-AA bonus increased to 400%. At 0AA, you will recieve a 4x bonus to AAXP, decreasing linearly until a total of 300AA have been earned
```

---

## Entry 1264297691672743948
**Author:** Retribution EQ #change-log
**Date:** 2024-07-20T19:07:39.210000+00:00

```
- Actually, for sure, definitely, REALLY fixed Eejag this time
- Phara Dar's adds should now aggro correctly.
```

---

## Entry 1264518059532750898
**Author:** Retribution EQ #change-log
**Date:** 2024-07-21T09:43:19.002000+00:00

Rolling Next Update Changelog...
```
- Echo of Luck now guarantees Apocryphal rewards for quests
- Sympathetic Proc buffs now actually 16hr duration
- Sympathetic Procs can trigger even if the spell cannot apply to a mob (ie, Symp Heal can proc even if the buff was blocked)
- ST_SummonedPet handled correctly be implied targeting. (Petamorph wands)
- Bards are no longer compelled to sing forever.
- Fixed Berserkers not hitting more than 1x with Frenzy
- Fixed Froglok Beastlord warders.
- Familiar spells will no longer dismiss other types of pets when they fade.
- Ikaav's Venom now has a spell icon.

# Augmentation Overhaul #
- Augment Slots standardized across all items, into the following types;
   - Type 1 (Stats): All equippable items have at least one of these slots. Augs with only stats will fit into these slots.
   - Type 2 (Worn): Equippable items without a focus or worn effect will have one of these slots. Augs wih a Focus or Worn effect, along with Type 1 augs, will fit in these slots.
   - Type 3 (Spells): Currently unused.
   - Type 4 (Procs): All Weapons have at least one of these slots. Augs with Procs, Damage, Bane Damage, Elemental Damage, or Type 3 augments will fit in these slots.
   - Type 20 (Ornament): All PRI\SEC\RANGE items will have one of these slots for statless ornaments.
   - Type 21 (Ornament): All Visible Slot equipment will have these slots (Currently unused).
   - Two-Handed weapons have an additional Type 1 and Type 4 slot compared to 1-handed items.

- This should provide additional coherence to augment itemization, remove the relatively meaningless type 7\8 split, allow for items without foci\worn effects to be a little more valuable, and provide a much-needed boost to two-handed weapons.
- Any augments in slots which are no longer valid will be ejected from items when this gets deployed, and will need to be reinserted.

** THJ ONLY**
- (THJ) AA can be activated while casting
- (THJ) Items can be augmented even if it would result in an item that you can no longer use
- (THJ) Fixed Archery procs.
- (THJ) Fixed Reyfin Malakwa for Multiclass characters
- (THJ) Items upgraded to Legendary via Power Source now correctly show as attuned.
- (THJ) Legendary items may no longer be equipped in Power Source, and Enchanted->Legendary upgrades will eject the item from the Power Source instead of infinitely soaking XP
** THJ ONLY**
```

---

## Entry 1264807693298962432
**Author:** Retribution EQ #change-log
**Date:** 2024-07-22T04:54:13.073000+00:00

```
Pending Patch:

All World Buffs now correctly count down when in Bazaar.
Holy Elixir once again stacks with other HoTs
```

---

## Entry 1268576992429605067
**Author:** Catapultam
**Date:** 2024-08-01T14:32:04.016000+00:00

Retribution EQ #change-log

---

## Entry 1268577273339056153
**Author:** Retribution EQ #change-log
**Date:** 2024-08-01T14:33:10.990000+00:00

[Original Message Deleted]

---

## Entry 1268578766473527470
**Author:** Catapultam
**Date:** 2024-08-01T14:39:06.981000+00:00

```
* Added Multiple Pet functionality
 - First pet Summoned or Charmed is 'Primary Pet' and is controlled via Pet Window
 - Subsequent pets may be Summoned as Secondary Pets
   - Up to 2 Secondary pets may be Summoned
   - Charmed pets may not be Secondary Pets
   - Secondary Pets do not get their own pet control windows, but will obey the following commands
     - /pet attack
     - /pet back off
     - /pet hold
     - /pet ghold
   - Beneficial spells affecting the Primary Pet will mirrored on any Secondary Pets
   - Secondary Pets Cannot:
    - Utilize a pet bag
    - Zone with their owner 
 - Only one Pet per class may be summoned. (ie, a SHM/NEC/WAR may summon a Shaman spirit and a Necromancer pet, but not two Necromancer Pets)
```

---

## Entry 1268648098918567937
**Author:** Retribution EQ #change-log
**Date:** 2024-08-01T19:14:37.124000+00:00

```
Pending Patch/Reboot
- BST pets Zehkes, Khurenz, and Khati Sha have had their levels and HP adjusted
- BRD Epic can now be equipped in the range slot
- Echo of Memory added to Plane of Mischief ahead of Velious launch
- More Gods now give The God Slayer title.
```

---

## Entry 1269065307331493943
**Author:** Retribution EQ #change-log
**Date:** 2024-08-02T22:52:27.361000+00:00

**Adventurers**, *the time has come to brace yourselves for the icy challenges that lie ahead! The mystic land of Velious, long shrouded in legend and mystery, now calls to the bravest of Norrath's heroes.

Velious, the frozen continent, is a land of ancient secrets and formidable foes. Here, the towering ice-bound peaks and treacherous glaciers conceal forgotten dungeons, majestic dragon lairs, and the remnants of the great Coldain dwarves. The legendary giants of Kael Drakkel, the enigmatic dragons of the Temple of Veeshan, and the resilient Coldain dwarves await those bold enough to explore this frigid frontier.

Prepare your weapons, gather your allies, and steel your hearts against the biting cold. The journey through Velious will test your strength, courage, and resolve like never before. Will you rise to the challenge and uncover the hidden treasures and untold stories of this icy realm? The fate of Velious lies in your hands!

Welcome to Velious, where glory and peril are but a heartbeat away. Step forth, and let the adventure begin!*

**Patch Notes:**
```
When the server comes back up, all pending changes will come live, and addition to:

- Pets will now move behind mobs when not tanking
- Adjusted pet follow behavior
- Spells against Pets will now use their owner's resists in addition to their own
- Removed door to Plane of Mischief in Great Divide
- Manifest Elements is no longer granted as part of Mage Epic quest, and is removed from spellbooks
- Dire Charm now calculates 'light blue' correctly.
- Bard Song, Jonthan's Inspiration now has a self only proc component.
- Our beloved magic map is back with new functionality coming soon!
- LoY now releasing with Velious... 
```

A HUGE thank you to all our donators, contributors, and active community members! We are having a blast and love that you are too!

We prepared a special treat for you... **LoY launches with Velious launch today!**

Additionally, as we continue to grow, we have decided to normalize non emergency downtime to Tuesdays. So that everyone can better plan 👍 

Thanks to your contributions, this Tuesday we will be migrating to new hardware in a more centralized location! 

Every week, Retribution gets better, thank you for being here!

Have fun tonight!

---

## Entry 1269450676338167808
**Author:** Retribution EQ #change-log
**Date:** 2024-08-04T00:23:46.492000+00:00

08/03/2024
Immediate or Immediate-ish (new zone servers)
```
* Characters who are AFK\Idle for more than 10 minutes in the Bazaar and not Traders will be phased into a private instance. They will return to the public instance once they are no longer idle.
* Improved Implied Targeting
* Improved Bard spellbar refresh handling (maybe not perfect still)
* Aggressively unlock spellbar for classes other than Bard (Working on action-lock bug)
* First Orb of Retribution now has extra scaling based on progression stages unlocked.
* Pets use Ornaments again
* The Polymorphist will now help you become a Drakkin
* The Purveyor of Glamour has a significantly higher chance of giving you a random ornament that is cool, for some definition of cool.
* Player Ornaments work without re-equipping gear.
```

Next Reboot:
```
* Characters in the Bazaar are once again immune to IP limit checks
* Modulating Rod and Rod of Mystical Transvergence conversion rate increased
```

---

## Entry 1269763708481962027
**Author:** Retribution EQ #change-log
**Date:** 2024-08-04T21:07:39.171000+00:00

08/04/2024

All of this probably needs a reboot to be fully effective. Next reboot scheduled for DT on Tuesday.
```
* Reverted anti-idle script in Bazaar
* Azure Mind Crystal is now a targeted summon (target receives item)
* Sanguine Mind Crystal is now a targeted summon (target receives item)
* Bazaar vendor weapon augments are now all/all pri/sec/range
* Sympathetic Procs should no longer reflect back at their owner
```

---

## Entry 1270068579076935785
**Author:** Retribution EQ #change-log
**Date:** 2024-08-05T17:19:05.985000+00:00

8/05/2024
```
* Reworked NTOV script to spawn Vulak
* Removed lockpicking requirement from Chardok Royals
```

---

## Entry 1270428849955405916
**Author:** Retribution EQ #change-log
**Date:** 2024-08-06T17:10:41.256000+00:00

8/06/2024
Consolidated Changelog - Deploying
```
Retribution has migrated to new server infrastructure, located centrally in a Chicago datacenter.

Bug Fixes:
* Improved Implied Targeting - Characters should no longer nuke themselves when a mob dies before their spell lands
* Bard Spellbars should lock\unlock as anticipated
* Experimental fix for spellbar remaining locked under unknown condition
* Both Players and Pets should display Ornaments as anticipated
* IP limit checkks are once again ignored in the Bazaar. Reminder; you are expected to only play a maximum of 3 characters at a time. The hard limit is not enforced at 3, but please do not abuse this grace.
* Vulak should now reliabily spawn. In addition, Thylex of Veeshan will occasionally shout a hint as to which trigger mobs remain up.
* Jaled Dar's Shade should now stop Douging.
* Magician epic pet should now be affected by pet foci again.
* Experimental fix for hotbars occasionally being rearranged

Improvements:
* First Orb of Retribution now also scales based on the farthest progression stage which this account has unlocked this season.
* Rod of Mystical Transvergence conversion ratio enhanced
* Azure Mind Crystals are now a targeted summon
* Sanguine Mind Crysals are now a targeted summon
* Bazaar vendor Augments are now all\all and pri\sec\range
* Removed need for locking on doors to Chardok Royals.

EoM Services:
* The Polymorphist in the Bazaar now has Drakkin as a race-change option.
* The Purveyor of Glamour has a SIGNIFICANTLY higher chance of awarding an 'interesting' random augment
```

Post-Patch
```
* Allaclone and CharBrowser now function correctly.
```

---

## Entry 1271105399537537064
**Author:** Retribution EQ #change-log
**Date:** 2024-08-08T13:59:03.246000+00:00

Hot-Fix
```
* Fixed zone server crash when handing items to charmed pets.
* Attempt at fixing certain mobs from summoning you under the world.
```

---

## Entry 1271499064210362481
**Author:** Catapultam
**Date:** 2024-08-09T16:03:20.218000+00:00

```
* Added the ability to consume items to add exp to the item in your power source.
  - Must be from the same upgrade series at a lower stage
  - Same step are worth 25% exp
  - One step lower are worth 6.25% exp
* Secondary pets now accept equipment traded to them
* Secondary pets now respond to pet commands
  - /pet qattack now sends pet attack command to one pet at a time, in a cycle
* 4 ranks of Mnemonic Retention are granted on character creation.
```

---

## Entry 1271660020295270425
**Author:** Catapultam
**Date:** 2024-08-10T02:42:55.139000+00:00

```
* Tinkering is available to any race
* Shamans can perform Alchemy
* Rogues can perform Poison Making
* Rogue Sneak\Hide now functions as anticipated
* Melee Combat Skills (Kick, Bash, Kick(s), Strike(s), Frenzy) are all on seperate cooldowns
* Human and Iksar Monks will correctly display Cured Silk type armors.
* Fixed HoTT showing incorrect HP for yourself.
* AA abilities with recasts shorter than their duration will now suspend
* Item EXP to powersource now consumes a portion instead of all exp.
```

---

## Entry 1272971478454898777
**Author:** Retribution EQ #change-log
**Date:** 2024-08-13T17:34:11.130000+00:00

**Consolidated Change Log**
*Note:* Some of these changes already went live, but all of them will be live on reboot.

```
- Mage Epic now correctly impacted by Pet Power 15
- Monster Summoning III now impacted by Pet Power 15
- Zumaik's Animation  now impacted by Pet Power 15
- Spirit of Khurenz stats increased to be in line with Pet Power 15 pets of other classes.
- Emissary of Thule now has an appropriate Pet Power 15 pet.
- Throwing Axes now stack to 100
- Sentry Badain now lets you know the 10th ring war is being worked on and returns your items.
- Enchanter Epic NPC Nadia Starfeast now summons the Enchanter's Sack on turn-in as well as a phrase for those following different guides.
- Bristlebane's Mischievous Mayhem should now be correctly casting every 48 seconds (up from 30).
- GoD quests accidentally enabled by allowing VP 2.0 have had their rewards scaled down instead of removed. If you paid plat for these items and no longer want them, DM me for a refund (Hoshkar and Xygoz quests).
- All Manastone qualities have been set back to a 1-second cast for this season. This may change in future seasons.
- Throw Stone no longer shares a CD with other major skills.
- Explosion of Spite, Beacon of the Righteous, and Area Taunt have had their range increased to 60. This is an increase of 10, 30, and 20 range respectively.
- Group leadership AA requires 100 Dark Blue kills per point.
- Raid leadership AA requires 50 Dark Blue kills per point.
- All poison vendors in the bazaar have had their faction removed.
- Progression NPCs "A Faded Memory" now see through invis, hide, and improved invis.
- Many item stat changes from the king-me channel.
- Ranger AA Frost Arrows has had its damage increased to match Flaming Arrows. Its mana cost per tick has been removed.
- Ranger AA Flaming Arrows has had its mana cost removed.
- Ranger spells Flaming Arrow (Not the AA) and Burning Arrow now apply a called shots effect, increasing archery damage taken by 10 and 20% for 3 ticks.
- Ranger AA Trick Shot occurrence increased to 5% per rank.
- Spell: Trickster's Calling has had it's duration reduced to 20 seconds.
- Crown of Rile has had its original click effect restored - Extinguish Fatigue, restoring Endurance instead of Stamina.
- Druid spell Nature Walker's Behest has had the durability of its pet increased (not its damage).

```

---

## Entry 1273152817099706388
**Author:** Retribution EQ #change-log
**Date:** 2024-08-14T05:34:45.632000+00:00

```
Tearel Overhaul

Tearel now allows you to attune the map to any destination you have previously discovered.
He can now also attune the map to your current expedition, but like group ports it takes special reagents (EoM).
Unlocking group ports or expedition attunements will unlock both.
If you already unlocked group ports, you may now use Tearel to return to your active expedition.
```

---

## Entry 1273377641671430257
**Author:** Retribution EQ #change-log
**Date:** 2024-08-14T20:28:07.987000+00:00

```
* Bazaar and Back will now place you in a semi-random place in the Bazaar
* Bazaar and Back will now prompt nearby group members if they want to travel with you. (beepboops can use /yes to accept it) (thanks @Chroma)
* Pets should no longer be unshrinkable monstrosities
* Pet names are now static (Parsers rejoice)
* Revamped pet names
```

---

## Entry 1273891017434726481
**Author:** Retribution EQ #change-log
**Date:** 2024-08-16T06:28:06.307000+00:00

```
* Combat Fury normalized for all classes which normally obtain it. Now applies to all weapon skills (Rangers, it now works for archery).
* Veteran's Wrath normalized for all classes
* Mastery of the Past is now fully available to all spellcasting classes
* Shield Block is fully available to all classes able to equip shields
* Spell Casting Subtlety is now fully available to call spellcasting classes

Hotfix:
* Fixed bug preventing rogue from using SoS (Only effective in reloaded zones until reboot)
* Fixed bug around combat fury being a pre-req for other AA
```

---

## Entry 1274023304469942294
**Author:** Catapultam
**Date:** 2024-08-16T15:13:45.994000+00:00

```
* Fury of Magic is no longer available to hybrids
* Fists of Steel no longer applies to 1HB weapons
```

---

## Entry 1274465896978448579
**Author:** Retribution EQ #change-log
**Date:** 2024-08-17T20:32:28.271000+00:00

```
Hotfix:
* Haste now applies to combat skills again. (Should fix timer bugs)
```

---

## Entry 1274778415710470184
**Author:** Retribution EQ #change-log
**Date:** 2024-08-18T17:14:18.543000+00:00

```
Hotfix:

Vulak is no longer rooted in place. It is highly recommended you pull him off his platform before engaging. Unless, of course, you enjoy lava.
```

---

## Entry 1274855094273310810
**Author:** Catapultam
**Date:** 2024-08-18T22:19:00.137000+00:00

```
Hateplaneb is now fixed
```

---

## Entry 1275275502965362720
**Author:** Retribution EQ #change-log
**Date:** 2024-08-20T02:09:33.380000+00:00

```
Next Patch:
* Mage Summoned items modified as follows;
  - Staff of Tracing: Symp Strike I -> Burn (1s/30s)
  - Staff of Warding: Symp Strike II -> Cancel Magic (1s/30s)
  - Staff of Runes: Symp Strike III -> Symp Strike I (1s/30s)
  - Staff of Symbols: Symp Strike IV -> Ward of Calliav (1s/30s)

  - Dagger: Burn -> Burst of Flame
  - Snake Fang: Poison -> Weak Poison
  - Spear of Warding: Rune I (unchanged)
  - Sword of Runes: Rune II (Unchanged)
  - Dagger of Symbols: Shock of Flame -> Shock of Blades

* Apocryphal Fire Crystal Staff: Sympathetic Strike V -> Sympathetic Strike III
* Blur of Axes damage is now scaled based on level.
```

---

## Entry 1275278018083815468
**Author:** Catapultam
**Date:** 2024-08-20T02:19:33.031000+00:00

```
Next Patch:
* Cleric summoned hammers are no-drop.
* Pets no longer accept no-drop items given to them by anyone other than their owner.
* Add sliding cap on how much exp can be earned per kill; variable on both player level and con color
* Fixed Fists of Steel
* Multipet Version 2:
 - Primary\Secondary pet distinction is gone
 - Summon or Charm in any order
 - One per per originating class;
   - One Mage summon or charm
   - One Enchanter summon or charm
   - One Necromancer summon or charm
   - etc
 - Targeting pet switches pet window
 - Pet commands with a pet targeted send command only to that pet
 - /pet qattack - sends one pet at a time
 - Pets will be forced into Ext Target slots 18, 19, 20
* Death no longer results in exp loss.

Hotfix:
* Lowered base Exp rate by a moderate amount
* Increased group size exp penalty
* Increased Item Exp rates by a moderate amount
```

---

## Entry 1275628398600785940
**Author:** Aporia
**Date:** 2024-08-21T01:31:50.256000+00:00

```
Effective immediately:

- With the decrease of overall exp gain, hell levels have been removed.

- Exp loss on death has also now been removed.
```

---

## Entry 1275637372138295417
**Author:** Catapultam
**Date:** 2024-08-21T02:07:29.714000+00:00

Consolidated Patch.
```
* Cleric summoned hammers are no-drop.
* Pets no longer accept no-drop items given to them by anyone other than their owner.
* Add sliding cap on how much exp can be earned per kill; variable on both player level and con color
* Fixed Fists of Steel
* Multipet Version 2:
 - Primary\Secondary pet distinction is gone
 - Summon or Charm in any order
 - One pet per originating class;
   - One Mage summon or charm
   - One Enchanter summon or charm
   - One Necromancer summon or charm
   - etc
 - Targeting pet switches pet window
 - Pet commands with a pet targeted send command only to that pet
 - /pet qattack - sends one pet at a time
 - Pets will be forced into Ext Target slots 18, 19, 20
* Death no longer results in exp loss.
* Lowered base Exp rate by a moderate amount
* Increased group size exp penalty
* Increased Item Exp rates by a moderate amount
* Hell Levels removed

Hot-Fix (may need new zone server!)
* Tab\F8 should no longer target pets.
* Reverted H2H-only limit on FoS for now.
```

---

## Entry 1275678617942228993
**Author:** Catapultam
**Date:** 2024-08-21T04:51:23.480000+00:00

Round 2!
```
* Dimensional Armory will selectively equip mage pets.
* Pets can be traded items again
* Fixed invulnerable monks
* FoS limited to H2H again
```

---

## Entry 1276052667470188625
**Author:** Catapultam
**Date:** 2024-08-22T05:37:43.837000+00:00

Running changelog for next patch
```
* Items upgraded via Power Source will retain charges.
* Fixed skillcaps problems, including 2HP
* Level 1 Skills set to cap for that level (Except tradeskills, etc). Skills displayed at level 1 are fucked, don't try to make sense of them.
* First point in new skills is automatically assigned at level-up.
* Revert to vanilla stacking logic, hopefully clears up weird song stacking stuff.
* Fixed not being able to trade your pets no-drop items.
* Fixed typos
```

---

## Entry 1276101765921509417
**Author:** Catapultam
**Date:** 2024-08-22T08:52:49.820000+00:00

```
* Lots of progress on cleaning up /who. Apparently I don't remember exactly how /rol and /anon work. More to come
```

---

## Entry 1276194813896822829
**Author:** Retribution EQ #change-log
**Date:** 2024-08-22T15:02:34.186000+00:00

```
Effective on reboot, some effective immediately:

- Banded armor can be combined again.
- Every quest in Jaggedpine now gives the correct faction.
- Klandicar now gives the correct faction.
- Phara Dar now heals to full if disengaged and depops his adds.
- Ella Foodcrafter now lets players know she has [two tasks].
- Circlet of the Falinkan quest now requires correct level to complete (kindly down from ally).
```

---

## Entry 1276243407290761216
**Author:** Catapultam
**Date:** 2024-08-22T18:15:39.754000+00:00

```
* Implemented Client<->Server handshaking. You will be disconnected after a short period of time if you are not using the client modification plugin.
* Implemented improved MQ2 detection. 
```

---

## Entry 1276566684332851331
**Author:** Catapultam
**Date:** 2024-08-23T15:40:15.007000+00:00

```
* Autoinventory now skips Power Source and Ammo
* Refromatted /who results
* Updated Description and names of Dire Charm variants to distinguish allowed targets.
* Updates/Fixes to Melee Skill reuse timers
* Knight's Advantage stacks now
```

---

## Entry 1276746251861229568
**Author:** Catapultam
**Date:** 2024-08-24T03:33:47.242000+00:00

8/23 - Pending Reboot
```
* Items which gain a click upon being upgraded to Legendary no longer have 0 charges.
* Charmed pets no longer consume a pet slot after charm breaks
* Glyph AAs can no longer be purchased.
* Skill reuse times fixed (finally), Thanks @Carolus
* Familiars no longer spawn a pet.
* Spell Procs (Poison, buffs, AA, etc) work with ranged and throwing attacks
```

---

## Entry 1277511372816519231
**Author:** Catapultam
**Date:** 2024-08-26T06:14:06.293000+00:00

```
Reworked Item Experience
- Not sharing a lot here, figure this one out yourselves.
- This one is way better.
- Items become no-drop as soon as you feed them XP.
- Ok, fine. It's con and level based, totally independent of item stats. Relatively easy to get to enchanted, significantly harder to get legendary.
- Harder at higher levels, but you can kill faster, so... evaluate that how you want.
- Removed exact % feedback for leveling rate.
```

---

## Entry 1278227086808715314
**Author:** Catapultam
**Date:** 2024-08-28T05:38:05.806000+00:00

```
Item Experience Rework (Again)
- Using your Power Source slot to progress an item no longer carries an experience penalty.
- Any item which receives experience becomes no-drop immediately.
- Reworked scaling rates;
  - Rates vary based on item tier, con-level of kill, current level, and total stats of the item.
  - Higher con differences = more item progression
  - Lower current level = more item progression
  - Normal -> Enchanted = less progression required
  - Enchanted -> Legendary = MUCH more progression required
  - More total stats = more progression required
 - Re-implemented Consume Item
  - Still maps to the 4x for normal->enchanted, 4/8x for enchanted -> legendary.
  - No-Drop items MAY NOT be consumed (It was this or break the ratio above to prevent cheese).
```

---

## Entry 1278501238148960351
**Author:** Catapultam
**Date:** 2024-08-28T23:47:28.579000+00:00

```
- Can consume higher-tier items (reg in PS, consume enchanted).
- attempt to fix pet taunt
```

---

## Entry 1279089267922178139
**Author:** Retribution EQ #change-log
**Date:** 2024-08-30T14:44:05.802000+00:00

Effective on reboot:

```
Lockpicking requirement from SSRA doors has been removed.
Key items are still required.
Certain bags have had their capacity slightly increased on RC/Apoc versions
Zerker AA Tireless Sprint now correctly increases movement rank by 10% for RKII and RKIII
Rangers once again have access to the Shield Block AA
Veteran's Wrath AA once again effects all weapon types (certain weapon types were not benefitting from this AA as intended since the normalization- this has been fixed).
Ranger spells Flaming Arrow and Burning Arrow now correctly proc Symp Strikes. Their base damage has been decreased but now act as short DoTs.
Monks now have access to three ranks of the Hastened Destructive Force AA
Monks now have access to four ranks of the Hastened Defensive Poses AA
Gliblixl Rocktok no longer spawns in the Bazaar
```

---

## Entry 1280040224138727529
**Author:** Retribution EQ #change-log
**Date:** 2024-09-02T05:42:51.432000+00:00

```
Effective now:

remains of Vah Kerrath no longer randomly eats Soul Essences

NE Tower in Sanctus Seru now has working teleporters

Luclin BST pet has slightly increased base stats and now correctly benefits from PP20 gauntlets from VT

On reboot:

Certain ranger selfbuff procs that were unable to proc from archery, now proc from archery

Certain item clickies no longer require reagents

Group ports now work again when players are in an instance
```

---

## Entry 1280206113660473560
**Author:** Retribution EQ #change-log
**Date:** 2024-09-02T16:42:02.576000+00:00

```
- Deleted several RC and Apoc 'tradeskill tools'
- Quests which check for the presence of items now correctly detect when those items are in the bottom two slots of inventory.
_ Clockwork Bankers and Merchants now work again, and are no longer 'pets'.
_ Mage Epic pet is affected by pet focus items once again
- Tearel should be more reliable
_ AHR now triggers correctly when all other bosses in zone are dead.
- AHR spawn conditions survives zone reset.
- Thylex of Veeshan is far less talkative
- Fixed SoL-completion Bag Upgrade
```

---

## Entry 1281396861147676696
**Author:** Retribution EQ #change-log
**Date:** 2024-09-05T23:33:38.900000+00:00

```
Spirit of the Howler Pet level increased.
Nature Walker's Behest Pet HP reduced.
Torturing Winds Debuff reduced to 2 minutes from 2 hours.
```

---

## Entry 1282507287625469994
**Author:** Catapultam
**Date:** 2024-09-09T01:06:05.203000+00:00

```
- Detrimental spells now stack with beneficial spells.
  - ie; If you have SoW and get Snared, your run speed is now SoW speed minus the Snare reduction
- Short Duration spells (Song Window) no longer have stacking conflicts with normal buffs.
- If somehow a short duration buff overwrites a long duration buff, or vis versa, they will go to the correct window.
```

---

## Entry 1283931437963149325
**Author:** Catapultam
**Date:** 2024-09-12T23:25:09.103000+00:00

```
* Debuffs now clear automatically when ending combat
* Fixed bug causing 'You are weakened and cannot rest' to display inappropriately.
* Rogues can backstab with any weapon
* Cleaned up casting and interrupt messages (THIS WAS ACTUALLY REALLY CLEVER GUYS)
* There is now a minimum time between activating Bandolier sets (10 seconds).
* Monk skill attacks now trigger Fists of Steel proc (but not damage)
* Added Situational Awareness AA - Increases Tracking skill by 10 points per rank.
```

---

## Entry 1284232804883890287
**Author:** Catapultam
**Date:** 2024-09-13T19:22:40.576000+00:00

```
* Druid DS now scales correctly
* Fixed several issues surrounding being unable to manipulate inventory while casting. 
* Expected behavior\Please test the following specifically;
  - Inventory, Hotkeys, Skills, etc should be usable while casting
  - Spell casting messages (for self and other) should be created correctly.
  - Spell interrupt messages should be created correctly.
  - Bard Song interrupt messages should be created correctly (no cast messages for Bard Songs)
  - Monk alt-appearance gear should use unique graphics
```

PATCH REQUIRED

---

## Entry 1284366282204123227
**Author:** Catapultam
**Date:** 2024-09-14T04:13:04.049000+00:00

```
* Attempt to resolve issues with power source upgrading to legendary
* Reduced floor on legendary experience scalar for item upgrading
* AA Abilities now use implied targeting
* Spirit of Cheetah moved to short duration buff box
* Combat Mana\HP\Endurance Regeneration is now displayed the actual value from the server.
* Resists now display the actual value on the server
```

---

## Entry 1284637798019633182
**Author:** Retribution EQ #change-log
**Date:** 2024-09-14T22:11:58.464000+00:00

Pending Patch

```
Enchanter AA Phantasmic Reflex has been changed. ALL SPELLS cast by an enchanter, now have a SMALL chance to grant the caster SMALL rune.

Legendary Staff of Writhing and Legendary Ancient Prismatic Staff now have had their proc restored in addition to their click.
```

---

## Entry 1284649224260292678
**Author:** Aporia
**Date:** 2024-09-14T22:57:22.692000+00:00

```
Hell levels removed for real this time.
```

---

## Entry 1284767213877854229
**Author:** Catapultam
**Date:** 2024-09-15T06:46:13.609000+00:00

```
* Fix dupe when upgrading items with power source
* Low-level characters get a multiplier on power source leveling rate.
* Unresistable spells are actually unresistable
* Short-Duration buffs no longer zone with pet.
```

---

## Entry 1284796823336259585
**Author:** Retribution EQ #change-log
**Date:** 2024-09-15T08:43:53.054000+00:00

```
* Hole door is now 'click to enter' instead of being a literal door
```

---

## Entry 1285072099698016303
**Author:** Retribution EQ #change-log
**Date:** 2024-09-16T02:57:44.053000+00:00

Pending Patch

```
Trueshot Discipline increased hit chance was broken. It has been fixed (0 to 12%).

Berserker Discs - Head Strike, Leg Strike, Leg Cut, Head Pummel, Head Crush, Divertive Strike, and Distracting Strike, have had their reagent requirements removed. They also now share a CD with Throw Stone.

Berserker Disc Focused Fury increased hit chance was broken. It has been fixed (0 to 50%).

Warrior Disc Precision increased hit chance was broken. It has been fixed (0 to 50%).

Monk Discs - Phantom Wind, Zephyr, Echo, and Call now share a CD with Throw Stone
```

---

## Entry 1285073862718918656
**Author:** Aporia
**Date:** 2024-09-16T03:04:44.390000+00:00

Pending Patch:

**Discipline Timer Rework**

As you know shared timers between different class discs for melee and hybrid classes has been a huge hinderance in their expected cross performance.

A decision was made on how to make this work within the confines of the system.

After next patch:

ALL OFENSIVE DISCIPLINES, BETWEEN CLASSES, WILL NO LONGER SHARE A COOLDOWN.

Offensive disciplines that shared a cooldown WITHIN a single class, continue to share a cooldown.

ALL DEFENSIVE DISCIPLINES, BETWEEN CLASSES, WILL NOW SHARE A COOLDOWN. (All riposite Discs will share a timer, all dodge, parry, and damage reduction Discs will share a timer).

Defensive disciplines that shared a cooldown WITHIN a single class, continue to share a cooldown.

This will be a net increase in DPS for those stacking melee classes and a net decrease in certain mitigation combinations.

*Note: This is disciplines ONLY not AA.*

---

## Entry 1285383939115978868
**Author:** Catapultam
**Date:** 2024-09-16T23:36:52.364000+00:00

```
* Clickies become attuned when successfully clicked.
* Fixed power source upgrading from duping items (for real this time)
* Mandatory 0.5s recast removed Beneficial instant-clicks.
* Exclude Pacify and Mez from Cascade of Decay
* Pets will taunt undead mobs now (?!)
* All Weapon Proc (SPA 85) spells stack
```

---

## Entry 1285646038744567849
**Author:** Catapultam
**Date:** 2024-09-17T16:58:21.785000+00:00

```
* Hopefully fixed power source dupe (again again)
* Removed Fury of Magic AA from Hybrids again
```

---

## Entry 1286022083201208392
**Author:** Catapultam
**Date:** 2024-09-18T17:52:37.770000+00:00

```
* Restored Fury of Magic, Spell Casting Fury, Destructive Fury to Hybrids
* (Ingenuity was never removed)
* Ingenuity now works as described - it ONLY affects spells from items (Procs, Clicks)
* Return to the Valley Beneath the Son of Fixing Power Source Dupes
* Removed several duplicated AA
* Adjusted client validation so that it does not boot players from Bazaar, and gives more info on how to get correct client.
```

---

## Entry 1286236109008797730
**Author:** Retribution EQ #change-log
**Date:** 2024-09-19T08:03:05.499000+00:00

Pending Patch

```
- Instruments now display their correct Resonance level based on item tier.
- Tier 1 and 2 items are always magical.
- Bard Epic instrument effect corrected
- Fixed Bash reuse timer w\ haste
- Fixed clockwork summons
- Fixed wizard sword\cleric hammers
- Added Beastlord and Berserker to a number of old-world items which were missing them
- Reduced CD of Bestial Alignment
- SE_MeleeLifetap applies to SpecialAttackDamage
- Fixed containers for 'Strike of Shissar N' poisons
```

---

## Entry 1286425410141290609
**Author:** Catapultam
**Date:** 2024-09-19T20:35:18.406000+00:00

```
- Fixed Disc Timers
- Totally nuked all traces of LDON camps
- Lost track of bug fixes.
- FD should no longer cure debuffs
- Pet debuffs should be removed on resting, skipping ones cast by their owner to faciliate charm.
- Pet bag and multiple pets plays nice now
- Project Illusion now works on Pets.
- Fixed BS with non-1hp damage
- Power Source no longer applies stats.
- Improved stacking of proc spells (multi-class proc spells will stack)
- Improved stacking of DS (multi-class DS will stick, but not every DS from same class)
```

---

## Entry 1287147068732997703
**Author:** Catapultam
**Date:** 2024-09-21T20:22:55.222000+00:00

```
* Only Must-Equip clickies will become attuned when clicking from inventory
* Numerous quest script fixes
* Honey, I shrunk the bats.
```

---

## Entry 1287917817815109632
**Author:** Catapultam
**Date:** 2024-09-23T23:25:36.123000+00:00

```
* Fixed Bard foci (again)
* Legendary items are once again Attuneable
* Attuneable items become no-drop when you gain experience with them equipped, rather than immediately upon equip.
* Fixed pet target HoTT
* Fixed per commands breaking if you have a familiar as first pet
* Fixed familiars attacking if you have something other than a familiar as first pet
* Improved coherency of pet window swapping
* Fixed losing access to pet window if charm pet was focused pet when it died\charm broke
* Buff stacking is bypassed for spells you cast against other buffs you cast which don't share a class
```

---

## Entry 1288303500970692668
**Author:** Catapultam
**Date:** 2024-09-25T00:58:10.153000+00:00

```
* Fixed infinity buff stacking from non-class sources
* Fixed crash bug
* Fixed attune-on-exp bouncing
```

---

## Entry 1288338475724312656
**Author:** Catapultam
**Date:** 2024-09-25T03:17:08.784000+00:00

```
* EoM Loot Buff increases Item XP rate
* Mobs will IGNORE pets which have pet taunt off; all aggro the pet would have generated is transferred to their owner.
* Pet AoEs now work without the pet having aggro on each mob individually first.
* Legendary Augments are no longer attuneable.
```

---

## Entry 1288893446676807752
**Author:** Catapultam
**Date:** 2024-09-26T16:02:24.170000+00:00

PENDING

```
* Added Beastlord and Berserker to a number of old-world items which were missing them
* Reduced aggro transfer from taunt-off pets to owner
* Consume Item will no longer delete items as they become Legendary
* Improved NPC Model Upgrade routines
  - Fixed Wolf Models
* Racial skills add to skillcaps
* Improved skill-up messages (shows current/cap)
* Fixed access to #myskills
* Fixed access to #mystats
* Reduced CD of Bestial Alignment
* SE_MeleeLifetap applies to SpecialAttackDamage
* Fixed containers for 'Strike of Shissar N' poisons
```

---

## Entry 1290078652939112509
**Author:** Aporia
**Date:** 2024-09-29T22:31:59.363000+00:00

Pending Patch:

```
- Iron Oxide spawns fixed in Steamfont Mountains.
- SH Casino (Therin Asakith) now properly rewards all illusion items
- Lambent Boots, Gaunts, and Greaves quest turn ins have been fixed
- Staff of Writhing proc rate has been fixed across all versions
- Satchel of the Hero is now no drop and has 100% WR
- Gnome Warrior GM, Narron Jenork has returned and once again offers his Watchman Boots quest
- Ranger AA Protection of the Spirit Wolf CD reduced to 15 minutes
- Plane of Sky quest Test of Preparation fixed
- Lower Guk WP move from Safe Hall to Undead Side Entrance
- Jboots click effect changed for Lego version!
- Spirit of Cheetah recast time lowered to 3 minutes
- Swarm Pet Mistwalker HP increased to 600
- Clarified description on Paladin's Blessing of Light AA
- Shaman AA Rabid Bear now gives double attack/regen/cold resist at rank 1. These stats and proc chance have been lowered across Rk 2 and 3.
- Cleric AA Divine Avatar now gives higher stats at lower ranks but has had its effect cap reduced on max ranks.
```

---

## Entry 1290575831361523777
**Author:** Catapultam
**Date:** 2024-10-01T07:27:35.936000+00:00

```
- Added support for up to 500 disc timers
- All discs on seperate timers (This will change!)
- Reworked custom skill timers to reduce packet traffic by at least 100x
- Static instances are now generated dynamicly
- All of the above patch
```

---

## Entry 1290694483100569703
**Author:** Catapultam
**Date:** 2024-10-01T15:19:04.715000+00:00

```
- Restored vanilla timers to discs
- Discs assigned to multiple classes use original timer IDs
- Discs assigned to individual classes use a class-unique set of timer IDs
```

---

## Entry 1291141623316615188
**Author:** Catapultam
**Date:** 2024-10-02T20:55:51.250000+00:00

```
- Swarm pets created by pets now belong to that pet's owner.
- Items upgraded via power source can no longer trigger Discovery events.
- Items upgrading via power source will no longer gain any significant exp while in a raid.
- #mystats now dumps all pet info at once, regardless of target
- default UI elements for Player and Group windows are now non-resizable, and can be moved more intuitively.
- Pet Commands other than /pet attack and /pet back are issued ONLY to your focused pet (the one which has the pet window)
- Added additional stages to Power Source exp reports.
```

---

## Entry 1292298737808445541
**Author:** Catapultam
**Date:** 2024-10-06T01:33:48.843000+00:00

```
- Added Tutorial Popups for; Welcome, Buff Suspending, Power Source\Upgraded Items, Sympathetic Procs
- Added two newbie tasks that helps guide the player from level 1->51, introduce key concepts and faciliate Kunark unlock
```

---

## Entry 1292338022649561121
**Author:** Retribution EQ #change-log
**Date:** 2024-10-06T04:09:55.079000+00:00

```Cabilis, Lake of Ill Omen, Warsliks Woods, Swamp of No Hope, Field of Bone, Kurn's Tower, Shar Vahl, Shadeweaver's Thicket, Hollowshade Moor, and Paludal Caverns are all now available in classic.```

---

## Entry 1293037243723939890
**Author:** Catapultam
**Date:** 2024-10-08T02:28:22.374000+00:00

```
* DD spell cast times reduced to 3 seconds if above 3 seconds, Any time reduced this way added to recast times.
* Cast times on spell inspect window are now correct, and correctly account for Spell Haste.
* Spell Cast bar will still end 'early' when Spell Haste is in effect.
* Archery and Throwing weapons now check Double and Triple Attack skills
* Fixed PBAoE being limited to 4 targets
* Adjusted item leveling so that item stats is weighted over character level
* EoM Exp AND Loot buffs apply to item leveling rate
```

---

## Entry 1293076847604535327
**Author:** Catapultam
**Date:** 2024-10-08T05:05:44.675000+00:00

```
* Item Exp actually takes item stats into account.
* Ranged Attacks can skill up DA\TA
```

---

## Entry 1293346133531430913
**Author:** Catapultam
**Date:** 2024-10-08T22:55:47.443000+00:00

```
* Classes eligible to buy an AA are now listed in the AA Description
* Removed low-level bonus to item leveling, now solely based on con of kill and stats on item
```

---

## Entry 1293592147341082697
**Author:** Retribution EQ #change-log
**Date:** 2024-10-09T15:13:21.706000+00:00

```
* Lowered Damage on Sympathetic Strike I-III
* Sacrificial Dagger adjusted to Sympathetic Strike II
* Black Tome with Silver Runes adjusted to Sympathetic Strike III

* Twincast will no longer apply to most procs
* Calliav\Prism Skin type runes provide immunity to DS while active, and DS hits do not burn their charges.
```

---

## Entry 1293597206405840899
**Author:** Catapultam
**Date:** 2024-10-09T15:33:27.881000+00:00

```
* Players are immune to stun for a short time after being Stunned
* Increased the amount of allowed movement while casting spells
* Instant-cast Disciplines can be used while casting
* Disciplines with casting time will interrupt spellcasting.
* Fixed pet buffs randomly not working based on resummoning pets, etc
```

---

## Entry 1293714261134278699
**Author:** Catapultam
**Date:** 2024-10-09T23:18:35.903000+00:00

```
* Vision of Ayonae added to Bazaar
 - For characters with exactly 1 class, the Vision can add two random classes.
 - For characters with more than 1 class, the Vision can remove a class. This removal has a cost in EOM and a cooldown.
   - Cooldown set to 1 day and EoM cost to 0 for Beta
   - All skills, spells, disciplines, and AA which are unusable after the class drop are deleted.
```

---

## Entry 1294369641543762014
**Author:** Catapultam
**Date:** 2024-10-11T18:42:50.769000+00:00

```
- Experimental fix for the noloot\nocast bug
- Misc bug fixes
```

---

## Entry 1294787699277959189
**Author:** Aporia
**Date:** 2024-10-12T22:24:03.500000+00:00

Pending Reboot

```
- Waypoint added to Lake Rathe
- Black Insanity and Dark Courage weapons have had their bane damage increased on each version.
- Inscribable Words ground spawn fixed in Nagafen's Lair.
- Spawn location of Avisiris has been corrected.
- Gliblixl Rocktok now sells starter Bard Instruments in the bazaar.
- Philter of Translocation now properly labeled Philter of Major Translocation
```

---

## Entry 1295116943312818217
**Author:** Aporia
**Date:** 2024-10-13T20:12:21.395000+00:00

```
- Glidara Myllar script fixed.
- Bryn Fynndel script fixed.
- Orc Impaler quest should now be completable.
- Mojax Hikspin script fixed.
- Enchanter slow cast times reduced to match comparable Shaman slow cast times. This effects: Tepid Deeds, Shiftless Deeds, Forlorn Deeds, Dreary Deeds, and Desolate Deeds.
- Echo of the Past added to Crushbone
- Echo of the Past added to Befallen
- Echo of the Past added to Kurn's Tower
- Echo of the Past added to Runnyeye
- Echo of the Past added to The Warrens
- Echo of the Past added to Blackburrow
- Echo of the Past added to Sol A
- Echo of the Past added to Upper Guk
- Monk Disciplines Voiddance and Whirlwind have had their base CD reduced to 28 minutes from 40.
- Echo of the Past for Dreadlands has been moved to its port in spot.

```

**Important Note:**

It has been decided that VP 2.0 launching with Kunark is a poor overall experience for a number of reasons.

VP moving forward will drop 1.0 loot and its bosses will be scaled back to fit in between Kunark progression targets and Velious dragons. They will keep most of their mechanics but the effects and stats have been reduced by about 60%.

This should make it feel like an end game Kunark experience, and with the availability of Enchanted/Legendary gear, still worth doing in era.

The mobs and abilities may be adjusted further.

---

## Entry 1295934257541283881
**Author:** Retribution EQ #change-log
**Date:** 2024-10-16T02:20:04.292000+00:00

```
- Scout Malom now correctly spawns The Spirit of Torment.
```

---

## Entry 1297301475860414606
**Author:** Aporia
**Date:** 2024-10-19T20:52:54.541000+00:00

```
- Pet buffs that include mitigation can no longer be dispelled.
- Blur of Axes base damage increase has been reduced.
- Tearel can now interact with players that are invis/hidden/SoS.
- Prince Selrach Di'zok has had his stun component removed. Blind lasts up to 24 seconds.
- Sneak Attack description fixed.
- RoRZ description fixed.
- Notlav the Scalekeeper no longer spawns.
- Minor VP 1.0 fixes.
- Trickster's Calling reduced to 10s
```
**Important Note:**

Innoruuk in Hate has been changed similarly to the Dragons in VP 2.0.

Loot has been changed to the original (Post Revamp) version 1.5. His difficulty has been reduced in kind. All of his revamped loot can now be worn by any race.

---

## Entry 1298343309261013104
**Author:** Aporia
**Date:** 2024-10-22T17:52:46.980000+00:00

Deployed

```
- Many Hate 2.0 and OoE items available in classic have been reduced to bring them in line with progression expectations.
- Many LoY and OoE items available in Kunark have been reduced to bring them in line with progression expectations.
- More AA/Spell description corrections.
- Backstab damage from non-1hp sources has been reduced.
- Corrected map files for Hate, The Hole, Gunthak, Nadox, Veksar, and Sebilis have been added to the patcher.

```

---

## Entry 1298551768585605191
**Author:** Catapultam
**Date:** 2024-10-23T07:41:07.556000+00:00

```
- Removed all lockouts from respawning instances
- Raid\Flag bosses no longer spawn in respawning instances
- Non-Respawning instances will become more difficult based on the number of players above 2 in an expedition.
- Players may no longer be added to an expedition once the progression flag mob spawns.
```

---

## Entry 1299068357512790077
**Author:** Aporia
**Date:** 2024-10-24T17:53:51.954000+00:00

```
- Frenzied Burnout AA cost reduced to 3/6/9/12/12/12
- Elemental Earth AA no longer exploitable for massive HoT
- NPC Melee Interrupts reduced
- Sarkis Ebonblade now talks to Shadowknights as intended
```

---

## Entry 1299074291568082975
**Author:** Catapultam
**Date:** 2024-10-24T18:17:26.743000+00:00

working log; all pending
```
- Added a short lockout to Respawning instances (1 hour)
- Added Hand of the Gods proc to cleric epic
- Power Source item improvement rate calculation is now always based on the top-tier version of the item, then scaled down for lower tiers.
- Fixed Rage Volley casting animation
- Discs now correctly start their timers when activated while casting.
- Fixed spell haste display
- Fixed melee mitigation effect on pets
- Enabled AAEXP at level 1
- Reduced max level during classic to 50
- Echo buffs now scale by level more appropriately.
```

---

## Entry 1299609834563440670
**Author:** Aporia
**Date:** 2024-10-26T05:45:30.143000+00:00

Deployed

```
- Assassinate can now trigger at level 50
- Buffs that effect spell critical damage should now stack
- Hitting level 50 will now automatically grant one class AA
- Main task updated to require level 50 instead of 51
- Weirdness fixed around Echo of the Brood server buff
- Dreadlands Echo is no longer... in places other than Dreadlands <_<
- Fists of Steel renamed to Way of Steel. Way of Steel procs off kicks/strikes and also increases the damage of kicks and strikes the same way Fists of Steel increased h2h damage. Way of Steel does not increase h2h damage.
```

---

## Entry 1300170230915534848
**Author:** Aporia
**Date:** 2024-10-27T18:52:19.045000+00:00

Deployed
```
- All auto granted starting AA now have an AA cost of 0 to allow players to progress total AA count at the same rate.
- Cleric now starts with Purify Soul AA instead of Twincast AA
- Purify Soul is now a 15 minute CD
- Druid now starts with Entrap instead of Paralytic Spores
- Druid and Necromancer no longer start with Critical Affliction AA
- Druid, Necromancer, Enchanter, and Shaman now begin with an innate 3% chance to crit with DoTs
- Enchanter and Shaman now also start with the Destructive Cascade AA
- Shooting a bow/throwing things now levels Offense (thank you Carolus)
- Spell crit chance and bonus now stack correctly (thank you Grek)
- Players no longer autojoin deprecated channels. General, OOC, and AUC are now the preferred global channels (thank you Trust)
- Support, Bug, and LFG channels are now available to new players that join Discord by default
- Warrior and Berserker starting quest item adjusted.
- Bard Discipline Deftdance has had its base CD reduced and now has Hastened AA available
- Updated Consume Item AA description
```

---

## Entry 1300605985504624640
**Author:** Catapultam
**Date:** 2024-10-28T23:43:51.035000+00:00

Deployed
```
- Implemented per-kill AAEXP cap which is informed by: con of mob, level of player. Exp Rate buffs increase this cap.
- Decreased amount of exp needed to improve items to (Enchanted)
- Pet inventory and buffs no longer fade on zone (@Secrets)
- Marsingers 3\4 require Kunark to be unlocked
- Removing classes should now correctly store changes to player profile
- Echo of the Brood now has a small spell haste component
- All auto granted starting AA now have an AA cost of 0 to allow players to progress total AA count at the same rate.
- Cleric now starts with Purify Soul AA instead of Twincast AA
- Purify Soul is now a 15 minute CD
- Druid now starts with Entrap instead of Paralytic Spores
- Druid and Necromancer no longer start with Critical Affliction AA
- Druid, Necromancer, Enchanter, and Shaman now begin with an innate 3% chance to crit with DoTs
- Enchanter and Shaman now also start with the Destructive Cascade AA
- Shooting a bow/throwing things now levels Offense (thank you Carolus)
- Spell crit chance and bonus now stack correctly (thank you Grek)
- Players no longer autojoin deprecated channels. General, OOC, and AUC are now the preferred global channels (thank you Trust)
- Support, Bug, and LFG channels are now available to new players that join Discord by default
- Warrior and Berserker starting quest item adjusted.
- Bard Discipline Deftdance has had its base CD reduced and now has Hastened AA available
- Updated Consume Item AA description
```

---

## Entry 1300929901423231056
**Author:** Catapultam
**Date:** 2024-10-29T21:10:58.608000+00:00

Deployed
```
- Fixed some NPC quest text
- Fixed charm breaks
- Fixed Way of Steel (Nerfed Monks)
- Added additional starting port locations
- Charm spells can be refreshed
- Reduced some annoying noises (@Mith) (REMOVED)
- Autofire\throw can be used while casting bard songs
- Guild Management Window now shows correct classes
- Lifetaps can once again critically heal
```

---

## Entry 1301255542051831931
**Author:** Catapultam
**Date:** 2024-10-30T18:44:57.384000+00:00

Pending
```
- Removing class correctly removes spells
- AAXP settings preserved on zone
- Project Illusion works on all pets
```

---

## Entry 1301273391797506099
**Author:** Aporia
**Date:** 2024-10-30T19:55:53.095000+00:00

Deployed
```
- EoM cost reduced from 5 to 2 for The Mischievous Halfling and the Purveyor of Glamour.
- Death tip now correctly reflects gameplay on THJ.
- New friends added to the campfire.
- Updated website.
- Dragon Trigger in Skyfire no longer incorrectly attacks players
- AA cap for white mobs increased to 6%
- AA scale blue, light blue, and green mobs slightly increased
```

---

## Entry 1301593922492956733
**Author:** Catapultam
**Date:** 2024-10-31T17:09:33.568000+00:00

Deployed

```
- Removing class correctly removes spells
- AAXP settings preserved on zone
- Project Illusion works on all pets
- EoM cost reduced from 5 to 2 for The Mischievous Halfling and the Purveyor of Glamour.
- Death tip now correctly reflects gameplay on THJ.
- New friends added to the campfire.
- Updated website.
- Dragon Trigger in Skyfire no longer incorrectly attacks players
- AA cap for white mobs increased to 6%
- AA scale blue, light blue, and green mobs slightly increased
- Fixes for memory leaks around item improvement and pets (@Secrets)
```

---

## Entry 1302047213064683530
**Author:** Catapultam
**Date:** 2024-11-01T23:10:46.462000+00:00

Deployed 11/1/24.

Welcome to Release.

```
- Added #tim (Toggle Improved Models). Use this command to disable upgraded NPC models if you hate fun.
- Non-Bards can no longer interrupt spell casting by clicking the gem multiple times.

Class Removal
- Vision of Ayonae now requires EoM to remove a class, and has a 7-day initial cooldown. This cooldown will increase by 7 days, permanently, each time it is used on a character.
- When removing a class, invalid skills are also removed.

Abilities
- Improved Frenzy damage scaling based on Primary Weapon
- Improved damage from Way of Steel
- Druid AA Nature's Guardian has had its CD reduced for ranks 5 and 6.
- Ranger AA Bow Mastery works as intended again.
- Lifetap spells can once again crit heal

Misc
- Re-Introduced and fixed 'Hunter' titles
- Item Discovery Broadcasts should filter under 'Experience Messages'
- Custom bazaar NPCs can no longer be mistakenly attacked.
- Fear now causes NPCs to flee again
- Megosh Thistlethorn is back in game but with OoE scripts stripped
- Some quests have had their components/items made lore again.
```

---

## Entry 1302287329112756244
**Author:** Catapultam
**Date:** 2024-11-02T15:04:54.589000+00:00

Pending
```
- Updated Gambling Halfling text
- Cryomancy and and Pyromancy are no longer level restricted
- Bow Mastery fixed frfr
- Mobs should flee when feared now
- Charm spells should overwrite any other Charm spell cast by the same caster on the same mob.
- Adjusted item experience gain
  - clamped exp gain based on tier
  - adjusted exp gain calculation

- Fixed crash related to activating AAs while in a group
```

---

## Entry 1302291165894152242
**Author:** Aporia
**Date:** 2024-11-02T15:20:09.349000+00:00

Deployed

```
- Way of Steel should now display correctly to all monk combos (please remember to patch).
- Halfling Rogue GM text corrected.
- Incorrectly scaled legendary items fixed (improved).
- Certain unusable poison crafting components removed from Bazaar vendor.
- Berserker starting weapon now *actually* a 2hander.
- Compensating measure implemented for bugged starting quests. If you have a bugged starting quest from last night, please remove the quest, relog, go to the fading memory in bazaar, and say "note", then proceed with the quest.
- EoM buffs disappearing under certain circumstances has been resolved.
- Item leveling appearing to pause at certain points has been resolved.
```

---

## Entry 1302321345014534207
**Author:** Catapultam
**Date:** 2024-11-02T17:20:04.612000+00:00

Pending on fresh zone servers
```
- Fixed crash related to moving bag contents
```

---

## Entry 1302710180533899408
**Author:** Catapultam
**Date:** 2024-11-03T19:05:10.224000+00:00

Deployed over last two days, sorry has been crazy;
```
- Updated Gambling Halfling text
- Cryomancy and and Pyromancy are no longer level restricted
- Bow Mastery fixed frfr
- Mobs should flee when feared now
- Charm spells should overwrite any other Charm spell cast by the same caster on the same mob.
- Adjusted item experience gain
  - clamped exp gain based on tier
  - adjusted exp gain calculation

- Fixed crash related to activating AAs while in a group
- Way of Steel should now display correctly to all monk combos (please remember to patch).
- Halfling Rogue GM text corrected.
- Incorrectly scaled legendary items fixed (improved).
- Certain unusable poison crafting components removed from Bazaar vendor.
- Berserker starting weapon now *actually* a 2hander.
- Compensating measure implemented for bugged starting quests. If you have a bugged starting quest from last night, please remove the quest, relog, go to the fading memory in bazaar, and say "note", then proceed with the quest.
- EoM buffs disappearing under certain circumstances has been resolved.
- Item leveling appearing to pause at certain points has been resolved.
- Fixed crash related to moving bag contents

- Fixed memory leak related to loading AA information
```

Known major issues
```
- Item leveling does not work as anticipated via kill-exp. Consuming does work as expected.
- Bazaar is VERY slow when local population over 100
```

---

## Entry 1302710373446586460
**Author:** Catapultam
**Date:** 2024-11-03T19:05:56.218000+00:00

Pending
```
- Characters who are Rangers will display their Bow as their default weapon instead of their melee weapons.
- Discovery of Enchanted items will no longer trigger a world announcement.
```

---

## Entry 1303013816132440124
**Author:** Catapultam
**Date:** 2024-11-04T15:11:42.592000+00:00

Immediate effect
```
- Reduced Exp from Spirocs in Plane of Sky
- Terror, Fear, Dread, and Dracoliche no longer spawn in respawning Plane of Fear instances
- Respawning Instances now have the same lockout DURATION as Static instances

- Parcel purchase from /baz window is now free.
```

---

## Entry 1303422359621079101
**Author:** Catapultam
**Date:** 2024-11-05T18:15:06.950000+00:00

Deployed
```
- New global buff system (Thanks @Secrets)
- Fishing can result in Enchanted and Legendary items
```

---

## Entry 1303442945671692420
**Author:** Catapultam
**Date:** 2024-11-05T19:36:55.047000+00:00

@here

```
- Fixed zone crashes
```

---

## Entry 1303530351636774976
**Author:** Aporia
**Date:** 2024-11-06T01:24:14.253000+00:00

```
- Oracle of K`arnon respawn lowered to 1 hour with a 30 minute variance.
- Sir Lucan D`Lere respawn lowered to 1 hour with a 30 minute variance.
- Marl Kastane respawn lowered to 1 hour with a 30 minute variance.
- Lost Iksar quest text now makes sense.
- Cryomancy and Pyromancy description now correctly reflects that it can be used on spells below level 60.
- Bosses once again correctly spawn inside of non-respawning instances
- Geometry updated for several problematic zones (thanks Trust!)
- Black Block of Ore no longer looks like a book
- Druid spell Protection of Rock now correctly scales again
- Enchanter spell Weakness now correctly stronger than Insipid Weakness
- Necro AA Death Bloom had its health cost and mana regen halved per tick
- Shaman AA Spiritual Blessing is now marked as non dispellable
- Bard AA Funeral Dirge can no longer be resisted
- Warrior AA Warlord’s Resurgence has had its description corrected
- Enchanter spell Boon of the Clear Mind is now correctly tuned between C1 and C2
- EoM Haste once again grants haste V1 and is now correctly applying
- Echo for hate removed from Oasis
- Apothic Kilt (Legendar) now gives correct stats
- Echo for Runnyeye now works correctly
- Echo added to Cazic Thule
- BST AA Gelid Rending can now proc with any weapon
- Cazic Thule no longer despawns under certain unintended conditions
```

Some of these are live, some of these are pending. Trying to iterate quickly to get all your reports addressed.

For a little background, things like this are not necessarily fixed in order of importance- beyond server stability and playability, every report is important.

So, when we have small amounts of time or limited capacity, we bite off little things.

Rest assured, our OCD will guarantee every report gets looked at 🙂

---

## Entry 1303619142045143072
**Author:** Catapultam
**Date:** 2024-11-06T07:17:03.536000+00:00

Deployed 11/6/24

```
- Updated to EQEmu v22.57.1
- Mages no longer lose TEMPORARY items when logged off
- More than 4 proc buffs can simultaneously apply (but no more than 4 will proc in any combat round)
- Necromancers get full damage from Vampiric Embrace
- Dragons are no longer tiny
- Crocodiles are no longer huge
- Spoot remains an asshole
- Shrink and Grow, except specifically pet-targeted, no longer affects NPCs or Pets.
- Echo of Luck works correctly for quest turn-ins.
- Charm can be refreshed?
```

---

## Entry 1303902189189857281
**Author:** Catapultam
**Date:** 2024-11-07T02:01:47.234000+00:00

Deployed 11/7/24
```
- Added Disenchanted Bags
- Charm pets will not clear inventory on refreshing charm
- Fixed clicking off pet buffs
- Shrink\Grow works on pets
- Rabid Bear moved to song window
- Clean up pets on charm break a little better, hopefully resolving intermittent issues with hostile npc seeming to be a friendly
- Marl Kastane should spawn for Shadowknights who need him upon entering Kerra Ridge
- Removed Deity from all items
- Adjusted negative stats on edge case upgraded items
- Pets & Suspended buffs persist through death
- Added more descriptive text to instance offer dialogue
```

---

## Entry 1304647984100806717
**Author:** Catapultam
**Date:** 2024-11-09T03:25:18.597000+00:00

Hotfix 11/8/24 - This requires a fresh zone server until reboot, so only zones which have been closed for 5 mins or longer.
```
- Attempt to fix pet buffs causing periodic frame skips for some users
```

Deployed 11/9/24
```
- Respawning instance lockout lowered to 2 hours.
- Mobs with respawn times longer than 2 hours will not spawn inside Respawning instances.
- Lowered Non-respawning instance lockout to 16 hours.
```

---

## Entry 1304979313254207538
**Author:** Catapultam
**Date:** 2024-11-10T01:21:53.623000+00:00

Hotfix 11/8/24  - This requires a fresh zone server until reboot, so only zones which have been closed for 5 mins or longer.
```
- Attempt to fix 'Invisible Mobs' issue
```

Deployed 11/9/24
```
- Tearal and Son of Tearal can now attune your Bazaar and Back ability to either Bazaar or East Commonlands, respectively.
- Plane of Sky scripts should all work now.
```

---

## Entry 1305270536628338759
**Author:** Catapultam
**Date:** 2024-11-10T20:39:06.686000+00:00

Deployed 11/10/24
```
- Additional fixes for 'Invisible Mobs' issue
- Deployed sharding system for Bazaar (Thanks @Akkadius)
- Misc unstream fixes

- Windstriker has had its proc changed to Lightning Bolt
- Rain Caller has had its click removed and replaced with the same spell (Firestrike) as a proc
```

Notable Known Issues
```
- Using the 'ride along' feature of Bazaar and Back for a group member with a different target zone will result in undefined behavior
```

---

## Entry 1305393437985734676
**Author:** Catapultam
**Date:** 2024-11-11T04:47:28.653000+00:00

Deployed 
```
- Disabled Anti-AFK script in the Bazaar
- Fixed Ride-Along bazaar and back targets
- Charm spells should no longer inappropriately redirect as implied targets.
- ZEM is applied to per-kill aaxp cap
```

---

## Entry 1305908449619607663
**Author:** Aporia
**Date:** 2024-11-12T14:53:56.995000+00:00

Deployed:
```
- Noble Dojorn and Overseer of Air now correctly drop Efreeti War Maul
- Bryn Fynndel now correctly accepts the Shadow Coded Book
- Geometry updated across many zones to fix mobs falling through the world ie Fear - Thank you Trust!
- The frequency of charm pets breaking and aggroing other mobs reduced (faction wars)
- Players now informed why they can't pull a dz when they aren't the leader (because they aren't the leader)
- Charm can *actually* be refreshed in combat now
- Sanguine Mind Crystal and Azure Mind Crystal now behave well with implied targeting
- Mojax can no longer spawn infinite Duggin Scumbers 
- Previously non-resizable windows are now resizable by default
- Glidara Myllar now accepts Warning to Glidara
```

Pending Patch/Reboot:
```
- Warrior AA Gut Punch description fixed
- Certain items that had incorrect stats for their legendary versions have been fixed
- Cleric AA Turn Undead description fixed
```

---

## Entry 1305993720575037471
**Author:** Catapultam
**Date:** 2024-11-12T20:32:47.175000+00:00

Deployed
```
- Pets survive death again (frfr)
- Parcel purchases work again
```

---

## Entry 1306393344519442453
**Author:** Catapultam
**Date:** 2024-11-13T23:00:44.948000+00:00

Deployed
```
- ZEM normalized to 2.0 for zones with ZEM below 2.0
```

---

## Entry 1306665076367036507
**Author:** Catapultam
**Date:** 2024-11-14T17:00:30.869000+00:00

Deployed
```
- Update to EQEmu v22.59.1
- Fix invisible mobs (Thanks @Akkadius - you are the real MVP!)
- Sweaty Bird Farmers rejoice - ported WFH Spiroc Island script (Thanks @Trust)
- Added Secondary usability to Thornstinger
```

---

## Entry 1306853645442224129
**Author:** Catapultam
**Date:** 2024-11-15T05:29:49.240000+00:00

Deployed
```
- Attempt to fix pet illusion targeting (Cannot duplicate on test, theoretical edge case fix)

- Group Incentive Program
 - In the interest of promoting sharing instances for the health of server resources...
 - Respawning Instances are now subject to the same scaling rules as Non-Respawning instances (3+ players adds to mob difficulty)
 - For each expedition member past the second;
   - 25% stronger mobs
   - 25% more XP
   - 25% more AAXP
   - 25% more item Exp
   - 25% chance for each mob to drop an additional set of loot
   - increased chance of legendary rolls
```

---

## Entry 1307044028734378104
**Author:** Catapultam
**Date:** 2024-11-15T18:06:20.154000+00:00

Pending
```
- Fix crash related to additional loot
```

---

## Entry 1307433633753202742
**Author:** Aporia
**Date:** 2024-11-16T19:54:29.229000+00:00

Pending reboot/patch
```
- Monk AA Grappling Strike description corrected.
- Monk AA Destructive Force should now work correctly.
- Putrid Skeletons once again drop Putride Rib Bone for Monk Sash quest
- Cazic Quill and Jagged Diamond Dagger can now be quested above their base version
- Many misc item fixes
- Highpass safe location no longer puts you outside the map (fixes evac in zone).
- Wizard AA Cryomancy and Pyromancy buffs should now stack. Only one can trigger at a time.
- Malka Rale should now spawn more often for Rogue Epic
- Monk AA Way of Steel description corrected.
- Greenmist SK armor has been added back to loot tables in PoFear.
- Druid AA Nature's Guardian HP and AC increased.
- Denise Songweaver in PoSky now expects the correct items for the Bard Test of Tone
- Warrior AA Battle Leap description corrected
- Grandmaster H'Qilm has had their spawn rate increased to match the rest of Hate named.
- All Echo of the Past are now immune to all player damage.
```

---

## Entry 1307724713937862677
**Author:** Catapultam
**Date:** 2024-11-17T15:11:08.153000+00:00

```
- Pet illusion wands should work as expected. You may need to resummon any necro pets.```

---

## Entry 1307944944706650153
**Author:** Aporia
**Date:** 2024-11-18T05:46:15.260000+00:00

```
- Pets can once again be summoned in PoSky
- Ranger AA Precision of the Pathfinder description updated.
- Veteran's Wrath AA description, updated.
- Formula changed on Cinda's Charismatic Carillon and negative resist mod added
- Echo's learn to spell better
- Sirran will now accept key items regardless of what island he is on.
- Spiroc Lord will now stay dead if Guardian is dead
- Bags can now be sent through parcel (money still cannot).
```

---

## Entry 1308440149453049907
**Author:** Aporia
**Date:** 2024-11-19T14:34:01.272000+00:00

```
- Cazel now always drops his spoon.
- Echo of the Past now available in Kithicor.
- Echo of the Past now available in Rathe Mountains.
- Significantly increased performance in zones over time.
- Sending plat via the parcel is working again! (Thank you Neckkola!)
```

---

## Entry 1308919463030165574
**Author:** Aporia
**Date:** 2024-11-20T22:18:38.534000+00:00

Implemented:
```
- Many AA descriptions have been updated to provide more information (thank you Alebrije!)
- Bard aggro from songs has had its aggro reduced to 25% of its former cap.
- Extended EXP bonus turned off.
- Grand Master Lozz no longer speaks of Apocryphal things.
- Kurn's Tower DZ no longer drops you in the middle of the zone (lol sorry)

```

Pending Patch/Reboot:
```
- Wizard AA Improved Familiar now correctly summons a drake instead of a baby skeleton on rank 3 and 4
- Form of the Black wolf illusion now matches Spirit of the Black Wolf duration.
- ENC AA Mana Draw recast set on spell to match AA to avoid odd CD interactions.
- Several Legendary items missing Heroic stats have been fixed.
- All NPCs with a spawn time of > 1 hour, that don't have their own DZ, and are needed for epic quests have had their spawn time reduced to 1 hour.
- The following starting cities have had these NPCs receive Parcel training!

- Antonica
(West) Freeport: Lindie Rains
Grobb: Grallvek
Halas: Grots
Neriak - Commons: Lynsalai
Oggok: Klob Pulp
Rathe Mountains: Zok Malka
Rivervale: Teelie Meegles
South Qeynos: Ren Pinemyer
Surefall Glade: Grathin Nilm

- Faydwer
AkAnon: Zenrel Ottonoggin
Greater Faydark: Merchant Vaelias
Northern Felwithe: Laernian Caelael
North Kaladim: Marsha Stonepenner

- Odus
The Erudin Palace: Sparlus Penfold
Paineel: Henly Nictropus

- Kunark
East Cabilis: Klok Faziz

- Luclin
Shar Vahl: Laanas Sejiir

- All Soulbinders are now immune to player damage
- Important NPCs in EC tunnel are now immune to player damage
```

We are planning on a reboot tomorrow morning or afternoon to bring live pending and new changes.

Many good things in the works!

---

## Entry 1309582982549602315
**Author:** Catapultam
**Date:** 2024-11-22T18:15:13.915000+00:00

Deployed
```

- Adjusted SPA 294 (SE_CriticalSpellChance) to no longer stack its critical damage modifier, as originally intended)
- Adjusted AA "Destructive Fury" to use SPA 155 (SE_SpellCritDmgIncrease) to increase critical damage directly.
- Added AA "Destructive Fury" to Wizards
- Adjusted AA "Arcane Destructive Fury to use SPA 155 (SE_SpellCritDmgIncrease) to increase critical damage directly.
- Reduced Crit Damage Bonus from "Arcane Destructive Fury" to 10% per rank 
- Adjusted Spell "Improved Familiar" to use SPA 155 (SE_SpellCritDmgIncrease) to increase critical damage directly.
- Adjusted Spell "Spirit of the Black Wolf" to use SPA 155 (SE_SpellCritDmgIncrease) to increase critical damage directly.

- Implemented 1x/char AA reset on Vision of Aayonae.
- Implemented 1x/char free class change on Vision of Aayonae.

- Fixed error preventing Melee Damage Bonus spell effects from working.
- Being over-cap on unused AA no longer results in AA loss, only the inability to earn additional AA
- SE_MeleeLifetap now works with Ranged and Throwing attacks

- All Expedition locks have been reset.
```

---

## Entry 1309678834458562560
**Author:** Catapultam
**Date:** 2024-11-23T00:36:06.791000+00:00

Deploying
```
- Corrected logical error preventing Base Crit Damage Ratio from applying
- Temporarily disabled 1x/char AA reset on Vision of Aayonae.
```

---

## Entry 1310448565931474955
**Author:** Aporia
**Date:** 2024-11-25T03:34:45.075000+00:00

Deployed
```
- Several instantly spawnable quest NPCs are no longer attackable.
- Cleric epic returned to primary only. This is a tradeoff for having the same proc as the level 50 summoned hammer
- Berserker epic had stats rebalanced for Kunark/Velious era.
- Fixed edge cases where group heals wouldn't heal pets.
- Echo for Chardok moved inside of Chardok
- Echo added for Warslik Woods
- Echo added for Burning Wood
- Echo added for Lake of Ill Omen - Echo added for Overthere
- Echo added for South Karana
- Respawn time reduced on a sleeping ogre
- Respawn time reduced on Verina Tomb
```

---

## Entry 1310651946822013050
**Author:** Catapultam
**Date:** 2024-11-25T17:02:54.858000+00:00

Deployed (Client Patch)
```
- Increased zoom-out distance (thanks @iamclint)
- Implemented /fov command to adjust field-of-view; 45 (default) - 90 (thanks @iamclint)
- Potentially fixed Crash-on-Zone into certain zones such as HateplaneB and Bazaar
```

---

## Entry 1310692059795034183
**Author:** Aporia
**Date:** 2024-11-25T19:42:18.536000+00:00

```
- Echo added for Lake Rathe
- Crag spiders look less human and more spider|
- More LoY items tuned down to be between Kunark and Velious loot
```

---

## Entry 1311249916022100048
**Author:** Catapultam
**Date:** 2024-11-27T08:39:01.825000+00:00

Deployed
```
Client Plugin:
- Fixed client memory leak in map
- Targeting mobs from map is limited distance (50 units) or Line of Sight.
- /mapfilter custom will only show mobs you can see the names of
- You now use the highest tracking skill of anyone in your group to evaluate mobs-on-map name visibility

Epics:
- Added 2H versions of Innoruuk's Curse and Fiery Avenger.
- Added 'Change Stance' click effect on Innoruuk's Curse and Fiery Avenger to shift between 1H and 2H forms.
```

---

## Entry 1311563335329779764
**Author:** Aporia
**Date:** 2024-11-28T05:24:26.811000+00:00

Pending Reboot/Patch:

```
- Vessel Drozlin respawn lowered to 1hr.
- Hastened Celestial Hammer AA adjusted and re-enabled.
- Rogue/Monk Strikethrough AA display bug fixed
- Echo added to OoT
- Echo added to Droga
- Echo added to Nurga
- A Mischievous Halfling now has Thanksgiving food and drink!
```

---

## Entry 1312210013049061387
**Author:** Aporia
**Date:** 2024-11-30T00:14:06.794000+00:00

```
- Scale armor and other chain like armor with missing graphics should now be fixed
- Hastened Celestial hammer has had its pre-requisites removed
- Many AA descriptions updated (thank you Alebrije)
- Misc quest fixes
- Echo added to Kaesora
- The Tangrin respawn time reduced
- Account actions taken around custom Macro Quest sources.
- Turkeys are no longer lore, but are now no-drop 
- Pumpkin Spice Latte is now no-drop
- Turkeys and Pumpkin Spiced Lattes now have a rare chance to drop from enemies until Sunday night
- Echo added to Highpass (I couldn't trust rogues to play nice...)
- Quest EXP temporarily disabled
```

---

## Entry 1312479580904362005
**Author:** Catapultam
**Date:** 2024-11-30T18:05:16.779000+00:00

Deployed
```
(Client Update, DEPLOYED)
- Experimental Fix for 'You can't use that command right now...` while spamming Disciplines
- Even Better fix for 'You can't use that command right now...` while spamming Disciplines
- Doubled Target Range on Map.
- Improved Map performance.

(Server Update, DEPLOYED)
- Prevent slow effects from causing uninitialized skill timers to be set to ~80 years in the future
- Situational Awareness AA adjusted to provide effective skill instead of actual 'skill points'.
- Haste now displays on a scale starting at 0%.
- Haste is no longer over-applied to activated Melee skills (Kick, Bash, Backstab, Frenzy, etc).
- Moved several previously unfilterable combat messages (Master Wu, Strikethrough, Stun) to Skills chat-window filter. Options filter window is unchanged.
- Dispel should no longer trigger a lag spike for some players.
- Pets will prioritize equipping items in their primary and secondary slots ahead of any other slots.

(Quests, DEPLOYED)
- The Polymorphist will now allow you to change Deity.
- The Polymorphist will now allow you to 'reset' a pet name, so a new random static will be generated the next time you summon that pet type.
- Solomen will now respond to his linked prompt.
- Tomekeeper Dahl will no longer eat items turned in by non-Monks.
- Deep will no longer eat items turned in by non-Monks (@Grek)
```

---

## Entry 1312621082380992636
**Author:** Aporia
**Date:** 2024-12-01T03:27:33.360000+00:00

```
Option added to Omat Vastsea's quest script to summon back Natasha to make it easier for players who ran into issues during the Cleric epic to fix their quest state.

By saying "I wish to see Natasha", you can trigger a spawn of Natasha. Who is now immune to player damage.

Thank you Grig
```

---

## Entry 1312645296576135229
**Author:** Aporia
**Date:** 2024-12-01T05:03:46.474000+00:00

```
Rejoice.
- /friend works correctly again

Rejoice harder.
- /ignore works correctly again

(Thanks Akk!)
```

---

## Entry 1312932176060223628
**Author:** Catapultam
**Date:** 2024-12-02T00:03:43.873000+00:00

Deployed
```
- Combat Skill activation should no longer impose a 1-second cooldown on other skills.
- Adjusted Map targeting range again
- Doubled Tracking\Situational Awareness range for mobs that you have LoS on
- Cleaned up parsed spell information for SPA relevant to Sympathetic Healing
(If you are interested in helping to clean up the spell parser in general, and are comfortable working with C-Strings, hit me up! There's a pile of EOM)
```

---

## Entry 1313142732813766719
**Author:** Catapultam
**Date:** 2024-12-02T14:00:24.515000+00:00

Deployed
```
- Experimental fix for those crashing on logging\zoning into the Bazaar
```

---

## Entry 1313276869738631230
**Author:** Catapultam
**Date:** 2024-12-02T22:53:25.250000+00:00

```
(Quests, Deployed)
- Re-enabled 'Slayer Titles'
- Various fixes to Toirgan Mines scripts (@Trust)
- Various quest and script fixes (@Grek)
- Various quests and script fixes (@Trust)
```

---

## Entry 1313560375739941017
**Author:** Catapultam
**Date:** 2024-12-03T17:39:58.348000+00:00

12/3/24

Pending Reboot & Patch
```
- Corrected Hoshkar AoE to apply a sane slow effect, instead of a negative attack speed
- Para Dar's Slow AoE is now curable.
- Corpse decay time will never be longer than the respawn time of the mob.
- Hunter's Fury should no longer block Trueshot Discipline
```

---

## Entry 1314128377191465030
**Author:** Catapultam
**Date:** 2024-12-05T07:17:00.447000+00:00

Deployed
```
- Fix for crash-on-zone for some clients
```

---

## Entry 1314426106375573516
**Author:** Catapultam
**Date:** 2024-12-06T03:00:04.616000+00:00

Deployed (-ish)
```
- Fixed 'Spells are 255 until you zone once'
- Possibly fixed some pets poofing on server-down (Sorry, it won't work on the next server-down, probably)
- Disc timers are no longer transferred to new characters when you camp to character select and switch toons
- Spell Procs added by buffs must be unique (@Grek)
- Potentially fixed client memory leak causing collidable objects to no longer be collidable
```

---

## Entry 1314802696938586153
**Author:** Catapultam
**Date:** 2024-12-07T03:56:30.803000+00:00

Deployed (Client Patch)
```
- ACTUALLY FIXED NOCLIP OBJECTS (Thanks @Bakemono for enormous troubleshooting help)
```

---

## Entry 1314840330230566975
**Author:** Catapultam
**Date:** 2024-12-07T06:26:03.279000+00:00

Rolling Deployment (Will show up in zones other than the bazaar as time goes on, after reboot will be effective everywhere)
```
- Adjusted spell damage messages to show spell, and pet owners.
- Adjusted DoT damage messages to be normal non-melee hits
- Potentially fixed Explorer path progression quests not unlocking flags reliabily
```

---

## Entry 1315148539457703938
**Author:** Aporia
**Date:** 2024-12-08T02:50:46.085000+00:00

Deployed:

```
- Extended Ingenuity AA has been enabled for Bards
- Bladed Song is now unresistable and has had a second rank added.
- Dance of Blades, Bladewhirl Proc now has a -100 chromatic check on landing. It's AC shred and resist debuff now scales with level.
- Funeral Dirge now increases physical damage taken by 10/15/20% and has had its duration doubled
- Hastened Funeral Dirge AA is now available (5 Rks) putting Funeral Dirge down to 10 minutes at max level
- Song of Stone has had its pet stats increased significantly and its cooldown reduced significantly

These changes were made to reinforce the support nature of the Bard and its viability across multiple builds.

Thank you for your patience as we continue to try navigate player feedback!
```

---

## Entry 1315352052188184646
**Author:** Catapultam
**Date:** 2024-12-08T16:19:27.301000+00:00

Deployed
```
Quests
- Revamp of 'Thieves Aboard the Ship' event (Thanks @Trust)
- Plane of Sky keys are no longer removed from inventory when leaving the zone (Thanks @Trust)

Bug Fixes
- Apply MeleeLifeTap to Archery damage
- Temporary Stun Immunity after being stunned now correctly applies to non-spell stuns.
- Flags should be consistent between different zones.
- Worn ATK is no longer double-counted under certain circumstances.

Misc
- Bonus AAEXP from Veterancy will now give feedback indicating when the bonus will end.
- Bonus AAEXP from Veterancy is now applied after the per-kill AAEXP cap.
- Revamped Healing messages
- Revamped Rune messages
```

---

## Entry 1315454822505517128
**Author:** Catapultam
**Date:** 2024-12-08T23:07:49.654000+00:00

Hotfix
```
- Reduced maximum veterancy bonus from 5x to 3x AAEXP
```

This impact of the change allowing Veterancy to apply AFTER the per-kill cap was significantly greater than appeared in testing. This change will still result in overall higher AAEXP rates than prior to the most recent patch.

---

## Entry 1315493798641401887
**Author:** Catapultam
**Date:** 2024-12-09T01:42:42.289000+00:00

Rolling Deploy (Requires new zone server; new DZ does not guarantee this)
```
- Corrected Veterancy scaling formula to correctly function near the end of the scaling range
```

---

## Entry 1316279399741657161
**Author:** Catapultam
**Date:** 2024-12-11T05:44:24.187000+00:00

Rolling Deploy (Requires new zone server; new DZ does not guarantee this)
```
- Fixed SE_GiveDoubleRiposte (Knave's Return Stab, Furious Refrain, Return Kick, etc)
- Probably fixed UCS problems again (thanks @Akk)
- Removing a class no longer removes spells you can still use due to other classes
- Removing a class unequips items which are no longer usable
```

---

## Entry 1316438968958455849
**Author:** Catapultam
**Date:** 2024-12-11T16:18:28.453000+00:00

```
- Removed Class Requirements from all epic quests (Thanks @Prymetyme)
```

---

## Entry 1316571786611261500
**Author:** Catapultam
**Date:** 2024-12-12T01:06:14.649000+00:00

Consolidated Changelog

```
- Corrected Veterancy scaling formula to correctly function near the end of the scaling range
- Fixed SE_GiveDoubleRiposte (Knave's Return Stab, Furious Refrain, Return Kick, etc)
- Probably fixed UCS problems again (thanks @Akk)
- Removing a class no longer removes spells you can still use due to other classes
- Removing a class unequips items which are no longer usable
- Removed Class Requirements from all epic quests (Thanks @Prymetyme)
```

Rolling Deploy (Requires new zone server; new DZ does not guarantee this)
```
- Detrimental Sympathetic procs should no longer target their caster under any circumstance
```

---

## Entry 1317508462522925087
**Author:** Catapultam
**Date:** 2024-12-14T15:08:15.589000+00:00

12/14/24

Bug Fixes
```
- Implemented experimental change to fix the 'no cast bar' bug. This MAY reintroduce a worse bug, but looks good in brief testing. Please report any instances of randomly not being able to cast or perform certain other activities.
- All starting AA now cost 0 points; this may cause your current 'spent' AA total to decrease when it is next updated.
- Significantly reduced the complexity of checking for bard song auto-refresh
- Poisons are no longer equippable.
- Removed several remaining class checks on epics.
```

New Features
```
- The Purveyor of Glamour will create Glamour-Stones (Transmog Ornaments) for Armor!
  - NOT Hero's Forge.
  - Works with modern & legacy player models
  - 5Kpp + sacrificial item
  - Not Dyable

- Removed tradeskill recipe for Vial of Prismatic Dye
- Added Vial of Prismatic Dye to Augs merchant in Bazaar
- Adjusted Vial of Prismatic Dye pricing (Sell from vendor @ 50k, Buy from vendor @ 100p)

- The Purveyor of Glamour will now create 'Hero's Forge' style Armor Glamour-Stones!
  - Generated through 'custom work' randomization system
  - 2 EoM each, tradable.

- The Vision of Ayonae can now reset your AA!
  - Each character gets one free reset
  - Subsequent resets cost 10 EoM and incur a stacking 7 day cooldown (identical to dropping a class)

- Added Petamorph Wands: Wrulon, Phoenix (Red, Blue), Telmira, Stoneworker, Giant Ant, Gorilla, Crushbone Orc, Lightning Dervish, Lava Dervish, Stone Dervish
- Pets will spawn using the appearance of any equipped Petamorph Wands
```

The Vial of Prismatic Dye changes are likely going to be something that many people disagree with. We are choosing the take a different experience for armor appearance customization on this server vs official or other emulated servers. I feel that armor dyes are a 'quick and dirty' solution that allows getting whatever appearance you want quickly and easily, and removes a lot of the fun in finding the exact combination of gear to achieve the look you want. Transmog accomplishes this better, and serves as a plat sink that we definitely need. However, I am leaving Dyes in-game, for those who do want to use that shortcut, with an additional plat sink component.


Additionally, for those who do not want to deal with Heros' Forge armor appearances, please remember they can be disabled in the Options menu.

---

## Entry 1317579139951235225
**Author:** Catapultam
**Date:** 2024-12-14T19:49:06.401000+00:00

DEPLOYED
```
- Added 10 titles for prolific Gamblers.
```

---

## Entry 1317589922177093672
**Author:** Catapultam
**Date:** 2024-12-14T20:31:57.084000+00:00

```
- Added title for owning a Vial of Prismatic Dye
```

---

## Entry 1318237038197342208
**Author:** Catapultam
**Date:** 2024-12-16T15:23:21.566000+00:00

```
- Glamour-Stones now have teal names.
- Added `missingspells` argument to `/outputfile`. Use like `/outputfile missingspells [filename]` (where `filename` is optional) to output a level-sorted list of spells to a file in your EQ directory. File name defaults to `<character>-MissingSpells.txt`. (Thanks @dannuic)
```

---

## Entry 1318262438977736856
**Author:** Catapultam
**Date:** 2024-12-16T17:04:17.584000+00:00

ROLLING DEPLOYMENT (Will be inconsistent which zones this works on until next reboot. Do not expect bazaar to be effected)
```
- Unattuner should now function again
```

---

## Entry 1319751613853859863
**Author:** Catapultam
**Date:** 2024-12-20T19:41:44.542000+00:00

Consolidated Changelog
```
- Unattuner works again
- Added 10 titles for prolific Gamblers.
- Added title for owning a Vial of Prismatic Dye
- Glamour-Stones now have teal names.
- Guild Names and permissions should now propagate to all zone servers correctly.
- Additional perfomance improvements around Bard Songs.
- Pets which you cannot cast no longer survive your death (the same as buffs).


 - Creatures all across Norrath, Luclin, and the Planes have come into possession of Strangely Wrapped Gifts
 - Strange Elves from beyond this world have appeared in the Bazaar and EC Tunnel, seeking these gifts.
 - Do you open them? Or return them?

```

---

## Entry 1320263658823221339
**Author:** Catapultam
**Date:** 2024-12-22T05:36:25.576000+00:00

Small WIP Changelog...
```
- Reworked Clockwork Banker & Resupply Agent Tools
 - No longer uses a pet slot
 - Summoned for 15 minutes or until owner leaves the zone
 - Can only summon one of each type at a time
```

---

## Entry 1320539762389422122
**Author:** Aporia
**Date:** 2024-12-22T23:53:33.796000+00:00

Deployed

```
- Paladin AA Blessing of Life Rk 2 and 3 now available for an increased base heal amount and proc rate.
- Paladin AA Healing Light Rk 2 and 3 now available for an increased proc rate (up to 30%)
```

Deployed
```
All single target Paladin stun spells now have a small damage component to proc Sympathetic Strike.
```

---

## Entry 1320638822970687630
**Author:** Catapultam
**Date:** 2024-12-23T06:27:11.679000+00:00

Deployed
```
- Shadowknight pets now have their own unique spells
 - Each has (SHD) appended to the spell name
 - New scrolls added to Bazaar spell vendors
 - Vision of Ayonae can help you unmem spells (say 'unmem') if you have a now-uncastable spell memorized.
```

---

## Entry 1320912696492691486
**Author:** Catapultam
**Date:** 2024-12-24T00:35:28.215000+00:00

This is also Deployed.

---

## Entry 1321019345039790141
**Author:** Catapultam
**Date:** 2024-12-24T07:39:15.210000+00:00

The below is deployed on THJ Test Server and is available for further testing.

Merry Christmas?

```
New:
- Added per-class pet bags. See bag vendor in the Bazaar. If you choose not to use a pet bag, no item reimbursements will be given for lost items.
- Reworked NPC hand-ins, it should now be impossible to hand an item to an NPC and have it eaten (other than pets without a pet bag).

Removed:
- Enchanter pets will no longer hand back items given to them. Use the Enchanter's Syncrosatchel to equip your pet or rely on vanilla charm-gear mechanics.

Bug Fix:
- Corrected bug applying spell damage\crit incorrectly to pets
- Corrected bug preventing heal amount from being applied to pet procs
- Corrected bug preventing spell damage from being applied to pet DoT procs
- Pets using 2h weapons no longer reduce added damage by 1/2

Adjusted:
- Pets now inherit their owner's spell damage, heal amount, critical spell damage and critical healing on procs\spells, split evenly between all (non-swarm) pets owned by their owner.
- Pets with 2H weapons equipped no longer equip an offhand.
- Pets use equipped weapon delay instead of standard NPC delay.
```

---

## Entry 1321237072048033833
**Author:** Catapultam
**Date:** 2024-12-24T22:04:25.374000+00:00

New **TEST** build
```
New:
- Added per-class pet bags. See bag vendor in the Bazaar. If you choose not to use a pet bag, no item reimbursements will be given for lost items.
- Reworked NPC hand-ins, it should now be impossible to hand an item to an NPC and have it eaten (other than pets without a pet bag).

Removed:
- Charmed pets will no longer hand back items given to them. Use a Syncrosatchel to equip your pet or rely on vanilla charm-gear mechanics.

Bug Fix:
- Corrected bug applying spell damage\crit incorrectly to pets
- Corrected bug preventing heal amount from being applied to pet procs
- Corrected bug preventing spell damage from being applied to pet DoT procs
- Pets using 2h weapons no longer reduce added damage by 1/2
- No-Rent\TEMPORARY bags should now correctly be replaced by their disenchanted versions instead of destroying their contents.

Adjusted:
- Pets now inherit 50% of their owner's spell damage, heal amount, critical spell damage and critical healing on procs\spells.
- Pets with 2H weapons equipped no longer equip an offhand.
- Pets use equipped weapon delay instead of standard NPC delay.
```

---

## Entry 1321688812581027932
**Author:** Catapultam
**Date:** 2024-12-26T03:59:28.710000+00:00

Rolling log for *TEST* while I get velious ready.... Final patch notes will be re-posted prior to Velious launch.
```
New:
- Added per-class pet bags. See bag vendor in the Bazaar or Shady Swashbuckler in EC Tunnel. If you choose not to use a pet bag, no item reimbursements will be given for lost items.
- Reworked NPC hand-ins, it should now be impossible to hand an item to an NPC and have it eaten (other than pets without a pet bag).

Removed:
- Charmed pets will no longer hand back items given to them. Use a Syncrosatchel to equip your pet or rely on vanilla charm-gear mechanics.

Bug Fix:
- Corrected bug applying spell damage\crit incorrectly to pets
- Corrected bug preventing heal amount from being applied to pet procs
- Corrected bug preventing spell damage from being applied to pet DoT procs
- Pets using 2h weapons no longer reduce added damage by 1/2
- No-Rent\TEMPORARY bags should now correctly be replaced by their disenchanted versions instead of destroying their contents.
- Pets should no longer be deleted for players who are logged on as the server goes down.
- Berserker Disciplines should no longer be removed when dropping (non-Berserker) classes.
- Spells that you can no longer cast because of deleveling are no longer removed when dropping classes.
- Sympathetic Procs will no longer trigger twice for one of your pets.
- *Most* pets may once again be shrunk. Some are buggy still, working on it.

Adjusted:
- Pets now inherit 50% of their owner's spell damage, heal amount, critical spell damage and critical healing on procs\spells.
- Pets with 2H weapons equipped no longer equip an offhand.
- Pets use equipped weapon delay instead of standard NPC delay.
- Pets base damage is normalized to their new attack delay.
- Pets directly add their equipped weapon damage to their attacks.
- Syncrosatchels increased to 4 slots.
- TEMPORARY items will not expire while logged off if you can summon that item via a spell in your spellbook. (Or, for now, are a Magician)
- All spells should be deletable from spellbook (Requires additional client patch)

Misc:
- Progression targets for Luclin unlock have been finalized; Zlandikar, Klandikar, Wuoshi, Kelorek'Dar, and Dozekar the Cursed
```

---

## Entry 1323104912036462603
**Author:** Catapultam
**Date:** 2024-12-30T01:46:33.130000+00:00

```
Added:
- Urthron's Ultimate Unattuner has been added for sale from Gemcrafter Anuk
- Gnomish Quadramorphic Combinerator has been added for sale from Gemcrafter Anuk
- Vial of Prismatic Dye has been added for sale from Gemcrafter Anuk

Adjusted:
- Donal's Chestplate of Mourning now casts regular Complete Heal with a 30 second recast
- Melodic Breastplate clicks at level 1.

UX:
- Pets will no longer accept a Syncrosatchel which is traded to them.

Bug Fixes:
- Turn-ins with multiple identical items will once again function (@Akk)
- Recovering Parcels will no longer require an open top-level inventory slot (Thanks @Neckkola)
- Items with charges will no longer be interpreted as stacked items for quest turnins. (@Akk)
- Restored No-Rent\Temporary item timer to 1800 seconds (was set to 1 second for debugging, which made it to prod)
- Non-Mages who can summon an item will find that those items are much more permanent.
- Corrected model for velium spiders in Velketor's Labyrinth
- Corrected model for crystal golems in Velketor's Labyrinth
- Corrected model for gargoyles in Velketor's Labyrinth
- Corrected model for Velketor the Sorcerer
- Corrected model for Snow Cougars
- Corrected a script error in Dain Frostreaver IV
- Thunder Spirit Princess will once again accept 10 gold
- Fixed zone crash on conning mobs in some edge cases
- Fixed zone crash on handing items to pets in some edge cases
- SE_FadingMemories no longer applies to the caster of the effect instead of the target when applied to an NPC.
- Pets are cleaned up on death once more
- Fixed bad plat handling on Purveyor of Glamour and a few other NPCs
- Tradeskill combines will display skill-up messages.
- GM Training will display skill-up messages.
- Custom Helms will now return the correct quality
- Reworked Tunare encounter (@Trust)
- Reworked Bristlebane encounter (@Trust)
- Reworked TOFS mirrors and keys (@Trust)
- Added DZs for TOFS, CC, Iceclad
```

---

## Entry 1323409018273923123
**Author:** Catapultam
**Date:** 2024-12-30T21:54:57.707000+00:00

I am a generous god.
```
- The Vision of Ayonae will now allow you to reduce your level, and return to up to your previous maximum level. This service costs 500pp per level changed.
```

---

## Entry 1323713355206234286
**Author:** Catapultam
**Date:** 2024-12-31T18:04:17.286000+00:00

```
- Experimental change for /baz crash
- Experimental change for crash-on-zone
```

---

## Entry 1323716631951577148
**Author:** Aporia
**Date:** 2024-12-31T18:17:18.523000+00:00

```
- Enchanter AA Mana Draw now has a 10 minute CD with Rk3 Hastened Gathering
- The Sleeper will no longer reset his HP to full when he roars.
- The Sleeper will now despawn his adds from phase 4 if a player dies and re-engages at full health.
- Misc Faction fixes (Thanks Trust!)
```

---

## Entry 1324047001591091262
**Author:** Catapultam
**Date:** 2025-01-01T16:10:04.783000+00:00

```
- Implemented limit of 599 total active traders to work around client bug (More comprehensive workaround to come)
```

---

## Entry 1324112534776713266
**Author:** Aporia
**Date:** 2025-01-01T20:30:29.112000+00:00

Out of respect for player time and expected engagement, the following changes have been made:

```
- Non raid bosses in ToV have had their HP reduced.
- Thifling Focuser's in PoG have had their HP reduced.
```

---

## Entry 1324929653957328956
**Author:** Catapultam
**Date:** 2025-01-04T02:37:25.506000+00:00

```
New:
- The Heroes' Journey patcher will now automatically back up your UI configurations and detect when they have become corrupted. (Thanks @Xackery!)

Adjustments:
- Bristlebane has been rebalanced
- Gaining XP while at AAXP cap no longer sets percentage of XP assigned to AA to 0%.

Bug Fixes:
- Countless script fixes (Thanks @Trust!)
- Traders should now be cleaned up if a zone server crashes (@Neckkola)
- Fixed a memory leak in pet bags
- All Handin quests should now work

```

Additionally; it is now possible for us to update quest scripts to allow handing in stacks at a time. This requires reworking the script, however, and so will not be a global change.

We are crowdsourcing quests which would benefit from this treatment -> [Here](https://docs.google.com/document/d/1D-BxDDT6pFQHfxA6dcqdbxU9f2mMFgvtZbTvMomF47E/edit?tab=t.0)

---

## Entry 1327449601371934735
**Author:** Aporia
**Date:** 2025-01-11T01:30:47.788000+00:00

Pending Patch:

```
- Burned Out Lightstone no longer glows so bright
- Echo of the Past should now be findable
- Lioness Matriarch and Lion Patriarch can now drop Lion Skins in addition to pelts. (Fleeting Quiver seekers rejoice)
- Killing Dozekar the Cursed now correctly spawns A Faded Memory
- Killing Kelorek`Dar now correctly spawns A Faded Memory
- Paladins now have access to the Shield Specialist AA
- The Shield Specialist AA has been increased for Warrior and Paladin to increase auto attack damage with your primary weapon by 20/40/60/80/100%
- Paladins now have access to the Holy Shield AA (The Paladin's shield is imbued with holy light increasing the Paladin's chance to proc all effects and allows the Paladin to cloak themselves in a runic shield while fighting. Requires maximum rank in Shield Specialist.)
- The Vicious Smash AA has had its effect doubled.
- A Tribute Master has been added to EC Tunnel
- Certain legendary items have had their missing stats added back.
- The Endless Cookie Platter now let’s you know that you do, indeed, summon a cookie.
- Updated description of Paladin Discipline Holyforge to indicate its effect against *all targets*. (This was always the case, most people just didn’t know.)
- Snarla the Fang now gives the correct faction
- Druid AA Wrath of the Wild tooltip has been updated to reflect its current implementation: “This ability will shield you with a charge based, large damage barrier of thorns. When each charge is consumed there is a chance to grant the player an additional blessing: Protection of the Spirit Wolf.”
- Enchanter AA Hastened Edict of Command has had Rk 1/2/3 added to the game. Rk3 brings the CD of Edict down to 30 minutes.
- Berzerker AA Hastened Savage Spirit is now available with the final rank bringing its CD to 20 minutes.
- Rogue AA Hasty Exit has had ranks added bringing its final CD to 5 minutes.
```

---

## Entry 1328923023532752966
**Author:** Catapultam
**Date:** 2025-01-15T03:05:39.006000+00:00

```
- The Polymorphist now allows you to set custom pet names
  - Default pet names have been reset as part of moving to new pet name system
- All Polymorphist services may now be purchased with platinum.

- Purchasing via Parcel from Bazaar now adds parcel tax once again
- Bazaar trader cap lifted.
- Traders not in-zone will display as 'Bazaar Shard N' where N is the shard where they are located

- Kerafyrm encounter adjusted.
- Wizard Familiar spells no longer spawn a flappy
- Cycle Pet\Self hotkey will now cycle between all pets (@Salty)
- Removed servers other than THJ from server list (@Splose)

- Blinded By Fury is now a short-duration buff that is not suspend-able.
- Frenzy Weapon Scaling is now sum of Primary + Secondary
- Added Tunable to Frenzy Weapon Scaling (default same value as before)
  - FrenzyScaleOnWeaponAmount
- Added Monk Kick\Strike weapon damage scaling and tunable.
  - MonkScaleOnWeaponAmount
- Added Monk Kick\Strike Hand\Foot damage scaling and tunable
 - MonkScaleOnHandFeetQuality
```

---

## Entry 1328936987754889247
**Author:** Catapultam
**Date:** 2025-01-15T04:01:08.336000+00:00

BONUS CHANGELOG
```
- Lokar To`Biath in neriakc now accepts stacks of items.
- Lashun Novashine in North Qeynos now accepts stacks of items.
- Captain Tillin in South Qeynos now accepts stacks of items.
- Captain Bosec in Highkeep now accepts stacks of items.
- Trooper Mozo in Cabilis now accepts stacks of items.
- Pandos Flintside in West Freeport now accepts stacks of items.
- Niola Impholder in South Felwithe now accepts stacks of items.
```

---

## Entry 1329263425905229878
**Author:** Catapultam
**Date:** 2025-01-16T01:38:17.256000+00:00

NINJA CHANGELOG
```
- Polymorphist now properly accepts EoM
```

---

## Entry 1329465177497665590
**Author:** Aporia
**Date:** 2025-01-16T14:59:58.584000+00:00

Pending Reboot:

```
- Typhoon Breath has had its curse counters cut in half and it's cooldown tripled. 
```

---

## Entry 1329893093335371877
**Author:** Catapultam
**Date:** 2025-01-17T19:20:21.670000+00:00

CHANGES

```
- Kerafyrm event adjusted.
  - Typhoon Breath has had its curse counters cut in half and it's cooldown tripled. 
  - The Warders have been reintroduced to the pool of potential adds for the ecnounter.
- Fixed missing 'the Naughty' and 'the Grinch' titles
- Fixed Double\Triple attack not working for Throwing
- Rysva To`Biath will now allow completion of the Book of Scale quest
- Instant-Cast clickies can be activated while singing bard songs (@Zimp)
- Improved logic around rune stacking with regard to bard songs (@Zimp)
- Reverted change that resulted in bags not being able to be sold back to EoM vendor
- Unattuner and Gnomish Quadramorphic Combinerator can only be sold back to EoM vendor if they were purchased with EoM
- Unattuner and GQC is no longer NO-DROP
- Vibrating Gauntlet\Hammer of Infuse will preserve augments when swapping (invalid augs will fall out)
- Characters with a Trader's Satchel in their inventory who find themselves in a zone other than Bazaar will be moved back to Bazaar

- Fixed inspect item not working when outside of the instance containing a Bazaar trader.
- Fixed off-by-1 error with regard to Bazaar Shard numbering

- Added Bag of Bartering and Belt Pouches of Bartering to Echo of Memory in Bazaar
 - These bags will allow you to Sell All or Keep One Per Stack of their contents when interacting with a Merchant
 - Bag of Bartering - 30 slots, Max Size Giant, 100% WR
 - Belt Pouches of Bartering - 100 slots, Max Size Small, 100% WR
   - Pro Tip: Put this one in your LAST inventory slot to act like a 'filter' for preconfigured junk in combination with 'Keep One Per Stack' sell mode
```

KNOWN ISSUES
```
- Traders in Bazaar Shard 1 will show as their name if you are in any open world zone, not just the Bazaar
```

EXTRA
```
An EXPERIMENTAL client configuration change has been added to the 'extra' directory in the patcher. BACK UP and then replace your 'resources/Memory.ini' file with this if you experience frequent crashes while zoning, especially if you have gone to discord for help and been told it was the 'graphics memory crash'. 
```

---

## Entry 1331723721295003740
**Author:** Aporia
**Date:** 2025-01-22T20:34:37.387000+00:00

Changes:
```
- Kildrukaun the Ancient's Typhoon Breath now casts once every 45 seconds instead of 15.
- Bladesoul's Spiritual Diadem now correctly classified as armor
- Lvl 50+ Druid and Shaman pets will now benefit from Pet Power 15, 20, and 25.
- Misc item description updates
- A Knight of Luclin now correctly reports the targets needed for Luclin unlock
- Fixed Z-axis of ground spawns in Lake Rathe
- Key of Torsis is now correctly set to a 100% drop rate
- Stun Resist AAs are being squished to prevent overflows. Steadfast Will will now be available for (WAR/PAL/SK/MNK/BER). Dauntless Perseverance has been removed entirely as stun resist > 100 does nothing. 
```

Pending Patch:
```
Unflinching Resolve and Stalwart Endurance have been removed from the game.
- Any player that has a single point of Unflinching Resolve or Stalwart Endurance will be given Steadfast Will on next downtime.
```

---

## Entry 1331997123805184092
**Author:** Catapultam
**Date:** 2025-01-23T14:41:01.625000+00:00

```
- Type 21 Glamour-Stones no longer require item type armor
- Fixed EoM-purchased Gnomish Quadramorphic Combinerator
- Bazaar Parcel Fee removed when inside the Bazaar (any instance)
- Disabled 'Warp to Trader' functionality from Find Trader
- Changing Pal\SK Epic from one form to another will no longer eat augs

- Added Delivery Vouchers & Direct to Inventory Delivery
  - Purchased from Merchant Aina for platinum
  - Purchased from Echo of Memory for EoM
  - Each direct to inventory delivery will consume 1 Delivery Voucher from your Alt Currency.

- Increased standard stack size to 1000
- All items have a sell value based on stats.
- Item Previews are now avaiable (alt-rightclick item icon in 'item inspect' window) (@dannuic)
```

---

## Entry 1332028783162818775
**Author:** Catapultam
**Date:** 2025-01-23T16:46:49.804000+00:00

```
- Items should now never be able to be sold for more than they are bought for.
- No-Rent items can not be sold via Bags of Bartering
- Custom Pet Names restored
```

---

## Entry 1332759507641827409
**Author:** Aporia
**Date:** 2025-01-25T17:10:28.096000+00:00

Pending Server Reboot:

```
- Consolidated logic on both populating and executing Bags of Bartering. This should reduce confusion and increase accuracy about which items are actually eligible to be sold.
- Berserker Summoned Axes may no longer be vendored
- No-Rent items may no longer be vendored
- Items with Augments may no longer be auto-vendored
- Removed a bunch of inaccessible NPCs from the Bazaar
- Added NO-VALUE tag to many items given by trivial quest scripts.
- Added NO-VALUE tag to all summoned items
- All players with Tracking should now be able to filter track results (@Salty)
- Fixed memory leak in client which caused map to not properly reset spawn lists under some circumstances (@dannuic)
- Reduced the 'merchant multiplier' on most items.
- Fixed several memory leaks (@Akk)
- Re-enabled direct inventory delivery via Delivery Vouchers
- Adjusted client memory map in a speculative fix for out of memory client crashes (@Drake)

Quest Fixes:
- Quests fixes related to Qeynos Badge (@Trust)
- Implemented JFP War (@Trust)
- Cleaned up Shaman Cudgel & Skull quest (@Trust)
  - Added Flags to each step to monitor progress
  - Added faction and level checking per step
  - Added notice of flags being assigned (So they are not "Invisible")
  - Added Dialog to Oxyn "Progress" that will output current progress point.
  - Limited a quest turn-in that can be exploited for fast and unlimited EXP
- Misc Befallen cleanup (@Trust)
- Fixed Faction hits around Giant Scarab quests in Kaladim (@Trust)
- Various Quest fixes in qey2hh1 (@Trust)
- Corrected several quests which rewarded the wrong items.

- Added Mystic Soulbinding Apparatus to Gemcrafter Anuk This reusable device allows you to attune any item, preventing it from being accidentially sold or|| traded.

- Unflinching Resolve and Stalwart Endurance have been removed from the game.
- Any player that has a single point of Unflinching Resolve or Stalwart Endurance will be given Steadfast Will

- The vendor cost of items has increased as the sell value on some has increased.

```

---

## Entry 1332857825009078393
**Author:** Catapultam
**Date:** 2025-01-25T23:41:08.783000+00:00

```
- Fixed Guild Member level display. (Client Patch Required)
```

---

## Entry 1334259808114839553
**Author:** Catapultam
**Date:** 2025-01-29T20:32:07.603000+00:00

```
- Updated to EQEmu v22.61.1
```
https://github.com/EQEmu/Server/pull/4617
https://github.com/EQEmu/Server/pull/4627

---

## Entry 1334900028866826271
**Author:** Catapultam
**Date:** 2025-01-31T14:56:08.125000+00:00

```
- Peridots are no longer marked NO VALUE
- Fixed Bag of Bartering prompt not displaying in some circumstances.
- Bag of Bartering prompt is now sorted by item stats and value, but may be truncated for large item lists.

- Reduced packet resend aggressiveness - This may help with connection stability for some users (@Akkadius)
```

---

## Entry 1335823574799224852
**Author:** Aporia
**Date:** 2025-02-03T04:05:58.634000+00:00

```
- The Echo of the Past for Nagafen's Lair, Permafrost, and Velketor's lab have been moved inside their respective zones. 
- If you see an Echo of the Past in Lavastorm or Everfrost, please ignore them and zone in to the respective zone to pull your DZ.
- Great Divide still has an Echo of the Past but it is now at the succor location to the south of the zone and is meant to spawn a DZ for Great Divide itself.
```

---

## Entry 1336033147346878590
**Author:** Catapultam
**Date:** 2025-02-03T17:58:44.623000+00:00

Posting this early because it went out early
```
- Updated Default Maps (@Lachadan)
- Added Dark Mode maps option (dropdown menu in map window) (@Lachadan)
```

---

## Entry 1337208133201690625
**Author:** Catapultam
**Date:** 2025-02-06T23:47:43.081000+00:00

THIS CHANGELOG IS FOR LUCLIN RELEASE AND IS NOT COMPLETE

```
- Updated to EQEmu 22.62.2
- 'Improved the netcode' (@Akkadius)

Fixes:
- Purify Body should now work as expected (@Fluff)
- BoBs will no longer sell to any merchant regardless of faction
- Players entering or leaving the zone in a Non-Respawning instance with more than 2 members will no longer cause mobs to heal
- Faded Memory should spawn for Zlandikar and the other guy
- Items with slots incorrectly set to only allow one wrist have been corrected to allow both wrists.
- Fix zone crash that could occur when a script not directly attached to an NPC could instruct a recently dead NPC to Move to a new location.
- Various NPCs will no longer flee when kicked.
- Certain tradeskill recipes will no longer return incorrect items via Salvage AA (@Trust)
- Fixed various luclin encounters (thx @Trust, @Zimp, others)
- Gnomes can now acquire Tinkering Mastery AA
- Fixed a number of Haste spells that were actually Slows (Bards, Rejoice!)
- Fixed Reverse DS effects not working
- Doppelgangers will no longer use ranged attacks, they will only cast spells.

Changes:
- Languid Bite and Deep Sleep should now trigger off AA casts (@Zimp)
- Magicians no longer keep TEMPORARY items unless they have a spell that can summon them (like any other class)
- Added QUEST tag to most items used in any kind of quest Turn-In.
- Ring of the Shissar is now No-Trade
- SPA 185 (SE_DamageModifier) now stacks.
- Adjusted Arx key to only work inside Sanctus Seru, and be instance aware
- Lord Inquisitor Seru will banish any attacker who does not possess an Arx 

New:
- Returned Jolum to the Bazaar
  - Jolum will exchange your summoned Grandmaster's Satchel for a permanent, 30-slot Grandmaster's Carry-All. This item is LORE.
  - Grandmaster's Satchel and Grandmaster's Carry-All are now No-Drop.
- Added 15 additional ranks of Mystical Attuning
- Added Knight's Rebuke AA for Paladins
  - Allows Bash on Riposte


```

---

## Entry 1337209418198286398
**Author:** Aporia
**Date:** 2025-02-06T23:52:49.448000+00:00

THIS CHANGELOG IS ALSO FOR LUCLIN RELEASE AND IS NOT COMPLETE/MAY CHANGE BEFORE LAUNCH

```
**Balance**

- Cleric's Divine Avatar has been scaled down, but remains one of the most powerful AA's in the game. Duration reduced to 2 minutes. Melee damage bonus and proc chance reduced to 100.
- Pet's now have a hard cap on how much Flurry, Crit, Crit Damage, and Proc rate they can access (75%/75%/75%/100)
- Wizard AA Improved Familiar no longer gives stacking critical spell damage (Total decrease of 7.8% with all crit damage buffs going.)

- Warrior's Battle Leap AA duration to 12 seconds and increase damage modifier SPA 185 to 25% at RkI. RkII has been added for purchase for a 50% increase.
- Warrior's Fellstrike Discipline duration increased to 1.5 min
- Paladin's Holyforge Discipline now does crit and 50% SPA 185 *instead of crit and crippling blow* but had it's duration reduced to 2 minutes
- Rogue's Lethality increased to 40% SPA 185
- Rogue's Thief's Vengeance Discipline was increased to a 12 second duration
- Rogue only piercers now give additional backstab damage (x3)
- Druid's Spirit of the Bear now adds 75% SPA 185
- Druid's Spirit of the White Wolf now reduces spell cost by 20-25%, increases chance to critical heal by 15% and increases the chance to critical heal on a heal over time by 20%.
- Druid's Spirit of the Black Wolf now reduces spell cost by 20-25%, increases chance to land a critical hit with detrimental spells by 10%, increases critical spell damage by 50%, increases critical DoT chance by 10% and critical DoT damage by 50%
- Shaman's Rabid Bear proc now has a -50 disease resist modifier and a -50 disease resist check on the proc
- Shaman's Rabid Bear can now increase the stat cap of Str and Dex by 25/50/75

**Additional Changes:**

- Named mob spawn chance increased in SSRA basement (Strange Green Metal mobs)
- Bard Hymn of the Last Stand detrimental portion can no longer crit or get modified by spell damage and kill you.
- Aten Ha Ra's Silence of the Shadows now has a 24s recast time. Word of Command now has a 6s recast time.
- Fixed several broken spawns in Sanctus Seru
- Fungal Infusion now gives back 250 endurance in addition to its regular 250 mana
- Divine Hammer of Consternation and it's Corrupted counterpart now proc Divine Shield instead of Divine Aura
- Bixie parts can now drop from Bixies in PoM
- ZEM of Velious zones reduced.
- ZEM of Luclin zones increased.
- Thief's Vengeance Endurance cost lowered to 350
- Mark of Karn now has a -75 resist check and takes only 2 seconds to cast.

**DZs Added**

- Grimling Forest
- Acrylia Caverns
- The Gray
- The Deep
- The Fungus Grove
- Umbral Plains
- Dawnshroud Peaks
- Twilight Sea
- Vex Thel
- Sanctus Seru
- Katta Castellum
- Ssraeshza Temple
- Akheva Ruins
- Grieg's End
- Feerrott
- Lesser Faydark
- Swamp of No Hope

**The 10th Ring War is now working!** 
A HUGE thank you to Pippz and the many hands that went in to fixing this!

10th Ring War rewards have had their stats increased:

- (Crown of Narandi, only awarded if Churn stays alive)
- (Eye of Narandi, only awarded if Kurgin stays alive)
- (Earring of the Frozen Skull, only awarded if Corbin stays alive)
- (Faceguard of Bentos the Hero, only awarded if Dobbin stays alive)
- (Choker of the Wretched, only if Garadain stays alive)
- (Ring of Dain Frostreaver IV, always rewarded)

**The Ring of Fire is in for Luclin!** 
A HUGE thank you to Trust and the hands that went in to testing this!
```

---

## Entry 1337893727150014565
**Author:** Aporia
**Date:** 2025-02-08T21:12:01.416000+00:00

Pending Reboot:

```
- Vex Thall Trash HP has been reduced by 50%
- Vex Thall ZEM has been increased.
- All VT mobs are a minimum of level 60
- Fungal Infusion now removes curse counters!
- Silence on Thall Va Xakra, and Diabo Xi Xin Thall now behave like Aten Ha Ra's. For every 12 seconds you are silenced, you will now have a 12 second reprieve.
```

---

## Entry 1338377526820601906
**Author:** Catapultam
**Date:** 2025-02-10T05:14:28.246000+00:00

```
- Various spells and songs corrected to have haste instead of Slay Undead
- Lord Inquisitor Seru now correctly uses certain abilities if he has the support of any of his Praeserti
- Lord Inquisitor Seru's death reward event will now fire more reliabily
- Many fixes to various encounter scripts (@Trust, @Zimp)
- Removed Fling effect from Battle Leap (@Aporia)
- Removed Warders in VT
- Removed depop timer from The Insanity Crawler
- XTC unrooted
- Ssra High Priest unrooted
- Various double-spawns of bosses in ssrratemple have been removed
- Shadowstone idol NO-VALUE tag removed
- Reduced the HP of VT trash by 50%
- Reduced the respawn time of VT trash to match other XP zones.
- Bane Weapons will allow skill attacks (Frenzy, Backstab, Monk attacks, etc) to function.
- A File Cabinet respawn time adjusted to 1 hour, 59 minutes, 59 seconds, making it eligible to spawn in respawning instances.
- Power Source item growth rate increased. We will monitor this for re-evaluation.
- Removed ranks 7-9 of Fury of Magic which were incorrectly made available to hybrid classes.


Doppelganger Rework
- The enchanter AA Doppelganger has been largely reworked.
- Doppelgangers now gain the Equipment, (Long-Duration) Buffs, and Spells of the Enchanter who created them has at time they are created.
- They will use Nukes, Lifetaps, DoTs, Slows, Debuffs, and Snares. They will NOT use any other type of spell, including AoE spells.
```

---

## Entry 1338412565780238357
**Author:** Catapultam
**Date:** 2025-02-10T07:33:42.185000+00:00

Hotfix
```
- Returned Destructive Fury to Wizard AA list.
- Removed Fear, Blind, and Charm spells from Doppelganger spell lists (requires new zone server, may not work in existing instances)
- Removed extra 10 ranks of (unpurchasable) Fury of Magic from some classes (will remain visible in bazaar, also a new zone servers thing)
```

---

## Entry 1338759014258970654
**Author:** Catapultam
**Date:** 2025-02-11T06:30:21.939000+00:00

```
- Fixed Praesertum Mapta's infinite healing exploit
- Fixed players being immune to stun for a period of time after being stunned.
- Removed several undesirable spells from Doppelgangers
- Doppelgangers no longer use AoE spells of any type from their owner's memorized spell list.
- Lowered the spawn time of A File Cabinet

- Players will become immune to silence for a period of time after becoming silenced.
```

---

## Entry 1339477902109966367
**Author:** Aporia
**Date:** 2025-02-13T06:06:58.159000+00:00

```
Please be aware, Doppelganger is being actively worked on as we try to make it behave more offensively.

We realize that not being able to control what default spells were being used was not an ideal UX and are working toward a more intuitive spell set.

Expect Doppelganger to cast spells from you bar + their original nukes for now.

Thank you!
```

---

## Entry 1339745754541064212
**Author:** Catapultam
**Date:** 2025-02-13T23:51:19.155000+00:00

```
- Fixed regression in zone scaling script. Mobs should no longer heal when someone enters or leaves zone
- Worg pets should no longer try to visually hold weapons.
- Speculative fix to make glamour appearances more reliable.
- Adjusted Doppelganger spellcasting priority
- Adjusted Doppelganger spell stacking
- Adjusted pet aggro distribution (pet taunt on\off)
```

---

## Entry 1341103053197283349
**Author:** Catapultam
**Date:** 2025-02-17T17:44:44.372000+00:00

```
- Consolidated Echo of Aegolism, Echo of the Grove, Echo of the Brood, Echo of Focus, and Echo of Koadiac into Echo of Power.
- Replaced Knight's Rebuke with existing AA: Knight's Return Strike
- Fixed several errors with Valentine's Day event scripts
- Prevented Forlorn Follower of Erolisi from replacing certain NPCs
```

Important Information & Errata:

- Forlorn Follower of Erollisi are *still* whatever their base NPC is. They still have the same quests, scripts, etc. If you need them to *die* for some event to work correctly, just kill them, don't use their dialogue to make them depop.
- Echo of Power is not a direct 1:1 comparison to the effects of the old buffs, and may be adjusted in the future. The application of buff scaling makes the consolidated buff scale a little bit differently than the composite buffs.

---

## Entry 1347611729353244775
**Author:** Aporia
**Date:** 2025-03-07T16:47:53.693000+00:00

```
Return Bash now available to Paladins and Warriors and functions similarly to Return Kick

The following items have had their heroic stats and mod2 stats corrected:

Crown of the Defender (Legendary)
Bone Ring of Disharmony (Legendary)
Vial of Suspended Mana (Legendary)
Strands of Power (Legendary)
Bone Collar of the Possessed (Legendary)
Armband of Serenity (Legendary)
Boneweave, Bracer of the Enslaved (Legendary)
Crown of the Undead Warmaster (Legendary)
Earring of Death (Legendary)
Earring of Fond Memories (Legendary)
Gauntlet of the Fire Ring (Legendary)
Gem Encrusted Choker (Legendary)
Seer's Orb of Power (Legendary)
Skull Charm of the Oracle (Legendary)
Totem of the Corpsemaster (Legendary)
Warmaster's Mask of Battle (Legendary)
Bracelet of the Manawielder (Legendary)
Grimling Medallion of Power (Legendary)
Grimling Archmage's Nosering (Legendary)
Medallion of the Hero of Shar Vahl (Legendary)

Avatar of Agony, Avatar of Suffering, Avatar of Pain, and Avatar of Anguish are now the only mobs on their spawn table.

The following items are now no drop:

Screaming Sphere
Quintessence of Elements
Enchanted Ring of Torden
Symbol of Torden
Mark of Torture
Mark of Lashing
Mark of Flame
Mark of Stone
Mark of Suffocation
Mark of Execution
Gryme's Crypt Key
Mound of Living Stone
Globe of Dancing Flame
Sphere of Coalesced Water
Amorphous Cloud of Air
Crystalline Globe
Wind Etched Key

Runic Strike should now stack with Rune

The following explorer progression items have been made all/all so that they can be leveled by any hero:

Mask of Secrets
Sebilite Scale Mask
Helot Skull Helm
Helm of Rile
Stronghorn's Horn
Shackle of Auctoririas
Sword of Pain
Siren Hair Earring
Ring of the Shissar
Shadel Bandit Ring
Zekhas' Katar
Blade of Insanity
Elemental Binder
Djarn's Amethyst Ring
Crown of the Froglok Kings
Scalp of the Ghoul Lord

The explorer progression path for Luclin no longer requires the Unadorned Scepter and now requires a Burning Ring from Umbral Plains.
```

---

## Entry 1347615496207466548
**Author:** Catapultam
**Date:** 2025-03-07T17:02:51.781000+00:00

```
- Updated to EQEmu v23.2
  - Zone State Preservation
    - Zone States are now preserved when the zone is internally shut down or the server is restarted
    - Spawned Mobs (including PH\Named or scripted spawns), Loot, and other zone parameters will be restored after zone shutdown.
    - Some EVENT SCRIPTS may still break if you unload a zone during the event. Please report these as bugs.
  - Fix various crashes (https://github.com/EQEmu/Server/releases)

- Bug Fixes
  - Fixed ATK not being applied properly from items.
  - Pet-only spells should more reliably land on pets.
  - Mobs should no longer summon players under the world.
  - Beneficial DoT (read, Lich) should no longer break rogue sneak/hide

- BREAKING CHANGE
  - Items will now attune IMMEDIATELY upon being equipped. No reimbursement will be given for accidentally attuned items.
  - Items with 'Must Equip' type click effects will ONLY be castable from inventory slots if ATTUNED
  - Explorer Progression Path is now ACCOUNT BOUND. This will reset progress made at the per-character level. Please contact a guide if you require reimbursement.

- Changes
  - Players will become immune to being summoned for 10 seconds after being summoned.
  - Removed Snare and Slow components from shaman Torpor line
  - Moved shaman Torpor line into short-duration buffs
  - Echo of Power should now properly stack with all other buffs
  - Global Buffs should more reliably re-apply.
  - Removed several useless\nonworking AA (Extended Shielding, Trap Navigation)
  - All versions of Dire Charm are now undispellable
  - Fixed an exploit with Parcels
  - Adjusted pet aggro transfer rules.
  - Fixed crash zoning into North Ro
```

---

## Entry 1347823190017052734
**Author:** Catapultam
**Date:** 2025-03-08T06:48:09.844000+00:00

```
- Re-enabled Zone State Preservation
- Fixed incorrectly calculated stat caps
- Fixed crash that could occur with certain player events (@Neckkola)
- Fixed Class-Specific titles not working
- Fixed Bazaar Parcel Purchase Discount
- Titles are now deduplicated
- Fixed incorrect mobs spawning in restored respawning instances
- Adjusted most Summoned items to not require equipping to cast.
- Fixed The Polymorphist not accepting Echo of Memory for deity changes
- Praeserti no longer flee
- Fixed Bladed Song
```

---

## Entry 1348875672461901824
**Author:** Catapultam
**Date:** 2025-03-11T04:30:21.213000+00:00

```
- Re-enabled Zone State Preservation
- Fixed Bazaar Parcel Purchase Discount
- Fixed incorrect mobs spawning in restored respawning instances
- Fixed The Polymorphist not accepting Echo of Memory for deity changes
- Praeserti no longer flee
- Fixed Bladed Song
- Removed Parcel fee for Bazaar purchases in EC and Bazaar
```

(Yes, this changelog is posted again on purpose.)

---

## Entry 1349412549308842084
**Author:** Catapultam
**Date:** 2025-03-12T16:03:42.628000+00:00

```
- Doppelgangers now respect spell recast times of spells they inherit from their owner.
- Swarm pets inherit spell modifiers from their owner even when their owner has no other pets
- Zone State restoration is now improved in such a way as to prevent spawning multiple mobs on zone restore.
```

---

## Entry 1349425683507708005
**Author:** Catapultam
**Date:** 2025-03-12T16:55:54.065000+00:00

Hotfix -> Requires new zone zervers to take effect
```
- Fixed pets not correctly calculating spell proc rate
```

---

## Entry 1349491176792658022
**Author:** Aporia
**Date:** 2025-03-12T21:16:08.881000+00:00

This is a changelog post to test the new patcher.

```
Words. Changes. Nerfed monks.
```

---

## Entry 1352780052215107604
**Author:** Catapultam
**Date:** 2025-03-21T23:04:57.886000+00:00

Part 1
```
Augmentations
  - Reworked Augment slot schema
   - All Visible Slot (head\arms\chest\legs\feet\wrist) have a Type 21 (Armor Glamour) slot
   - All Weapon\Shield Slot (Pri\Sec\Range) have a Type 20 (Weapon Glamour) slot
   - All items EXCEPT pri\sec\range\charm\ammo have Type 1 slot
   - All items EXCEPT charm\ammo have Type 2 slot
   - All pri\sec\range have Type 2 and Type 4 slots (2 total slots)
   - All 2-handed primary have extra Type 2, Type 4 slots (4 total slots)
  - Removed LORE from Kerafyrm augments
  - All LEGENDARY augments are now ATTUNABLE, and will attune when slotted
  - Renamed all Glamour-Stones to `Glamour - 'Item Name'
  - It is now possible to create augmented items which are both NO TRADE and unusable by you.

Bazaar
 - Purveyor of Glamour will now randomly reward Weapon or Armor Glamours when asked to provide a random Glamour.
 - Purveyor of Glamour will now accept 4 Glamour augments to produce a new random Glamour
 - The 'Prestiege' Bazaar search paramter has been replaced with 'Glamour' and can be used include or exclude those items from search.
 - Vision of Ayonae will reset AAs for 5 EoM (down from 10), and no longer imposes a cooldown.
 - Vision of Ayonae will refund all now-unusable AA when removing a class.

Spells
 - Dispel can now be cast on other players without redirection by implied targeting.
 - Dispel cast by a player on a player or player's pet can no longer remove beneficial effects.
 - Dispel cast by a player on a player or player's pet can no longer remove any effects with counters (poison, disease, curse, etc)
 - Melee damage no longer interrupts casted direct healing spells. (Movement, stun, silence, etc, still can)
 - Calliav line is now instant-cast
 - Removed scaling of Bard rune songs via Heal Amount.
 - Bard rune songs are no longer expended via damage, instead offering a flat damage reduction.
 - All single-target DoT spells and songs have had their cast times reduced to 1 second, the amount removed from their cast time added to recast time.
 - All single-target DoT spells with a base duration greater than 30 seconds have had their durations doubled.
 - All single-target DoT songs have had their duration increased to 1 minute.
 - NEW SPELL: Aspect of the Reptile (DRU 60)

Disciplines
 - Puretone discipline now stacks with all other bard mods
 - Puretone discipline now additionally grants immunity to silence for the duration

AA
 - The following AA always stacks with all other effects: Rabid Bear, Union of Spirits, Ancestral Aid, Guardian of the Forest, Hunter's Fury, Killing Spree, Spirit of the Black Wolf, Spirit of the White Wolf

Pets
 - Substantially reduced direct mitigation bonuses from pet buffs.
 - Added Greater Syncrosatchels for Necromancer, Enchanter, Beastlord; Available from Merchant Aina at level 60
 - Pets are no longer valid targets for NPC Rampage while they have taunt off
 - Sympathetic (Healing) will no longer affect all pets when triggered by a pet-only spell, and will instead behave similarly to sympathetic buffs with other AoE spells (It will hit your current target or implied target when cast).
 - Reworked aggro sharing with pets; pets with taunt off will now give a SMALL amount of aggro to their owner (just enough to get their owner on the mob's aggro list), and a LARGE portion of their aggro to other pets with taunt on.
 - Pets with taunt off and an owner who is feigned or invisible will not transfer aggro in this way, but will temporarily lose the ability to be immune to gaining aggro.
 - Fixed pet caption on Charm
 - MR from Gear and Buffs is no longer considered when checking for charm break
```

---

## Entry 1352780161384317089
**Author:** Catapultam
**Date:** 2025-03-21T23:05:23.914000+00:00

Part 2
```
*** KNOWN ISSUES ***
- The Plane of Time expedition does not currently recover cleanly from being fully shut down during PHASE 3. Please complete Phase 3 before leaving the zone for any extended period of time.

Misc
 - Removed all spells and disciplines from vendors which are otherwise obtainable from quests in PoP.
 - Celestial Fists are now Must-Equip to click (Reminder, Must-Equip can click from inventory once attuned)
 - Mobs should no longer restore from saved state with 0 hp
 - Mobs should no longer slowly levitate into the air as zone is suspended and reloaded
 - Adjusted several PoP ZEMs
 - Nerfed Mnk/Mnk/Mnk
 - Added PoK book to Bazaar
 - Added many new Enchanted\Legendary items, should have full coverage now.
 - Valentine's Day buffs have come to an end!

POP Events
 - Planes of Power progression flags are *account wide*
 - Check the Storyline window for a flagging guide!
 - HoHA - Crazed Norrathians now have a one minute timer before spawning in each room. (Pippz)
 - Agnarr - Stun duration cut in half. 15s Recast Added.
 - Tallon Zek PoTactics - Knockback distance cut in half. Proc chance reduced to 20%.
 - Hebabbilys the Ragelord - Max damage and slow mitigation reduced.
 - High Councilman of the Queen - No longer have a chance to softblur every 6 seconds.
 - PoAir - Wave of White Noise now correctly has a 45 second recast.
 - Wind of Xegony is now a magic debuff instead of a curse as it should be.
 - The Rathe Councilmen are no longer immune to CC.
 - Trash in Time P3 is now susceptible to some form of CC or kiting.
 - Rallos Zek's stun reduced to 4sec duration.
 - Quarm is no longer slowable.
 - Vallon Zek no longer FDs his target and instead stuns and swaps targets.
 - Rallos Zek and Innoruuk should no longer be able to be separated from their adds.

Quests
 - Fused Mnemonic of Khati Sha is now completable.
 - Increased stats of Signet of the Arcane
```

---

## Entry 1352847240527609957
**Author:** Catapultam
**Date:** 2025-03-22T03:31:56.828000+00:00

Running changelog for Post-PoP hotfixes.
```
- Corrected flagging logic for Aerin`Dar event.
- Corrected flagging logic for Grummus event
- Corrected flagging logic for Hedge event
- Corrected goup port logic for PoJ trials (@Gregggggg)
- Corrected group port logic for Keeper of Souls (@Greggggg)

- Fixed zone crash related to tradeskills
- Fixed inability to mix enchanted\legendary in standard tradeskill combines
```

---

## Entry 1354667173997449316
**Author:** Catapultam
**Date:** 2025-03-27T04:03:42.780000+00:00

```
- Removed level requirement from the Plane of Time.
- Exp gain from level 63 to 65 has been increased.
- Pet level adjusted for BST/NEC/ENC pets using Time focus.
- Respawn time in Plane of Tactics and Plane of Water have been reduced to match other respawn times.
- Pheonixs in Plane of Fire no longer charm (and/or crash your game).
- Echo added to Tenebrous Mountains.
- Echo added to Dalnir's Crypt.
- Aid Grimel should now be able to be completed.
- Added 2nd Type 4 augment slot to Bows
- Augments currently Slotable in type 1 & 2 are now also slotable in type 4.
- Plane of Time - Phase 4 and later bosses should no longer double-spawn
- NUMEROUS Plane of Time fixes and adjustments to bring events more in-line to expectations
- Reworked Plane of Earth ring events
- Askr no longer despawns in Non-Respawning instances
- Trial of Torture now properly granting flags

- The approximately one thousand characters who achieved level 65 prior to this patch will recieve the title 'of the One Thousand'
```

---

## Entry 1356635539750650037
**Author:** Catapultam
**Date:** 2025-04-01T14:25:17.746000+00:00

```
- Implemented the new Player Rendering Overhaul!
This feature, unique to THJ, will provide an unparalleled graphics experience like you have never seen before! Enjoy AAA quality which you had never imagined that you'd see in this game. Please note that this is a REQUIRED feature, and out of date clients will be disconnected automatically, so please remember to patch!

- Nerfed Mnk/Mnk/Mnk
- Removed several redundant player classes; Monks, Rogue, Warrior, Wizard, Berserker are all classes who's roles are better performed by other classes, and so these have been permanently disabled.
- Bard has been removed because it is just too much trouble and causes too many bugs.
```

---

## Entry 1356802123106357349
**Author:** Catapultam
**Date:** 2025-04-02T01:27:14.313000+00:00

4/2/2025 (Yes, this one is real)
```
- Reverted class deletions. Implemented <<# a u t o s k i l l>> instead
  - Initially supports the following Skill attacks
      Backstab
      Bash
      Tiger Claw
      Eagle Strike
      Dragon Punch / Tail Rake
      Flying Kick
      Round Kick
      Kick
      Frenzy
  - Absolutely no timer deconfliction is executed by the command, please only enable skills you want to be used.

- Implemented #attackmode
  - Rangers no longer display their bow by default. Any character can use #attackmode ranged to preferentially use their bow for autoattack and display

- Implemented #petcmd
  - Pet window buttons (and hotkeys created from them, or /pet commands) only send instructions to the 'active pet' (the pet displayed in the window)
  - 'Triple-pet' UI mod is not recommended, as it may be confusing as to which pet is 'active'
  - added #petcmd to send instructions to ANY pets (send commands by class name, etc)
  - Usage: #petcmd [attack, qattack, follow, guard, sit, stop, taunt (on\\off), hold (on\\off), ghold (on\\off), spellhold (on\\off), focus (on\\off), back, regroup (on\\off)] [all, mag, bst, nec, enc, shm, dru, brd, shd].
  - Any number of command and target verbs may be used at the same time, and in any order
  - /pet health and #petcmd health now display inventory for that pet

- Removed access to #mystats. On most servers, the inventory\player profile page is inaccurate and so mystats is needed. On this one, due to the unique nature of our technology, the inverse is true.

- Corrected bug which allowed creation of augmented items that were not usable in any slots.
- Syncrosatchels or equivalents will now consider slotted augments to determine which slot an item can be equipped into
- Splinters of Time which are not PRI\SEC\RANGE no longer require slotting into a weapon
- Dispel-type spells cast by players on players or player pets are no longer resistable.
- Dispel-type spells cast by mobs are now resistable.
- Fixed Monk class names display on Character Select
- Sol Ro Tower respawn timers have been fixed.
- Legends of Norrath cards no longer have a self consume clicky effect and have an updated lore.
- Innoruuk and Rallos Zeks adds no longer leash and assist their god
- Aid Grimmel quest npc should be more responsive now.
- The rztwl event in plane of tactics should behave even more as expected, with failure timers removed.
- The Fennin event in plane of fire should now correctly resume when returning to the zone and no longer fails on timeout.
- Plane of Earth a ring events rewritten to be more resilient to zoning out. (Thanks Pippz)
- Echo added to Splitpaw
- Mortal Coil is no longer blocked by random clickies
- Villagers in HoHA are now tethered and will not run full marathons.
- 61-65 LDoN spells have been added to PoP parchment turn in rewards
- 50-60 LDoN spells have been added to Warders, Ancients, Lords and Ladies in Velious
- Mistakenly remaining GoD and OoW spells have been removed from PoK vendors *and* player spellbooks.
- Lvl 62 BST and lvl 63 Necro pet now correctly scale their level.
- The likelihood of finding weapon augments has increased on the Glamour NPC.
- Aspect of the Reptile duration has been increased.
- /shield now works for Warriors level 30 or greater
- All entities are capped at 35 worn Shielding
- Switched Prismatic Strike to Chromatic resist type
```

---

## Entry 1357226963760316516
**Author:** Catapultam
**Date:** 2025-04-03T05:35:24.218000+00:00

Late Night Hotfix
```

- Temporarily disabled global buffs through Apocrypha and the event Signets (Manually extended for 24hrs!)

* Needs new Zone Server (Probably won't work in Bazaar, will be more reliabile as zones cycle out) *
- #commands will be consumed in any channel (the spam should go down)
- attackmode ranged should be less laggy and more reliable for displaying weapons correctly

* Needs CLIENT UPDATE (PATCH) *
- Added the following command aliases
  /pet (#petcmd)
  /attackmode (#attackmode)
  /autoskill (#autoskill)
- #commands should no longer echo in chat (even if nobody could see them when properly consumed)
```

---

## Entry 1357428075155165204
**Author:** Catapultam
**Date:** 2025-04-03T18:54:32.911000+00:00

```
- Re-Enabled Global Buffs
- Various backend performance improvements (@Akk)
- Zebuxoruk now drops minimum of Enchanted quality augments, and can rarely drop additional augments.
- Lord Inquisitor Seru has a higher probability of dropping additional loot based on the number of difficulty-enhancing buffs present on him
```

---

## Entry 1357601537861615697
**Author:** Catapultam
**Date:** 2025-04-04T06:23:49.643000+00:00

Hotfix
```
- Pets which are not taunting should REALLY be immune to rampage now.
- Kerafyrm may now have more than one scale.

- Pets will only resync gear when inventory operations are performed with the pet bag instead of all operations
- Reduced the number of equipment change packets being sent in certain circumstances
```

---

## Entry 1359585216825655307
**Author:** Catapultam
**Date:** 2025-04-09T17:46:15.563000+00:00

**Auto AFK**

**Why this Change?** Part of what we see in a critical hub zone such as Bazaar, is extremely high CPU, lag, causing a bad experience for other players trying to zone into the zone and function at all. This change aims to drastically reduce packet spam in the zone, keeping the zone lean and leading to a much better player experience when using the Bazaar. When a player with 4 pets is running in circles in the zone, it sends enormous amounts of position updates to X number of players in the zone, even those who are idle and don't need all of these updates.

When clients go AFK they stop receiving packet updates for movement. When they go un-AFK they get synchronized with all the clients around them.

**Changes**

* When in a non-combat zone (Bazaar) - auto AFK timer is 60 seconds
* When in a combat zone - auto AFK timer is 10 minutes
* When you go AFK, we also toggle the native /afk flag on the client now
* When a client initiates a trade with another client, both clients in the trade get auto-marked as non-AFK
* When a client finishes a trade with another client, both clients in the trade get auto-marked as non-AFK
* Heading now takes part in triggering when a client "moved" to remove them from auto AFK status
* Client messaging is now simply "You are AFK." / "You are no longer AFK."

```
- Fixed an issue where spawn locations weren't being restored properly after zone state restoration. (@Akk)
- Fixed an issue where restoring an in-progress Plane of Time B instance would sometimes not restore properly. (@Akk)
- Fixed a scenario where sometimes players would not be able to enter certain open world zones while others would not experience said issue. (@Akk)
- Improved Bazaar search performance (@Akk)
- Prismatic Scale of the Elements (Legendary) is now Attunable instead of No Trade.
- Splinters of Time without a proc are now the correct aug type.
- Bard song aggro was incorrectly inflated. Fixed.
- Ranger archery bonus now correctly begins at 50 instead of 51.
- Hand of Ro now stacks with other -Fire Resist debuffs
- Pets can once again be issued commands from the default range.
- Xegony key will now Keyring
- Symbol of Torden will now Keyring
- Prevent pets from being added to mob hate lists if they are on hold (@Zimp)
- 2H Bash & Slam now works with Autoskill (@Duneathor)
- Reduced the Damage Shield component of Blessing of Praesertum Matpa
- Revamped 'Stats' page on Default UI
- /autoskill now supports Taunt
- Fixed inconsistencies around basic stat caps and certain spell effects
- Fixed pets with taunt off still pulling aggro
- Fixed pets with taunt off still eating rampage
- Fixed swarm pets not obeying custom pet restrictions (proc rate etc) (@Grek)
- Added the following EQTypes for UI makers.
    ClassAbbrList = 6666,
    TrueEvasion = 6667,
    TrueMitigation = 6668,
    WornATK = 6669,
    ItemExp = 6670,
    SpellCritRate = 6671,
    SpellCritRatio = 6672,
    HealCritRate = 6673,
    HoTCritRate = 6674,
    DoTCritRate = 6675,
    DoTCritRatio = 6676,
    MeleeCritRate = 6677,
    MeleeCritRatio = 6678,
    PetFlurryRate = 6679,
    PetMeleeCritRate = 6680,
    PetAvoidance = 6681,
    PetMeleeMitigation = 6682,
    PrimaryActualDelay = 6683,
    SecondaryActualDelay = 6684,
    Pet0Taunt = 6685,
    Pet1Taunt = 6686,
    Pet2Taunt = 6687,
    Pet0Hold = 6688,
    Pet1Hold = 6689,
    Pet2Hold = 6690,
    Pet0GHold = 6691,
    Pet1GHold = 6692,
    Pet2GHold = 6693,
    Pet0Focus = 6694,
    Pet1Focus = 6695,
    Pet2Focus = 6696,
    Pet0Spellhold = 6697,
    Pet1Spellhold = 6698,
    Pet2Spellhold = 6699,
    Pet0SPO = 6700,
    Pet1SPO = 6701,
    Pet2SPO = 6702,    
    CapClairvoyance = 6703,
    CapHealAmount = 6704,
    CapSpellDamage = 6705,
    CapWornATK = 6706,
    ArcheryCritRate = 6707,
    RuneAmount = 6708,
    SpellRuneAmount = 6709
```

Known Issues:
```
- Pets with taunt OFF should be ignored by mobs - This is not working correctly
```

---

## Entry 1361550724663873648
**Author:** Catapultam
**Date:** 2025-04-15T03:56:29.149000+00:00

## Changelog April 14 2025

## **Auto Idle and Auto-AFK Updates**

The **Idle** and **AFK** systems have been separated to improve player experience and reduce unnecessary network load.

- In non-combat, players become idle after 1 minute and AFK after 10 minutes.
- In combat, players become idle after 10 minutes and AFK after 30 minutes.

### Key Changes:
- **Idle** now reduces client position updates to improve performance in crowded zones like the Bazaar.
- **AFK** is now fully independent of idle and manual `/afk`. Automatic AFK will not override or be overridden by manual AFK status.
- Manual `/afk` remains active until toggled off and is unaffected by automatic behavior.
- Automatic AFK messages no longer interfere with manual or automatic AFK or idle states.
- The following actions now reset idle and AFK timers:
  - Moving items
  - Casting spells
  - Using `/autoattack`
  - Receiving messages
- **Trade** (start or finish) now forces a position sync for both parties.
- **Wearchange packets** (e.g., armor appearance updates) are now sent even while idle.
- **Buyers** and **Traders** are excluded from automatic AFK entirely.

---

## 💰 **Alternate Currency Improvements**

- **Alternate currency** is now account-wide.
- Currency counts now automatically refresh when:
  - Reclaiming items
  - Creating currency
  - Updating currency values
- The **Reclaim** button now functions correctly with currency items on the cursor.

---

## 🐞 Fixes & Improvements

- Fixed integer underflow on 0-value runes.
- Fixed **Frenzy** so it can now critically hit as intended.
- Fixed **weapon glamours** not appearing on pets.
- Resolved various issues with glamours, illusions, and idle logic in the Bazaar.
- Pets summoned by **Doppelgangers** now correctly belong to their summoner’s owner.
- Fixed a bug where pets could become permanently detached from their owner.
- Fixed bug causing pet aggro to clear whenever taunt command was set, regardless of setting.
- Fixed a bug preventing pets with taunt off from properly gaining the 'Immune to NPC Aggro' flag
- Fixed a bug which caused pets to taunt enemies attacking their owner at unlimited range.

---

---

