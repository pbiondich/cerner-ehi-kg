# LH_D_EP_MIPS_S3

> This table contains the information about br_eligible_provider.N I it s a clone of table LH_D_EP_MIPS. It is needed due to an issue where a change for Stage 3 code would break stage 2 code, This way, stage 2 code can use the original LH_D_EP_MIPS table and the stage 3 code can use the new LH_D_EP_MIPS_S3 table and Stage 3 code change will not affect the data on the LH_D_EP_MIPS.

**Description:** LH_D_EP_MIPS_S3  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_ELIGIBLE_PROVIDER table. |
| 4 | `D_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | The unique key from the lh_d_nurse_unit table |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EP_NAME` | VARCHAR(250) |  |  | Name of the provider/physician |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | Extract date of the record |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `GPRO_ID` | DOUBLE | NOT NULL |  | The primary key of the BR_GPRO table |
| 10 | `GPRO_NAME` | VARCHAR(250) |  |  | Name of the TIN from the BR_GPRO table |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 13 | `LH_D_EP_MIPS_S3_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_EP_MIPS_S3 table. |
| 14 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the nurse unit associated with the quality measure. Foreign key to the code_value table for code set 220. |
| 15 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 16 | `NPI_TXT` | VARCHAR(200) |  |  | Stores the eligible providers's national provider number. |
| 17 | `TAX_ID_NBR_TXT` | VARCHAR(250) |  |  | Stores the TIN or tax id number from the BR_GPRO table. |
| 18 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The source which updated/inserted the row |
| 21 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

