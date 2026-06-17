# BR_MDRO

> Stores the base information about an MDRO.

**Description:** Bedrock Multi-drug resistant organism  
**Table type:** REFERENCE  
**Primary key:** `BR_MDRO_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_MDRO_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_MDRO table. |
| 2 | `MDRO_NAME` | VARCHAR(100) | NOT NULL |  | Name of the multi-drug resistant organism. |
| 3 | `MDRO_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Name of MDRO formatted in all upper case. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_MDRO_CAT_EVENT](BR_MDRO_CAT_EVENT.md) | `BR_MDRO_ID` |
| [BR_MDRO_CAT_ORGANISM](BR_MDRO_CAT_ORGANISM.md) | `BR_MDRO_ID` |

