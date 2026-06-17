# CMT_SUBSET_MEMBER_LOAD

> LOAD TABLE FOR CMT_SUBSET_MEMBER

**Description:** CMT_SUBSET_MEMBER_LOAD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_CMTI` | VARCHAR(255) |  |  | The child cmti for the relationship |
| 2 | `CHILD_CONCEPT_CKI` | VARCHAR(255) |  |  | The child concept cki for the relationship |
| 3 | `CHILD_SUBSET_ID` | DOUBLE | NOT NULL |  | The subset ID for the child |
| 4 | `LIST_SEQUENCE` | DOUBLE |  |  | The sequence of the relationship |
| 5 | `PARENT_CMTI` | VARCHAR(255) |  |  | The parent CMTI for the relationship |
| 6 | `PARENT_CONCEPT_CKI` | VARCHAR(255) |  |  | The parent concept cki for the relationship |
| 7 | `SUBSET_ID` | DOUBLE | NOT NULL |  | The SUBSET ID for the relationship |
| 8 | `SUBSET_MEMBER_LOAD_ID` | DOUBLE | NOT NULL |  | Unique Value Identifier |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

