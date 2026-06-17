# ALERT_AUDIT_ALLERGY_DOM

> Stores additional domain information relating to allergy interactions. The scope of the auditing is limited to data provided by the consumer that relates to a particular interaction.

**Description:** Alert Audit Allergy Domain  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_ALLERGY_DOM_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_ALLERGY_ID` | DOUBLE | NOT NULL | FK→ | The ID of the allergy interaction on table Alert_audit_allergy. |
| 3 | `ALLERGY_ID` | DOUBLE | NOT NULL |  | The ID of the allergy (from the allergy table) associated to this audit record. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code associated to the order. |
| 5 | `DRUG_ALLERGY_IND` | DOUBLE | NOT NULL |  | Indicates if the interaction is a drug-allergy interaction or an allergy-drug interaction. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter_id associated to the subject of the allergy interaction. |
| 7 | `FREETEXT_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if a free text override reason was provided. |
| 8 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature_id associated to the allergy. |
| 9 | `NO_OVERRIDE_REASON_IND` | DOUBLE | NOT NULL |  | The indicator denoting if an override reason was provided. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL |  | The ID of the order from the Orders table. |
| 11 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | The code value of the override reason |
| 12 | `OVERRIDE_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text_id relating to the free text override reason. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_AUDIT_ALLERGY_ID` | [ALERT_AUDIT_ALLERGY](ALERT_AUDIT_ALLERGY.md) | `ALERT_AUDIT_ALLERGY_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `OVERRIDE_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

