# ALERT_AUDIT_TRANSACTION

> Stores audit transactions for clinical alerting. An audit transaction describes all of the clinical alerts that were fired during a single transaction for a consumer.

**Description:** Alert Audit Transaction  
**Table type:** ACTIVITY  
**Primary key:** `ALERT_AUDIT_TRANSACTION_ID`  
**Columns:** 10  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `DOMAIN_DATA_IND` | DOUBLE | NOT NULL |  | Indicates where consumer supplied domain data exists for the audited alerts of the transaction. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the patient whom the clinical checking is being performed for. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel performing the clinical checking. |
| 5 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | The date/time the transaction was performed. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_ALLERGY](ALERT_AUDIT_ALLERGY.md) | `ALERT_AUDIT_TRANSACTION_ID` |
| [ALERT_AUDIT_DRUG](ALERT_AUDIT_DRUG.md) | `ALERT_AUDIT_TRANSACTION_ID` |
| [ALERT_AUDIT_DUP](ALERT_AUDIT_DUP.md) | `ALERT_AUDIT_TRANSACTION_ID` |
| [ALERT_AUDIT_FOOD](ALERT_AUDIT_FOOD.md) | `ALERT_AUDIT_TRANSACTION_ID` |

