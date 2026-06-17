# ROOM

> The room table is an extension to the location table which contains information specific to a room type of location. A room is specified within the context of a nurse unit or outpatient location.

**Description:** Room  
**Table type:** REFERENCE  
**Primary key:** `LOCATION_CD`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CLASS_CD` | DOUBLE | NOT NULL |  | User defined room class types. Examples include "private", "semi-private", "ward", etc. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FIXED_BED_IND` | DOUBLE |  |  | Set to TRUE, if this room has a set or fixed number of beds. Set to FALSE, if the number of beds in this room varies and they do not have specific numbers or identifiers. If false, the user does NOT define beds for the room. |
| 9 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. User defined. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. Unique internal identifier. |
| 11 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The parent location for the room. Indicates the nurse unit associated with the room. Internal unique identifier. |
| 12 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The category of treatment, surgery, or general resources associated with the room. May be used during ATD transactions to validate whether the patient should be placed in the room. |
| 13 | `TELEMETRY_IND` | DOUBLE |  |  | Telemetry indicator. Not currently in use as of March 1997. To be deleted. |
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
| `LOC_NURSE_UNIT_CD` | [NURSE_UNIT](NURSE_UNIT.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BED](BED.md) | `LOC_ROOM_CD` |

