# BLOT_STRIP

> Defines the strips which make up a molecular blot test. The temparature and probe number range for each strip is specified.

**Description:** Blot Strip  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENDING_PROBE` | DOUBLE |  |  | Ending probe number of the range of probes included on the strip. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relates the blot strip to the inventory lot and related blot. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `STARTING_PROBE` | DOUBLE |  |  | Beginning probe number of the range of probes included on the strip. |
| 4 | `STRIP_SEQ` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique. This is necessary since strip temperature is alpha numeric. Also determines the order of display. |
| 5 | `STRIP_TEMPERATURE` | VARCHAR(20) |  |  | Temperature at which the blot strip is incubated during testing. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [MOLECULAR_BLOT](MOLECULAR_BLOT.md) | `LOT_NUMBER_ID` |

