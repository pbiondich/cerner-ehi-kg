# ALERT_AUDIT_DUP_CAT_CAUSE

> Stores the causes of each audited category duplicate therapy alert. The scope of the auditing is limited to the most basic reference information utilized by the clinical checking service.

**Description:** Alert Audit Duplication Category Cause  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_DUP_CAT_CAUSE_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_DUP_ID` | DOUBLE | NOT NULL | FK→ | Alert audit duplicate therapy alert id |
| 3 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | The drug identifier of the causing drug of a category duplication. |
| 4 | `OBSERVED_OCCURRENCES_NBR` | DOUBLE | NOT NULL |  | The number of observed occurrences for this drug. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_AUDIT_DUP_ID` | [ALERT_AUDIT_DUP](ALERT_AUDIT_DUP.md) | `ALERT_AUDIT_DUP_ID` |

