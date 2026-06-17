# LH_CNT_IC_ADV_MICRO

> Stores microbiology culture results that were signed from the IC Advisor

**Description:** LH CNT IC ADV MICRO  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_IC_ADV_MICRO_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Body location where the collection was done (left arm, right thumb, etc.). |
| 4 | `COLLECT_DT_TM` | DATETIME |  |  | This field includes the date and time the specimen was collected. |
| 5 | `COLLECT_LOC_BED_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the bed location at which this order was collected. This could be used to join to the LOCATION table. |
| 6 | `COLLECT_LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the building location at which this order was collected. This could be used to join to the LOCATION table. |
| 7 | `COLLECT_LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the facility location at which this order was collected. This could be used to join to the LOCATION table. |
| 8 | `COLLECT_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the nurse unit location at which this order was collected. This could be used to join to the LOCATION table. |
| 9 | `COLLECT_LOC_ROOM_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the room location at which this order was collected. This could be used to join to the LOCATION table. |
| 10 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | ENCOUNTER ID for this record |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EVENT_CD` | DOUBLE | NOT NULL |  | It is the code that identifies the most basic unit of the storage, i.e. RBC, discharge summary, image. |
| 14 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_Class_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 15 | `EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for an event. Uniquely identifies a logical clinical event row. There may be more than one row with the same event_id. |
| 16 | `LH_CNT_IC_ADV_MICRO_ID` | DOUBLE | NOT NULL | PK | THE PRIMARY KEY |
| 17 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | States whether the result is normal. This can be used to determine whether to display the event tag in different color on the flowsheet. For group results, this represents an "overall" normalcy. i.e. Is any result in the group abnormal? Also allows different purge criteria to be applied based on result. |
| 18 | `POSITIVE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive, 1 = Positive. |
| 19 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET 8. Result status code. Valid values: authenticated, unauthenticated, unknown, cancelled, pending, in lab, active, modified, superseded, transcribed, not done. |
| 20 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Source of collection (blood, sputum, stool, etc.) |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_ADV_MICRO_ORG](LH_CNT_IC_ADV_MICRO_ORG.md) | `LH_CNT_IC_ADV_MICRO_ID` |

