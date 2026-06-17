# HF_D_RESULT_INDICATOR

> This is the HealthFacts dimension table that contains standard values for the normalcy of gen lab results

**Description:** HF_D_Result_Indicator  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PHIN_CODE` | VARCHAR(10) |  |  | PHINVADs is expecting a specific code for valid nursing units. Only records that match the PHINVads table will be populated. |
| 2 | `PHIN_CONCEPT_DESC` | VARCHAR(100) |  |  | PHINVADs has defined long descriptions for abnormal flags. This translates the Health Data values to a standard concept description for HL7. |
| 3 | `RESULT_INDICATOR_DESC` | VARCHAR(60) |  |  | The textual description of the normality of the result (out of range, not normal, etc.) |
| 4 | `RESULT_INDICATOR_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

