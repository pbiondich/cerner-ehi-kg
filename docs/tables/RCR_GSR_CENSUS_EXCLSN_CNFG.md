# RCR_GSR_CENSUS_EXCLSN_CNFG

> This table is used to store the Code values of the Encounter type Codes and Encounter Class type codes which needs to excluded from the GSR Daily Census Extract

**Description:** RCR_GSR_CENSUS_EXCLSN_CNFG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | DOUBLE |  |  | Code Set from Code_Value table ; |
| 2 | `CODE_VALUE` | DOUBLE |  | FK→ | Field to Store the Code_Value from Code_Value table |
| 3 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created |
| 4 | `ENTITY_CDF_MEANING` | VARCHAR(12) |  |  | Field to Store the CFD Meaning from Code_Value table; |
| 5 | `ENTITY_CKI` | VARCHAR(255) |  |  | Field to Store the CKI from Code_Value table |
| 6 | `ENTITY_NAME` | VARCHAR(40) |  |  | Field to Store the Display field from Code_Value table |
| 7 | `ENTITY_TYPE_TXT` | VARCHAR(100) |  |  | Field Indicating the Type of Code; Example - possible values are ENCOUNTER_CODE_TYPE or ENCOUNTER_CLASS_TYPE |
| 8 | `EXCLUDE_IND` | DOUBLE |  |  | Field to Indicate if the code Value needs to be Excluded from the Extract, Value 1 indicates its excluded |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `RCR_GSR_CENSUS_EXCLSN_CNFG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

