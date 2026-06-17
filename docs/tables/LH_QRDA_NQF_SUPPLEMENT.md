# LH_QRDA_NQF_SUPPLEMENT

> This table is used to calculate aggregated count for supplement data (gender, race, ethnicity, payer) for each provider and measure needed in QRDA Category 3 file for submission. It contains the outcome for all qualified patients for each measure. This table is at the grain of one patient per provider and measure per row. The combination of parent_entity_id and measure_group is unique.

**Description:** LH_QRDA_NQF_SUPPLEMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the encounter associated to the supplement data. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 8 | `LH_QRDA_NQF_SUPPLEMENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_NQF_SUPPLEMENT table. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `MEASURE_GROUP` | VARCHAR(50) |  |  | Population group like NQF2_0024, CMS_0065 etc. It will also have sub-measure level detail |
| 11 | `OUTCOME_FLAG` | DOUBLE | NOT NULL |  | Numeric value to determine if the patient is in numerator/denominator/exclusion/ipp |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the supplement data is related (i.e. lh_qrda_nqf_id) |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table this supplement data is related (i.e. LH_QRDA_NQF) |
| 14 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 15 | `SRC_UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

