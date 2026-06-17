# HF_D_ISOLATE

> This is the HealthFacts dimension table that contains standard values for isolates

**Description:** health facts dimension isolates  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_LOINC_CODE` | VARCHAR(10) |  |  | An alternate LOINC code that is not PHIN approved |
| 2 | `ANTIBIOGRAM_IND` | DOUBLE |  |  | Indicates if the isolate is commonly found on antibiograms |
| 3 | `ANTIBIOGRAM_NAME` | VARCHAR(25) |  |  | A short version of the isolate name used for antibiogram reporting purposes |
| 4 | `HEALTHAWARE_IND` | DOUBLE |  |  | Indicates if the record was generated via the HealthAware solution. |
| 5 | `ISOLATE_CATEGORY` | VARCHAR(30) |  |  | A high level category for the isolate. Generally this is the genus |
| 6 | `ISOLATE_CODE` | DOUBLE |  |  | No such field on this table. |
| 7 | `ISOLATE_GROUP` | VARCHAR(30) |  |  | Identifies the areas within an antibiogram report that a isolate should be displayed |
| 8 | `ISOLATE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines an isolate |
| 9 | `ISOLATE_NAME` | VARCHAR(50) |  |  | The scientific name for the isolate |
| 10 | `ISOLATE_REPT_CATEGORY` | VARCHAR(30) |  |  | The reporting category for the isolate. Typically the genus; however sometimes this is at a finer grain than the genus |
| 11 | `ISOLATE_TYPE` | VARCHAR(25) |  |  | The type of isolate |
| 12 | `ODIN_IND` | DOUBLE |  |  | Indicates if the isolate is typically reportable |
| 13 | `PHIN_LOINC_CODE` | VARCHAR(10) |  |  | The PHIN approved LOINC codes used for reporting purposes |
| 14 | `SNOMEDCT_CODE` | VARCHAR(15) |  |  | A newer version of the SNOMED code. Only populated when the SNOMEDCT code is different from the SNOMED code |
| 15 | `SNOMED_CODE` | VARCHAR(15) |  |  | The SNOMED code(s) for the isolate |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

