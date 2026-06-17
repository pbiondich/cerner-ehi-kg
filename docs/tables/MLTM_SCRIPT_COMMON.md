# MLTM_SCRIPT_COMMON

> This table contains a listing of information about Common Scripts for specific drugs and drug products.

**Description:** Multum Script Common  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_CODE` | DOUBLE |  | FK→ | This field contains a unique identifier for each common script category. |
| 2 | `DOSE_AMOUNT` | DOUBLE |  |  | Dose Amount in specified units |
| 3 | `DOSE_TO_AMOUNT` | DOUBLE |  |  | Dose to Amount in specified quantity |
| 4 | `DOSE_TO_UNIT` | DOUBLE | NOT NULL |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 5 | `DOSE_UNIT` | DOUBLE | NOT NULL |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 6 | `DURATION_AMOUNT` | DOUBLE |  |  | Duration Amount - in specified units |
| 7 | `DURATION_UNIT` | DOUBLE |  |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 8 | `FREQUENCY_CODE` | DOUBLE | NOT NULL | FK→ | This field contains a numeric identifier assigned to a frequency of administration. |
| 9 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL |  | The Main Multum Drug Code (MMDC) is Multum's designator for groups of similar drug products. This is an extremely important code for developers who are using Multum's database products because it serves as the primary link to all of Multum's tables containing drug product information. An MMDC is assigned to each unique combination of the following fields: active ingredient(s), strength, route of administration, and dosage form. As a result, the MMDC is a very useful field for identifying dru |
| 10 | `QUANTITY_AMOUNT` | DOUBLE |  |  | Quantity Amount - in specified units |
| 11 | `QUANTITY_TO_AMOUNT` | DOUBLE |  |  | Quantity to Amount in specified units |
| 12 | `QUANTITY_TO_UNIT` | DOUBLE |  |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 13 | `QUANTITY_UNIT` | DOUBLE |  |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 14 | `RATE_AMOUNT` | DOUBLE |  |  | Rate Amount - in specified units |
| 15 | `RATE_AMOUNT_UNIT` | DOUBLE |  |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 16 | `RATE_TIME` | DOUBLE |  |  | Rate Time -in specified units |
| 17 | `RATE_TIME_UNIT` | DOUBLE |  |  | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 18 | `ROUTE_CODE` | DOUBLE | NOT NULL | FK→ | This field contains a unique code for each route of administration. |
| 19 | `SCRIPT_ID` | DOUBLE | NOT NULL |  | Prescription Category Identifier. This field contains a unique identifier for each prescription. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATEGORY_CODE` | [MLTM_SCRIPT_CATEGORY](MLTM_SCRIPT_CATEGORY.md) | `CATEGORY_CODE` |
| `FREQUENCY_CODE` | [MLTM_FREQUENCY](MLTM_FREQUENCY.md) | `FREQUENCY_CODE` |
| `ROUTE_CODE` | [MLTM_CLINICAL_ROUTE](MLTM_CLINICAL_ROUTE.md) | `ROUTE_CODE` |

