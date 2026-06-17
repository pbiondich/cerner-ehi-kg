# ALERT_AUDIT_ALLERGY

> Stores audited allergy interactions where each interaction is tied to an auditing transaction. The scope of the auditing is limited to the most basic reference information utilized by the clinical checking service.

**Description:** Alert Audit Allergy  
**Table type:** ACTIVITY  
**Primary key:** `ALERT_AUDIT_ALLERGY_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_AUDIT_ALLERGY_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `ALERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the Alert Audit Transaction table. |
| 3 | `ALLERGY_ALR_CATEGORY_ID` | DOUBLE | NOT NULL |  | The allergy category id of the allergy. |
| 4 | `ALLERGY_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | The allergy identifier from the mltm_drug_id table. |
| 5 | `CLASS_ID` | DOUBLE | NOT NULL |  | The allergy class id of the drug and allergy found in the mltm_alr_class table. |
| 6 | `DCP_ENTITY_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The dcp_entity_reltn_id relating to the customization details of the allergy interaction. |
| 7 | `DESC_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text_id relating to the description of the allergy interaction |
| 8 | `DRUG_ALLERGY_IND` | DOUBLE | NOT NULL |  | Indicates if the interaction is a drug-allergy interaction or an allergy-drug interaction. |
| 9 | `DRUG_ALR_CATEGORY_ID` | DOUBLE | NOT NULL |  | The allergy category ID of the drug. |
| 10 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | The drug identifier from the table mltm_drug_id. |
| 11 | `INTERACTION_LEVEL_FLAG` | DOUBLE | NOT NULL |  | The interaction level of the allergy interaction. 0- Drug, 1 - Category, 2 - Class. |
| 12 | `INTERACTION_TYPE_ID` | DOUBLE | NOT NULL |  | The interaction type id of the allergy interaction from the mltm_alr_text_map table.. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| [ALERT_AUDIT_ALLERGY_DOM](ALERT_AUDIT_ALLERGY_DOM.md) | `ALERT_AUDIT_ALLERGY_ID` |

