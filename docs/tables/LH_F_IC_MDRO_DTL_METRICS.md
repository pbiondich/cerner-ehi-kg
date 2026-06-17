# LH_F_IC_MDRO_DTL_METRICS

> This fact table is used to store Infection Control MDRO DTAIL Lighthouse Report.

**Description:** LH_F_IC_MDRO_DTL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CAI_HAI_FLAG` | DOUBLE |  |  | identify CAI or HAI |
| 3 | `CDI_DESIGNATION_TXT` | VARCHAR(100) |  |  | CDIFF Designation |
| 4 | `COLLECT_DT_TM` | DATETIME |  |  | Identifies the specimen source for the organism. |
| 5 | `COLLECT_UTC_DT_TM` | DATETIME |  |  | Identifies the specimen source for the organism; normalized to GMT. |
| 6 | `D_BODY_SITE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the specimen source for the organism. |
| 7 | `D_COLL_BED_ID` | DOUBLE | NOT NULL | FK→ | Identifies the bed of specimen source collected for the organism. |
| 8 | `D_COLL_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Identifies the building of specimen source collected for the organism. |
| 9 | `D_COLL_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility of specimen source collected for the organism. |
| 10 | `D_COLL_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nurse unit of specimen source collected for the organism. |
| 11 | `D_COLL_PREV_BED_ID` | DOUBLE | NOT NULL | FK→ | Identifies the bed location prior to the collection of the specimen source for the organism. |
| 12 | `D_COLL_PREV_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Identifies the building location prior to the collection of the specimen source for the organism. |
| 13 | `D_COLL_PREV_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility location prior to the collection of the specimen source for the organism. |
| 14 | `D_COLL_PREV_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nurse unit location prior to the collection of the specimen source for the organism. |
| 15 | `D_COLL_PREV_ROOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the room location prior to the collection of the specimen source for the organism. |
| 16 | `D_COLL_ROOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the room of specimen source collected for the organism. |
| 17 | `D_ORGANISM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the reported organism or serology |
| 18 | `D_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the body site for the organism. |
| 19 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 20 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id associated with the organism/serology result. From the clinical_event table. |
| 21 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 22 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 23 | `HAI_DEVICE_LATERALITY` | VARCHAR(100) |  |  | Identifies the laterality of the device. |
| 24 | `HAI_DEVICE_LOCATION` | VARCHAR(100) |  |  | Identifies the location of the device. |
| 25 | `HAI_EVENT_ID` | DOUBLE | NOT NULL |  | Identifies the clinical event of the HAI event |
| 26 | `HAI_SUBTYPE` | VARCHAR(100) |  |  | Identifies the specific HAI within the HAI type. |
| 27 | `HAI_TYPE` | VARCHAR(50) |  |  | Identifies the HAI type of infection (BSI, UTI, PN, SSI , MDRO CDI) |
| 28 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 29 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 30 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 31 | `LH_F_IC_MDRO_DTL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_IC_MDRO_DTL_METRICS table. |
| 32 | `MDRO_CAT_NAME` | VARCHAR(150) |  |  | Identified the mdro category name which setting in bedrock . |
| 33 | `MDRO_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of MDRO |
| 34 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence of the microbiology result; 0 if serology. |
| 35 | `ORGANISM_ENTITY_NAME` | VARCHAR(50) |  |  | ORGANISM or SEROLOGY |
| 36 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 37 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 40 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_BODY_SITE_ID` | [LH_D_BODY_SITE](LH_D_BODY_SITE.md) | `D_BODY_SITE_ID` |
| `D_COLL_BED_ID` | [LH_D_BED](LH_D_BED.md) | `D_BED_ID` |
| `D_COLL_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_COLL_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_COLL_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_COLL_PREV_BED_ID` | [LH_D_BED](LH_D_BED.md) | `D_BED_ID` |
| `D_COLL_PREV_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_COLL_PREV_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_COLL_PREV_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_COLL_PREV_ROOM_ID` | [LH_D_ROOM](LH_D_ROOM.md) | `D_ROOM_ID` |
| `D_COLL_ROOM_ID` | [LH_D_ROOM](LH_D_ROOM.md) | `D_ROOM_ID` |
| `D_ORGANISM_ID` | [LH_D_ORGANISM](LH_D_ORGANISM.md) | `D_ORGANISM_ID` |
| `D_SOURCE_ID` | [LH_D_SOURCE](LH_D_SOURCE.md) | `D_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BED](LH_D_BED.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BED](LH_D_BED.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BODY_SITE](LH_D_BODY_SITE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ORGANISM](LH_D_ORGANISM.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ROOM](LH_D_ROOM.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ROOM](LH_D_ROOM.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_SOURCE](LH_D_SOURCE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

