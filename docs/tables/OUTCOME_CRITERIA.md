# OUTCOME_CRITERIA

> Used to hold outcome criteria definitions for active outcomes

**Description:** Outcome criteria table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from nomenclature table, which is used for evaluation of alpha response base outcomes |
| 2 | `OPERATOR_CD` | DOUBLE | NOT NULL |  | Mathematical operator code from code set 17909, which determines the comparison to be performed during outcome evaluation |
| 3 | `OUTCOME_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from outcome_activity table, which is used to store active outcome definitions |
| 4 | `OUTCOME_CRITERIA_ID` | DOUBLE | NOT NULL |  | Unique identifier for an outcome criteria |
| 5 | `RESULT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit codes to be used in conjunction with result value during outcome evaluation |
| 6 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | A value that is compared to an actual result during outcome evaluation. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field is used to order the outcome criteria for display |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `OUTCOME_ACTIVITY_ID` | [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `OUTCOME_ACTIVITY_ID` |

