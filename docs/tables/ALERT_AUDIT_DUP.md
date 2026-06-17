# ALERT_AUDIT_DUP

> Stores audited duplicate therapy alerts where each duplication is tied to an auditing transaction. The scope of the auditing is limited to the most basic reference information utilized by the clinical checking service.

**Description:** Alert Audit Duplication  
**Table type:** ACTIVITY  
**Primary key:** `ALERT_AUDIT_DUP_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_DUP_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the Alert Audit Transaction table. |
| 3 | `CATEGORY_DUPLICATION_IND` | DOUBLE | NOT NULL |  | Indicator denoting if the duplication is for a category or drug. |
| 4 | `CATEGORY_LEVEL_FLAG` | DOUBLE | NOT NULL |  | The level at which the duplication occurs at. 0 - Not a category duplication, 1 - First level, 2 - Second level, 3 - Third level. |
| 5 | `DCP_ENTITY_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The dcp_entity_reltn_id relating to the customization details of the duplicate therapy alert. |
| 6 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | The drug identifier relating to the duplicate therapy alert. |
| 7 | `MAXIMUM_OCCURRENCES_NBR` | DOUBLE | NOT NULL |  | The maximum number of allowed occurrences of the alert. |
| 8 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL |  | The Multum duplication category of the drug. |
| 9 | `OBSERVED_OCCURRENCES_NBR` | DOUBLE | NOT NULL |  | The number of observed occurrences resulting in the duplication. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_AUDIT_TRANSACTION_ID` | [ALERT_AUDIT_TRANSACTION](ALERT_AUDIT_TRANSACTION.md) | `ALERT_AUDIT_TRANSACTION_ID` |
| `DCP_ENTITY_RELTN_ID` | [DCP_ENTITY_RELTN](DCP_ENTITY_RELTN.md) | `DCP_ENTITY_RELTN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_DUP_CAT_CAUSE](ALERT_AUDIT_DUP_CAT_CAUSE.md) | `ALERT_AUDIT_DUP_ID` |
| [ALERT_AUDIT_DUP_DOM](ALERT_AUDIT_DUP_DOM.md) | `ALERT_AUDIT_DUP_ID` |

