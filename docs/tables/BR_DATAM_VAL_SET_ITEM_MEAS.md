# BR_DATAM_VAL_SET_ITEM_MEAS

> Details about value sets, their related vocabulary coding sets, and QRDA measures.

**Description:** Bedrock Datamart Value Set Item Measure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAM_VAL_SET_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The value set and vocabulary item that this measure is related to. The corresponding value id from the BR_DATAMART_MAP_VALUE table. |
| 2 | `BR_DATAM_VAL_SET_ITEM_MEAS_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_DATAM_VAL_SET_ITEM_MEAS table. |
| 3 | `DRUG_CATEGORY_TXT` | VARCHAR(100) | NOT NULL |  | The Multum drug class. |
| 4 | `DRUG_DESC` | VARCHAR(1650) |  |  | Provides a display value used for Medications only. |
| 5 | `DRUG_EXCLUSION_IND` | DOUBLE |  |  | Indicates if the medication administration should be excluded. |
| 6 | `MAPPING_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether this value needs to be mapped for e-submission. |
| 7 | `MEAS_IDENT` | VARCHAR(50) | NOT NULL |  | Measure number (used for PQRS only). Not currently in Millennium. |
| 8 | `MEAS_MAX_VALUE` | DOUBLE |  |  | The highest acceptable limit for inclusion in this QRDA measure. This is used for submission of actual results, established by CMS, not in Millennium. |
| 9 | `MEAS_MIN_VALUE` | DOUBLE |  |  | The lowest acceptable limit for inclusion in this QRDA measure. This is used for submission of actual results, established by CMS, not in Millennium. |
| 10 | `MEAS_UOM_TXT` | VARCHAR(30) |  |  | The unit of measure associated with the min_value and max_value. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VOCAB_ITEM_DESC` | VARCHAR(300) |  |  | The display value for the vocabulary item related to this measure. |
| 17 | `VOCAB_ITEM_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The last date and time that this vocabulary item is effective for this measure. |
| 18 | `VOCAB_ITEM_QUALIFIER_TXT` | VARCHAR(40) | NOT NULL |  | Field for providing additional details about a vocabulary item as it relates to this measure. |
| 19 | `VOCAB_OID_TXT` | VARCHAR(40) | NOT NULL |  | Object Identifier for this vocabulary as related to this measure. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAM_VAL_SET_ITEM_ID` | [BR_DATAM_VAL_SET_ITEM](BR_DATAM_VAL_SET_ITEM.md) | `BR_DATAM_VAL_SET_ITEM_ID` |

