# MLTM_RXB_ORDER

> Multum Rx Builder Order Table Table

**Description:** Multum Rx Builder Order Table  
**Table type:** REFERENCE  
**Primary key:** `DRUG_IDENTIFIER`, `ORDER_ID_NBR`  
**Columns:** 10  
**Referenced by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | PK | Drug IdentifierColumn |
| 2 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE |  | FK→ | Main Multum Drug Code. FK from MLTM_NDC_MAIN_DRUG_CODE table |
| 3 | `ORDER_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique identifier for each prescription category. |
| 4 | `ORDER_ID_NBR` | DOUBLE | NOT NULL | PK | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 5 | `ORDER_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This field contains a unique identifier for each prescription type. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MAIN_MULTUM_DRUG_CODE` | [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `MAIN_MULTUM_DRUG_CODE` |
| `ORDER_CATEGORY_ID` | [MLTM_RXB_ORDER_CATEGORY](MLTM_RXB_ORDER_CATEGORY.md) | `ORDER_CATEGORY_ID` |
| `ORDER_TYPE_ID` | [MLTM_RXB_ORDER_TYPE](MLTM_RXB_ORDER_TYPE.md) | `ORDER_TYPE_ID` |

## Referenced by (18)

| From table | Column |
|------------|--------|
| [MLTM_RXB_ORDER_DISPENSE_MAP](MLTM_RXB_ORDER_DISPENSE_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_DISPENSE_MAP](MLTM_RXB_ORDER_DISPENSE_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORDER_DURATION_MAP](MLTM_RXB_ORDER_DURATION_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_DURATION_MAP](MLTM_RXB_ORDER_DURATION_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORDER_FREQUENCY_MAP](MLTM_RXB_ORDER_FREQUENCY_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_FREQUENCY_MAP](MLTM_RXB_ORDER_FREQUENCY_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORDER_INSTRUCTION_MAP](MLTM_RXB_ORDER_INSTRUCTION_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_INSTRUCTION_MAP](MLTM_RXB_ORDER_INSTRUCTION_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORDER_PRN_MAP](MLTM_RXB_ORDER_PRN_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_PRN_MAP](MLTM_RXB_ORDER_PRN_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORDER_REFILL_MAP](MLTM_RXB_ORDER_REFILL_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORDER_REFILL_MAP](MLTM_RXB_ORDER_REFILL_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORD_CLINICAL_RTE_MAP](MLTM_RXB_ORD_CLINICAL_RTE_MAP.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORD_CLINICAL_RTE_MAP](MLTM_RXB_ORD_CLINICAL_RTE_MAP.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORD_DOSE_AMOUNT](MLTM_RXB_ORD_DOSE_AMOUNT.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORD_DOSE_AMOUNT](MLTM_RXB_ORD_DOSE_AMOUNT.md) | `ORDER_ID_NBR` |
| [MLTM_RXB_ORD_DOSE_RATE](MLTM_RXB_ORD_DOSE_RATE.md) | `DRUG_IDENTIFIER` |
| [MLTM_RXB_ORD_DOSE_RATE](MLTM_RXB_ORD_DOSE_RATE.md) | `ORDER_ID_NBR` |

