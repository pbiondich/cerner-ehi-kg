# CDI_AXLIC_USAGE

> This table contains AX license usage information captured at various intervals. This data will be used for reporting purposes.

**Description:** CDI AX License Usage  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_AXLIC_USAGE_ID` | DOUBLE | NOT NULL |  | The Cerner generated unique primary key of this table. |
| 2 | `LICENSES_IN_USE_NBR` | DOUBLE | NOT NULL |  | The total number of licenses in use at the time of the collection. |
| 3 | `LICENSE_DT_TM` | DATETIME | NOT NULL |  | The date and time the license usage information was collected. |
| 4 | `LICENSE_GROUP_NM` | VARCHAR(128) | NOT NULL |  | The name of the license group. |
| 5 | `LICENSE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of license. 0 - AX License, 2 - ERMX License, 6 - WFX License, 7 - WX License. |
| 6 | `TOTAL_LICENSES_NBR` | DOUBLE | NOT NULL |  | The total number of licenses available in the group. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

