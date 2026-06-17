# SN_DIAGNOSTIC_REL

> SurgiNet Diagnostic Relationship

**Description:** SurgiNet Diagnostic Relationship table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSTIC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Diagnostic Group IdColumn |
| 2 | `DIAGNOSTIC_ID` | DOUBLE | NOT NULL | FK→ | Diagnostic IDColumn |
| 3 | `DIAGNOSTIC_REL_ID` | DOUBLE | NOT NULL |  | The Unique Id on the table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSTIC_GROUP_ID` | [SN_DIAGNOSTIC_GROUP](SN_DIAGNOSTIC_GROUP.md) | `DIAGNOSTIC_GROUP_ID` |
| `DIAGNOSTIC_ID` | [SN_DIAGNOSTIC](SN_DIAGNOSTIC.md) | `DIAGNOSTIC_ID` |

