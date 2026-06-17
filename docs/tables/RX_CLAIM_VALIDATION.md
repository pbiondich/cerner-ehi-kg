# RX_CLAIM_VALIDATION

> Rx_claim_validation - Stores validation rules for prescription entry.

**Description:** RX CLAIM VALIDATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MANF_ITEM_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VALIDATION_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4519 |
| 8 | `VALIDATION_FIELD_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4522 |
| 9 | `VALIDATION_ID` | DOUBLE | NOT NULL |  | UNIQUE ID FOR EACH FIELD |
| 10 | `VALIDATION_SEQ` | DOUBLE |  |  | SEQUENCE OF VALIDATION FIELDS |
| 11 | `VALIDATION_TYPE_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4520 |
| 12 | `VALUE` | DOUBLE |  |  | THRESHOLD VALUE FOR EACH FIELD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

