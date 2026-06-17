# CRITIQUE_CODE_ASSIGNMENTS

> The Critique_Code_Assignments table contains coded information about an exam critique.

**Description:** Critique Code Assignments  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITIQUE_INFO_ID` | DOUBLE | NOT NULL |  | The Critique_Info_Id is a foreign key the exam_critique_info table. |
| 2 | `CRITIQUE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Critique_Prsnl_id contains the id of the Radiologist doing the critique of a Resident, Transcriptionist, or Technologist |
| 3 | `CRITIQUE_TYPE_CD` | DOUBLE | NOT NULL |  | The Critique_Type_Cd contains the codes that identify the specifics about the critique. (ex. too light, too dark, etc.) |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITIQUE_PRSNL_ID` | [CRITIQUE_PRSNL](CRITIQUE_PRSNL.md) | `CRITIQUE_PRSNL_ID` |

