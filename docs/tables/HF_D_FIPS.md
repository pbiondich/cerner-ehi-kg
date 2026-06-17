# HF_D_FIPS

> BLANK

**Description:** HF_D_FIPS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNTY_DESC` | VARCHAR(40) |  |  | The county of the FIPS |
| 2 | `COUNTY_FIPS_CODE` | VARCHAR(10) |  |  | The county FIPS code. |
| 3 | `FIPS_CLASS_CODE` | VARCHAR(10) |  |  | The FIPS class code |
| 4 | `FIPS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `STATE_FIPS_CODE` | VARCHAR(10) |  |  | The state code for the FIPS. |
| 6 | `STATE_POST_CODE` | VARCHAR(10) |  |  | The state postal code for the FIPS. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

