# LH_CNT_WL_POP

> This table stores the relationship between encounters and the LH_CNT_WL table. Effectively identifying the underlying populations for a given worklist.

**Description:** lh_cnt_wl_pop  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_WL_POP_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the ENCOUNTER table, indicating which encounter is being associated to a worklist. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LH_CNT_WL_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the LH_CNT_WL table, indicating which worklist this encounter belongs to. |
| 6 | `LH_CNT_WL_POP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the parent row on the PERSON table, indicating which person is being associated to a worklist. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LH_CNT_WL_ID` | [LH_CNT_WL](LH_CNT_WL.md) | `LH_CNT_WL_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_CNT_WL_FACTOR](LH_CNT_WL_FACTOR.md) | `LH_CNT_WL_POP_ID` |
| [LH_CNT_WL_POP_STATUS](LH_CNT_WL_POP_STATUS.md) | `LH_CNT_WL_POP_ID` |

