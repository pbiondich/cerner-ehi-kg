# LH_PROMPT_CCN_LIST

> This table will contain the ccn informaiton needed for stage 3 prompt

**Description:** LH_PROMPT_CCN_LIST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CCN_ID` | DOUBLE | NOT NULL |  | The unique number for the organization coming from br_ccn table |
| 2 | `CCN_NAME` | VARCHAR(100) |  |  | The name of the organization** OBSOLETE COLUMN ** |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the load was run and the row qualified |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LH_PROMPT_CCN_LIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_PROMPT_CCN_LIST table. |
| 8 | `LOC_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Begin Effective Date and Time coming from Location Table.** OBSOLETE COLUMN ** |
| 9 | `LOC_END_EFFECTIVE_DT_TM` | DATETIME |  |  | End Effective Date and Time coming from Location Table.** OBSOLETE COLUMN ** |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Organization Id coming from Organization table. |
| 12 | `ORG_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Begin Effective Date and Time coming from Organization Table.** OBSOLETE COLUMN ** |
| 13 | `ORG_END_EFFECTIVE_DT_TM` | DATETIME |  |  | End Effective Date and Time coming from Organization Table.** OBSOLETE COLUMN ** |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL |  | Person Id coming from Prsnl table |
| 15 | `TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | the number assigned for each organization |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source which update/inserted the row |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

