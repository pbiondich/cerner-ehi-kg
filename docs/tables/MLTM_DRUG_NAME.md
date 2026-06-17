# MLTM_DRUG_NAME

> This table contains names used to identify a drug or drug product.

**Description:** MLTM DRUG NAME  
**Table type:** REFERENCE  
**Primary key:** `DRUG_SYNONYM_ID`  
**Columns:** 8  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_NAME` | VARCHAR(255) |  |  | This field contains Multum's succinct, fixed-length generic drug names. This field also contains brand names, which are the drug names as they appear on labels of drug products. |
| 2 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | PK | This field contains a unique numeric identifier for a description of a drug. |
| 3 | `IS_OBSOLETE` | VARCHAR(1) |  |  | This field indicates whether a drug is currently available on the market in the United States. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [MLTM_DMD_NAME_MAP](MLTM_DMD_NAME_MAP.md) | `DRUG_SYNONYM_ID` |
| [MLTM_DRC_GROUP_RELTN](MLTM_DRC_GROUP_RELTN.md) | `SYNONYM_ID` |
| [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_SYNONYM_ID` |
| [MLTM_DRUG_NAME_GLOBAL_TYPE](MLTM_DRUG_NAME_GLOBAL_TYPE.md) | `DRUG_SYNONYM_ID` |
| [MLTM_MANUFACT_DRUG_NAME](MLTM_MANUFACT_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| [MLTM_MMDC_ATTRIBUTE](MLTM_MMDC_ATTRIBUTE.md) | `GENERIC_SYNONYM_ID` |
| [MLTM_ORDER_CATALOG](MLTM_ORDER_CATALOG.md) | `DRUG_SYNONYM_ID` |
| [MLTM_RXN_MAP](MLTM_RXN_MAP.md) | `DRUG_SYNONYM_ID` |
| [PBS_OCS_MAPPING](PBS_OCS_MAPPING.md) | `DRUG_SYNONYM_ID` |

