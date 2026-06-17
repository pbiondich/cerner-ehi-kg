# LH_CNT_IC_MICRO_EVENT

> This table will contain a list of microbiology events to be displayed in the LabID MDRO/CDI Report

**Description:** LH_CNT_IC_MICRO_EVENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Body_site_cd for the body site location of specimen collection. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Cd for the microbiology/serology order. |
| 3 | `COLLECTED_BED_CD` | DOUBLE | NOT NULL |  | Stores code value of the bed where the sample is collected. |
| 4 | `COLLECTED_DT_TM` | DATETIME |  |  | DT_TM of the specimen collection. |
| 5 | `COLLECTED_FAC_CD` | DOUBLE | NOT NULL |  | Stores code value of the facility where the sample is collected. |
| 6 | `COLLECTED_LOC_CD` | DOUBLE | NOT NULL |  | Location_cd for the location in which the specimen was collected. |
| 7 | `COLLECTED_ROOM_CD` | DOUBLE | NOT NULL |  | Stores code value of the room where the sample is collected. |
| 8 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Stores date time when the row is created. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encntr_id for the encounter in which the specimen was collected. |
| 10 | `ENC_TYPE_CD` | DOUBLE | NOT NULL |  | Encntr_type_cd of the encounter during specimen collection. |
| 11 | `EVENT_CD` | DOUBLE | NOT NULL |  | Cd for the associated serology event. |
| 12 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event_ID for the microbiology event on clinical_event. |
| 13 | `LH_CNT_IC_MICRO_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_MICRO_EVENT table. |
| 14 | `MDRO_CAT_ID` | DOUBLE | NOT NULL | FK→ | Id for the associated MDRO category on the br_mdro_cat table. |
| 15 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Cd for the organism associated with the micro event. |
| 16 | `REFERRED_EVENT_ID` | DOUBLE | NOT NULL |  | Event_id for the referred susceptibility event. |
| 17 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Specimen_type_cd for the collected specimen source. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MDRO_CAT_ID` | [BR_MDRO_CAT](BR_MDRO_CAT.md) | `BR_MDRO_CAT_ID` |

