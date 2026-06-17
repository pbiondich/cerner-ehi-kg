# HF_D_PAYER

> The dimension table of the possible payers.

**Description:** HF_D_PAYER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CO_DISPLAY` | VARCHAR(100) |  |  | This is the Critical Outcomes description they want to see in the Critical Outcome Business Objects reports. |
| 2 | `CO_IND` | DOUBLE |  |  | This is an indicator 0 (no) or 1 (yes) if this is to be used for Critical Outcomes mappings. Some CO values are combinations and HF are separate or vice versa. |
| 3 | `HF_IND` | DOUBLE |  |  | Indicates if the record was generated via the Health Facts solution. |
| 4 | `PAYER_CODE` | VARCHAR(30) |  |  | The two character standard code found in the UB-04 billing file format. |
| 5 | `PAYER_CODE_DESC` | VARCHAR(60) |  |  | The long description for the primary payer. |
| 6 | `PAYER_ID` | DOUBLE |  |  | PRIMARY KEY |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

