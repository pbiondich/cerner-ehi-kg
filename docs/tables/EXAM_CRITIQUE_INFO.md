# EXAM_CRITIQUE_INFO

> The Exam_Critique Info table contains information about an exam critique. Info includes who did the critique, when it was done, etc.

**Description:** Exam Critique Info  
**Table type:** ACTIVITY  
**Primary key:** `CRITIQUE_INFO_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENTS` | VARCHAR(255) |  |  | The Comments field contains any general comments that the radiologist has about the critique. |
| 2 | `CREATED_BY_ID` | DOUBLE | NOT NULL | FK→ | The Created_By_Id field contains the unique identifier for the radiologist that has performed the critique. |
| 3 | `CREATED_DT_TM` | DATETIME |  |  | The Created_Dt_Tm field captures the date and time that the critique was performed. |
| 4 | `CRITIQUE_INFO_ID` | DOUBLE | NOT NULL | PK | The Critique_Info_Id uniquely identifies a row within the Exam_Critique_Info table. It has no other meaning or purpose other than to serve as a unique id. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Order_Radiology table. This serves as the tie between the order and the critique info. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CRITIQUE_PRSNL](CRITIQUE_PRSNL.md) | `CRITIQUE_INFO_ID` |

