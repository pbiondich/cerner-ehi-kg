# TRACKING_AUDIT

> Store an audit record of events that occur in tracking.

**Description:** TRACKING AUDIT  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_AUDIT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_TYPE_CD` | DOUBLE | NOT NULL |  | Audit Type - from code set 4002045. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encntr_id from the encounter table. |
| 3 | `TRACKING_AUDIT_ID` | DOUBLE | NOT NULL | PK | Primary Key for the tracking_audit table. |
| 4 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Code-Value from code-set 16370. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_AUDIT_ELEMENT](TRACKING_AUDIT_ELEMENT.md) | `TRACKING_AUDIT_ID` |

