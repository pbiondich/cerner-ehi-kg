# LH_QRDA_SETUP_DATA

> Stores data in relation to how an entity is setup when running the QRDA loads.

**Description:** Lighthouse Quality Reporting Document Architecture Setup Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CPC_ID` | DOUBLE | NOT NULL | FK→ | The BR_CPC_ID for the CPC the QRDA load was run for when run for CPCs. |
| 2 | `BR_GPRO_ID` | DOUBLE | NOT NULL | FK→ | The BR_GPRO_ID for the group the QRDA load was run for when run for Groups. |
| 3 | `BR_GPRO_SUB_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the BR_GPRO_SUB table. |
| 4 | `CATEGORY_NUMBER` | DOUBLE |  |  | Whether the QRDA load was run as a Category 3 or Category 1 load. |
| 5 | `D_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The LH_D_PERSONNEL_ID for the provider the QRDA load was run for when run for individuals. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_QRDA_SETUP_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_SETUP_DATA table.; |
| 11 | `REPORTING_YEAR` | DOUBLE |  |  | The year the QRDA load was run for. |
| 12 | `SETUP_TYPE` | VARCHAR(50) |  |  | A short identifier for the type of data being stored. |
| 13 | `SETUP_VALUE` | DOUBLE | NOT NULL |  | An ID of a value represented in setup, such as a location ID. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 17 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_CPC_ID` | [BR_CPC](BR_CPC.md) | `BR_CPC_ID` |
| `BR_GPRO_ID` | [BR_GPRO](BR_GPRO.md) | `BR_GPRO_ID` |
| `D_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

