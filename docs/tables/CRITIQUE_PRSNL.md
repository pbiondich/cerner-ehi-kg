# CRITIQUE_PRSNL

> The Critique_Prsnl table contains the list of personnel that are being critiqued.

**Description:** Critique Prsnl  
**Table type:** ACTIVITY  
**Primary key:** `CRITIQUE_PRSNL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENTS` | VARCHAR(255) |  |  | The comments field contains comments about each report that is being critiqued. |
| 2 | `CRITIQUED_ID` | DOUBLE | NOT NULL | FK→ | The Critiqued_Id idendifies the personnel whose work is being critiqued. |
| 3 | `CRITIQUE_INFO_ID` | DOUBLE | NOT NULL | FK→ | The Critique_Info_Id is a foreign key the exam_critique_info table. |
| 4 | `CRITIQUE_PRSNL_ID` | DOUBLE | NOT NULL | PK | The critique_prsnl_id is the person doing the critique |
| 5 | `CRITIQUE_RELTN_FLAG` | DOUBLE |  |  | Defines the relationship the person being critiqued has with the procedure. |
| 6 | `READ_IND` | DOUBLE |  |  | Indicator to say if the resident, transcriptionist, or technologist has read this critique. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITIQUED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CRITIQUE_INFO_ID` | [EXAM_CRITIQUE_INFO](EXAM_CRITIQUE_INFO.md) | `CRITIQUE_INFO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CRITIQUE_CODE_ASSIGNMENTS](CRITIQUE_CODE_ASSIGNMENTS.md) | `CRITIQUE_PRSNL_ID` |

