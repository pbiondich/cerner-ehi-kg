# LH_AMB_EP_RELTN_2025

> Table containing the relationships of providers to encounters for Meaningful Use NQF Stage 2 2025

**Description:** LH_AMB_EP_RELTN_2025  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIBUTION_OPTION` | VARCHAR(10) |  |  | The attribution option selected in bedrock. |
| 3 | `CHARGE_RELTN_CD` | VARCHAR(200) |  |  | The relationship code for the provider to the charge |
| 4 | `ENCNTR_PRSNL_R_CD` | DOUBLE |  |  | The relationship code for the provider to the encounter |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_AMB_EP_RELTN_2025_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_EP_RELTN_2025 table. |
| 11 | `LH_AMB_QUAL_ENCNTR_2025_ID` | DOUBLE |  | FK→ | Identifies the unique record in LH_AMB_QUAL_ENCNTR_2025 that matches. |
| 12 | `PROVIDER_ID` | DOUBLE |  |  | The unique provider id from PRSNL. |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 16 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_AMB_QUAL_ENCNTR_2025](LH_AMB_QUAL_ENCNTR_2025.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_AMB_QUAL_ENCNTR_2025_ID` | [LH_AMB_QUAL_ENCNTR_2025](LH_AMB_QUAL_ENCNTR_2025.md) | `LH_AMB_QUAL_ENCNTR_2025_ID` |

