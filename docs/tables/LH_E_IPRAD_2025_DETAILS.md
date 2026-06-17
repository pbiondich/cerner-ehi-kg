# LH_E_IPRAD_2025_DETAILS

> Stores details for data gathered by the LH_E_IPRAD_2025 script.

**Description:** Lighthouse eMeasures Inpatient Excessive Radiation 2025 Metrics Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Indicated whether the row is active or inactive. |
| 2 | `CT_CATEGORY_TXT` | VARCHAR(60) |  |  | The category used to determine a threshold for excessive radiation dose or image noise from a CT scan. |
| 3 | `CT_GLOBAL_NOISE_VALUE_TXT` | VARCHAR(60) |  |  | The global noise in the CT scan image |
| 4 | `CT_RESULT_DT_TM` | DATETIME |  |  | The date time for the result of a CT scan |
| 5 | `CT_SIZE_ADJUSTED_VALUE_TXT` | VARCHAR(60) |  |  | The size adjusted value for radiation received during a CT scan |
| 6 | `DEN_IND` | DOUBLE |  |  | Indicates the scan qualifies for the Denominator |
| 7 | `EXCLUDE_IND` | DOUBLE |  |  | Indicates the scan qualifies for the Denominator Exclusions |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 13 | `LH_E_IPRAD_2025_DETAILS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_IPRAD_2025_DETAILS table. |
| 14 | `LH_E_IPRAD_2025_METRICS_ID` | DOUBLE |  | FK→ | Unique generated number that identifies a single row on the LH_E_IPRAD_2025_METRICS table. Associates details to the parent table. |
| 15 | `NUM_IND` | DOUBLE |  |  | Indicates the scan qualifies for the Numerator |
| 16 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The event id for the CT scan. |
| 17 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Currently, parent entity columns will come either from the CLINICAL_EVENT table or the LH_IMPORT_QRDA table. It will be the CLINICAL_EVENT table when loaded from Millennium data. It will be LH_IMPORT_QRDA when imported from files provided by another vendor. |
| 18 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 19 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 20 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) |  |  | The name of the task updating the record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_E_IPRAD_2025_METRICS](LH_E_IPRAD_2025_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_E_IPRAD_2025_METRICS_ID` | [LH_E_IPRAD_2025_METRICS](LH_E_IPRAD_2025_METRICS.md) | `LH_E_IPRAD_2025_METRICS_ID` |

