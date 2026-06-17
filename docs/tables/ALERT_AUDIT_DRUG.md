# ALERT_AUDIT_DRUG

> Stores audited drug-drug interactions where each interaction is tied to an auditing transaction. The scope of the auditing is limited to the most basic reference information utilized by the clinical checking service.

**Description:** Alert Audit Drug  
**Table type:** ACTIVITY  
**Primary key:** `ALERT_AUDIT_DRUG_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_DRUG_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the Alert Audit Transaction table. |
| 3 | `DCP_ENTITY_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The dcp_entity_reltn_id relating to the customization details of the drug-drug interaction. |
| 4 | `DESC_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text_id relating to the description of the drug-drug interaction. |
| 5 | `DRUG_IDENTIFIER_1` | VARCHAR(6) | NOT NULL |  | The first drug identifier. |
| 6 | `DRUG_IDENTIFIER_1_SUBJECT_IND` | DOUBLE | NOT NULL |  | Indicator denoting whether the first drug identifier is the subject of the drug-drug interaction. |
| 7 | `DRUG_IDENTIFIER_2` | VARCHAR(6) | NOT NULL |  | The second drug identifier. |
| 8 | `SEVERITY_DETAILS_BIT` | DOUBLE | NOT NULL |  | The severity details of the drug-drug interaction. |
| 9 | `SEVERITY_FLAG` | DOUBLE | NOT NULL |  | The severity of the drug-drug interaction. 0 - Minor, 1 - Moderate, 2 - Major |
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
| `DESC_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_DRUG_DOM](ALERT_AUDIT_DRUG_DOM.md) | `ALERT_AUDIT_DRUG_ID` |

