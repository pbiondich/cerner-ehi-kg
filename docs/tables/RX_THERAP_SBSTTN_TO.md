# RX_THERAP_SBSTTN_TO

> Medication therapeutic substitution reference data for a drug that may be substituted.

**Description:** Therapeutic Substitution To  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `THERAP_SBSTTN_FROM_ID` | DOUBLE | NOT NULL | FK→ | The drug that this TO row is a substitute for. |
| 3 | `THERAP_SBSTTN_TO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_THERAP_SBSTTN_TO table. |
| 4 | `TO_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Result order catalog code pointing to ORDER_CATALOG table. Only valued when the prms_catalog_cd is valued. Represents the catalog to substitute for what was originally selected to order. |
| 5 | `TO_DRUG_FORM_CD` | DOUBLE | NOT NULL |  | The drug form that will be used on the substituted to synonym. |
| 6 | `TO_FREQ_CD` | DOUBLE | NOT NULL |  | Frequency to be used with the substitution. |
| 7 | `TO_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Points to the MEDICATION_DEFINITION table. Only valued when the prms_item_id is valued Represents the item to substitute for what was originally selected to order. |
| 8 | `TO_ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | The order sentence ID that will be used on the substituted to synonym. |
| 9 | `TO_RTE_CD` | DOUBLE | NOT NULL |  | Route of administration to be used with the substitution. |
| 10 | `TO_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Result dose will be substituted for the ordered dose if the substitution qualifies. |
| 11 | `TO_STRENGTH_VALUE` | DOUBLE | NOT NULL |  | Substitute To Dose strength. Result dose will be substituted for the ordered dose if the substitution qualifies. |
| 12 | `TO_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Points to the ORDER_CATALOG_SYNONYM table. Only valued when the prms_synonym_id is valued. |
| 13 | `TO_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Ordered dose must match to qualify for the substitution. |
| 14 | `TO_VOLUME_VALUE` | DOUBLE | NOT NULL |  | Ordered dose must match to qualify for the substitution. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `THERAP_SBSTTN_FROM_ID` | [RX_THERAP_SBSTTN_FROM](RX_THERAP_SBSTTN_FROM.md) | `THERAP_SBSTTN_FROM_ID` |
| `TO_CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `TO_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `TO_ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `TO_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

