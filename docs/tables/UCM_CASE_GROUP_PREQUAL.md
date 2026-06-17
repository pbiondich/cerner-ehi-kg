# UCM_CASE_GROUP_PREQUAL

> Contains case groups for which cases prequalify

**Description:** Unified Case Manager - Case Group Prequal  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVALUATED_IND` | DOUBLE | NOT NULL |  | Evaluated Indicator - true if the case has been evaluated for inclusion in real case group. |
| 2 | `TRIGGER_UCM_CASE_ID` | DOUBLE | NOT NULL |  | Case that triggered the initial formation of the prequalification rows. Generically describes what will route to the same unified case manager case group. |
| 3 | `UCMR_CASE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the reference case group to which this case type prequlifies. |
| 4 | `UCM_CASE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the case group related to this record. |
| 5 | `UCM_CASE_GROUP_PREQUAL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a case group for which a case is prequalified. |
| 6 | `UCM_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the case related to this record. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_GROUP_ID` | [UCMR_CASE_GROUP](UCMR_CASE_GROUP.md) | `UCMR_CASE_GROUP_ID` |
| `UCM_CASE_GROUP_ID` | [UCM_CASE_GROUP](UCM_CASE_GROUP.md) | `UCM_CASE_GROUP_ID` |
| `UCM_CASE_ID` | [UCM_CASE](UCM_CASE.md) | `UCM_CASE_ID` |

