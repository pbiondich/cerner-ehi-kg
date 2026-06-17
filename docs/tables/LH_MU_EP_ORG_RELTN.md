# LH_MU_EP_ORG_RELTN

> Identifies which Organizations an Eligible provider belongs to so they can be reported properly in the Lighthouse Meaningful Use reports

**Description:** LH_MU_EP_ORG_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EP_NAME` | VARCHAR(100) |  |  | The Full Name of the Eligible Provider |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LH_MU_EP_ORG_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_EP_ORG_RELTN table. |
| 8 | `NPI_NBR_TXT` | VARCHAR(200) |  |  | The National Provider Identification used to uniquely identify a Eligible Provider |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Unique Identifier for the Organization |
| 10 | `ORG_NAME` | VARCHAR(100) |  |  | The name of the Organization the Eligible Provider is associated to |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 14 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

