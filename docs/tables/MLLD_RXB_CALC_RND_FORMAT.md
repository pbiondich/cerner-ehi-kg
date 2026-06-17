# MLLD_RXB_CALC_RND_FORMAT

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_CALC_RND_FORMAT  
**Table type:** REFERENCE  
**Primary key:** `FORMAT_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORMAT_CODE` | VARCHAR(1) | NOT NULL |  | Alpha code to define format |
| 2 | `FORMAT_DESCRIPTION` | VARCHAR(50) | NOT NULL |  | Description of format |
| 3 | `FORMAT_ID` | DOUBLE | NOT NULL | PK | Externally generated sequence ID |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLLD_RXB_CALC_RND_MASK](MLLD_RXB_CALC_RND_MASK.md) | `ROUNDING_FORMAT_ID` |

