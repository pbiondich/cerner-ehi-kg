# ALERT_AUDIT_FOOD_DOM

> Stores additional domain information relating to drug-food interactions. The scope of the auditing is limited to data provided by the consumer that relates to a particular interaction.

**Description:** Alert Audit Food Domain  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_FOOD_DOM_ID` | DOUBLE | NOT NULL |  | The primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_FOOD_ID` | DOUBLE | NOT NULL | FK→ | The alert_audit_food_id related to the drug-food interaction. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code associated to the order. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID associated to the order. |
| 5 | `FREETEXT_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if a free text override reason was provided. |
| 6 | `NO_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if an override reason was provided. |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL |  | The ID of the order from the Orders table. |
| 8 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The code value of the override reason. |
| 9 | `OVERRIDE_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text_id relating to the free text override reason. |
| 10 | `SEVERITY_FLAG` | DOUBLE | NOT NULL |  | The severity of the drug-food interaction from the consumer's perspective. 0 - Minor, 1 - Moderate, 2 - Major. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_AUDIT_FOOD_ID` | [ALERT_AUDIT_FOOD](ALERT_AUDIT_FOOD.md) | `ALERT_AUDIT_FOOD_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `OVERRIDE_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

