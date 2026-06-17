# WH_OTH_XREF_WORK

> Work table containing all possible values to be mapped by the Health Data Mapping Tool.

**Description:** WH OTH XREF WORK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVAL_STATUS` | VARCHAR(50) |  |  | Approval status of the xref row. A = Approved, R = Rejected |
| 2 | `CLIENT_CODE_SET` | VARCHAR(20) |  |  | Client code set to be mapped. |
| 3 | `CLIENT_TABLE_NAME` | VARCHAR(30) |  |  | Client table name containing the value to be mapped. |
| 4 | `CLIENT_VALUE_REF` | VARCHAR(100) |  |  | Client value to be mapped. |
| 5 | `DESC1` | VARCHAR(255) |  |  | Dimension description 1 |
| 6 | `DESC2` | VARCHAR(255) |  |  | Dimension description 2 |
| 7 | `DESC3` | VARCHAR(255) |  |  | Dimension description 3 |
| 8 | `DESC4` | VARCHAR(255) |  |  | Dimension description 4 |
| 9 | `DIMENSION_KEY` | DOUBLE |  |  | Dimension identifier |
| 10 | `DIMENSION_MEANING` | VARCHAR(50) |  |  | Subject area name of the dimension being mapped. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system, but may be adjusted if there is >1 HF feed from the client. |
| 12 | `MAPPING_STATUS` | VARCHAR(50) |  |  | Mapping status of the row. N = New value, C = Changed value |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 16 | `XREF_WORK_KEY` | DOUBLE |  |  | Unique generated number that identifies a singgle row on the wh_oth_xref_work table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

