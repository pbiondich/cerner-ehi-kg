# HF_D_RELEASE

> BLANK

**Description:** HF_D_RELEASE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RELEASE_BEG_DT_TM` | DATETIME |  |  | The begin effective date and time of the release. |
| 2 | `RELEASE_END_DT_TM` | DATETIME |  |  | The end effective date and time of the release. |
| 3 | `RELEASE_ID` | DOUBLE |  |  | PRIMARY KEY |
| 4 | `RELEASE_NUMBER` | VARCHAR(255) |  |  | The identifying number of the release. The release numbers are about a month behind the actual month to match the ONC website information. |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

