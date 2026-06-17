# HF_D_COUNTRY

> Dimension table that stores the list of potential countries for HealthSentry.

**Description:** HF_D_COUNTRY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNTRY_CODE` | VARCHAR(10) |  |  | The PHINVADs concept code that represents the country. |
| 2 | `COUNTRY_ID` | DOUBLE |  |  | PRIMARY KEY |
| 3 | `COUNTRY_NAME` | VARCHAR(50) |  |  | The name of the country. |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

