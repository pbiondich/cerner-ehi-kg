# RXS_ALERT_AUDIT_HX

> Maintains the audit history for an alert.

**Description:** RxStation Alert Audit History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date the audit was performed. |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who performed the audit. |
| 3 | `FOREIGN_CREATE_PRSNL_NAME` | VARCHAR(255) | NOT NULL |  | Name of an external personnel who create the audit. |
| 4 | `RXS_ALERT_AUDIT_HX_ID` | DOUBLE | NOT NULL |  | Unique number that identifies a single row on the RXS_ALERT_AUDIT_HX table. |
| 5 | `RXS_ALERT_ID` | DOUBLE | NOT NULL | FK→ | The RxStation alert whose history this row relates to. |
| 6 | `RXS_AUDIT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of audit activity that was performed. |
| 7 | `RXS_FOREIGN_DEVICE_ALERT_ID` | DOUBLE | NOT NULL | FK→ | The foreign system alert whose history this row relates to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RXS_ALERT_ID` | [RXS_ALERT](RXS_ALERT.md) | `RXS_ALERT_ID` |
| `RXS_FOREIGN_DEVICE_ALERT_ID` | [RXS_FOREIGN_DEVICE_ALERT](RXS_FOREIGN_DEVICE_ALERT.md) | `RXS_FOREIGN_DEVICE_ALERT_ID` |

