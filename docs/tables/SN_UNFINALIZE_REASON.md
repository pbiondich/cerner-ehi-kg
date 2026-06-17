# SN_UNFINALIZE_REASON

> Stores user's reasons for unfinalizing a case/document type.

**Description:** SN Unfinalize Reason  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the action was done and this entry made. |
| 2 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PERIOPERATIVE_DOCUMENT table |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who unfinalized case/document type |
| 4 | `UNFINALIZE_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason case/document type was unfinalized |
| 5 | `UNFINALIZE_REASON_FREE_TXT` | VARCHAR(255) |  |  | Additional unfinalize comments |
| 6 | `UNFINALIZE_REASON_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERIOP_DOC_ID` | [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `PERIOP_DOC_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

