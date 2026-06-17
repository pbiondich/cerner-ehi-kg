# LH_D_ANTIBIOTIC

> Dimension table to store Antibiotics Reference Data for Infection Control Reports

**Description:** LH_D_ANTIBIOTIC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | CODE SET 1011 |
| 3 | `ANTIBIOTIC_DESCRIPTION` | VARCHAR(60) |  |  | The description of the antibiotic |
| 4 | `ANTIBIOTIC_DISPLAY` | VARCHAR(50) |  |  | The display value for the antibiotic |
| 5 | `ANTIBIOTIC_MEANING` | VARCHAR(50) |  |  | The Cerner-identified meaning for the antibiotic |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `D_ANTIBIOTIC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_ANTIBIOTIC table. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data |
| 11 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record wad first loaded into the table. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 15 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

