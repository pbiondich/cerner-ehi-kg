# TRACKING_AUDIT_ELEMENT

> Store elements of information about a tracking audit event.

**Description:** TRACKING AUDIT ELEMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_DT_TM` | DATETIME |  |  | Date/Time value to be audited. |
| 2 | `AUDIT_ELEMENT_NAME` | VARCHAR(255) | NOT NULL |  | The name of the element being audited. |
| 3 | `AUDIT_ELEMENT_STRING` | VARCHAR(255) | NOT NULL |  | The string value of the Element being audited. |
| 4 | `AUDIT_ELEMENT_TXT` | VARCHAR(255) |  |  | Sometimes the value is a double, sometimes it's a string. This column stores the string value. |
| 5 | `AUDIT_FLAG` | DOUBLE |  |  | Audit Flag - 0 = Incomplete, 1 = Complete.NULL implies no value assigned. |
| 6 | `AUDIT_STRING` | VARCHAR(255) |  |  | String value to be audited. |
| 7 | `AUDIT_VALUE` | DOUBLE |  |  | Numeric value to be audited. |
| 8 | `TRACKING_AUDIT_ELEMENT_ID` | DOUBLE | NOT NULL |  | Primary Key for the tracking_audit_element table. |
| 9 | `TRACKING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the tracking_audit table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_AUDIT_ID` | [TRACKING_AUDIT](TRACKING_AUDIT.md) | `TRACKING_AUDIT_ID` |

