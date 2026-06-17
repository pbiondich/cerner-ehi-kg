# SURG_PROC_DURATION

> Contains the default durations for a specific surgical procedure, surgical area, and surgeon.

**Description:** Surgical Procedure Duration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_CLEANUP_DUR` | DOUBLE | NOT NULL |  | The default cleanup duration associated with this procedure, area, and surgeon. |
| 2 | `DEF_POST_CLOSURE_DUR` | DOUBLE | NOT NULL |  | The default post-closure duration associated with this procedure, area, and surgeon. |
| 3 | `DEF_PRE_INCISION_DUR` | DOUBLE | NOT NULL |  | The default pre-incision duration associated with this procedure, area, and surgeon. |
| 4 | `DEF_PROCEDURE_DUR` | DOUBLE | NOT NULL |  | The default procedure duration associated with this procedure, area, and surgeon. |
| 5 | `DEF_SETUP_DUR` | DOUBLE | NOT NULL |  | The default setup duration associated with this procedure, area, and surgeon. |
| 6 | `HIST_CLEANUP_DUR` | DOUBLE | NOT NULL |  | The historical cleanup duration associated with this procedure, area, and surgeon. |
| 7 | `HIST_POST_CLOSURE_DUR` | DOUBLE | NOT NULL |  | The historical post-closure duration associated with this procedure, area, and surgeon. |
| 8 | `HIST_PRE_INCISION_DUR` | DOUBLE | NOT NULL |  | The historical pre-incision duration associated with this procedure, area, and surgeon. |
| 9 | `HIST_PROCEDURE_DUR` | DOUBLE | NOT NULL |  | The historical procedure duration associated with this procedure, area, and surgeon. |
| 10 | `HIST_SETUP_DUR` | DOUBLE | NOT NULL |  | The historical setup duration associated with this procedure, area, and surgeon. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of the surgeon to whom these default durations are associated. If this value is 0, the values are generic durations for the procedure and area. |
| 12 | `REC_CLEANUP_DUR` | DOUBLE | NOT NULL |  | The recent cleanup duration associated with this procedure, area, and surgeon. |
| 13 | `REC_POST_CLOSURE_DUR` | DOUBLE | NOT NULL |  | The recent post-closure duration associated with this procedure, area, and surgeon. |
| 14 | `REC_PRE_INCISION_DUR` | DOUBLE | NOT NULL |  | The recent pre-incision duration associated with this procedure, area, and surgeon. |
| 15 | `REC_PROCEDURE_DUR` | DOUBLE | NOT NULL |  | The recent procedure duration associated with this procedure, area, and surgeon. |
| 16 | `REC_SETUP_DUR` | DOUBLE | NOT NULL |  | The recent setup duration associated with this procedure, area, and surgeon. |
| 17 | `SURG_PROC_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the SURG_PROC_DETAIL table indicating the entry associated with this surgical procedure. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_PROC_DETAIL_ID` | [SURG_PROC_DETAIL](SURG_PROC_DETAIL.md) | `SURG_PROC_DETAIL_ID` |

