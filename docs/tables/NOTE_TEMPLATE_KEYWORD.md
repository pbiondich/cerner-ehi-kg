# NOTE_TEMPLATE_KEYWORD

> Keywords

**Description:** list of all keywords associated with Clinical Templates  
**Table type:** REFERENCE  
**Primary key:** `NOTE_TEMPLATE_KEYWORD_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_STATUS_IND` | DOUBLE |  |  | Indicates whether the keyword is currently active |
| 2 | `NOTE_TEMPLATE_KEYWORD_ID` | DOUBLE | NOT NULL | PK | Unique primary key to table. |
| 3 | `TEMPLATE_KEYWORD` | VARCHAR(50) | NOT NULL |  | keyword |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TEMPLATE_KEYWORD_RELTN](TEMPLATE_KEYWORD_RELTN.md) | `NOTE_TEMPLATE_KEYWORD_ID` |

