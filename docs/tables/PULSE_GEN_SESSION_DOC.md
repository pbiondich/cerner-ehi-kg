# PULSE_GEN_SESSION_DOC

> Contains information about a document that a pulse generator has created for a session.

**Description:** Pulse Gen Session Document  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_DESC` | VARCHAR(50) |  |  | A short description of the report type for the pulse generaor document e.g. EGM Report or Capture Threshold |
| 2 | `DOC_DT_TM` | DATETIME |  |  | The date and time for the document |
| 3 | `DOC_LEN_NBR` | DOUBLE |  |  | The number of pages for this session document |
| 4 | `DOC_UID` | VARCHAR(50) | NOT NULL |  | The UID for the document content |
| 5 | `PULSE_GEN_SESSION_DOC_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `PULSE_GEN_SESSION_ID` | DOUBLE | NOT NULL | FK→ | The session associated with this pulse generator episode document |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_SESSION_ID` | [PULSE_GEN_SESSION](PULSE_GEN_SESSION.md) | `PULSE_GEN_SESSION_ID` |

