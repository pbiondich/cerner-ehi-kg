# HF_OTH_HS_FACILITY_BREAKOUT

> Work table that is used to help explode out the Facilities per Health System.

**Description:** HF_OTH_HS_FACILITY_BREAKOUT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system, but may be adjusted if there is >1 HF feed from the client. |
| 3 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Hospital to identify the associated hospital. |
| 4 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to. |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

