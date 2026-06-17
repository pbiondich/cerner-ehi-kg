# LH_D_IC_ANTIBGRM_GROUP_R

> Dimension table to store content IC Antibiogram Group Relation Data for Infection Control Reports

**Description:** LH_D_IC_ANTIBGRM_GROUP_R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL |  | identifies the source configure with this encounter type group ; 0 for non-encounter type group. Unique generated number that identifies a single row on the LH_D_ENCNTR_TYPE table. |
| 4 | `D_IC_ANTIBGRM_GROUP_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_IC_ANTIBGRM_GROUP_R table. |
| 5 | `D_ORGANISM_ID` | DOUBLE | NOT NULL |  | identifies the organism configure with this organism group; 0 for non-organism group. Unique generated number that identifies a single row on the LH_D_ORGANISM table. |
| 6 | `D_SOURCE_ID` | DOUBLE | NOT NULL |  | identifies the source configure with this specimen group ; 0 for non-specimen group. Unique generated number that identifies a single row on the LH_D_SOURCE table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 9 | `GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of groups to be setup ( 1 = organism group 2 = Encounter type group 3= Specimen group) |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data |
| 11 | `LH_CNT_IC_ANTIBGRM_GROUP_ID` | DOUBLE | NOT NULL |  | Primary key from the LH_CNT_IC_ANTIBGRM_GROUP table. |
| 12 | `LH_CNT_IC_ANTIBGRM_GROUP_R_ID` | DOUBLE | NOT NULL |  | Primary key from the LH_CNT_IC_ANTIBGRM_GROUP_R table. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | the value of parent_entity_id in LH_CNT_IC_ANTIBGRM_GROUP_R table |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | the value of parent_entity_name in LH_CNT_IC_ANTIBGRM_GROUP_R table |
| 15 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record wad first loaded into the table. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

