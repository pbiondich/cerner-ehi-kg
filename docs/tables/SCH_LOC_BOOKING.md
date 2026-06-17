# SCH_LOC_BOOKING

> Table that contains location bookings for a person and encounter.

**Description:** Schedule Location Booking  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BED_CD` | DOUBLE | NOT NULL | FK→ | The bed that is being booked into. |
| 2 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date/Time of Location Booking |
| 3 | `BUILDING_CD` | DOUBLE | NOT NULL | FK→ | The building that is being booked into. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The patient encounter that is being booked to the location. |
| 5 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date/Time of Location Booking |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility that is being booked into. |
| 7 | `FORCE_IND` | DOUBLE |  |  | Force the Location Booking even if the existing number of bookings exceeds the quota. |
| 8 | `FORCE_NBR_BOOKING` | DOUBLE | NOT NULL |  | The number of bookings at the location at the time this location booking was forced. |
| 9 | `FORCE_QUOTA` | DOUBLE | NOT NULL |  | The quota at the location at the time this location booking was forced. |
| 10 | `GRANTED_DT_TM` | DATETIME | NOT NULL |  | The date and time that the location booking was created. |
| 11 | `GRANTED_PRSNL_ID` | DOUBLE | NOT NULL |  | The person id of the user who created the location booking. |
| 12 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The nurse unit that is being booked into. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient who is being booked to the location. |
| 14 | `ROOM_CD` | DOUBLE | NOT NULL | FK→ | The room that is being booked into. |
| 15 | `SCH_LOC_BOOKING_ID` | DOUBLE | NOT NULL |  | Unique identifier for a row on the sch_loc_booking table. |
| 16 | `STATUS_FLAG` | DOUBLE |  |  | The current status of the location booking.1=IN-PROGRESS, 2=VERIFIED,3=WRITTEN,4=RELEASED |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WRITTEN_DT_TM` | DATETIME |  |  | The date and time the corresponding record was written. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

