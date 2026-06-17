# LH_QRDA_EC_DETAIL

> This schema will be used to store the patient outcome information measure wise for each EC.

**Description:** LH_QRDA_EC_DETAIL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. Part of the FK relationship to the LH_QRDA_EC parent table. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LH_QRDA_EC_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_EC_DETAIL table. |
| 8 | `LH_QRDA_EC_ID` | DOUBLE | NOT NULL | FK→ | Primary key of lh_qrda_ec table |
| 9 | `MEASURE_GROUP` | VARCHAR(50) |  |  | Name of measure. |
| 10 | `OUTCOME_FLAG` | DOUBLE |  |  | Outcome flag of a patient |
| 11 | `REPORTING_CATEGORY` | DOUBLE |  |  | Indicates if the report category is QRDA 1 or QRDA 3. |
| 12 | `REPORTING_YEAR` | DOUBLE |  |  | Stores the reporting year. |
| 13 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source |
| 14 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_QRDA_EC](LH_QRDA_EC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_QRDA_EC_ID` | [LH_QRDA_EC](LH_QRDA_EC.md) | `LH_QRDA_EC_ID` |

