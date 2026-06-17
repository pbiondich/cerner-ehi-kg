# TL_MULTIPATIENT_XREF

> Indicates whether the code is for a person, role, or default.

**Description:** TL MULTIPATIENT XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MULTIPATIENT_DEFAULT_PREF` | DOUBLE |  |  | A number that identifies which of seven possibilities is used as a view default. 1: all patients, 2: all pats in a specific loc, 3: all pats assigned to a prov., 4: all pats in a pat list, 5: all tasks, 6: all tasks assigned to a prov, 7: all tasks that prov has priv. |
| 2 | `MULTIPATIENT_IND` | DOUBLE | NOT NULL |  | An indicator used to determine if the parent_entity_cd is a person, position, or application default. 0 = person, 1 - position, 2 = app default. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A unique number that is used to identify a specific person, position, or app default. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the parent table that corresponds to the parent_entity_cd: PERSON, PRNSL_ROLE, or MASTER |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

