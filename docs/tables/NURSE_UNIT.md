# NURSE_UNIT

> The nurse unit table is an extension to the location table which contains information specific to a nurse unit type of location. A nurse unit is a hospital inpatient grouping of rooms and beds and identified within the

**Description:** Nurse Unit  
**Table type:** REFERENCE  
**Primary key:** `LOCATION_CD`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATD_REQ_LOC` | DOUBLE |  |  | ATD Requisition Location. PharmNet. Not currently in use as of March 199. To be deleted. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CART_QTY_IND` | DOUBLE |  |  | PharmNet. Not currently in use as of March 1997. To be deleted. |
| 8 | `DISPENSE_WINDOW` | DOUBLE |  |  | PharmNet. Not currently in use as of March 1997. To be deleted. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The field identifies a patient location. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 11 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | Internal identifier for the building in which the nurse unit is physically located. |
| 12 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Internal identifier for the facility in which the nurse unit is physically located. |
| 13 | `LOC_OVERFLOW_CD` | DOUBLE | NOT NULL |  | If the nurse unit is full, the suggested alternate location to be used for Admits and Transfers |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PM_AUTO_DISCH_PARM_SET_R](PM_AUTO_DISCH_PARM_SET_R.md) | `LOC_NURSE_UNIT_CD` |
| [ROOM](ROOM.md) | `LOC_NURSE_UNIT_CD` |

