# LH_CNT_WL_FLTR_LIST

> This table holds saved worklist filters by user id.

**Description:** Lighthouse Content Worklist Filter List  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | This value determines if the worklist Mpage when loaded will pull in this record's value by default. |
| 3 | `LH_CNT_WL_FLTR_LIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_WL_FLTR_LIST table. |
| 4 | `LH_CNT_WL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key that links to LH_CNT_WL |
| 5 | `LIST_NAME` | VARCHAR(255) | NOT NULL |  | Name given to define the filters being saved by the user. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key that links to LONG_TEXT where the filter JSON string is stored. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User ID of person who created/updated the record. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_WL_ID` | [LH_CNT_WL](LH_CNT_WL.md) | `LH_CNT_WL_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

