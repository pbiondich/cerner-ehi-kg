# LH_ABS_SAMP_INFO

> Hold information about eqc/abstractor sampling. Total population size, CCN measure sampling, sample numbers

**Description:** LH_ABS_SAMP_INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_MEAN` | VARCHAR(100) |  |  | The category_mean of the condition being documented |
| 2 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 3 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_ABS_SAMP_INFO_ID` | DOUBLE | NOT NULL |  | Primary key of this table |
| 10 | `MEDICARE_SAMP_CNT` | DOUBLE | NOT NULL |  | Sampled population for the CCN/Measure combination that is Medicare |
| 11 | `MEDICARE_TOTAL_CNT` | DOUBLE | NOT NULL |  | Total population for the CCN/Measure combination that is Medicare |
| 12 | `MONTH_DT_TM` | DATETIME |  |  | Month this sample was over |
| 13 | `NON_MEDICARE_SAMP_CNT` | DOUBLE | NOT NULL |  | Sampled population for the CCN/Measure combination that is non-Medicare |
| 14 | `NON_MEDICARE_TOTAL_CNT` | DOUBLE | NOT NULL |  | Total population for the CCN/Measure combination that is non-Medicare |
| 15 | `STRATUM_TXT` | VARCHAR(50) |  |  | If the documented data was tied to a condition's stratum, this holds that stratum |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `UPDT_TASK_TXT` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. (TEXT FORMAT) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |

