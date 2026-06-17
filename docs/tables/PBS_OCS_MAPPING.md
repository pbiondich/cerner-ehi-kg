# PBS_OCS_MAPPING

> Map PBS Codes to Millennium order_catalog_synonym table

**Description:** PBS_OCS_MAPPING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(99) | NOT NULL | FK→ | DNUM. Key to MLTM_DRUG_ID table |
| 3 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | CNUM. Key to MLM_DRUG_NAME table |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `MAIN_MULTUM_DRUG_CODE` | DOUBLE | NOT NULL | FK→ | FK value from MLTM_NDC_MAIN_DRUG_CODE |
| 6 | `PBS_DRUG_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key PBS_DRUG |
| 7 | `PBS_OCS_MAPPING_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:REFERENCE SEQThis is the value of the unique primary identifier of the PBS_OCS_MAPPING table. It is an internal system assigned number. |
| 8 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key ORDER_CATALOG_SYNONYM |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `DRUG_SYNONYM_ID` | [MLTM_DRUG_NAME](MLTM_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| `MAIN_MULTUM_DRUG_CODE` | [MLTM_NDC_MAIN_DRUG_CODE](MLTM_NDC_MAIN_DRUG_CODE.md) | `MAIN_MULTUM_DRUG_CODE` |
| `PBS_DRUG_ID` | [PBS_DRUG](PBS_DRUG.md) | `PBS_DRUG_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

