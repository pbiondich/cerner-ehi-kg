# LH_QRDA_NQF_AGG

> This table is used to store elements that are used to store aggregated count for each provider and measure needed in QRDA Category 3 file for submission. This table is at the grain of one provider and measure per row.

**Description:** LH_QRDA_NQF_AGG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_CPC table |
| 3 | `BR_GPRO_ID` | DOUBLE | NOT NULL |  | Primary Key of BR_GPRO table |
| 4 | `BR_GPRO_SUB_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the BR_GPRO_SUB table. |
| 5 | `CMS_PROGRAM` | VARCHAR(100) |  |  | Type of submission program: 'NQF', 'PQRS', 'GPRO-PQRS', 'GPRO-NQF', 'CPC' |
| 6 | `DEN_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 7 | `DEN_EXCL_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 8 | `DEN_EXCP_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 9 | `D_PRSNL_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 10 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time on which the status of the problem was changed |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 12 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 13 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 14 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 15 | `IPP_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 17 | `LH_QRDA_NQF_AGG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_NQF_AGG table. |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 19 | `MEASURE_GROUP` | VARCHAR(50) |  |  | The name of the table this Other Template section is related (i.e. LH_QRDA_PQRS) |
| 20 | `MSR_PERCENT` | DOUBLE |  |  | Contains the calculated measure percentage, derived from either a measure-specific calculation or as the result of a generic measure calculation of (numerator / (denominator - exclusions - exceptions) |
| 21 | `MSR_POP_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 22 | `NUM_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 23 | `NUM_EXCL_CNT` | DOUBLE |  |  | This field contains the count of numerator exclusion patients in respective measures. |
| 24 | `NUM_EXCP_CNT` | DOUBLE |  |  | The value of the primary identifier of the table to which the Other Template section is related (i.e. lh_qrda_pqrs_id) |
| 25 | `QRDA_TAG` | VARCHAR(50) |  |  | The tag associated with the filtered QRDA data records. |
| 26 | `REPORTING_CATEGORY` | DOUBLE |  |  | Indicates if the report category is QRDA 1 or QRDA 3. |
| 27 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 28 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 29 | `SRC_UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 33 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

