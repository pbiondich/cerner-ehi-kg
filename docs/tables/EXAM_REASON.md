# EXAM_REASON

> The Exam_Reason table contains the relationships between orderable procedures and coded reasons for exam.

**Description:** Exam Reason  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies a certain orderable procedure. |
| 2 | `EXAM_REASON_ID` | DOUBLE | NOT NULL | FK→ | The exam_reason_id is a unique, meaningless number that serves only as an identifier for a reason for exam |
| 3 | `ICD9_ID` | DOUBLE | NOT NULL |  | The ICD9_id field serves as a foreign key to the Nomenclature table. It identifies the ICD9 code that has been been attached to the procedure/reason for exam combination. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence field allows for the ability to tie multiple ICD9 codes to a given reason for exam. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |
| `EXAM_REASON_ID` | [CODED_EXAM_REASON](CODED_EXAM_REASON.md) | `EXAM_REASON_ID` |

