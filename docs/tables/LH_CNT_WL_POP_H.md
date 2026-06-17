# LH_CNT_WL_POP_H

> Archive for lh_cnt_wl_pop table. This table stores the relationship between encounters and the LH_CNT_WL table. Effectively identifying the underlying populations for a given worklist.

**Description:** LH_CNT_WL_POP_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the ENCOUNTER table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LH_CNT_WL_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the LH_CNT_WL table. |
| 6 | `LH_CNT_WL_POP_H_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `LH_CNT_WL_POP_ID` | DOUBLE | NOT NULL |  | The foreign key to the parent row on the LH_CNT_WL_POP table. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the PERSON table |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LH_CNT_WL_ID` | [LH_CNT_WL](LH_CNT_WL.md) | `LH_CNT_WL_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

