# LH_D_IC_ANTIBGRM_ORG_DSC

> Dimension table to store content IC Antibiogram Organism Disclaim and Suppression Reference Data for Infection Control Reports

**Description:** LH_D_IC_ANTIBGRM_ORG_DSC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record became effective; defaults to 1/01/1800. |
| 3 | `D_ANTIBIOTIC_ID` | DOUBLE | NOT NULL |  | identifies the antibiotic configure with this suppression/disclaimer. Unique generated number that identifies a single row on the LH_D_ANTIBIOTIC table. |
| 4 | `D_FACILITY_ID` | DOUBLE | NOT NULL |  | identifies the facility configure with this suppression/disclaimer. Unique generated number that identifies a single row on the LH_D_FACILITY table. |
| 5 | `D_IC_ANTIBGRM_ORG_DSC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_IC_ANTIBGRM_ORG_DSC table. |
| 6 | `D_ORGANISM_ID` | DOUBLE | NOT NULL |  | identifies the organism configure with this suppression/disclaimer. Unique generated number that identifies a single row on the LH_D_ORGANISM table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record is no longer effective; defaults to 12/31/2100. |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data |
| 10 | `LH_CNT_IC_ANTIBGRM_GROUP_ID` | DOUBLE | NOT NULL |  | Unique ID for each group in LH_CNT_IC_ANTIBGRM_GROUP table |
| 11 | `LH_CNT_IC_ANTIBGRM_ORG_DSC_ID` | DOUBLE | NOT NULL |  | Unique ID for declaim-suppression of organism group or Facility in LH_CNT_IC_ANTIBGRM_ORG_DSC table |
| 12 | `LONG_TEXT` | VARCHAR(1000) |  |  | The actual long data of suppression or disclaimer. |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long_text_id of suppression/disclaimer on LH_CNT_IC_ANTIBGRM_ORG_DSC table. Unique generated number that identifies a single row on the LONG_TEXT_REFERENCE table. |
| 14 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record wad first loaded into the table. |
| 15 | `SUPPRESS_IND` | DOUBLE |  |  | The actual long data for suppression /disclaimer. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

