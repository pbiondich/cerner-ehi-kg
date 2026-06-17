# ALERT_AUDIT_DRUG_DOM

> Stores additional domain information relating to drug-drug interactions. The scope of the auditing is limited to data provided by the consumer that relates to a particular interaction.

**Description:** Alert Audit Drug Domain  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_DRUG_DOM_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_DRUG_ID` | DOUBLE | NOT NULL | FK→ | The ID of the drug-drug interaction on table alert_audit_drug. |
| 3 | `CAUSING_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code of the ingredient of the order that caused the alert. |
| 4 | `CAUSING_ORDER_ID` | DOUBLE | NOT NULL |  | The order id of the order that caused the alert. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID associated to the subject order. |
| 6 | `FREETEXT_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if a free text override reason was provided. |
| 7 | `NO_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if an override reason was provided. |
| 8 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The code value of the override reason. |
| 9 | `OVERRIDE_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text_id relating to the free text override reason. |
| 10 | `SEVERITY_FLAG` | DOUBLE | NOT NULL |  | The severity of the drug-drug interaction from the consumer's perspective. 0 - Minor, 1 - Moderate, 2 - Major. |
| 11 | `SUBJECT_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code of the ingredient of the subject order. |
| 12 | `SUBJECT_ORDER_ID` | DOUBLE | NOT NULL |  | The order ID of the subject order. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_AUDIT_DRUG_ID` | [ALERT_AUDIT_DRUG](ALERT_AUDIT_DRUG.md) | `ALERT_AUDIT_DRUG_ID` |
| `CAUSING_CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `OVERRIDE_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SUBJECT_CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

