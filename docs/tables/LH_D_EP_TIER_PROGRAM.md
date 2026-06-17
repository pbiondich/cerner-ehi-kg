# LH_D_EP_TIER_PROGRAM

> This table contains the ep info

**Description:** LH_D_EP_TIER_PROGRAM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Id for the providers to identity them |
| 2 | `BR_ELIGIBLE_PROV_UPDT_DT_TM` | DATETIME |  |  | Date and time the row was updated in the br_group_prov table |
| 3 | `BR_ELIGIBLE_PROV_UPDT_PRSNL_NM` | VARCHAR(100) |  |  | This column contains the full name of the personnel who updated the Eligible Provider information in bedrock. |
| 4 | `BR_EP_ACTIVE_IND` | DOUBLE |  |  | Active ind |
| 5 | `BR_GROUP_RELTN_UPDT_DT_TM` | DATETIME |  |  | Date and time the row was updated in the br_group_reltn table |
| 6 | `BR_GROUP_RELTN_UPDT_PRSNL_NM` | VARCHAR(100) |  |  | This column contains the full name of the personnel who updated the tier information in bedrock. |
| 7 | `EP_NAME` | VARCHAR(100) |  |  | The name of the Provider |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the load was run and the row qualified |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | This column is needed for all lh_d_* tables |
| 10 | `LH_D_EP_TIER_PROGRAM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_EP_TIER_PROGRAM table. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `MEDICAID_ACTIVE_IND` | DOUBLE |  |  | Active ind for the medicaid row |
| 13 | `MEDICAID_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beg date and time for medicaid row |
| 14 | `MEDICAID_END_EFFECTIVE_DT_TM` | DATETIME |  |  | #REF! |
| 15 | `MEDICAID_PROGRAM_ID` | DOUBLE | NOT NULL |  | The program id for the medicaid row |
| 16 | `MEDICAID_STAGE_CD` | DOUBLE | NOT NULL |  | The cd value for the medicaid rows ( e.g. S2Y2) |
| 17 | `MEDICAID_UPDT_DT_TM` | DATETIME |  |  | update Date and time for the medicaid row |
| 18 | `MEDICARE_ACTIVE_IND` | DOUBLE |  |  | Active ind for medicare row |
| 19 | `MEDICARE_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beg date and time for medicare row |
| 20 | `MEDICARE_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The end date and time for medicaid row |
| 21 | `MEDICARE_PROGRAM_ID` | DOUBLE | NOT NULL |  | The program id for medicare |
| 22 | `MEDICARE_UPDT_DT_TM` | DATETIME |  |  | update date and time for the medicare row |
| 23 | `MEDICARE_YEAR` | VARCHAR(50) |  |  | The year the provider is configured as MEDICARE |
| 24 | `NPI_TXT` | VARCHAR(50) |  |  | The unique number to identify the Provider |
| 25 | `PERSONNEL_ACTIVE_IND` | DOUBLE |  |  | Active ind |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL |  | Id for the provider coming from prsnl table |
| 27 | `PROCESS_DT_TM` | DATETIME |  |  | Date and time when the load was run and the row qualified |
| 28 | `TIER1_ID` | DOUBLE | NOT NULL |  | The id of the tier the ep is associated with |
| 29 | `TIER1_NAME` | VARCHAR(100) |  |  | The name of the Tier the ep is associated with |
| 30 | `TIER2_ID` | DOUBLE | NOT NULL |  | The id of the tier the ep is associated with |
| 31 | `TIER2_NAME` | VARCHAR(100) |  |  | The name of the Tier the ep is associated with |
| 32 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_SOURCE` | VARCHAR(50) |  |  | Source which updated the row |
| 35 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

