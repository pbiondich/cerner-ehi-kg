# OEN_SEQUENCE

> Holds the possible sequences of steps.

**Description:** OEN SEQUENCE  
**Table type:** REFERENCE  
**Primary key:** `SEQUENCE_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CUSTOM_IND` | DOUBLE |  |  | Was this sequence built custom on site? |
| 3 | `PROTOCOL_FLAG` | DOUBLE |  |  | Which protocol does this sequence apply to. |
| 4 | `SEQUENCE_DESC` | VARCHAR(255) |  |  | Text description |
| 5 | `SEQUENCE_ID` | DOUBLE | NOT NULL | PK | Unique sequence_id |
| 6 | `SERVICE_FLAG` | DOUBLE |  |  | What service does this sequence apply to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `USAGE_FLAG` | DOUBLE | NOT NULL |  | Determines if used as error sequence or step sequence |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [OEN_ERROR_SEQ_R](OEN_ERROR_SEQ_R.md) | `SEQUENCE_ID` |
| [OEN_INTERFACE_ERR_R](OEN_INTERFACE_ERR_R.md) | `SEQUENCE_ID` |
| [OEN_SEQ_STEP_R](OEN_SEQ_STEP_R.md) | `SEQUENCE_ID` |

