# REF_RANGE_NOTIFY_TRIG

> Contains the relationship between the reference range factor table and one to many EKM (Expert Knowledge Module) rules.

**Description:** Reference Range Notify Trigger  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific row in the reference_range_factor table. |
| 2 | `REF_RANGE_NOTIFY_TRIG_ID` | DOUBLE | NOT NULL |  | Identifies a specific relationship between the reference range factor table and one to many Expert Knowledge Module rules |
| 3 | `TRIGGER_NAME` | VARCHAR(30) | NOT NULL |  | The name of the Expert Knowledge System rules to execute. |
| 4 | `TRIGGER_SEQ_NBR` | DOUBLE | NOT NULL |  | Identifies the importance of this trigger name for a given reference range factor. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

