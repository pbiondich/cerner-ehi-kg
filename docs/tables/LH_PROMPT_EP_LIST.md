# LH_PROMPT_EP_LIST

> This table contains the information about br_eligible_provider

**Description:** LH_PROMPT_EP_LIST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Br_eligible_provider_id |
| 2 | `EP_NAME` | VARCHAR(100) |  |  | Name of the provider |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the load was run and the row qualified |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LH_PROMPT_EP_LIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_PROMPT_EP_LIST table. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `NPI_TXT` | VARCHAR(100) |  |  | Unique number associated with the providers |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Organization_ID coming from Organization Table. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL |  | Person id of the provider from prsnl table |
| 12 | `POR_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Beg Effective Dt tm coming from PRSNL_ORG_RELTN Table. |
| 13 | `POR_END_EFFECTIVE_DT_TM` | DATETIME |  |  | End Effective Dt tm coming from PRSNL_ORG_RELTN Table. |
| 14 | `PROVIDER_ID` | DOUBLE | NOT NULL |  | Provider id from the br_eligible_provider table |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source which updated/inserted the row |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

